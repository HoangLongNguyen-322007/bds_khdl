import pandas as pd
import numpy as np
import os
import glob
from utils import audit_data, normalize_vn, clean_price, clean_area

# Scikit-learn imports
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, RobustScaler

def run_pipeline():
    # 1. Load the latest raw dataset
    raw_files = glob.glob("../data/raw/*.csv")
    if not raw_files:
        print("Không tìm thấy dữ liệu thô nào trong data/raw/!")
        return
    latest_file = max(raw_files, key=os.path.getctime)
    print(f"Đang đọc dữ liệu từ: {latest_file}")
    df = pd.read_csv(latest_file, encoding='utf-8-sig')

    print("\n[BƯỚC 1] KIỂM TOÁN DỮ LIỆU BAN ĐẦU")
    audit_data(df)

    print("\n[BƯỚC 2] LÀM SẠCH CƠ BẢN VÀ NHẤT QUÁN DỮ LIỆU (CONSISTENCY)")
    # Xóa dòng trùng lặp
    df = df.drop_duplicates()
    
    # Chuẩn hóa tiếng Việt cột location và title
    df['location'] = df['location'].apply(normalize_vn)
    df['title'] = df['title'].apply(normalize_vn)
    
    # Chuẩn hóa giá và diện tích
    df['price_ty'] = df['price'].apply(clean_price)
    df['area_m2'] = df['area'].apply(clean_area)
    
    # Bỏ cột cũ
    df = df.drop(columns=['price', 'area'])
    
    print("\n[BƯỚC 3] XỬ LÝ KHUYẾT THIẾU (MISSING VALUES)")
    # MCAR: Xóa các dòng bị thiếu cột Price hoặc Area (do không thể dự đoán nếu thiếu target/feature chính)
    df = df.dropna(subset=['price_ty', 'area_m2'])
    
    # MAR: Điền khuyết số phòng (rooms) bằng Median của dữ liệu
    # Tạo missing indicator cho rooms (MNAR)
    df['rooms_is_missing'] = df['rooms'].isna().astype(int)
    
    print("\n[BƯỚC 4] XỬ LÝ OUTLIERS")
    # Sử dụng IQR Rule cho cột giá
    Q1 = df['price_ty'].quantile(0.25)
    Q3 = df['price_ty'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers_count = ((df['price_ty'] < lower_bound) | (df['price_ty'] > upper_bound)).sum()
    print(f"Phát hiện {outliers_count} giá trị ngoại lệ (Outliers). Áp dụng Winsorize (clip).")
    df['price_ty'] = df['price_ty'].clip(lower=lower_bound, upper=upper_bound)
    
    print("\n[BƯỚC 5] ĐÓNG GÓI PIPELINE (TRANSFORMATION)")
    # Chia ra feature và target
    X = df.drop(columns=['price_ty'])
    
    # Phân loại cột
    numeric_features = ['area_m2', 'rooms', 'rooms_is_missing']
    categorical_features = ['location'] # Lưu ý: thực tế cần bóc tách riêng quận huyện
    
    # Pipeline cho biến số: Fill Median + Dùng RobustScaler (tốt cho BĐS)
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', RobustScaler())
    ])

    # Pipeline cho biến phân loại: OneHotEncoding
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='other')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', drop='first'))
    ])

    # ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])
    
    # Chạy preprocessor
    X_processed = preprocessor.fit_transform(X)
    print(f"Kích thước ma trận đặc trưng sau Pipeline: {X_processed.shape}")
    
    # Lưu dữ liệu sạch
    os.makedirs("../data/processed", exist_ok=True)
    processed_file = "../data/processed/bds_processed_ready.csv"
    df.to_csv(processed_file, index=False, encoding='utf-8-sig')
    print(f"Hoàn thành! Đã lưu dữ liệu sạch tại: {processed_file}")

if __name__ == "__main__":
    run_pipeline()
