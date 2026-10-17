import os
import sys
import re
import unicodedata
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, RobustScaler
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Thiết lập style đồ thị
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

def normalize_vn(text):
    if pd.isna(text): return ''
    text = str(text)
    text = unicodedata.normalize('NFC', text)
    text = re.sub(r'\|\|\d+', '', text)
    return re.sub(r'\s+', ' ', text).lower().strip()

def clean_area(x):
    if pd.isna(x): return np.nan
    s = str(x).lower().replace('m²', '').replace('m2', '').replace(',', '.').strip()
    m = re.search(r'([0-9]+\.?[0-9]*)', s)
    return float(m.group(1)) if m else np.nan

def clean_price(x):
    if pd.isna(x): return np.nan
    s = str(x).lower().replace('triệu/m²', '').replace('triệu/m2', '').strip()
    if 'inf' in s: return np.nan
    m = re.findall(r'[0-9]+(?:[\.,][0-9]+)?', s)
    if not m: return np.nan
    try:
        p = float(m[0].replace(',', '.'))
        return p if 0 < p < 1e6 and not np.isinf(p) else np.nan
    except:
        return np.nan

def clean_dim(x, max_val=50.0):
    if pd.isna(x): return np.nan
    s = str(x).lower().replace('m', '').replace(',', '.').strip()
    m = re.search(r'([0-9]+\.?[0-9]*)', s)
    if not m: return np.nan
    val = float(m.group(1))
    if 1000 <= val <= 35000:
        val = val / 1000.0
    if val < 1.0 or val > max_val:
        return np.nan
    return val

def clean_rooms(x):
    if pd.isna(x): return np.nan
    s = str(x).lower().replace('phòng', '').strip()
    try: return float(s)
    except: return np.nan

def extract_address_details(addr):
    if pd.isna(addr): return '', ''
    addr_clean = normalize_vn(addr)
    parts = [p.strip() for p in addr_clean.split(',')]
    street, ward = '', ''
    for p in parts:
        if ('đường ' in p or 'phố ' in p) and not street:
            street = re.sub(r'^(đường|phố)\s+', '', p).strip()
        if ('phường ' in p or 'xã ' in p) and not ward:
            ward = re.sub(r'^(phường|xã)\s+', '', p).strip()
    return street, ward

def run_data_cleaning():
    print("==================================================================")
    print("PHẦN 1: LÀM SẠCH, LỌC 18 THÁNG GẦN NHẤT & CHI TIẾT HÓA BẤT ĐỘNG SẢN")
    print("==================================================================")
    
    raw_path = "data/raw/raw.csv"
    processed_path = "data/processed/clean.csv"
    
    if not os.path.exists(raw_path):
        if os.path.exists(processed_path):
            print(f"[*] Đọc dữ liệu đã xử lý từ: {processed_path}")
            return pd.read_csv(processed_path, low_memory=False)
        raise FileNotFoundError(f"Không tìm thấy file {raw_path}!")
        
    print(f"[*] Đọc dữ liệu gốc từ: {raw_path}")
    df = pd.read_csv(raw_path, low_memory=False)
    print(f"-> Kích thước dữ liệu ban đầu: {df.shape[0]:,} dòng, {df.shape[1]} cột")
    
    # 1. Lọc theo thời gian: 18 tháng gần nhất
    df['dt'] = pd.to_datetime(df['Ngày'], errors='coerce')
    max_date = df['dt'].max()
    cutoff_date = max_date - pd.DateOffset(months=18)
    print(f"-> Áp dụng mốc thời gian: Từ {cutoff_date.strftime('%Y-%m-%d')} đến {max_date.strftime('%Y-%m-%d')} (18 tháng gần nhất)")
    df = df[df['dt'] >= cutoff_date].copy()
    print(f"-> Dữ liệu trong cửa sổ 18 tháng: {len(df):,} bản ghi (Loại bỏ các năm cũ 2020-2024)")
    
    # 2. Xóa trùng lặp
    initial_len = len(df)
    df = df.drop_duplicates()
    print(f"-> Đã loại bỏ {initial_len - len(df)} bản ghi trùng lặp.")
    
    # 3. Chuẩn hóa chuỗi văn bản
    for col in ['Quận', 'Huyện', 'Loại hình nhà ở', 'Giấy tờ pháp lý']:
        if col in df.columns:
            df[col] = df[col].apply(normalize_vn)
            
    # 4. Ép kiểu số học
    df['Diện tích m2'] = df['Diện tích'].apply(clean_area)
    df['Giá_m2_trieu'] = df['Giá/m2'].apply(clean_price)
    df['Số phòng ngủ'] = df['Số phòng ngủ'].apply(clean_rooms)
    df['Số tầng'] = pd.to_numeric(df['Số tầng'], errors='coerce')
    df['mat_tien_m'] = df['Rộng'].apply(lambda x: clean_dim(x, max_val=30.0))
    df['chieu_sau_m'] = df['Dài'].apply(lambda x: clean_dim(x, max_val=60.0))
    
    # 5. Loại bỏ khuyết MCAR (Giá và Diện tích) & Lọc Outlier thực tế (10 - 500 tr/m2, 10 - 500 m2)
    before_drop = len(df)
    df = df.dropna(subset=['Giá_m2_trieu', 'Diện tích m2']).copy()
    df = df[(df['Diện tích m2'] >= 10.0) & (df['Diện tích m2'] <= 500.0)]
    df = df[(df['Giá_m2_trieu'] >= 10.0) & (df['Giá_m2_trieu'] <= 500.0)]
    print(f"-> Bản ghi hợp lệ sau khi loại bỏ giá trị khuyết và ngoại lệ cực trị: {len(df):,} dòng (Loại {before_drop - len(df)} dòng)")
    
    # 6. Chuẩn hóa BĐS Đất (Số tầng = 0) và cờ thiếu số tầng
    land_patterns = r'đất\s+nền|đất\s+thổ\s+cư|đất\s+dịch\s+vụ|đất\s+nông\s+nghiệp|đất\s+đấu\s+giá|đất\s+phân\s+lô|lô\s+đất|thửa\s+đất|mảnh\s+đất|bán\s+đất'
    mask_land = df['Loại hình nhà ở'].str.contains(r'đất', regex=True) | \
                (df['Địa chỉ'].apply(normalize_vn).str.contains(land_patterns, regex=True) & ~df['Địa chỉ'].apply(normalize_vn).str.contains('cầu đất'))
    df.loc[mask_land, 'Số tầng'] = 0.0
    df.loc[mask_land, 'Loại hình nhà ở'] = 'đất'
    df['Thieu_So_Tang'] = df['Số tầng'].isna().astype(int)
    
    # 7. CHI TIẾT HÓA BẤT ĐỘNG SẢN (38 CỘT ĐẶC TRƯNG)
    # A. Thời gian
    df['nam'] = df['dt'].dt.year.astype(int)
    df['thang'] = df['dt'].dt.month.astype(int)
    df['quy'] = df['dt'].dt.quarter.astype(int)
    df['nam_thang'] = df['dt'].dt.strftime('%Y-%m')
    
    # B. Vị trí & Phố phường
    noi_do = ['quận ba đình', 'quận hoàn kiếm', 'quận tây hồ', 'quận đống đa', 'quận hai bà trưng', 'quận cầu giấy', 'quận thanh xuân']
    df['khu_vuc_noi_do'] = df['Quận'].apply(lambda x: 1 if any(d in x for d in noi_do) else 0)
    streets_wards = df['Địa chỉ'].apply(extract_address_details)
    df['duong_pho'] = [s[0] for s in streets_wards]
    df['phuong_xa'] = [s[1] for s in streets_wards]
    
    # C. Kích thước & Hình dáng
    df['ty_le_dai_rong'] = np.where((df['mat_tien_m'] > 0) & (df['chieu_sau_m'] > 0), df['chieu_sau_m'] / df['mat_tien_m'], np.nan)
    df['hinh_dang_dat'] = df['ty_le_dai_rong'].apply(lambda r: 'Mặt tiền lớn' if r < 1.0 else ('Vuông vắn' if 1.0 <= r <= 2.5 else ('Dài hẹp' if r > 2.5 else 'Không xác định')))
    
    # D. Công năng xây dựng
    df['phan_loai_tang'] = df['Số tầng'].apply(lambda f: 'Thấp tầng (<=3)' if f <= 3 else ('Trung tầng (4-6)' if f <= 6 else ('Cao tầng (>6)' if f > 6 else 'Không rõ')))
    df['tong_dien_tich_san_m2'] = np.where(df['Số tầng'].fillna(1) >= 1, df['Diện tích m2'] * df['Số tầng'].fillna(1), df['Diện tích m2'])
    df['dien_tich_moi_phong_ngu_m2'] = np.where(df['Số phòng ngủ'] > 0, df['Diện tích m2'] / df['Số phòng ngủ'], np.nan)
    df['mat_do_phong_ngu'] = np.where(df['Diện tích m2'] > 0, df['Số phòng ngủ'].fillna(0) / df['Diện tích m2'], np.nan)
    
    # E. Pháp lý & Loại hình chi tiết
    df['co_so_do'] = df['Giấy tờ pháp lý'].apply(lambda x: 1 if 'sổ' in str(x).lower() else 0)
    df['loai_nha_mat_pho'] = df['Loại hình nhà ở'].apply(lambda x: 1 if ('mặt phố' in str(x).lower() or 'mặt tiền' in str(x).lower()) else 0)
    df['loai_nha_ngo_hem'] = df['Loại hình nhà ở'].apply(lambda x: 1 if ('ngõ' in str(x).lower() or 'hẻm' in str(x).lower()) else 0)
    df['loai_can_ho'] = df['Loại hình nhà ở'].apply(lambda x: 1 if ('căn hộ' in str(x).lower() or 'chung cư' in str(x).lower()) else 0)
    df['loai_biet_thu_lien_ke'] = df['Loại hình nhà ở'].apply(lambda x: 1 if ('biệt thự' in str(x).lower() or 'liền kề' in str(x).lower()) else 0)
    
    # F. Định giá & Phân khúc thị trường
    df['Tong_Gia_ty'] = (df['Giá_m2_trieu'] * df['Diện tích m2']) / 1000.0
    df['phan_khuc_tong_gia'] = df['Tong_Gia_ty'].apply(lambda p: 'Bình dân (<3 tỷ)' if p < 3 else ('Trung cấp (3-7 tỷ)' if p < 7 else ('Khá (7-15 tỷ)' if p < 15 else ('Cao cấp (15-30 tỷ)' if p < 30 else 'Siêu sang (>30 tỷ)'))))
    df['phan_khuc_don_gia'] = df['Giá_m2_trieu'].apply(lambda p: 'Rẻ (<60 tr/m²)' if p < 60 else ('Phổ thông (60-100 tr/m²)' if p < 100 else ('Cao (100-180 tr/m²)' if p < 180 else 'Rất cao (>180 tr/m²)')))
    
    df = df.drop(columns=['dt'])
    
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(processed_path, index=False, encoding='utf-8-sig')
    print(f"\n[✅] Đã lưu dữ liệu sạch hoàn chỉnh ({len(df):,} dòng, {len(df.columns)} cột) tại: {processed_path}\n")
    return df

def run_eda(df):
    print("==================================================================")
    print("PHẦN 2: EDA & PHÂN TÍCH TƯƠNG QUAN (VỚI CÁC ĐẶC TRƯNG BĐS CHI TIẾT)")
    print("==================================================================")
    
    figures_dir = "reports/figures"
    os.makedirs(figures_dir, exist_ok=True)
    
    num_cols = ['Giá_m2_trieu', 'Tong_Gia_ty', 'Diện tích m2', 'Số tầng', 'Số phòng ngủ', 
                'mat_tien_m', 'chieu_sau_m', 'khu_vuc_noi_do', 'co_so_do', 'tong_dien_tich_san_m2']
    corr = df[num_cols].corr()
    print("\n--- MA TRẬN HỆ SỐ TƯƠNG QUAN PEARSON ---")
    print(corr.round(4))
    
    # 1. Heatmap Ma trận tương quan
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='RdBu_r', vmin=-1, vmax=1, fmt='.3f', linewidths=0.8)
    plt.title('Ma Trận Tương Quan Giữa Đơn Giá, Tổng Giá & Các Thuộc Tính BĐS Chi Tiết', 
              fontsize=12, fontweight='bold', pad=12)
    plt.tight_layout()
    corr_img_path = os.path.join(figures_dir, '01_correlation_heatmap.png')
    plt.savefig(corr_img_path, dpi=300)
    plt.close()
    print(f"[+] Đã lưu biểu đồ Heatmap: {corr_img_path}")
    
    # 2. Phân phối Đơn giá & Tổng giá nhà (18 tháng gần nhất)
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Subplot 1: Đơn giá (Triệu/m²)
    sns.histplot(df['Giá_m2_trieu'], kde=True, ax=axes[0], color='#2b5c8f', bins=45, stat='count')
    med_p = df['Giá_m2_trieu'].median()
    mean_p = df['Giá_m2_trieu'].mean()
    q25_p = df['Giá_m2_trieu'].quantile(0.25)
    q75_p = df['Giá_m2_trieu'].quantile(0.75)
    
    axes[0].axvline(med_p, color='crimson', linestyle='--', linewidth=2, label=f'Trung vị (Median): {med_p:.1f} tr/m²')
    axes[0].axvline(mean_p, color='darkorange', linestyle='-', linewidth=2, label=f'Trung bình (Mean): {mean_p:.1f} tr/m²')
    axes[0].axvline(q25_p, color='gray', linestyle=':', linewidth=1.5, label=f'Q1 (25%): {q25_p:.1f} tr/m²')
    axes[0].axvline(q75_p, color='gray', linestyle=':', linewidth=1.5, label=f'Q3 (75%): {q75_p:.1f} tr/m²')
    
    axes[0].set_title('Phân Phối Đơn Giá 18 Tháng Gần Nhất (Triệu VNĐ / m²)\n(Phân phối Lệch Phải Tự Nhiên - Right Skewed)', 
                      fontsize=12, fontweight='bold', pad=10)
    axes[0].set_xlabel('Đơn Giá (Triệu VNĐ / m²)', fontsize=11)
    axes[0].set_ylabel('Số lượng tin đăng', fontsize=11)
    axes[0].legend(loc='upper right', frameon=True, fontsize=10)
    axes[0].set_xlim(0, 500)
    
    # Subplot 2: Tổng giá nhà (Tỷ VNĐ)
    tong_gia_subset = df[df['Tong_Gia_ty'] <= 35]['Tong_Gia_ty']
    sns.histplot(tong_gia_subset, kde=True, ax=axes[1], color='#e67e22', bins=45, stat='count')
    med_tot = df['Tong_Gia_ty'].median()
    mean_tot = df['Tong_Gia_ty'].mean()
    
    axes[1].axvline(med_tot, color='crimson', linestyle='--', linewidth=2, label=f'Trung vị (Median): {med_tot:.2f} Tỷ')
    axes[1].axvline(mean_tot, color='navy', linestyle='-', linewidth=2, label=f'Trung bình (Mean): {mean_tot:.2f} Tỷ')
    
    axes[1].set_title('Phân Phối Tổng Giá Bất Động Sản (Tỷ VNĐ)\n(Dải phổ biến ≤ 35 Tỷ - Chiếm > 99.5% dữ liệu)', 
                      fontsize=12, fontweight='bold', pad=10)
    axes[1].set_xlabel('Tổng Giá (Tỷ VNĐ)', fontsize=11)
    axes[1].set_ylabel('Số lượng tin đăng', fontsize=11)
    axes[1].legend(loc='upper right', frameon=True, fontsize=10)
    axes[1].set_xlim(0, 35)
    
    plt.tight_layout()
    dist_img_path = os.path.join(figures_dir, '02_price_distribution.png')
    plt.savefig(dist_img_path, dpi=300)
    plt.close()
    print(f"[+] Đã lưu biểu đồ Phân phối: {dist_img_path}")
    
    # 3. Phân tán: Diện tích & Mặt tiền vs Giá
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Subplot 1: Diện tích vs Tổng giá (Tập trung dải thực tế 10 - 220 m², <= 35 tỷ)
    sample_df = df[(df['Diện tích m2'] <= 220) & (df['Tong_Gia_ty'] <= 35)].sample(min(3500, len(df)), random_state=42)
    sns.regplot(data=sample_df, x='Diện tích m2', y='Tong_Gia_ty', ax=axes[0],
                scatter_kws={'alpha': 0.35, 'color': '#1f77b4', 's': 25}, 
                line_kws={'color': '#d62728', 'linewidth': 2.5})
    axes[0].set_title('Tương Quan Diện Tích (m²) vs Tổng Giá (Tỷ VNĐ)\n(Quy mô diện tích quyết định tổng mức đầu tư)', fontsize=12, fontweight='bold', pad=12)
    axes[0].set_xlabel('Diện tích (m²)', fontsize=11, fontweight='bold')
    axes[0].set_ylabel('Tổng giá (Tỷ VNĐ)', fontsize=11, fontweight='bold')
    axes[0].set_xlim(10, 220)
    axes[0].set_ylim(0, 35)
    
    # Subplot 2: Mặt tiền vs Đơn giá (Tập trung dải mặt tiền thực tế 1.5 - 16m, <= 420 tr/m²)
    sample_mt = df.dropna(subset=['mat_tien_m'])
    sample_mt = sample_mt[(sample_mt['mat_tien_m'] >= 1.5) & (sample_mt['mat_tien_m'] <= 16.0) & (sample_mt['Giá_m2_trieu'] <= 420.0)]
    sample_mt = sample_mt.sample(min(3500, len(sample_mt)), random_state=42)
    
    sns.regplot(data=sample_mt, x='mat_tien_m', y='Giá_m2_trieu', ax=axes[1],
                scatter_kws={'alpha': 0.35, 'color': '#2ca02c', 's': 25}, 
                line_kws={'color': '#ff7f0e', 'linewidth': 2.5})
    axes[1].set_title('Tương Quan Mặt Tiền (m) vs Đơn Giá (Triệu/m²)\n(Mặt tiền lớn gia tăng giá trị thương mại & thanh khoản)', fontsize=12, fontweight='bold', pad=12)
    axes[1].set_xlabel('Mặt tiền (m)', fontsize=11, fontweight='bold')
    axes[1].set_ylabel('Đơn giá (Triệu/m²)', fontsize=11, fontweight='bold')
    axes[1].set_xlim(1.5, 16.0)
    axes[1].set_ylim(20, 420)
    
    plt.tight_layout()
    scatter_img_path = os.path.join(figures_dir, '03_price_vs_area_scatter.png')
    plt.savefig(scatter_img_path, dpi=300)
    plt.close()
    print(f"[+] Đã lưu biểu đồ Scatter: {scatter_img_path}")
    
    # 4. Boxplot Giá theo Quận (Top 12 quận xếp theo Trung vị)
    top_districts = df['Quận'].value_counts().head(12).index
    df_top_dist = df[df['Quận'].isin(top_districts)].copy()
    df_top_dist['Quận_Label'] = df_top_dist['Quận'].str.title()
    order = df_top_dist.groupby('Quận_Label')['Giá_m2_trieu'].median().sort_values(ascending=False).index
    plt.figure(figsize=(14, 6))
    sns.boxplot(data=df_top_dist, x='Quận_Label', y='Giá_m2_trieu', order=order, hue='Quận_Label', palette='Spectral', legend=False)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.title('Phân Bố Đơn Giá 18 Tháng Gần Nhất (Triệu/m²) Theo Quận (Xếp theo Trung vị)', fontsize=12, fontweight='bold')
    plt.xlabel('Quận / Huyện', fontsize=11)
    plt.ylabel('Giá (Triệu/m²)', fontsize=11)
    plt.ylim(0, 500)
    plt.tight_layout()
    dist_box_path = os.path.join(figures_dir, '04_price_by_district_boxplot.png')
    plt.savefig(dist_box_path, dpi=300)
    plt.close()
    print(f"[+] Đã lưu biểu đồ Boxplot theo Quận: {dist_box_path}\n")

def run_modeling(df):
    print("==================================================================")
    print("PHẦN 3: XÂY DỰNG MÔ HÌNH HỒI QUY (VỚI 38 ĐẶC TRƯNG BĐS CHI TIẾT)")
    print("==================================================================")
    
    figures_dir = "reports/figures"
    
    num_cols = [
        'Diện tích m2', 'Số phòng ngủ', 'Số tầng', 'Thieu_So_Tang', 
        'mat_tien_m', 'chieu_sau_m', 'ty_le_dai_rong', 'khu_vuc_noi_do', 
        'co_so_do', 'tong_dien_tich_san_m2', 'dien_tich_moi_phong_ngu_m2', 
        'mat_do_phong_ngu', 'loai_nha_mat_pho', 'loai_nha_ngo_hem', 
        'loai_can_ho', 'loai_biet_thu_lien_ke'
    ]
    # Bỏ 'Loại hình nhà ở' khỏi cat_cols để tránh trùng lặp với các cờ nhị phân loai_nha_*
    cat_cols = ['Quận', 'Giấy tờ pháp lý', 'hinh_dang_dat', 'phan_loai_tang']
    
    X = df[num_cols + cat_cols].copy()
    y = df['Giá_m2_trieu']
    
    num_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', RobustScaler())
    ])
    
    cat_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='khong_ro')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', drop='first'))
    ])
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', num_transformer, num_cols),
            ('cat', cat_transformer, cat_cols)
        ]
    )
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"-> Mẫu Huấn Luyện (Train): {len(X_train):,} | Mẫu Kiểm Thử (Test): {len(X_test):,}\n")
    
    models = {
        'Linear Regression': LinearRegression(),
        'Ridge Regression': Ridge(alpha=10.0),
        'Random Forest': RandomForestRegressor(n_estimators=100, max_depth=16, random_state=42, n_jobs=-1),
        'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=6, random_state=42)
    }
    
    results = []
    trained_pipelines = {}
    
    print(f"{'Mô hình':<22} | {'MAE (Triệu/m²)':<16} | {'RMSE (Triệu/m²)':<16} | {'R² Score':<10}")
    print("-" * 72)
    
    for name, model in models.items():
        pipe = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('model', model)
        ])
        pipe.fit(X_train, y_train)
        preds = pipe.predict(X_test)
        
        mae = mean_absolute_error(y_test, preds)
        rmse = np.sqrt(mean_squared_error(y_test, preds))
        r2 = r2_score(y_test, preds)
        
        results.append({'Model': name, 'MAE': mae, 'RMSE': rmse, 'R2': r2})
        trained_pipelines[name] = pipe
        print(f"{name:<22} | {mae:<16.2f} | {rmse:<16.2f} | {r2:<10.4f}")
        
    results_df = pd.DataFrame(results)
    
    # 5. Biểu đồ so sánh mô hình
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    sns.barplot(data=results_df, x='Model', y='R2', ax=axes[0], hue='Model', palette='Blues_d', legend=False)
    axes[0].set_title('So Sánh R² Score Trên Dữ Liệu 18 Tháng (Càng cao càng tốt)', fontweight='bold')
    axes[0].set_ylim(0, 1.0)
    for p in axes[0].patches:
        axes[0].annotate(f"{p.get_height():.3f}", (p.get_x() + p.get_width() / 2., p.get_height()),
                         ha='center', va='bottom', fontsize=10, xytext=(0, 3), textcoords='offset points')
        
    sns.barplot(data=results_df, x='Model', y='MAE', ax=axes[1], hue='Model', palette='Reds_d', legend=False)
    axes[1].set_title('So Sánh MAE (Sai số đơn giá - Càng thấp càng tốt)', fontweight='bold')
    for p in axes[1].patches:
        axes[1].annotate(f"{p.get_height():.2f}", (p.get_x() + p.get_width() / 2., p.get_height()),
                         ha='center', va='bottom', fontsize=10, xytext=(0, 3), textcoords='offset points')
    plt.tight_layout()
    compare_img_path = os.path.join(figures_dir, '05_model_comparison.png')
    plt.savefig(compare_img_path, dpi=300)
    plt.close()
    print(f"\n[+] Đã lưu biểu đồ so sánh mô hình: {compare_img_path}")
    
    # Lưu mô hình tốt nhất
    best_model_name = results_df.sort_values(by='R2', ascending=False).iloc[0]['Model']
    best_pipe = trained_pipelines[best_model_name]
    save_path = 'house_price_model.pkl'
    joblib.dump(best_pipe, save_path)
    print(f"\n[🏆] Mô hình xuất sắc nhất: {best_model_name}")
    print(f"[🏆] Đã lưu Pipeline vào: {save_path}")
    
    # 6. Feature Importance từ Random Forest
    rf_model = trained_pipelines['Random Forest'].named_steps['model']
    ohe = trained_pipelines['Random Forest'].named_steps['preprocessor'].named_transformers_['cat'].named_steps['onehot']
    cat_feature_names = ohe.get_feature_names_out(cat_cols).tolist()
    all_feature_names = num_cols + cat_feature_names
    
    importances = rf_model.feature_importances_
    feat_df = pd.DataFrame({'Feature': all_feature_names, 'Importance': importances}).sort_values(by='Importance', ascending=False)
    
    plt.figure(figsize=(12, 7))
    sns.barplot(data=feat_df.head(15), x='Importance', y='Feature', hue='Feature', palette='viridis', legend=False)
    plt.title('Top 15 Đặc Trưng Quan Trọng Nhất Quyết Định Giá Nhà (Random Forest)', fontsize=12, fontweight='bold')
    plt.xlabel('Mức độ ảnh hưởng (Importance Score)', fontsize=11)
    plt.ylabel('Tên đặc trưng', fontsize=11)
    plt.tight_layout()
    feat_img_path = os.path.join(figures_dir, '06_feature_importance.png')
    plt.savefig(feat_img_path, dpi=300)
    plt.close()
    print(f"[+] Đã lưu biểu đồ Feature Importance: {feat_img_path}\n")

def main():
    df_clean = run_data_cleaning()
    run_eda(df_clean)
    run_modeling(df_clean)
    print("==================================================================")
    print("🎉 HOÀN TẤT TOÀN BỘ PIPELINE, BÁO CÁO & MÔ HÌNH THÀNH CÔNG! 🎉")
    print("==================================================================")

if __name__ == "__main__":
    main()
