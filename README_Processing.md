# QUY TRÌNH CHUẨN HÓA VÀ LÀM SẠCH DỮ LIỆU BẤT ĐỘNG SẢN
*(Tài liệu dàn ý 15 Slides - Giải thích cặn kẽ từng dòng code cho Phân tích Dữ liệu)*

---

## SLIDE 1: TIÊU ĐỀ & BỐI CẢNH DỰ ÁN
*   **Thực trạng Dữ liệu thô (Raw Data):** Dữ liệu thu thập trực tiếp từ các trang web rao vặt bất động sản vô cùng lộn xộn. Các con số bị dính liền với chữ ("50 m2", "3 tỷ"), font chữ tiếng Việt không đồng nhất, thông tin bị khuyết thiếu trầm trọng, và chứa các tin rao bán ảo (giá trên trời).
*   **Mục tiêu giải quyết:** Xây dựng một luồng xử lý (Data Pipeline) tự động hóa bằng Python và thư viện Pandas để "gột rửa" dữ liệu thô thành một bảng Dữ liệu sạch (Clean Data).
*   **Kết quả kỳ vọng:** Dữ liệu chuẩn mực 100%, sẵn sàng đưa vào các biểu đồ trực quan hóa (Data Visualization), tính toán thống kê và xây dựng các mô hình dự báo giá nhà.

---

## SLIDE 2: 6 BƯỚC CỐT LÕI CỦA QUY TRÌNH (PIPELINE)
*   **Bước 1 - Data Audit:** "Khám bệnh" toàn diện để tìm ra lỗi của dữ liệu.
*   **Bước 2 - Basic Cleaning:** Dọn dẹp các cột dư thừa và xóa các tin rao lặp lại.
*   **Bước 3 - Consistency:** Chuẩn hóa định dạng tiếng Việt và bóc tách con số thuần túy.
*   **Bước 4 - Missing Values:** Xử lý các ô dữ liệu bị người dùng bỏ trống.
*   **Bước 5 - Outliers:** Trị các "tin ảo" (giá trị ngoại lệ) bằng các quy tắc thống kê.
*   **Bước 6 - Encoding & Scaling:** Số hóa ngôn ngữ văn bản để phục vụ phân tích chuyên sâu.

---

## SLIDE 3: BƯỚC 1.1 - ĐỌC VÀ KIỂM TOÁN DỮ LIỆU (DATA AUDIT)
*   **Chi tiết vấn đề:** Khi nhận được một bộ dữ liệu lớn, ta không thể mở Excel ra xem từng dòng. Ta cần một hàm Python đóng vai trò như "máy chụp X-Quang" để quét toàn bộ dữ liệu chỉ trong 1 giây.
*   **Ảnh Code minh họa (Định nghĩa hàm):**
```python
# Định nghĩa hàm audit_data sử dụng các công cụ của Pandas
def audit_data(df: pd.DataFrame):
    # Lệnh .shape trả về (số_dòng, số_cột)
    print("1. KÍCH THƯỚC (Dòng, Cột):", df.shape)
    
    # Lệnh .info() cho biết kiểu dữ liệu của từng cột (chữ hay số)
    print("2. THÔNG TIN KIỂU DỮ LIỆU:")
    df.info() 
    
    # Lệnh .isna().sum() đếm tổng số ô bị trống (NaN) trong mỗi cột
    print("3. SỐ LƯỢNG Ô BỊ TRỐNG (MISSING):\n", df.isna().sum())
    
    # Lệnh .duplicated().sum() đếm số dòng giống hệt nhau 100%
    print("4. SỐ DÒNG TRÙNG LẶP HOÀN TOÀN:", df.duplicated().sum())
```

---

## SLIDE 4: BƯỚC 1.2 - CHẠY KIỂM TOÁN THỰC TẾ
*   **Chi tiết thực thi:** Tải file `.csv` thô vào bộ nhớ Pandas và kích hoạt hàm "khám bệnh" vừa tạo.
*   **Ảnh Code minh họa:**
```python
# Sử dụng pd.read_csv với chuẩn mã hóa utf-8 để đọc được dấu tiếng Việt
df = pd.read_csv("data/raw/bds_raw_hanoi_ultimate.csv", encoding='utf-8')

# Kích hoạt quá trình chụp chiếu dữ liệu
audit_data(df)
```
*   **Kết luận từ kiểm toán:** Kết quả in ra cho thấy có hàng loạt dòng bị trùng lặp do công cụ thu thập web cào đi cào lại 1 trang, và cột "Giá" đang bị hệ thống hiểu lầm là Văn bản (Object) thay vì Số thực (Float).

---

## SLIDE 5: BƯỚC 2.1 - LOẠI BỎ CỘT RÁC HỆ THỐNG
*   **Chi tiết vấn đề:** Quá trình lưu trữ file trước đó đã sinh ra một cột đánh số thứ tự mặc định tên là `Unnamed: 0`. Cột này không mang thông tin gì về ngôi nhà, giữ lại chỉ làm nặng quá trình phân tích.
*   **Ảnh Code minh họa:**
```python
# Kiểm tra nếu tồn tại cột rác 'Unnamed: 0' thì sử dụng lệnh drop để xóa
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])
```
*   **Giải thích Code:** Lệnh `df.drop(columns=[...])` sẽ gỡ bỏ hoàn toàn cột được chỉ định khỏi bảng dữ liệu.

---

## SLIDE 6: BƯỚC 2.2 - XÓA BẢN GHI TRÙNG LẶP (DUPLICATE)
*   **Chi tiết vấn đề:** Một môi giới có thể đăng 1 căn nhà lên nhiều trang khác nhau. Nếu phân tích trên dữ liệu trùng lặp, các con số trung bình và biểu đồ thống kê sẽ bị sai lệch (bị kéo về phía dữ liệu bị lặp).
*   **Ảnh Code minh họa:**
```python
# Xóa toàn bộ các dòng giống hệt nhau 100% (Chỉ giữ lại 1 bản gốc duy nhất)
df = df.drop_duplicates()
```
*   **Giải thích Code:** Hàm `drop_duplicates()` tự động quét tất cả các cột. Bất cứ khi nào nó phát hiện 2 dòng có thông tin y hệt nhau từng chữ một, nó sẽ xóa dòng thứ 2 trở đi.

---

## SLIDE 7: BƯỚC 3.1 - VẤN ĐỀ CỦA DỮ LIỆU CHỮ (TEXT) TRONG TIẾNG VIỆT
*   **Chi tiết khó khăn:** Do thói quen gõ phím của mỗi người dùng khác nhau, dữ liệu sẽ cực kỳ "bẩn":
    1. **Lỗi viết hoa/thường:** "Cầu Giấy", "CẦU GIẤY", và "cầu giấy" bị hệ thống đếm thành 3 quận khác nhau.
    2. **Lỗi khoảng trắng:** Người dùng vô tình bấm phím cách " Cầu Giấy " khiến hệ thống không nhận diện được.
    3. **Lỗi bảng mã:** Cùng một chữ nhưng gõ bằng các chuẩn Unicode khác nhau (NFC vs NFD) sẽ bị tách rời dấu.
*   **Hướng giải quyết:** Đưa mọi thứ về một tiêu chuẩn duy nhất: Unicode NFC, viết thường, và xóa khoảng trắng thừa.

---

## SLIDE 8: BƯỚC 3.2 - HÀM CHUẨN HÓA VĂN BẢN (NORMALIZATION)
*   **Chi tiết thực thi:** Viết một hàm chuyên dụng bằng Python để khắc phục triệt để 3 lỗi ở Slide 7.
*   **Ảnh Code minh họa:**
```python
import unicodedata

def normalize_vn(text):
    # Dùng pd.isna() kiểm tra: Nếu ô đó bị trống thì bỏ qua không xử lý
    if pd.isna(text): return text
    
    text = str(text) # Đảm bảo dữ liệu được ép về dạng Chuỗi
    
    # 1. unicodedata.normalize: Ép về chuẩn Unicode NFC để sửa lỗi font
    text = unicodedata.normalize('NFC', text) 
    
    # 2. lower(): Đưa mọi chữ cái về viết thường (lowercase)
    # 3. strip(): Cắt gọt khoảng trắng thừa ở đầu và cuối chuỗi
    return text.lower().strip()
```

---

## SLIDE 9: BƯỚC 3.3 - ÁP DỤNG CHUẨN HÓA CHO CÁC CỘT PHÂN LOẠI
*   **Chi tiết thực thi:** Thay vì sửa tay từng ô trong Excel (rất mất thời gian và dễ sai sót), ta dùng lệnh của Pandas để áp dụng hàm chuẩn hóa cho hàng nghìn dòng dữ liệu trong tích tắc.
*   **Ảnh Code minh họa:**
```python
# Lệnh .apply() quét qua toàn bộ các ô trong cột và chạy hàm normalize_vn
df['Quận'] = df['Quận'].apply(normalize_vn)
df['Loại hình nhà ở'] = df['Loại hình nhà ở'].apply(normalize_vn)
df['Giấy tờ pháp lý'] = df['Giấy tờ pháp lý'].apply(normalize_vn)
```
*   **Kết quả:** Sau bước này, biểu đồ thống kê theo Quận sẽ gom nhóm chính xác tuyệt đối, không còn tình trạng bị vỡ vụn do sai chính tả.

---

## SLIDE 10: BƯỚC 3.4 - BÓC TÁCH CON SỐ TỪ CHUỖI (DATA EXTRACTION)
*   **Chi tiết vấn đề:** Giá tiền đang bị dính chữ (ví dụ: `2,5 triệu/m2`). Phần mềm tính toán không thể thực hiện phép nhân/chia trên cụm từ này. Ta phải bóc tách lấy đúng con số `2.5`.
*   **Ảnh Code minh họa (Xử lý cột Giá):**
```python
def clean_price(x):
    if pd.isna(x): return np.nan
    
    # 1. Lệnh replace: Xóa các chữ đi kèm bằng cách thay thế chúng thành chuỗi rỗng ''
    # 2. Đổi dấu phẩy (,) thành dấu chấm (.) để chuẩn hóa số thập phân quốc tế
    s = str(x).lower().replace('triệu/m²', '').replace('triệu/m2', '').replace(',', '.').strip()
    
    # 3. Lệnh float(): Ép chuỗi văn bản thành số thực có chứa phần thập phân
    try: return float(s) 
    except: return np.nan

df['Giá_m2_trieu'] = df['Giá/m2'].apply(clean_price)
```

---

## SLIDE 11: BƯỚC 4.1 - HAI CHIẾN LƯỢC XỬ LÝ DỮ LIỆU KHUYẾT THIẾU
*   **Chiến lược 1 - Khuyết thiếu cốt lõi (MCAR):** Đối với các thông tin mang tính quyết định như Giá nhà và Diện tích, nếu người bán không nhập, ta **bắt buộc phải xóa bỏ dòng đó**. Việc tự suy đoán (bịa ra) mức giá sẽ phá hỏng tính trung thực của báo cáo phân tích.
*   **Chiến lược 2 - Khuyết thiếu có quy luật (MNAR):** Đối với các thông tin phụ như "Số tầng". Một mảnh đất nền sẽ tự nhiên không có số tầng. Ta không xóa dòng này, mà **tạo một Cờ hiệu (Indicator)** để ghi nhận lại đặc điểm "Không có tầng" này.

---

## SLIDE 12: BƯỚC 4.2 - THỰC THI XỬ LÝ KHUYẾT THIẾU
*   **Chi tiết thực thi:** Dịch 2 chiến lược từ lý thuyết sang các hàm can thiệp trực tiếp của Pandas.
*   **Ảnh Code minh họa:**
```python
# 1. CHIẾN LƯỢC XÓA BỎ (DROP)
# Lệnh dropna sẽ xóa sạch bất kỳ dòng nào bị khuyết ở cột Giá hoặc Diện tích
df = df.dropna(subset=['Giá_m2_trieu', 'Diện tích m2'])

# 2. CHIẾN LƯỢC TẠO CỜ HIỆU (INDICATOR)
# Lệnh isna() kiểm tra ô trống. Lệnh astype(int) đổi True/False thành 1 và 0.
# Ta tạo ra cột mới 'Thieu_So_Tang' chứa số 1 (Nếu thiếu tầng) và 0 (Nếu có tầng)
df['Thieu_So_Tang'] = df['Số tầng'].isna().astype(int)
```

---

## SLIDE 13: BƯỚC 5.1 - GIÁ TRỊ NGOẠI LỆ (OUTLIERS) LÀ GÌ?
*   **Chi tiết vấn đề:** Trên các trang bất động sản, thỉnh thoảng có người đăng tin nhà hẻm 10m2 nhưng giá 100 tỷ đồng. Đây là Điểm Ngoại Lệ (Outliers), chúng sẽ kéo sai lệch mức giá trung bình của toàn khu vực, làm biến dạng các biểu đồ phân tích thống kê.
*   **Giải pháp Thống kê:** Dùng quy tắc Hàng rào Interquartile Range (IQR).
    1. Lấy dữ liệu chia làm 4 phần. Tìm mức phân vị 25% (Q1) và 75% (Q3) để lấy ra phần đông phổ biến nhất ở giữa.
    2. Dùng công thức toán học để tính ra một **Mức trần (Upper bound)**. Bất cứ giá nào vọt qua mức trần này đều bị coi là bất thường.

---

## SLIDE 14: BƯỚC 5.2 - KỸ THUẬT CẮT NGỌN (CLIPPING) NGOẠI LỆ
*   **Chi tiết thực thi:** Thay vì xóa bỏ thẳng tay những căn nhà siêu đắt (làm thu hẹp lượng dữ liệu quý giá), ta dùng kỹ thuật "Cắt ngọn". Ta sẽ ép giá của chúng lùi về bằng đúng với Mức trần.
*   **Ảnh Code minh họa:**
```python
# 1. Lệnh quantile() tính mức phân vị 25% (Q1) và 75% (Q3) của cột Giá
Q1 = df['Giá_m2_trieu'].quantile(0.25)
Q3 = df['Giá_m2_trieu'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = max(0, Q1 - 1.5 * IQR) # Đặt sàn bằng 0 (Giá không thể âm)
upper_bound = Q3 + 1.5 * IQR         # Tính giới hạn Mức trần

# 2. Lệnh clip(): Quét toàn bộ cột, ép mọi giá trị > upper_bound xuống đúng bằng upper_bound
df['Giá_m2_trieu'] = df['Giá_m2_trieu'].clip(lower=lower_bound, upper=upper_bound)
```

---

## SLIDE 15: BƯỚC 6 - ĐÓNG GÓI BẰNG PIPELINE (CHUẨN HÓA TOÀN DIỆN)
*   **Chi tiết thực thi:** Bước cuối cùng, để các công cụ phân tích hoạt động trơn tru nhất, ta sử dụng thư viện Scikit-learn để chuẩn hóa thang đo (đưa các số liệu chênh lệch lớn về một tỷ lệ chung) và số hóa văn bản.
*   **Ảnh Code minh họa:**
```python
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, RobustScaler

# Pipeline cho biến Số: Tự động điền số Trung vị (median) -> Chuẩn hóa thang đo RobustScaler
num_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', RobustScaler())
])

# Pipeline cho biến Chữ: Tự động điền chữ 'khong_ro' -> Mã hóa thành các cột 0/1 (One-Hot)
cat_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='khong_ro')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', drop='first'))
])
```
*   **Tổng kết:** Đến đây, bộ dữ liệu đã được gột rửa hoàn toàn. Dữ liệu đã sẵn sàng 100% để phục vụ phân tích chuyên sâu, tạo báo cáo trực quan và chạy các mô hình tính toán dự báo!
