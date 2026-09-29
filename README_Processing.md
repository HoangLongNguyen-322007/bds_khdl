# QUY TRÌNH CHUẨN HÓA VÀ LÀM SẠCH DỮ LIỆU BẤT ĐỘNG SẢN
*(Tài liệu dàn ý 15 Slides - Giải thích chi tiết, chuyên sâu về Phân tích Dữ liệu)*

---

## SLIDE 1: TIÊU ĐỀ & BỐI CẢNH DỰ ÁN
*   **Thực trạng Dữ liệu (Pain Points):** Dữ liệu thu thập trực tiếp từ các trang web rao vặt luôn tồn tại 4 vấn đề lớn:
    1. Chứa "tin ảo" (nhà siêu nhỏ giá siêu cao).
    2. Lỗi định dạng chữ (dính liền chữ và số: "50 m2", "3 tỷ").
    3. Lỗi font tiếng Việt (gõ sai chính tả, khác bảng mã).
    4. Rất nhiều thông tin bị người đăng bỏ trống.
*   **Nhu cầu cấp thiết:** Nếu tính toán và vẽ biểu đồ ngay trên mớ dữ liệu hỗn độn này, toàn bộ báo cáo sẽ bị sai lệch hoàn toàn.

---

## SLIDE 2: MỤC TIÊU & QUY TRÌNH 6 BƯỚC CỐT LÕI
*   **Mục tiêu:** Xây dựng một luồng xử lý tự động (Data Pipeline) bằng thư viện Pandas để gột rửa dữ liệu thô thành Dữ liệu sạch 100%.
*   **6 Bước Tiền xử lý (Preprocessing Pipeline):**
    1. **Data Audit:** "Khám bệnh" toàn diện dữ liệu.
    2. **Basic Cleaning:** Dọn dẹp cột thừa và xóa tin rao lặp lại.
    3. **Consistency:** Chuẩn hóa tiếng Việt và bóc tách con số.
    4. **Missing Values:** Xử lý các ô dữ liệu bị bỏ trống.
    5. **Outliers:** Trị các "tin ảo" bằng quy tắc thống kê.
    6. **Encoding & Scaling:** Số hóa văn bản để máy tính hiểu.

---

## SLIDE 3: BƯỚC 1.1 - LÝ THUYẾT: KIỂM TOÁN DỮ LIỆU
*   **Chi tiết vấn đề:** Khi nhận được một bộ dữ liệu lớn gồm hàng chục ngàn dòng, ta không thể mở Excel ra xem bằng mắt thường. 
*   **Giải pháp:** Ta cần định nghĩa một hàm Python đóng vai trò như "máy chụp X-Quang" để quét toàn bộ hệ thống dữ liệu chỉ trong 1 giây, từ đó chỉ ra những "căn bệnh" đang tồn tại.

---

## SLIDE 4: BƯỚC 1.2 - THỰC THI: CHẠY LỆNH KIỂM TOÁN
*   **Ảnh Code minh họa:**
```python
# Đọc file dữ liệu thô (định dạng utf-8 để đọc tiếng Việt)
df = pd.read_csv("data/raw/bds_raw_hanoi_ultimate.csv", encoding='utf-8')

# 1. Kích thước (Shape): Bảng dữ liệu có bao nhiêu dòng, bao nhiêu cột?
print(df.shape) 

# 2. Kiểu dữ liệu (Info): Cột 'Giá' đang là Chữ hay Số?
df.info() 

# 3. Đếm ô trống (Isna): Cột nào bị người dùng bỏ trống nhiều nhất?
print(df.isna().sum()) 

# 4. Đếm trùng lặp (Duplicated): Có bao nhiêu tin rao bán bị copy giống hệt nhau?
print(df.duplicated().sum())
```

---

## SLIDE 5: BƯỚC 2.1 - LOẠI BỎ CỘT RÁC HỆ THỐNG
*   **Phân tích chuyên sâu:** Quá trình lưu file thô thường tự động sinh ra một cột đếm số thứ tự có tên là `Unnamed: 0`. Cột này không mang bất kỳ thông tin nào về ngôi nhà, giữ lại chỉ làm nặng quá trình tính toán.
*   **Ảnh Code minh họa:**
```python
# Kiểm tra nếu tồn tại cột rác 'Unnamed: 0' thì sử dụng lệnh drop để xóa sạch
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])
```

---

## SLIDE 6: BƯỚC 2.2 - XÓA BẢN GHI TRÙNG LẶP (DUPLICATE)
*   **Phân tích chuyên sâu:** Một môi giới có thể đăng 1 căn nhà lên nhiều trang khác nhau. Nếu phân tích trên dữ liệu này, việc tính "Mức giá trung bình của 1 quận" sẽ bị kéo lệch hoàn toàn về phía căn nhà bị lặp đó.
*   **Ảnh Code minh họa:**
```python
# Lệnh drop_duplicates tự động quét và so sánh từng chữ của tất cả các cột.
# Nếu phát hiện 2 dòng giống hệt nhau 100%, nó sẽ xóa bản sao và giữ lại 1 bản gốc.
df = df.drop_duplicates()
```

---

## SLIDE 7: BƯỚC 3.1 - VẤN ĐỀ CỦA DỮ LIỆU CHỮ (TEXT)
*   **Chi tiết khó khăn:** Máy tính rất máy móc. Dữ liệu gõ tay từ người dùng sẽ gây ra 3 lỗi khiến hệ thống không thể gom nhóm (Groupby):
    1. **Lỗi viết hoa/thường:** "Cầu Giấy", "CẦU GIẤY", và "cầu giấy" bị đếm thành 3 quận.
    2. **Lỗi khoảng trắng:** Vô tình bấm phím cách " Cầu Giấy ".
    3. **Lỗi bảng mã:** Cùng một chữ nhưng gõ bằng chuẩn Unicode khác nhau sẽ bị tách rời dấu (Cầu Giấy).

---

## SLIDE 8: BƯỚC 3.2 - HÀM CHUẨN HÓA VĂN BẢN (NORMALIZATION)
*   **Mục tiêu:** Viết một hàm Python duy nhất để giải quyết dứt điểm 3 lỗi ở Slide 7.
*   **Ảnh Code minh họa:**
```python
import unicodedata

def normalize_vn(text):
    if pd.isna(text): return text # Bỏ qua nếu ô bị trống
    
    text = str(text) # Ép về dạng chuỗi văn bản
    
    # 1. Ép về chuẩn Unicode NFC (Sửa dứt điểm lỗi font chữ tiếng Việt)
    text = unicodedata.normalize('NFC', text) 
    
    # 2. lower(): Ép thành chữ thường 100%
    # 3. strip(): Cắt gọt khoảng trắng thừa ở 2 đầu
    return text.lower().strip()
```

---

## SLIDE 9: BƯỚC 3.3 - ÁP DỤNG CHUẨN HÓA VĂN BẢN
*   **Chi tiết thực thi:** Thay vì sửa tay từng dòng Excel, ta dùng lệnh `.apply()` của Pandas để chạy hàm chuẩn hóa lướt qua hàng ngàn dòng chỉ trong 1 giây.
*   **Ảnh Code minh họa:**
```python
# Áp dụng hàm normalize_vn lên tất cả các cột chứa phân loại (văn bản)
df['Quận'] = df['Quận'].apply(normalize_vn)
df['Loại hình nhà ở'] = df['Loại hình nhà ở'].apply(normalize_vn)
df['Giấy tờ pháp lý'] = df['Giấy tờ pháp lý'].apply(normalize_vn)
```

---

## SLIDE 10: BƯỚC 3.4 - BÓC TÁCH CON SỐ TỪ CHUỖI (EXTRACTION)
*   **Phân tích chuyên sâu:** Phần mềm không thể tính toán cộng trừ trên một cụm từ như `2,5 triệu/m2`. Bắt buộc phải bóc tách lấy đúng con số `2.5`. Hơn nữa, chuẩn quốc tế dùng dấu chấm (`.`) cho số thập phân, ta phải đồng bộ hóa.
*   **Ảnh Code minh họa:**
```python
def clean_price(x):
    if pd.isna(x): return np.nan
    
    # 1. replace: Xóa bỏ chữ "triệu/m2"
    # 2. replace: Đổi dấu phẩy thành dấu chấm để chuẩn hóa thập phân
    s = str(x).lower().replace('triệu/m²', '').replace('triệu/m2', '').replace(',', '.').strip()
    
    # 3. float(): Ép chuỗi văn bản thành Số Thực (có phần thập phân) để tính toán
    try: return float(s) 
    except: return np.nan

df['Giá_m2_trieu'] = df['Giá/m2'].apply(clean_price)
```

---

## SLIDE 11: BƯỚC 4.1 - HAI CHIẾN LƯỢC XỬ LÝ KHUYẾT THIẾU
*   **Chiến lược 1 (Cắt bỏ hoàn toàn):** Áp dụng cho thông tin Cốt lõi (Giá, Diện tích). Nếu người bán không nhập, ta **bắt buộc phải xóa bỏ dòng đó**. Tuyệt đối không được tự suy đoán hay "bịa" ra giá nhà vì sẽ phá hỏng tính trung thực của báo cáo.
*   **Chiến lược 2 (Tạo Cờ hiệu):** Áp dụng cho thông tin Phụ (Ví dụ: Số tầng). Một mảnh đất nền sẽ tự nhiên không có số tầng. Ta không xóa để tránh phí dữ liệu, mà sẽ **Tạo một cờ hiệu** báo cáo "Nhà này không có tầng".

---

## SLIDE 12: BƯỚC 4.2 - THỰC THI: XÓA BỎ & ĐÁNH CỜ HIỆU
*   **Mục tiêu:** Dịch 2 chiến lược từ Slide 11 thành mã lệnh can thiệp.
*   **Ảnh Code minh họa:**
```python
# 1. CHIẾN LƯỢC XÓA BỎ (DROP)
# Lệnh dropna sẽ quét, thấy ô nào là NaN (trống) ở Giá/Diện tích thì xóa cả dòng đó.
df = df.dropna(subset=['Giá_m2_trieu', 'Diện tích m2'])

# 2. CHIẾN LƯỢC TẠO CỜ HIỆU (INDICATOR)
# isna(): Kiểm tra ô trống. astype(int): Biến True/False thành 1 và 0.
# Tạo ra cột mới chứa số 1 (Nếu thiếu số tầng) và 0 (Nếu có số tầng)
df['Thieu_So_Tang'] = df['Số tầng'].isna().astype(int)
```

---

## SLIDE 13: BƯỚC 5.1 - LÝ THUYẾT GIÁ TRỊ NGOẠI LỆ (OUTLIERS)
*   **Phân tích chuyên sâu:** "Tin ảo" (nhà hẻm 10m2 bán 100 tỷ) là những điểm Ngoại lệ (Outliers). Nó kéo mức giá trung bình của cả quận vọt lên sai sự thật.
*   **Cách trị (Quy tắc IQR):** 
    1. Chia dữ liệu làm 4 phần. Tìm mức phân vị 25% (Q1) và 75% (Q3) để lấy ra phần đông phổ biến nhất ở giữa.
    2. Dùng công thức thống kê tính ra một **Mức trần**. Giá nào vượt qua mức này đều bị coi là bất thường.

---

## SLIDE 14: BƯỚC 5.2 - KỸ THUẬT "CẮT NGỌN" (CLIPPING) NGOẠI LỆ
*   **Mục tiêu:** Thay vì xóa bỏ (làm thất thoát lượng lớn dữ liệu), ta dùng kỹ thuật "Cắt ngọn". Tức là ép mọi căn nhà siêu đắt lùi về bằng đúng với Mức trần vừa tính toán được.
*   **Ảnh Code minh họa:**
```python
# 1. Tìm Mức trần và Mức sàn của thị trường
Q1 = df['Giá_m2_trieu'].quantile(0.25)
Q3 = df['Giá_m2_trieu'].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + 1.5 * IQR  # Tính ra Mức trần tối đa

# 2. Lệnh clip(): Lưỡi dao cắt ngọn
# Ép mọi giá trị lớn hơn upper_bound xuống bằng đúng upper_bound
df['Giá_m2_trieu'] = df['Giá_m2_trieu'].clip(lower=0, upper=upper_bound)
```

---

## SLIDE 15: BƯỚC 6 - ĐÓNG GÓI BẰNG PIPELINE (CHUẨN HÓA ĐỊNH DẠNG)
*   **Phân tích chuyên sâu:** Để đưa vào các phần mềm tính toán và trực quan hóa mạnh mẽ nhất, dữ liệu cần 1 bước "số hóa" cuối cùng.
    *   *Scale:* Đưa các con số siêu lớn (tiền tỷ) và siêu nhỏ (số tầng) về chung một tỷ lệ.
    *   *Encode:* Biến toàn bộ chữ (VD: Quận Cầu Giấy) thành mã nhị phân 0 và 1.
*   **Ảnh Code minh họa:**
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, RobustScaler
from sklearn.impute import SimpleImputer

# Dây chuyền cho cột SỐ: Điền trung vị -> Chuẩn hóa thang đo tỷ lệ
num_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', RobustScaler())
])

# Dây chuyền cho cột CHỮ: Điền 'khong_ro' -> Mã hóa thành dãy số 0 và 1
cat_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='khong_ro')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', drop='first'))
])
```
