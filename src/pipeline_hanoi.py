import pandas as pd
import numpy as np
import os
import re
import unicodedata
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, RobustScaler

def normalize_vn(text):
    if pd.isna(text):
        return ''
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

def run_pipeline():
    raw_file = "data/raw/raw.csv"
    if not os.path.exists(raw_file):
        print(f"Không tìm thấy dữ liệu thô tại {raw_file}!")
        return
        
    print("=" * 65)
    print("🚀 TIỀN XỬ LÝ & CHI TIẾT HÓA BẤT ĐỘNG SẢN (18 THÁNG GẦN NHẤT) 🚀")
    print("=" * 65)
    df = pd.read_csv(raw_file, encoding='utf-8', low_memory=False)
    print(f"1. Tổng số dòng dữ liệu thô: {len(df):,} bản ghi")
    
    # 1. Lọc theo thời gian: Chỉ lấy 18 tháng gần nhất tính từ thời điểm cập nhật mới nhất
    df['dt'] = pd.to_datetime(df['Ngày'], errors='coerce')
    max_date = df['dt'].max()
    cutoff_date = max_date - pd.DateOffset(months=18)
    print(f"2. Lọc thời gian: Từ {cutoff_date.strftime('%Y-%m-%d')} đến {max_date.strftime('%Y-%m-%d')} (18 tháng gần nhất)")
    df = df[df['dt'] >= cutoff_date].copy()
    print(f"   -> Số lượng sau lọc thời gian: {len(df):,} bản ghi")
    
    # 2. Xóa trùng lặp
    df = df.drop_duplicates()
    
    # 3. Chuẩn hóa văn bản cơ bản
    df['Quận'] = df['Quận'].apply(normalize_vn)
    df['Huyện'] = df['Huyện'].apply(normalize_vn)
    df['Loại hình nhà ở'] = df['Loại hình nhà ở'].apply(normalize_vn)
    df['Giấy tờ pháp lý'] = df['Giấy tờ pháp lý'].apply(normalize_vn)
    
    # 4. Ép kiểu số học
    df['Diện tích m2'] = df['Diện tích'].apply(clean_area)
    df['Giá_m2_trieu'] = df['Giá/m2'].apply(clean_price)
    df['Số phòng ngủ'] = df['Số phòng ngủ'].apply(clean_rooms)
    df['Số tầng'] = pd.to_numeric(df['Số tầng'], errors='coerce')
    df['mat_tien_m'] = df['Rộng'].apply(lambda x: clean_dim(x, max_val=30.0))
    df['chieu_sau_m'] = df['Dài'].apply(lambda x: clean_dim(x, max_val=60.0))
    
    # 5. Lọc bỏ thiếu Giá hoặc Diện tích và lọc Outlier theo miền thực tế (10 - 500 tr/m2, 10 - 500 m2)
    df = df.dropna(subset=['Giá_m2_trieu', 'Diện tích m2']).copy()
    df = df[(df['Diện tích m2'] >= 10.0) & (df['Diện tích m2'] <= 500.0)]
    df = df[(df['Giá_m2_trieu'] >= 10.0) & (df['Giá_m2_trieu'] <= 500.0)]
    
    # 6. Chuẩn hóa BĐS Đất (Số tầng = 0) và cờ thiếu số tầng
    land_patterns = r'đất\s+nền|đất\s+thổ\s+cư|đất\s+dịch\s+vụ|đất\s+nông\s+nghiệp|đất\s+đấu\s+giá|đất\s+phân\s+lô|lô\s+đất|thửa\s+đất|mảnh\s+đất|bán\s+đất'
    mask_land = df['Loại hình nhà ở'].str.contains(r'đất', regex=True) | \
                (df['Địa chỉ'].apply(normalize_vn).str.contains(land_patterns, regex=True) & ~df['Địa chỉ'].apply(normalize_vn).str.contains('cầu đất'))
    df.loc[mask_land, 'Số tầng'] = 0.0
    df.loc[mask_land, 'Loại hình nhà ở'] = 'đất'
    df['Thieu_So_Tang'] = df['Số tầng'].isna().astype(int)
    
    # 7. CHI TIẾT HÓA BẢN GHI (TĂNG SỐ LƯỢNG CỘT TÍNH NĂNG)
    # A. Thời gian
    df['nam'] = df['dt'].dt.year.astype(int)
    df['thang'] = df['dt'].dt.month.astype(int)
    df['quy'] = df['dt'].dt.quarter.astype(int)
    df['nam_thang'] = df['dt'].dt.strftime('%Y-%m')
    
    # B. Vị trí & Khu vực
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
    
    # Loại bỏ cột phụ dt
    df = df.drop(columns=['dt'])
    
    # Lưu file
    os.makedirs("data/processed", exist_ok=True)
    out_file = "data/processed/clean.csv"
    df.to_csv(out_file, index=False, encoding='utf-8-sig')
    print(f"\n[✅] HOÀN TẤT! Đã lưu {len(df):,} bản ghi sạch với {len(df.columns)} cột chi tiết tại: {out_file}")

if __name__ == "__main__":
    run_pipeline()
