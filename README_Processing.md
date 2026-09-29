# QUY TRÌNH CHUẨN HÓA VÀ LÀM SẠCH DỮ LIỆU (TỪ A-Z)
*(Tài liệu có kèm Code minh họa - Dành riêng để thiết kế Slide Thuyết Trình)*

---

## SLIDE 1: TỔNG QUAN QUY TRÌNH
*   **Vấn đề:** Dữ liệu thu thập từ Internet (Raw Data) luôn tồn tại nhiều rác, sai định dạng, và thiếu sót.
*   **Mục tiêu:** Biến đổi dữ liệu thô thành Dữ liệu sạch (Clean Data) chuẩn mực để máy tính phân tích.
*   **Quy trình 6 bước cốt lõi:**
    1. Kiểm toán dữ liệu.
    2. Dọn rác cơ bản & Xóa trùng lặp.
    3. Chuẩn hóa Văn bản & Ép kiểu Số liệu.
    4. Xử lý Dữ liệu Khuyết thiếu (Missing).
    5. Xử lý Giá trị Ngoại lệ (Outlier).
    6. Mã hóa dữ liệu cho Máy tính (Encoding).

---

## SLIDE 2: BƯỚC 1 - KIỂM TOÁN DỮ LIỆU (DATA AUDIT)
*   **Mục tiêu:** Khám bệnh cho dữ liệu trước khi xử lý (đo kích thước, tìm lỗ hổng missing, tìm duplicate).
*   **Ảnh Code minh họa (Chụp phần này đưa lên slide):**
```python
def audit_data(df: pd.DataFrame):
    print("1. KÍCH THƯỚC (Dòng, Cột):", df.shape)
    print("2. THÔNG TIN KIỂU DỮ LIỆU:")
    df.info()
    print("3. SỐ LƯỢNG Ô BỊ TRỐNG (MISSING):\n", df.isna().sum())
    print("4. SỐ DÒNG TRÙNG LẶP HOÀN TOÀN:", df.duplicated().sum())

# Đọc file thô và tiến hành kiểm toán
df = pd.read_csv("data/raw/bds_raw_hanoi_ultimate.csv", encoding='utf-8')
audit_data(df)
```

---

## SLIDE 3: BƯỚC 2 - DỌN DẸP CƠ BẢN
*   **Mục tiêu:** Xóa cột rác sinh ra do lỗi hệ thống và xóa các dòng dữ liệu bị cào trùng lặp.
*   **Ảnh Code minh họa:**
```python
# 1. Xóa cột rác vô nghĩa (nếu có)
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])

# 2. Xóa toàn bộ các bản ghi bị trùng lặp
df = df.drop_duplicates()
```

---

## SLIDE 4: BƯỚC 3.1 - CHUẨN HÓA VĂN BẢN (TEXT NORMALIZATION)
*   **Mục tiêu:** Tránh lỗi font chữ tiếng Việt, đưa tất cả về chữ thường và cắt bỏ khoảng trắng thừa.
*   **Ảnh Code minh họa:**
```python
import unicodedata

def normalize_vn(text):
    if pd.isna(text): return text
    text = str(text)
    # Ép chuẩn Unicode NFC để chống lỗi font tiếng Việt
    text = unicodedata.normalize('NFC', text) 
    # Đưa về chữ thường và xóa dấu cách thừa ở 2 đầu
    return text.lower().strip()

# Áp dụng hàm chuẩn hóa cho các cột dạng chữ
df['Quận'] = df['Quận'].apply(normalize_vn)
df['Loại hình nhà ở'] = df['Loại hình nhà ở'].apply(normalize_vn)
df['Giấy tờ pháp lý'] = df['Giấy tờ pháp lý'].apply(normalize_vn)
```

---

## SLIDE 5: BƯỚC 3.2 - ÉP KIỂU SỐ LIỆU (DATA EXTRACTION)
*   **Mục tiêu:** Bóc tách chữ khỏi số (xóa "triệu/m2", xóa "phòng"), đổi dấu phẩy thành dấu chấm để máy tính hiểu đúng.
*   **Ảnh Code minh họa:**
```python
def clean_price(x):
    if pd.isna(x): return np.nan
    # Xóa chữ "triệu/m2" và đổi dấu phẩy (,) thành dấu chấm (.)
    s = str(x).lower().replace('triệu/m²', '').replace('triệu/m2', '').replace(',', '.').strip()
    try: 
        return float(s) # Ép về kiểu số thực
    except: 
        return np.nan

# Áp dụng để biến cột Giá từ Chữ sang Số
df['Giá_m2_trieu'] = df['Giá/m2'].apply(clean_price)

# Ép kiểu cho Số tầng (lỗi sẽ tự thành NaN)
df['Số tầng'] = pd.to_numeric(df['Số tầng'], errors='coerce')
```

---

## SLIDE 6: BƯỚC 4 - XỬ LÝ DỮ LIỆU KHUYẾT THIẾU (MISSING VALUES)
*   **Mục tiêu:** Xóa những dòng thiếu dữ liệu sinh tử (Giá, Diện tích). Tạo cờ đánh dấu cho thông tin phụ (Số tầng).
*   **Ảnh Code minh họa:**
```python
# CHIẾN LƯỢC 1: CẮT BỎ (MCAR)
# Bắt buộc xóa các dòng không có thông tin Giá hoặc Diện tích
df = df.dropna(subset=['Giá_m2_trieu', 'Diện tích m2'])

# CHIẾN LƯỢC 2: TẠO CỜ HIỆU (MNAR)
# Đất nền thường không có số tầng -> Tạo cột đánh dấu (1 = Thiếu, 0 = Có)
df['Thieu_So_Tang'] = df['Số tầng'].isna().astype(int)
```

---

## SLIDE 7: BƯỚC 5 - XỬ LÝ GIÁ TRỊ NGOẠI LỆ (OUTLIERS)
*   **Mục tiêu:** Dùng quy tắc IQR để tìm ra Mức trần. Ép giá của các căn nhà "siêu đắt" lùi về bằng Mức trần (Clipping) thay vì xóa.
*   **Ảnh Code minh họa:**
```python
# 1. Tính toán Mức sàn (Q1) và Mức trần (Q3)
Q1 = df['Giá_m2_trieu'].quantile(0.25)
Q3 = df['Giá_m2_trieu'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = max(0, Q1 - 1.5 * IQR) # Không cho giá âm
upper_bound = Q3 + 1.5 * IQR         # Giới hạn giá trần

# 2. Kỹ thuật Cắt ngọn (Clipping)
# Mọi căn nhà có giá cao hơn upper_bound sẽ bị ép bằng đúng upper_bound
df['Giá_m2_trieu'] = df['Giá_m2_trieu'].clip(lower=lower_bound, upper=upper_bound)
```

---

## SLIDE 8: BƯỚC 6 - MÃ HÓA CHO MÁY TÍNH (ENCODING & SCALING)
*   **Mục tiêu:** Đưa toàn bộ ngôn ngữ con người (chữ) sang mã nhị phân (One-Hot) và đồng nhất tỷ lệ các con số (Scaling).
*   **Ảnh Code minh họa:**
```python
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, RobustScaler

# 1. Pipeline xử lý biến Số (Điền trung vị -> Chuẩn hóa Robust)
num_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', RobustScaler())
])

# 2. Pipeline xử lý biến Chữ (Điền chữ 'khong_ro' -> Mã hóa 0/1)
cat_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='khong_ro')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', drop='first'))
])
```
