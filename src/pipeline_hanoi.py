import pandas as pd
import numpy as np
import os
import glob
import unicodedata
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, RobustScaler

def audit_data(df: pd.DataFrame):
    print("-" * 50)
    print("1. SHAPE (Dòng, Cột):", df.shape)
    print("2. INFO:")
    df.info()
    print("3. MISSING VALUES:")
    print(df.isna().sum())
    print("4. DUPLICATES:", df.duplicated().sum())
    print("-" * 50)

def normalize_vn(text):
    if pd.isna(text):
        return text
    text = str(text)
    text = unicodedata.normalize('NFC', text)
    return text.lower().strip()

def clean_area(x):
    if pd.isna(x): return np.nan
    s = str(x).lower().replace('m2', '').replace('m²', '').strip()
    try: return float(s)
    except: return np.nan

def clean_price(x):
    if pd.isna(x): return np.nan
    s = str(x).lower().replace('triệu/m²', '').replace('triệu/m2', '').strip()
    s = s.replace(',', '.') # Handle decimal mark
    try: return float(s)
    except: return np.nan

def clean_rooms(x):
    if pd.isna(x): return np.nan
    s = str(x).lower().replace('phòng', '').strip()
    try: return float(s)
    except: return np.nan

def run_pipeline():
    # 1. Load data
    raw_file = "data/raw/raw.csv"
    if not os.path.exists(raw_file):
        print(f"Không tìm thấy dữ liệu thô tại {raw_file}!")
        return
        
    print(f"Đang đọc 1 nguồn dữ liệu duy nhất từ: {raw_file}")
    df = pd.read_csv(raw_file, encoding='utf-8')
    
    print("\n[BƯỚC 1 & 2] KIỂM TOÁN DỮ LIỆU BAN ĐẦU")
    audit_data(df)
    
    print("\n[BƯỚC 3] LÀM SẠCH CƠ BẢN VÀ NHẤT QUÁN DỮ LIỆU")
    # Xóa cột Unnamed nếu có
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
        
    df = df.drop_duplicates()
    
    # Chuẩn hóa văn bản
    df['Quận'] = df['Quận'].apply(normalize_vn)
    df['Loại hình nhà ở'] = df['Loại hình nhà ở'].apply(normalize_vn)
    df['Giấy tờ pháp lý'] = df['Giấy tờ pháp lý'].apply(normalize_vn)
    
    # Ép kiểu dữ liệu
    df['Diện tích m2'] = df['Diện tích'].apply(clean_area)
    df['Giá_m2_trieu'] = df['Giá/m2'].apply(clean_price)
    df['Số phòng ngủ'] = df['Số phòng ngủ'].apply(clean_rooms)
    df['Số tầng'] = pd.to_numeric(df['Số tầng'], errors='coerce')
    
    print("\n[BƯỚC 4] XỬ LÝ KHUYẾT THIẾU (MISSING VALUES)")
    # Xóa các dòng không có Giá hoặc Diện tích (MCAR)
    df = df.dropna(subset=['Giá_m2_trieu', 'Diện tích m2'])
    
    # Tạo missing indicator cho số tầng (MNAR)
    df['Thieu_So_Tang'] = df['Số tầng'].isna().astype(int)
    
    print("\n[BƯỚC 5] XỬ LÝ OUTLIERS")
    # Sử dụng IQR Rule cho Giá
    Q1 = df['Giá_m2_trieu'].quantile(0.25)
    Q3 = df['Giá_m2_trieu'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = max(0, Q1 - 1.5 * IQR)
    upper_bound = Q3 + 1.5 * IQR
    
    outliers_count = ((df['Giá_m2_trieu'] < lower_bound) | (df['Giá_m2_trieu'] > upper_bound)).sum()
    print(f"Phát hiện {outliers_count} ngoại lệ giá. Đang cắt (clip) theo IQR...")
    df['Giá_m2_trieu'] = df['Giá_m2_trieu'].clip(lower=lower_bound, upper=upper_bound)
    
    print("\n[BƯỚC 6] ĐÓNG GÓI PIPELINE (TRANSFORMATION)")
    # Giữ lại các cột quan trọng
    features = ['Diện tích m2', 'Số phòng ngủ', 'Số tầng', 'Thieu_So_Tang', 'Quận', 'Loại hình nhà ở', 'Giấy tờ pháp lý']
    X = df[features].copy()
    y = df['Giá_m2_trieu']
    
    num_cols = ['Diện tích m2', 'Số phòng ngủ', 'Số tầng', 'Thieu_So_Tang']
    cat_cols = ['Quận', 'Loại hình nhà ở', 'Giấy tờ pháp lý']
    
    # Pipeline cho biến số: Fill Median + RobustScaler
    num_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', RobustScaler())
    ])

    # Pipeline cho biến phân loại: Fill 'khong_ro' + OneHot
    cat_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='khong_ro')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', drop='first'))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', num_transformer, num_cols),
            ('cat', cat_transformer, cat_cols)
        ])
    
    X_processed = preprocessor.fit_transform(X)
    print(f"Kích thước ma trận đặc trưng sau Pipeline: {X_processed.shape}")
    
    os.makedirs("data/processed", exist_ok=True)
    out_file = "data/processed/clean.csv"
    df.to_csv(out_file, index=False, encoding='utf-8-sig')
    print(f"Hoàn thành! Đã lưu dữ liệu sạch ({len(df)} dòng) tại: {out_file}")

if __name__ == "__main__":
    run_pipeline()
