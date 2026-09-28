# README: Nội Dung Các Chương Môn Học Khoa Học Dữ Liệu (INFO3020)

**Trường Đại học CMC – Khoa Công nghệ Thông tin & Truyền thông**  
**Giảng viên:** ThS. Phạm Ngọc Đông  
**Học phần:** INFO3020 – Nhập môn Khoa học Dữ liệu (Introduction to Data Science)

---

## 📌 Giới Thiệu Tổng Quan

Tài liệu README này tổng hợp chi tiết toàn bộ nội dung lý thuyết, phương pháp luận và kỹ thuật thực hành được giảng dạy từ **Tuần 2 đến Tuần 5**, thuộc hai chương cốt lõi đầu tiên của học phần:
- **Chương 1:** Tổng quan & Thu thập Dữ liệu (Overview & Data Collection)
- **Chương 2:** Làm sạch & Tiền xử lý Dữ liệu (Data Cleaning & Preprocessing)

---

## 📚 MỤC LỤC CHI TIẾT CÁC CHƯƠNG

---

### 🔹 CHƯƠNG 1: TỔNG QUAN & THU THẬP DỮ LIỆU

#### 📍 Tuần 2: Thu Thập Dữ Liệu Đa Nguồn (Multi-source Data Collection)

* **1. Bốn Con Đường Thu Thập Dữ Liệu (Four Routes to Data):**
  * **Open Data (Dữ liệu mở):** Quốc tế (World Bank, Our World in Data, Kaggle, UCI, WHO, UN) và Việt Nam (Tổng cục Thống kê - GSO, Cổng dữ liệu quốc gia, NHNN, Bộ Công Thương).
  * **Internal Databases (CSDL nội bộ):** Truy vấn dữ liệu doanh nghiệp qua SQL cơ bản (`SELECT`, `WHERE`, `JOIN`, `GROUP BY`). Nguyên tắc: Lọc và tổng hợp tại CSDL trước khi tải vào Python.
  * **APIs (Giao diện lập trình ứng dụng):** Hiểu cấu trúc HTTP Request (Method GET/POST, URL, Params, Headers, Body) và các HTTP Status Codes quan trọng (`200 OK`, `401 Unauthenticated`, `403 Forbidden`, `404 Not Found`, `429 Too Many Requests`, `5xx Server Error`). Quản lý Rate limits, Phân trang (Pagination) và Bảo mật API Keys qua tệp `.env` / `.gitignore`.
  * **Web Scraping (Cào dữ liệu web):** Phân biệt Crawling và Scraping; Cấu trúc DOM Tree & HTML; Sử dụng CSS Selectors và BeautifulSoup; Xử lý trang web động (JavaScript rendering) qua DevTools Hidden APIs, Playwright hoặc Selenium. Tuân thủ đạo đức và pháp lý (`robots.txt`, Terms of Service, Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân).

* **2. Các Định Dạng Dữ Liệu & 4 Bẫy CSV Tiếng Việt:**
  * So sánh đặc tính của CSV, JSON (dữ liệu lồng nhau với `json_normalize`), XML (`pd.read_xml`, `pd.read_html`), Excel và Parquet (bảo toàn dtypes, nén cao, tốc độ nhanh).
  * **4 bẫy CSV phổ biến với dữ liệu Việt Nam:**
    1. *Encoding:* Lỗi font bảng mã `cp1258`/`latin-1` từ Excel $\rightarrow$ dùng `utf-8-sig` (xử lý BOM).
    2. *Delimiter:* Dấu phân cách `;` thay vì `,`.
    3. *Decimal Mark:* Dấu phẩy thập phân `,` (kiểu Việt/Âu) vs dấu chấm `.`.
    4. *Bad Lines & Missing Disguises:* Chuỗi chứa dấu phẩy không ngoặc kép hoặc các từ miền như `"Thỏa thuận"`.

* **3. Cấu Trúc Pandas I/O & Quy Tắc Raw-Immutable:**
  * Cấu trúc Series (1D) và DataFrame (2D), vai trò cốt lõi của **Index**.
  * **6 dòng lệnh kiểm tra dữ liệu bắt buộc (Mandatory Audit Lines):**
    `df.shape`, `df.info()`, `df.head(10)`, `df.dtypes`, `df.isna().sum()`, `df.duplicated().sum()`.
  * **Quy tắc Dữ liệu Thô Nguyên Bản (Raw-Immutable Rule):** Dữ liệu thô lưu tại `data/raw/` kèm timestamp, không được ghi đè hay sửa tay qua Excel. Mọi bước biến đổi thực hiện bằng code và xuất ra `data/processed/`.
  * Thiết lập **Data Dictionary (Từ điển dữ liệu)** chuẩn hóa cho dự án.

---

### 🔹 CHƯƠNG 2: LÀM SẠCH & TIỀN XỬ LÝ DỮ LIỆU

#### 📍 Tuần 3: Chất Lượng Dữ Liệu & Xử Lý Dữ Liệu Khuyết Thiếu (Data Quality & Missing Data)

* **1. Đo Lường Chất Lượng Dữ Liệu & Quy Trình Làm Sạch:**
  * Triết lý: *Sử dụng mô hình đơn giản trên dữ liệu sạch đem lại hiệu quả vượt trội so với mô hình phức tạp trên dữ liệu bẩn.*
  * **6 chiều đo lường chất lượng dữ liệu (Data Quality Dimensions):**
    1. *Completeness (Đầy đủ):* Tỷ lệ giá trị bị thiếu.
    2. *Accuracy (Chính xác):* Giá trị có phản ánh đúng thực tế hay không.
    3. *Consistency (Nhất quán):* Cùng một thực thể được biểu diễn giống nhau.
    4. *Validity (Hợp lệ):* Giá trị thuộc miền cho phép.
    5. *Uniqueness (Duy nhất):* Không bị lặp bản ghi.
    6. *Timeliness (Kịp thời):* Tính mới và phù hợp mốc thời gian.
  * **3 cấp độ lỗi:** Value level, Record level, Relationship level.
  * **Quy tắc chi phí 1–10–100:** $1 để sửa khi nhập liệu, $10 để sửa khi làm sạch, $100 để khắc phục hậu quả sau quyết định sai.
  * **Quy trình 6 bước:** Audit $\rightarrow$ Missing values $\rightarrow$ Outliers $\rightarrow$ Consistency $\rightarrow$ Deduplicate $\rightarrow$ Re-validate.

* **2. Nhận Diện Dữ Liệu Khuyết (Spotting Missing Data):**
  * Nhận diện "Missing giấu mặt": Chuỗi rỗng (`""`), dấu gạch (`"-"`), từ miền (`"không rõ"`, `"Thỏa thuận"`), giá trị số đặc biệt (`-999`, `0`), ngày giả định (`1900-01-01`).
  * Sử dụng hàm kiểm toán `audit(df)` và trực quan hóa mô hình missing bằng thư viện `missingno` (Matrix, Bar plot, Heatmap).

* **3. Ba Cơ Chế Khuyết Thiếu & Phương Pháp Xử Lý (MCAR, MAR, MNAR):**
  * **MCAR (Missing Completely At Random):** Khuyết hoàn toàn ngẫu nhiên $\rightarrow$ Có thể xóa dòng (`dropna`).
  * **MAR (Missing At Random):** Khuyết phụ thuộc vào một biến quan sát được $\rightarrow$ Xử lý bằng **Group-wise Imputation** (`groupby().transform()`).
  * **MNAR (Missing Not At Random):** Khuyết phụ thuộc vào chính giá trị bị thiếu $\rightarrow$ Tạo cờ báo khuyết (**Missing-indicator column**) + mô hình hóa.
  * **Bẫy Data Leakage:** Tính toán tham số điền (mean/median) chỉ trên tập Train (hoặc bọc trong `Pipeline`), tuyệt đối không tính trên toàn bộ tập dữ liệu trước khi split.

---

#### 📍 Tuần 4: Giá Trị Ngoại Lệ, Nhiễu & Sự Nhất Quán (Outliers, Noise & Consistency)

* **1. Phân Biệt Outliers & Nhiễu (Noise):**
  * **3 dạng Outlier:** Point Outlier, Contextual Outlier, Collective Outlier.
  * **Nguồn gốc:** Lỗi nhập liệu, đo lường, xử lý vs. Sự kiện hiếm có thực tế (*Rare Event*).
  * **Phân biệt:** Ngoại lệ $\neq$ Lỗi. Phân biệt **Nhiễu (Noise)** (sai lệch ngẫu nhiên nhỏ toàn bộ dataset $\rightarrow$ xử lý bằng smoothing/binning) và **Outliers** (sai lệch lớn tập trung ở một vài điểm $\rightarrow$ xử lý từng điểm kèm nhật ký).

* **2. Phương Pháp Phát Hiện Outlier:**
  * **Z-score ($|z| > 3$):** Nhạy cảm với giả định phân phối chuẩn và bị hiện tượng Masking Effect (outlier làm phình $\sigma$, tự che giấu chính nó).
  * **Modified Z-score (dùng Median & MAD, $|M| > 3.5$):** Robust, không bị ảnh hưởng bởi giá trị cực trị.
  * **IQR Rule ($Q1 - 1.5 \times IQR$ đến $Q3 + 1.5 \times IQR$):** Chuẩn dùng trong biểu đồ Boxplot, thích hợp cho dữ liệu lệch (skewed).
  * **Machine Learning & Đa biến:** Isolation Forest, LOF, DBSCAN, Mahalanobis Distance.

* **3. Phương Pháp Xử Lý Outlier & Cleaning Log:**
  * **4 lựa chọn:** Keep (Giữ), Delete (Xóa nếu là lỗi xác minh), Cap/Winsorize (`clip` theo quantile 1%-99%), Transform (Log transform, PowerTransformer), hoặc đổi mô hình kháng outlier (Huber Regression, Tree-based models).
  * **Cleaning Log (Nhật ký làm sạch):** Bảng ghi lại bắt buộc gồm các cột `Step`, `Column`, `Finding`, `Action`, `Rows`, `Why` để đảm bảo tính tái lập (Reproducibility).

* **4. Đảm Bảo Tính Nhất Quán (Consistency):**
  * **Duplicate records:** Xóa trùng lặp theo Business Key (`drop_duplicates`); Tìm trùng gần đúng bằng Fuzzy Matching (`rapidfuzz`).
  * **Chuẩn hóa tiếng Việt:** Bẫy Unicode **NFC** vs **NFD** (chuẩn hóa về NFC trước khi so sánh/group/join); Chuyển chữ thường, strip khoảng trắng, map tên tỉnh thành theo danh mục 63 tỉnh/thành chuẩn.
  * **Dates & Units:** Parse ngày tháng (`dayfirst=True`, xử lý ngày tương đối `"hôm qua"`), chuẩn hóa đơn vị (triệu VND / USD / m² / ha).
  * **Validity Rules:** Thiết lập các quy tắc kiểm định hợp lệ bằng boolean mask / `assert` hoặc thư viện `pandera`.

---

#### 📍 Tuần 5: Biến Đổi, Thu Gọn & Tích Hợp Dữ Liệu (Transformation, Reduction & Integration)

* **1. Biến Đổi Dữ Liệu (Transformation):**
  * **Chuẩn hóa Thang đo (Scaling):**
    * *MinMaxScaler:* Đưa về đoạn $[0, 1]$, rất nhạy cảm với outlier.
    * *StandardScaler:* Đưa về Mean 0, Std 1 ($Z$-score), bảo toàn hình dạng phân phối.
    * *RobustScaler:* Dùng Median & IQR, lựa chọn mặc định cho dữ liệu có vệt đuôi dài (heavy tails / outliers).
    * Phân biệt các thuật toán bắt buộc scale (k-NN, SVM, PCA, Neural Net) vs không cần scale (Decision Tree, Random Forest).
  * **Biến đổi phi tuyến (Non-linear Transformation):** Log transform (`np.log1p`), Yeo-Johnson / Box-Cox (`PowerTransformer`) để giảm độ lệch (skewness).
  * **Rời rạc hóa (Binning):** `pd.cut` (ngưỡng cố định) vs `pd.qcut` (chia theo quantile).
  * **Mã hóa Biến Phân Loại (Encoding):**
    * *One-Hot Encoding:* Cho biến định danh (nominal), chú ý `drop_first=True` (tránh dummy trap) và `handle_unknown='ignore'`.
    * *Ordinal Encoding:* Chỉ dùng khi biến có thứ tự thực sự (Seniority, Education level).
    * *Biến phân loại bậc cao:* Group rare values thành `"Other"`, Frequency encoding, Target encoding.
  * Bọc toàn bộ quy trình tiền xử lý trong **Scikit-Learn Pipeline** để chống rò rỉ dữ liệu (Data Leakage).

* **2. Thu Gọn Dữ Liệu (Reduction):**
  * **Giảm số cột (Dimensionality Reduction):** `VarianceThreshold` (xóa cột gần như hằng số), loại bỏ cặp biến có độ tương quan cao ($r > 0.95$), chiếu không gian dữ liệu qua **PCA** (Principal Component Analysis - lưu ý scale dữ liệu trước khi PCA).
  * **Giảm số dòng (Cardinality Reduction):** Random sampling, Stratified sampling (bắt buộc khi lớp hiếm), Time-based split cho chuỗi thời gian.

* **3. Tích Hợp Dữ Liệu (Integration) & Preprocessing Pipeline:**
  * **ETL vs ELT:** Khác biệt thứ tự biến đổi và tầm quan trọng của việc giữ nguyên dữ liệu thô.
  * **Nối & Trộn dữ liệu (`concat`, `merge`):** 4 kiểu Join (Inner, Left, Right, Outer).
  * **Phòng ngừa bẫy Bùng Nổ Dòng (Row Explosion):** Sử dụng tham số `validate='many_to_one'`, kiểm tra `len(df)` trước và sau merge, sử dụng `indicator=True`.
  * **Entity Resolution:** Định danh thực thể qua kỹ thuật Blocking và Fuzzy Matching.
  * **Xoay chuyển dữ liệu:** Dạng Rộng (Wide) $\leftrightarrow$ Dạng Dài (Long - Tidy Data) qua `melt` và `pivot_table`. Tổng hợp dữ liệu với `groupby` & Named Aggregation.
  * **Đóng gói Preprocessing Pipeline:** Sử dụng `ColumnTransformer` và `Pipeline` để tự động hóa toàn bộ luồng tiền xử lý dữ liệu từ Raw đến Processed mà không gây rò rỉ dữ liệu.

---

## 🛠️ HƯỚNG DẪN TÁI LẬP & CẤU TRÚC THƯ MỤC THỰC HÀNH

```text
project-root/
├── data/
│   ├── raw/          # Dữ liệu thô ban đầu (Raw-immutable, kèm timestamp)
│   └── processed/    # Dữ liệu sạch sau tiền xử lý (Sẵn sàng cho EDA & Modeling)
├── src/
│   ├── utils.py      # Chứa hàm audit(df), normalize_vn()
│   └── pipeline.py   # Chứa ColumnTransformer & Preprocessing Pipeline
├── logs/
│   └── cleaning.csv  # Nhật ký làm sạch (Cleaning Log)
└── README.md         # Tài liệu tổng quan chương trình học
```

---
*Tài liệu tổng hợp dựa trên chuỗi bài giảng Khoa học Dữ liệu INFO3020 – CMC University.*
