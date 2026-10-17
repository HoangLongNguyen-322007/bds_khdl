# HỌC PHẦN KHOA HỌC DỮ LIỆU (INFO3020) - TÀI LIỆU TỔNG HỢP TOÀN DIỆN

Bản `README.md` này hệ thống hóa toàn bộ kiến thức, quy trình, thuật toán và khung lý thuyết của học phần **Khoa học Dữ liệu (INFO3020)** từ **Tuần 2 đến Tuần 12**.

---

## MỤC LỤC
1. [Chương 1: Tổng quan và Thu thập Dữ liệu (Tuần 2)](#chương-1-tổng-quan-và-thu-thập-dữ-liệu-tuần-2)
2. [Chương 2: Tiền xử lý và Làm sạch Dữ liệu (Tuần 3 - 5)](#chương-2-tiền-xử-lý-và-làm-sạch-dữ-liệu-tuần-3---5)
   - [Tuần 3: Chất lượng dữ liệu & Xử lý dữ liệu khuyết](#tuần-3-chất-lượng-dữ-liệu--xử-lý-dữ-liệu-khuyết)
   - [Tuần 4: Outliers, Nhiễu & Tính nhất quán văn bản tiếng Việt](#tuần-4-outliers-nhiễu--tính-nhất-quán-văn-bản-tiếng-việt)
   - [Tuần 5: Biến đổi, Giảm chiều, Tích hợp & Scikit-Learn Pipeline](#tuần-5-biến-đổi-giảm-chiều-tích-hợp--scikit-learn-pipeline)
3. [Chương 3: Phân tích Khám phá (EDA) và Trực quan hóa (Tuần 6 - 8)](#chương-3-phân-tích-khám-phá-eda-và-trực-quan-hóa-tuần-6---8)
   - [Tuần 6: Xác suất & Thống kê mô tả](#tuần-6-xác-suất--thống-kê-mô-tả)
   - [Tuần 7: Trực quan hóa dữ liệu & Nguyên lý thiết kế đồ thị](#tuần-7-trực-quan-hóa-dữ-liệu--nguyên-lý-thiết-kế-đồ-thị)
   - [Tuần 8: Báo cáo giữa kỳ EDA (Midterm Report)](#tuần-8-báo-cáo-giữa-kỳ-eda-midterm-report)
4. [Chương 4: Suy luận Thống kê và Mô hình hóa (Tuần 9 - 11)](#chương-4-suy-luận-thống-kê-và-mô-hình-hóa-tuần-9---11)
   - [Tuần 9: Suy luận Thống kê & A/B Testing](#tuần-9-suy-luận-thống-kê--ab-testing)
   - [Tuần 10: Phân tích Hồi quy (Linear Regression & Regularisation)](#tuần-10-phân-tích-hồi-quy-linear-regression--regularisation)
   - [Tuần 11: Phân loại, Metrics & Kỹ nghệ đặc trưng (Classification & Feature Engineering)](#tuần-11-phân-loại-metrics--kỹ-nghệ-đặc-trưng-classification--feature-engineering)
5. [Chương 5: Dữ liệu lớn, Đạo đức & Định kiến (Tuần 12)](#chương-5-dữ-liệu-lớn-đạo-đức--định-kiến-tuần-12)

---

## CHƯƠNG 1: TỔNG QUAN VÀ THU THẬP DỮ LIỆU (TUẦN 2)

### 1. 6 Họ nguồn dữ liệu chính & Bảng so sánh
* **Internal Databases**: Dữ liệu vận hành nội bộ (ERP, CRM, SQL). Sạch, đầy đủ, cấu trúc rõ ràng nhưng rào cản là phân quyền truy cập.
* **APIs**: Cổng kết nối có kiểm soát cho nhà phát triển. Cấu trúc chuẩn (JSON/XML), tươi mới nhưng bị giới hạn hạn ngạch (quota/rate limit) và API Key.
* **Web Scraping**: Trích xuất dữ liệu từ HTML trang web. Tự do thu thập dữ liệu công khai nhưng cấu trúc dễ gãy khi web đổi giao diện và chứa rủi ro pháp lý.
* **Open Data**: Dữ liệu công khai từ chính phủ/tổ chức (GSO, World Bank, Kaggle). Miễn phí, hợp pháp nhưng cập nhật chậm và độ chi tiết thô.
* **Surveys**: Khảo sát tự thiết kế. Thu thập đúng thông tin cần thiết nhưng tốn thời gian, chi phí và dễ lệch mẫu (sampling bias).
* **Logs & Sensors**: Nhật ký hệ thống, thiết bị IoT. Dung lượng cực lớn, thời gian thực nhưng cực kỳ thô và lẫn nhiều nhiễu.

#### Bảng so sánh 5 tiêu chí thu thập:
| Họ nguồn | Độ sạch | Công sức thu thập | Độ tươi mới | Độ ổn định | Rủi ro pháp lý |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Internal DB** | Cao | Thấp | Cao | Rất cao | Thấp (Nội bộ) |
| **API** | Cao | Trung bình | Rất cao | Cao | Thấp (Theo ToS) |
| **Web Scraping** | Thấp | Cao | Cao | Thấp | Cao |
| **Open Data** | Trung bình | Thấp | Thấp | Cao | Không |
| **Surveys** | Trung bình | Rất cao | Trung bình | Thấp | Thấp |
| **Logs/Sensors** | Rất thấp | Cao | Thời gian thực | Cao | Trung bình |

### 2. Định dạng dữ liệu & 4 bẫy CSV tiếng Việt
* **Định dạng dữ liệu**:
  * `CSV`: Dạng văn bản thuần, nhẹ, phổ biến nhưng không lưu kiểu dữ liệu (`dtype`) và cấu trúc lồng nhau.
  * `JSON`: Chuẩn trao đổi qua API, hỗ trợ cấu trúc cây/lồng nhau (nested).
  * `XML`: Cấu trúc thẻ lồng nhau, dung lượng nặng.
  * `Excel (.xlsx)`: Dành cho người dùng kinh doanh, hỗ trợ nhiều sheet và định dạng, không tối ưu cho dữ liệu lớn.
  * `Parquet`: Dạng cột (columnar format), nén nhỏ, đọc/ghi cực nhanh, giữ nguyên schema và `dtype`, tối ưu cho Big Data.
* **4 Bẫy CSV tiếng Việt**:
  1. **Lỗi mã hóa (Encoding)**: Tiếng Việt có dấu bị lỗi font khi lưu dạng `cp1258` hoặc `latin-1`. Khi làm việc với Excel trên Windows, cần dùng `utf-8-sig` (chứa BOM) thay vì `utf-8` thuần. Phát hiện mã hóa bằng `chardet.detect()`.
  2. **Dấu phân cách (Delimiter)**: Trong thiết lập hệ thống châu Âu/Việt Nam, Excel dùng dấu chấm phẩy `;` làm phân cách cột thay vì dấu phẩy `,`.
  3. **Dấu thập phân (Decimal Mark)**: Dùng dấu phẩy `,` cho số thập phân (ví dụ `12,5` thay vì `12.5`), khiến Pandas hiểu nhầm là chuỗi (`object`).
  4. **Dòng lỗi (Bad lines)**: Ô dữ liệu chứa dấu phẩy hoặc ký tự xuống dòng mà không bọc trong dấu ngoặc kép `""`.

### 3. Quy tắc Dữ liệu thô bất biến (Raw-Immutable Rule)
* **Nguyên tắc**: Dữ liệu thô (`data/raw/`) là bằng chứng gốc, tuyệt đối không được sửa tay hay ghi đè.
* **Quy trình**: Luôn giữ file thô kèm mốc thời gian (timestamp). Mọi thao tác biến đổi phải thực hiện bằng mã nguồn (code) và xuất kết quả ra thư mục `data/processed/`.

### 4. Pandas I/O & 6 câu hỏi kiểm tra dữ liệu bắt buộc
Khi nạp bất kỳ tệp dữ liệu nào, bắt buộc thực thi 6 câu lệnh kiểm tra:
```python
df.shape              # 1. Kích thước (Số dòng, Số cột)?
df.info()             # 2. Kiểu dữ liệu (dtypes) và bộ nhớ?
df.head(10)           # 3. Mẫu dữ liệu thực tế trông ra sao?
df.dtypes             # 4. Kiểu dữ liệu từng cột có đúng logic không?
df.isna().sum()       # 5. Số lượng giá trị khuyết ở mỗi cột?
df.duplicated().sum() # 6. Có bao nhiêu dòng trùng lặp hoàn toàn?
```

### 5. Thu thập qua API & Web Scraping lịch sự
* **API Checklist**:
  * Bắt buộc dùng `timeout` trong `requests.get(url, timeout=10)`.
  * Kiểm tra trạng thái HTTP: `r.raise_for_status()`.
  * Bảo mật: Không hard-code API Key vào code; lưu trong `.env` và thêm `.env` vào `.gitignore`.
  * Tránh quá tải server: Xử lý rate limit (HTTP 429) bằng `time.sleep()`.
  * Phẳng hóa dữ liệu JSON lồng nhau: `pd.json_normalize()`.
* **Web Scraping & Đạo đức**:
  * Phân biệt **Crawling** (duyệt tìm danh sách URL) và **Scraping** (trích xuất nội dung cụ thể từ trang).
  * Ưu tiên dùng `pd.read_html()` trích xuất bảng HTML trước khi viết parser phức tạp.
  * BeautifulSoup: Dùng CSS Selectors hoặc XPath; luôn kiểm tra `None` trước khi gọi `.get_text()`.
  * Dữ liệu động (JavaScript): Tìm API ẩn trong tab DevTools Network trước khi dùng Playwright/Selenium.
  * **Scraper lịch sự**: Đọc `robots.txt` & ToS, khai báo `User-Agent` chứa thông tin liên hệ, đặt thời gian chờ `time.sleep()`, không thu thập dữ liệu cá nhân (tuân thủ Nghị định 13/2023/NĐ-CP).

---

## CHƯƠNG 2: TIỀN XỬ LÝ VÀ LÀM SẠCH DỮ LIỆU (TUẦN 3 - 5)

### Tuần 3: Chất lượng dữ liệu & Xử lý dữ liệu khuyết

#### 1. 6 Chiều chất lượng dữ liệu (Data Quality Dimensions)
1. **Completeness (Tính đầy đủ)**: Tỷ lệ % dữ liệu không bị khuyết.
2. **Accuracy (Tính chính xác)**: Dữ liệu phản ánh đúng thực tế khách quan.
3. **Consistency (Tính nhất quán)**: Dữ liệu không mâu thuẫn giữa các bảng/hệ thống.
4. **Validity (Tính hợp lệ)**: Dữ liệu tuân thủ đúng định dạng, kiểu và miền giá trị.
5. **Uniqueness (Tính duy nhất)**: Không bị trùng lặp thực thể.
6. **Timeliness (Tính kịp thời)**: Dữ liệu còn cập nhật và đúng mốc thời gian.

* **Quy tắc chi phí 1-10-100**: Tốn 1$ để ngăn ngừa/sửa khi nhập $\rightarrow$ 10$ để làm sạch dữ liệu $\rightarrow$ 100$ chịu chi phí khắc phục khi đã ra quyết định sai lầm từ dữ liệu bẩn.
* **Quy trình làm sạch 6 bước**: Audit $\rightarrow$ Missing values $\rightarrow$ Outliers $\rightarrow$ Consistency $\rightarrow$ Deduplicate $\rightarrow$ Re-validate.

#### 2. Nhận diện Dữ liệu khuyết ngụy trang (Disguised Missingness)
* Giá trị khuyết không chỉ là `NaN`/`Null` mà thường ẩn dưới dạng:
  * Chuỗi rỗng: `""`, `" "`
  * Chuỗi mặc định: `"N/A"`, `"NULL"`, `"None"`, `"missing"`
  * Ngữ cảnh tiếng Việt: `"không rõ"`, `"Thỏa thuận"`, `"Chưa xác định"`
  * Số nguyên vô nghĩa: `-999`, `-1`, `0` (trong cột thu nhập/tuổi)
  * Ngày tháng mặc định: `1900-01-01`, `1970-01-01`
* Khai báo trực tiếp qua `na_values` khi đọc Pandas: `pd.read_csv('data.csv', na_values=['N/A', 'không rõ', -999])`.
* Trực quan hóa mẫu khuyết bằng `missingno`: `msno.matrix(df)`, `msno.bar(df)`, `msno.heatmap(df)`.

#### 3. 3 Cơ chế dữ liệu khuyết (Missing Mechanisms)
* **MCAR (Missing Completely At Random)**: Khuyết hoàn toàn ngẫu nhiên. Xác suất khuyết không phụ thuộc vào bất kỳ biến nào (đã quan sát hay chưa quan sát). Được phép xóa dòng mà không gây lệch (bias).
* **MAR (Missing At Random)**: Khuyết ngẫu nhiên có điều kiện. Xác suất khuyết phụ thuộc vào một biến quan sát được khác trong dữ liệu (ví dụ: Nam giới ít điền cột thu nhập hơn Nữ giới). Phương pháp xử lý: **Group-wise Imputation** (Gán theo nhóm).
* **MNAR (Missing Not At Random)**: Khuyết không ngẫu nhiên. Xác suất khuyết phụ thuộc vào chính giá trị bị khuyết (ví dụ: Người thu nhập cực cao cố tình giấu thu nhập). **Bắt buộc**: Tạo cột cờ chỉ báo (`missing_indicator`) và mô hình hóa trực tiếp.

#### 4. Các kỹ thuật xử lý dữ liệu khuyết & Bẫy rò rỉ
* **Xóa (Deletion)**: Không dùng `dropna()` trần. Bắt buộc chỉ định `subset=['col1', 'col2']`. Lưu ý bẫy mất mát dữ liệu dây chuyền: Nếu mỗi cột khuyết 5% trên 10 cột, xóa dòng có thể làm mất $1 - (0.95)^{10} \approx 40\%$ dữ liệu.
* **Gán đơn giản (Simple Imputation)**:
  * Mean: Chỉ dùng khi dữ liệu phân phối chuẩn, không có outlier. **Tác hại**: Làm thu hẹp phương sai nhân tạo và biến đổi hình dạng phân phối.
  * Median: Dùng cho dữ liệu lệch (skewed) hoặc có outlier.
  * Mode: Dùng cho biến định tính (categorical).
* **Gán theo nhóm (Group-wise Imputation)**: Dùng `df['val'] = df.groupby('category')['val'].transform(lambda x: x.fillna(x.median()))`.
* **Nội suy (Interpolation)**: Dùng cho chuỗi thời gian (`method='linear'`, `'time'`, `ffill`, `bfill`).
* **Gán đa biến (Multivariate Imputation)**: `KNNImputer`, `IterativeImputer` (MICE). Bắt buộc phải scale dữ liệu trước khi dùng KNNImputer.
* **Bẫy Data Leakage khi Impute**: Tính Mean/Median trên toàn bộ dataset trước khi chia Train/Test. **Quy tắc**: Bắt buộc tính toán tham số gán chỉ trên tập Train và apply lên Test, hoặc bọc trong `Pipeline`.

---

### Tuần 4: Outliers, Nhiễu & Tính nhất quán văn bản tiếng Việt

#### 1. Phân loại Outlier & Bản chất
* **3 Loại Outlier**:
  * Point Outlier: Điểm dữ liệu đơn lẻ nằm xa toàn bộ tập dữ liệu.
  * Contextual Outlier: Giá trị bất thường theo ngữ cảnh (ví dụ: Nhiệt độ 30°C là bình thường vào mùa hè nhưng là outlier vào mùa đông).
  * Collective Outlier: Nhóm các điểm dữ liệu hợp lệ khi đứng riêng lẻ nhưng bất thường khi xuất hiện cùng nhau.
* **Outlier vs Error vs Noise**: Outlier không đồng nghĩa với lỗi (Error). Outlier có thể là giao dịch gian lận hoặc đột biến y tế mang giá trị cao. Noise là nhiễu ngẫu nhiên nhỏ cần làm mịn.

#### 2. Phương pháp phát hiện Outlier
* **Z-score**: $z = (x - \mu) / \sigma$. Flag khi $|z| > 3$. **Nhược điểm**: $\mu$ và $\sigma$ bị kéo lệch bởi chính outlier, giả định phân phối chuẩn, dễ bị hiện tượng che giấu (Masking).
* **Modified Z-score**: Sử dụng Trung vị (Median) và Độ lệch tuyệt đối trung vị ($MAD = \text{median}(|x_i - \text{median}|)$).
  $$M_i = \frac{0.6745 \cdot (x_i - \text{median})}{MAD}$$
  Flag khi $|M_i| > 3.5$. Phương pháp chuẩn cho dữ liệu thực tế bị lệch.
* **IQR (Interquartile Range)**: $IQR = Q3 - Q1$.
  * Ngưỡng dưới = $Q1 - 1.5 \cdot IQR$
  * Ngưỡng trên = $Q3 + 1.5 \cdot IQR$
  * Phi tham số, không phụ thuộc giả định phân phối chuẩn.
* **Khoảng cách Mahalanobis**: Đo khoảng cách đa biến xét đến tương quan giữa các cột.
* **Thuật toán ML**: Isolation Forest (`contamination=0.05`), Local Outlier Factor (LOF), DBSCAN.

#### 3. Chiến lược xử lý Outlier
* **Keep**: Giữ nguyên nếu là sự kiện hiếm thực tế mang thông tin quan trọng.
* **Delete**: Xóa nếu xác minh chắc chắn là lỗi thiết bị/nhập liệu.
* **Cap / Winsorize**: Giới hạn giá trị tại bách phân vị 1% và 99% bằng `df['col'].clip(lower=p01, upper=p99)`.
* **Transform**: Áp dụng `np.log1p()` hoặc `PowerTransformer` để thu hẹp đuôi phân phối.
* **Đổi công cụ**: Chuyển sang dùng chỉ số robust (Median, IQR) hoặc mô hình cây (Decision Tree, XGBoost).

#### 4. Nhất quán & Xử lý văn bản tiếng Việt
* **Trùng lặp (Deduplication)**: Phân biệt trùng lặp toàn bộ (`df.duplicated()`) và trùng lặp theo khóa kinh doanh (Business Key). Sử dụng `rapidfuzz` để khớp mờ (fuzzy matching) các chuỗi bị lỗi chính tả.
* **Bẫy Chuẩn hóa Unicode Tiếng Việt (NFC vs NFD)**:
  * Chuỗi hiển thị giống hệt nhau nhưng không thể join/group vì một bên lưu dạng **NFC** (Composed: `ế`) và một bên lưu dạng **NFD** (Decomposed: `e` + `̂` + `́`).
  * **Giải pháp bắt buộc**: Chạy chuẩn hóa Unicode NFC cho toàn bộ cột văn bản:
    ```python
    import unicodedata
    df['text'] = df['text'].apply(lambda x: unicodedata.normalize('NFC', x) if isinstance(x, str) else x)
    ```
* **Ngày tháng & Đơn vị**: Thiết lập `dayfirst=True` trong `pd.to_datetime()`. Quy đổi chuỗi thời gian tương đối ("2 giờ trước") thành timestamp cố định dựa vào mốc cào dữ liệu.
* **Kiểm tra ràng buộc (Rule-based Validation)**: Viết các câu lệnh khẳng định `assert (df['age'] >= 0).all()` để bắt lỗi logic.
* **Nhật ký làm sạch (Cleaning Log)**: Bắt buộc ghi lại: Bước, Cột, Lỗi phát hiện, Thao tác xử lý, Số dòng ảnh hưởng, Lý do kinh doanh.

---

### Tuần 5: Biến đổi, Giảm chiều, Tích hợp & Scikit-Learn Pipeline

#### 1. Feature Scaling (Chuẩn hóa thang đo)
* **Min-Max Normalisation**: $x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}} \in [0, 1]$. Rất nhạy cảm với outlier.
* **Standardisation (Z-score Scaling)**: $x' = \frac{x - \mu}{\sigma}$. Chuyển về $\mu=0, \sigma=1$. Giữ nguyên hình dạng phân phối ban đầu.
* **RobustScaler**: $x' = \frac{x - \text{median}}{IQR}$. Tối ưu khi dữ liệu chứa outlier đuôi nặng.
* **Phân loại thuật toán**:
  * **Cần Scaling**: Thuật toán tính khoảng cách hoặc đạo hàm ($k$-NN, $k$-means, SVM, PCA, Gradient Descent, Logistic/Linear Regression có Regularisation).
  * **Không cần Scaling**: Mô hình dạng cây (Decision Tree, Random Forest, XGBoost).

#### 2. Mã hóa biến phân loại (Categorical Encoding)
* **One-Hot Encoding**: Dùng cho biến định danh không thứ tự (Nominal). Đặt `drop_first=True` để tránh Bẫy biến giả (Dummy Variable Trap). Đặt `handle_unknown='ignore'` trong production.
* **Ordinal Encoding**: Dùng cho biến có thứ tự (Ordinal). Bắt buộc truyền danh mục thứ tự thủ công qua `categories=[['Low', 'Medium', 'High']]`.
* **High-Cardinality Encoding**: Biến có hàng trăm nhóm $\rightarrow$ Gom nhóm tần suất thấp thành `"Other"`, mã hóa tần suất (Frequency Encoding), hoặc Target Encoding (cần k-fold out-of-fold để tránh rò rỉ).

#### 3. Giảm dữ liệu (Data Reduction) & Tích hợp (Data Integration)
* **Giảm cột**: Loại bỏ cột phương sai $\approx 0$ (`VarianceThreshold`), loại bỏ cột có độ tương quan $r > 0.95$, hoặc dùng **PCA** để chiếu không gian.
* **Giảm dòng**: Random Sampling, Stratified Sampling (khi lệch lớp), hoặc Aggregation.
* **Tích hợp dữ liệu**:
  * **ETL vs ELT**: ETL (Biến đổi trước khi lưu vào kho), ELT (Lưu dữ liệu thô vào Data Lake rồi mới biến đổi - tuân thủ Raw-Immutable).
  * **Bùng nổ dòng (Row Explosion)**: Xảy ra khi join trùng khóa ở cả 2 bên ($3 \text{ dòng} \times 4 \text{ dòng} = 12 \text{ dòng}$). Bắt buộc dùng `pd.merge(..., validate='many_to_one')` để ngắt chương trình khi vi phạm.
  * **Tidy Data**: Dùng `pd.melt()` chuyển bảng ngang (Wide) thành bảng dọc (Long/Tidy). Dùng `pivot_table()` để tổng hợp báo cáo.
  * **Named Aggregation**: Dùng `df.groupby('cat').agg(mean_val=('val', 'mean'), max_val=('val', 'max'))` để tránh tạo MultiIndex phức tạp.

#### 4. Scikit-Learn Pipeline hoàn chỉnh
```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

num_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

cat_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(drop='first', handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', num_transformer, num_cols),
    ('cat', cat_transformer, cat_cols)
])
```

---

## CHƯƠNG 3: PHÂN TÍCH KHÁM PHÁ (EDA) VÀ TRỰC QUAN HÓA (TUẦN 6 - 8)

### Tuần 6: Xác suất & Thống kê mô tả

#### 1. Nền tảng xác suất
* Mọi tập dữ liệu chỉ là một mẫu (sample) rút từ quần thể (population).
* **Biến ngẫu nhiên**:
  * Rời rạc (Discrete): Đếm được, mô tả bằng PMF (Probability Mass Function), vẽ bằng Bar chart.
  * Liên tục (Continuous): Đo lường được, mô tả bằng PDF (Probability Density Function), vẽ bằng Histogram/KDE.
* **Xác suất có điều kiện & Định lý Bayes**: $P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$.
  * **Testing Paradox**: Một xét nghiệm y tế có độ chính xác 99% cho căn bệnh có tỷ lệ 0.1% trong dân số thì xác suất thực sự bị bệnh khi nhận kết quả dương tính chỉ $\approx 9\%$ do tỷ lệ nền $P(A)$ quá nhỏ.
* **Định lý Giới hạn Trung tâm (CLT)**: Phân phối của các trung bình mẫu ($\bar{x}$) sẽ tiến về phân phối chuẩn khi kích thước mẫu $n \ge 30$, bất kể phân phối của quần thể gốc.
* **Sai số chuẩn (Standard Error)**: $SE = \frac{\sigma}{\sqrt{n}}$. Muốn giảm một nửa $SE$, kích thước mẫu $n$ phải tăng gấp 4 lần.

#### 2. 4 Họ đại lượng thống kê mô tả
1. **Location (Độ tập trung)**: Mean (nhạy cảm với outlier), Median (robust với dữ liệu lệch), Mode (biến định tính/đa đỉnh), Percentiles (P10, P50, P90). Với phân phối lệch phải: $\text{Mean} > \text{Median} > \text{Mode}$.
2. **Spread (Độ tán sắc)**: Range ($\max - \min$), Variance ($\sigma^2$), Standard Deviation ($\sigma$), IQR ($Q3 - Q1$), Coefficient of Variation ($CV = \frac{\sigma}{\mu}$ - dùng so sánh độ biến động giữa các đơn vị khác nhau).
3. **Shape (Hình dạng)**: Skewness (Độ lệch: $>0$ lệch phải, $<0$ lệch trái; $>1$ cần log transform) và Kurtosis (Độ nhọn/Độ nặng của đuôi).
4. **Relationship (Mối quan hệ)**: Covariance và Correlation.

#### 3. Tương quan vs Nhân quả (Correlation vs Causation)
* **Pearson's r**: Đo quan hệ tuyến tính $[-1, +1]$. Thất bại hoàn toàn với quan hệ phi tuyến (hình parabol) hoặc khi có outlier.
* **Spearman's rank**: Đo quan hệ đơn điệu (monotonic), phi tham số, chịu đựng được outlier.
* **Anscombe's Quartet & Datasaurus Dozen**: Các tập dữ liệu có cùng Mean, Std, Tương quan $r=0.816$ nhưng hình dạng biểu đồ hoàn toàn khác nhau. **Quy tắc vàng**: Bắt buộc phải vẽ đồ thị dữ liệu trước khi tin vào chỉ số thống kê.
* **Bẫy nhân quả**:
  * Biến nhiễu (Confounder): Biến thứ ba gây ra cả 2 biến.
  * Nghịch lý Simpson (Simpson's Paradox): Xu hướng xuất hiện trong các nhóm riêng lẻ bị đảo ngược hoàn toàn khi gộp chung dữ liệu.

---

### Tuần 7: Trực quan hóa dữ liệu & Nguyên lý thiết kế đồ thị

#### 1. Exploratory vs Explanatory Visualization
* **Exploratory (Khám phá)**: Vẽ cho chính mình, nhanh, nháp, số lượng nhiều để tìm pattern và lỗi dữ liệu.
* **Explanatory (Giải thích)**: Vẽ cho người đọc, tinh chỉnh kỹ lưỡng, chỉ chọn 3-5 biểu đồ đắt giá nhất, tiêu đề mang tính kết luận.

#### 2. Thứ tự kênh thị giác (Visual Channels Hierarchy)
Độ chính xác của mắt người khi cảm nhận dữ liệu (từ cao xuống thấp):
1. **Position (Vị trí)** - Chính xác nhất (Scatter plot, Bar plot)
2. **Length (Độ dài)** (Bar chart)
3. **Angle / Slope (Góc / Độ dốc)** (Pie chart, Slope chart)
4. **Area (Diện tích)** (Bubble chart)
5. **Color Intensity (Độ đậm màu)** (Heatmap)
6. **Color Hue (Tông màu)** - Kém nhất cho so sánh định lượng

* **Lý do Pie Chart thất bại**: Ép mắt người so sánh góc và diện tích (thứ tự 3 & 4) thay vì độ dài. **Giải pháp**: Thay thế bằng Horizontal Bar Chart.

#### 3. Data-Ink Ratio & 5 Bẫy biểu đồ
* **Data-Ink Ratio**: Tối đa hóa lượng mực dùng để truyền tải thông tin thực tế. Xóa bỏ khung viền đậm, hiệu ứng 3D, lưới nền tối và chú thích thừa.
* **5 Bẫy biểu đồ đánh lừa**:
  1. Trục Y bị cắt ngắt (Truncated Y-axis) trong Bar chart (**Quy tắc**: Bar chart trục Y bắt buộc xuất phát từ 0; Line chart thì không bắt buộc).
  2. Hai trục Y độc lập (Dual Y-axes) gây hiểu nhầm về tương quan.
  3. Hiệu ứng 3D làm méo mó góc nhìn.
  4. Cửa sổ thời gian tự chọn (Cherry-picking window).
  5. Đảo ngược trục Y.

#### 4. Palettes & Seaborn Best Practices
* **3 Loại bảng màu**:
  * Qualitative (Định tính): Cho các danh mục không thứ tự (tối đa 7-8 màu).
  * Sequential (Tuyến tính): Đơn sắc từ sáng đến tối cho lượng tăng dần.
  * Diverging (Phân kỳ): 2 màu đối lập qua điểm trung tâm 0.
* **Khả năng truy cập (Accessibility)**: Không dùng màu Đỏ/Xanh lá để so sánh (8% nam giới bị mù màu). Ưu tiên palette `viridis` hoặc `cividis`.
* **Seaborn Best Practices**: Bắt buộc đầu vào là Tidy Data. Sử dụng `ecdfplot` thay cho `histplot` khi so sánh phân phối giữa nhiều nhóm mà không lo chọn độ rộng bin.

---

### Tuần 8: Báo cáo giữa kỳ EDA (Midterm Report)
* **Cấu trúc chuẩn báo cáo 6 phần**:
  1. Context & Business Question (1 trang)
  2. Data Source & Data Dictionary (1 trang)
  3. Cleaning Log (2 trang - nêu rõ Lý do và Số dòng ảnh hưởng)
  4. Exploratory Data Analysis (3-4 trang - Thống kê 4 họ + Biểu đồ giải thích)
  5. Key Findings (3-5 kết luận cốt lõi)
  6. Limitations & Next Steps (1 trang)
* **5 Lỗi mất điểm nặng nhất**: Khẳng định nhân quả từ tương quan, Biểu đồ thiếu tiêu đề kết luận/nhãn/đơn vị, Thao tác làm sạch không có lý do, Notebook không chạy được từ đầu đến cuối (`Restart & Run All`), Nộp biểu đồ nháp thay vì biểu đồ giải thích.

---

## CHƯƠNG 4: SUY LUẬN THỐNG KÊ VÀ MÔ HÌNH HÓA (TUẦN 9 - 11)

### Tuần 9: Suy luận Thống kê & A/B Testing

#### 1. Thống kê Suy luận & Khoảng tin cậy (CI)
* Thống kê mô tả chỉ nói về tập mẫu quan sát được. Thống kê suy luận đưa ra kết luận về quần thể kèm theo mức độ không chắc chắn.
* **Khoảng tin cậy 95%**: $\text{CI}_{95\%} \approx \bar{x} \pm 1.96 \cdot SE$.
* **Diễn giải đúng**: *"Nếu lặp lại quy trình lấy mẫu 100 lần, khoảng 95 khoảng tin cậy tạo ra sẽ chứa giá trị thực $\mu$ của quần thể"*.

#### 2. Quy trình Kiểm định Giả thuyết 5 bước
1. **Phát biểu giả thuyết**: $H_0$ (Không có sự khác biệt/ảnh hưởng) và $H_1$ (Có sự khác biệt).
2. **Chọn mức ý nghĩa $\alpha$**: Thường chọn $\alpha = 0.05$ **trước khi xem dữ liệu**.
3. **Kiểm tra giả định & Chọn phép kiểm**: Kiểm định phân phối chuẩn, phương sai đồng nhất.
4. **Tính toán**: Đại lượng kiểm định, p-value, Khoảng tin cậy và Effect Size.
5. **Kết luận**: Bác bỏ $H_0$ nếu $\text{p-value} < \alpha$.

#### 3. Bản chất p-value & Bảng sai lầm
* **Định nghĩa p-value**: p-value là xác suất quan sát được dữ liệu cực đoan như thế này (hoặc hơn) **với giả định rằng $H_0$ đúng**.
* **4 Ngộ nhận**: p-value KHÔNG PHẢI là xác suất $H_0$ đúng; p-value nhỏ KHÔNG có nghĩa là hiệu ứng lớn; $p > 0.05$ KHÔNG chứng minh $H_0$ đúng; $p < 0.05$ KHÔNG đảm bảo ý nghĩa thực tiễn.
* **Bảng sai lầm**:
  * **Sai lầm Loại I ($\alpha$)**: Bác bỏ $H_0$ khi $H_0$ đúng (Báo động giả).
  * **Sai lầm Loại II ($\beta$)**: Không bác bỏ $H_0$ khi $H_0$ sai (Bỏ sót hiệu ứng).
  * **Power (Công suất)**: $1 - \beta$ (thường đặt ở mức $0.8$).
  * **Effect Size (Cohen's d)**: Đo độ lớn thực tế ($0.2$ nhỏ, $0.5$ trung bình, $0.8$ lớn).

#### 4. Cây chọn phép kiểm định thống kê
```
Dữ liệu 1 nhóm số vs Giá trị thực -> One-sample t-test
Dữ liệu 2 nhóm số độc lập:
    ├── Phân phối chuẩn -> Two-sample Welch's t-test (equal_var=False)
    └── Không chuẩn / Outliers -> Mann-Whitney U test
Dữ liệu 2 nhóm cặp đôi (Paired) -> Paired t-test / Wilcoxon signed-rank
Dữ liệu 3+ nhóm số:
    ├── Phân phối chuẩn -> One-way ANOVA + Tukey's HSD post-hoc
    └── Không chuẩn -> Kruskal-Wallis test
Dữ liệu 2 biến phân loại -> Chi-square test of independence (Fisher's exact nếu ô < 5)
```

#### 5. A/B Testing & 4 Bẫy chết người
* Phân nhóm ngẫu nhiên (Randomisation) là cách duy nhất triệt tiêu biến nhiễu.
* Phân nhóm theo User ID, không phân nhóm theo Session.
* Chỉ số: Primary metric (OEC), Secondary metrics, Guardrail metrics.
* **4 Bẫy chết người**:
  1. **Peeking**: Xem kết quả hàng ngày rồi dừng sớm khi thấy $p < 0.05$, làm vọt tỷ lệ báo động giả thực tế lên $>30\%$.
  2. **Multiple Comparisons**: Thử nghiệm nhiều biến thể cùng lúc mà không điều chỉnh ngưỡng Bonferroni ($\alpha_{\text{adjusted}} = \alpha / m$).
  3. **Sample Ratio Mismatch (SRM)**: Tỷ lệ mẫu thực tế giữa A và B lệch so với thiết kế 50/50 do lỗi kỹ thuật. Kiểm tra SRM bằng Chi-square test trước khi đọc kết quả.
  4. **Novelty Effect**: Người dùng tò mò với giao diện mới trong thời gian đầu.

---

### Tuần 10: Phân tích Hồi quy (Linear Regression & Regularisation)

#### 1. Mô hình Hồi quy tuyến tính
* **Hồi quy đơn**: $\hat{y} = \beta_0 + \beta_1 x$. $\beta_0$ (Intercept), $\beta_1$ (Slope).
* **Hồi quy đa biến**: $\hat{y} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_p x_p$.
* **Hàm mất mát OLS**: Tối thiểu hóa $\sum (y_i - \hat{y}_i)^2$.
* **2 Phương pháp giải**:
  * Closed-form: $\beta = (X^T X)^{-1} X^T y$ (chính xác, gãy khi đa cộng tuyến).
  * Gradient Descent: Lặp tối ưu, dùng cho dữ liệu lớn, bắt buộc phải scale dữ liệu.

#### 2. 3 Nghĩa vụ bắt buộc khi đọc hệ số $\beta$
1. Dùng từ *"đi kèm với / gắn liền với"*, tuyệt đối không dùng từ "gây ra".
2. Khẳng định *"khi giữ nguyên các biến khác trong mô hình"*.
3. Bổ sung *"trong phạm vi dữ liệu đã quan sát được"*.

#### 3. Đánh giá Mô hình & 4 Giả định LINE
* **Metrics**:
  * $MAE = \frac{1}{n} \sum |y_i - \hat{y}_i|$ (dễ giải thích, robust với outlier).
  * $RMSE = \sqrt{\frac{1}{n} \sum (y_i - \hat{y}_i)^2}$ (phạt nặng lỗi lớn).
  * $R^2$: Tỷ lệ phương sai giải thích được. Cảnh báo: $R^2$ luôn tăng khi thêm biến mới $\rightarrow$ dùng **Adjusted $R^2$** hoặc đánh giá $R^2$ trên tập Test.
* **4 Giả định LINE & Residual Plots**:
  * **L - Linearity**: Quan hệ tuyến tính (phần dư không tạo đường cong).
  * **I - Independence**: Phần dư không tự tương quan (không tạo hình sóng).
  * **N - Normality**: Phần dư xấp xỉ phân phối chuẩn (QQ-plot bám đường thẳng).
  * **E - Equal Variance (Homoscedasticity)**: Phương sai phần dư là hằng số (không bị xòe hình phễu - Funnel pattern). Nếu bị xòe, dùng Robust Errors (`HC3`) hoặc lấy $\log(y)$.

#### 4. Regularisation (Ridge & Lasso)
* **Ridge (L2)**: Phạt $\alpha \sum \beta_j^2$. Co hệ số về gần 0, xử lý đa cộng tuyến ($VIF > 10$).
* **Lasso (L1)**: Phạt $\alpha \sum |\beta_j|$. Kéo trực tiếp hệ số về đúng 0 $\rightarrow$ Tự động chọn lọc thuộc tính (Feature Selection).
* **Bắt buộc**: Phải Scale dữ liệu trước khi chạy Ridge/Lasso.

---

### Tuần 11: Phân loại, Metrics & Kỹ nghệ đặc trưng (Classification & Feature Engineering)

#### 1. Các thuật toán phân loại
* **Logistic Regression**: Dùng hàm Sigmoid $\sigma(z) = \frac{1}{1 + e^{-z}}$. Hệ số $e^\beta$ là Odds Ratio (Tỷ lệ Odds), không phải tỷ lệ xác suất trực tiếp.
* **$k$-Nearest Neighbours ($k$-NN)**: Dự báo theo $k$ điểm gần nhất. Bắt buộc phải scale dữ liệu.
* **Naive Bayes**: Dựa trên định lý Bayes với giả định các thuộc tính độc lập. Rất nhanh, tối ưu cho phân loại văn bản (TF-IDF).
* **Decision Trees**: Dễ giải thích, không cần scale dữ liệu, dễ bị overfitting $\rightarrow$ Giới hạn `max_depth`, `min_samples_leaf`.
* **Random Forest & XGBoost**: Tập hợp nhiều cây để tăng độ chính xác và giảm phương sai.

#### 2. Ma trận nhầm lẫn & Metrics cho Dữ liệu mất cân bằng
* **Bẫy Accuracy**: Trong bài toán Fraud 1%, mô hình luôn đoán "Không gian lận" đạt Accuracy 99% nhưng Recall gian lận bằng 0%.
* **Precision**: $\frac{TP}{TP + FP}$ - Chất lượng cảnh báo (tránh báo động giả - Spam).
* **Recall (Sensitivity)**: $\frac{TP}{TP + FN}$ - Độ bao phủ (tránh bỏ sót - Ung thư, Gian lận).
* **F1-Score**: Trung bình hài hòa giữa Precision và Recall: $F1 = 2 \cdot \frac{Precision \cdot Recall}{Precision + Recall}$.
* **ROC-AUC vs PR-AUC**:
  * ROC Curve (TPR vs FPR): Dùng cho dữ liệu cân bằng.
  * Precision-Recall Curve: **Bắt buộc dùng cho dữ liệu mất cân bằng nặng**.

#### 3. Xử lý Mất cân bằng lớp & Data Leakage
* Thiết lập `class_weight='balanced'` trong mô hình.
* Oversampling (SMOTE) / Undersampling: **Chỉ thực hiện trên tập Train**, tuyệt đối không resample trên tập Test.
* **Kỹ nghệ đặc trưng (Feature Engineering)**:
  * Thời gian: Cyclical Encoding cho giờ/tháng bằng $\sin\left(\frac{2\pi t}{T}\right)$ và $\cos\left(\frac{2\pi t}{T}\right)$ để nối liền điểm 23h và 0h.
  * Văn bản tiếng Việt: Tách từ bằng `underthesea.word_tokenize` $\rightarrow$ Biến đổi `TfidfVectorizer`.
* **4 Loại Data Leakage**: Target leakage, Train-Test leakage, Temporal leakage (dùng tương lai đoán quá khứ), Group leakage (cùng thực thể ở cả Train và Test).

---

## CHƯƠNG 5: DỮ LIỆU LỚN, ĐẠO ĐỨC & ĐỊNH KIẾN (TUẦN 12)

### 1. Dữ liệu lớn (Big Data) & Kiến trúc Spark
* **5Vs**: Volume, Velocity, Variety, Veracity (Scale làm nhân rộng dữ liệu bẩn), Value.
* **Scale Up vs Scale Out**: Scale Up (tăng cấu hình 1 máy); Scale Out (phân tán cụm máy cluster). **Quy tắc**: Tối ưu code/RAM trước khi scale out.
* **Spark Architecture**: Mô hình Driver - Executor.
  * **Lazy Evaluation**: Các phép biến đổi (Transformations: `select`, `filter`, `join`) là lười biếng, chỉ xây dựng kế hoạch thực thi DAG. Phép toán Eager (Actions: `count`, `collect`, `show`) mới kích hoạt tính toán thực sự.
  * **3 Nguyên nhân Spark job bị chết**: Shuffle quá nhiều qua mạng, Skew data (lệch khóa), và gọi `.collect()` kéo toàn bộ dữ liệu lớn về máy Driver làm tràn RAM.

### 2. Đạo đức Dữ liệu & Quyền riêng tư
* **5 Nguyên tắc Đạo đức**: Autonomy, Non-maleficence, Fairness, Transparency, Accountability.
* **Pháp lý**: Nghị định 13/2023/NĐ-CP (Việt Nam) & GDPR.
* **Phân loại dữ liệu**:
  * Direct Identifiers: Họ tên, CCCD, Email.
  * Quasi-Identifiers: Ngày sinh, Giới tính, Mã bưu chính (ghép lại có thể định danh duy nhất).
  * Sensitive Data: Y tế, Sinh trắc học, Tôn giáo.
* **Kỹ thuật Anonymisation**:
  * Pseudonymisation (Giả danh): Thay ID bằng mã hash (vẫn có thể đảo ngược).
  * Anonymisation (Ẩn danh): $k$-anonymity (mỗi bản ghi ẩn trong nhóm $k$ người giống nhau), Differential Privacy ($\epsilon$ - thêm nhiễu ngẫu nhiên vào truy vấn tổng hợp).

### 3. Định kiến (Bias) & Tính giải thích được (Explainability)
* **6 Dạng Bias**: Selection bias, Survivorship bias (Bẫy máy bay quay về), Measurement bias, Label bias, Historical bias, Aggregation bias.
* **Công bằng (Fairness Metrics)**: Demographic Parity, Equal Opportunity, Equalised Odds. (Các tiêu chí công bằng mâu thuẫn lẫn nhau về mặt toán học).
* **Tính giải thích được**: Sử dụng **SHAP (Shapley Additive exPlanations)** và **LIME** để giải thích đóng góp của từng thuộc tính vào dự báo của mô hình Black-box.
* **Tài liệu hóa**: Đính kèm **Datasheets for Datasets** và **Model Cards** cho mọi mô hình triển khai thực tế.
