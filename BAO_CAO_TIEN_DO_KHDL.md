# 📊 BÁO CÁO TIẾN ĐỘ TOÀN DIỆN DỰ ÁN KHOA HỌC DỮ LIỆU (INFO3020)
# ĐỀ TÀI: PHÂN TÍCH KHÔNG GIAN VÀ DỰ ĐOÁN GIÁ BẤT ĐỘNG SẢN TẠI HÀ NỘI
*(Tài liệu báo cáo tiến độ triển khai thực tế từ Tuần 1 đến Tuần 10: Thu Thập, Tiền Xử Lý, Kỹ Nghệ Đặc Trưng, EDA, Thống Kê Suy Luận & Chẩn Đoán Mô Hình Hồi Quy)*

---

## 📑 MỤC LỤC BÁO CÁO
1. [CHƯƠNG 1: BỐI CẢNH NGHIÊN CỨU & BÀI TOÁN KINH DOANH (TUẦN 1 - 2)](#chương-1-bối-cảnh-nghiên-cứu--bài-toán-kinh-doanh-tuần-1---2)
   - 1.1. Bối cảnh thị trường BĐS Hà Nội & 3 Câu hỏi kinh doanh cốt lõi
   - 1.2. Chiến lược thu thập dữ liệu & Tuân thủ đạo đức dữ liệu cá nhân
   - 1.3. Nguyên tắc dữ liệu thô bất biến (Raw-Immutable Rule)
2. [CHƯƠNG 2: KIỂM TOÁN CHẤT LƯỢNG & QUY TRÌNH TIỀN XỬ LÝ DỮ LIỆU (TUẦN 3 - 4)](#chương-2-kiểm-toán-chất-lượng--quy-trình-tiền-xử-lý-dữ-liệu-tuần-3---4)
   - 2.1. Kết quả kiểm toán chất lượng dữ liệu ban đầu
   - 2.2. Lọc chu kỳ 18 tháng gần nhất (2025 - 2026): Cơ sở kinh tế và kỹ thuật
   - 2.3. Quy trình chuẩn hóa văn bản, bảng mã tiếng Việt và bóc tách số học
   - 2.4. Xử lý dữ liệu khuyết & Chuẩn hóa bất động sản đất trống (Số tầng = 0)
   - 2.5. Giải quyết dứt điểm lỗi cắt cụt giá 175 triệu bằng Bộ lọc miền tri thức thực tế
   - 2.6. Nhật ký 10 bước làm sạch dữ liệu hoàn chỉnh (Data Cleaning Log)
3. [CHƯƠNG 3: KỸ NGHỆ ĐẶC TRƯNG & TỪ ĐIỂN DỮ LIỆU 38 BIẾN (TUẦN 5)](#chương-3-kỹ-nghệ-đặc-trưng--từ-điển-dữ-liệu-38-biến-tuần-5)
   - 3.1. Phương pháp luận tạo lập các biến phái sinh đa chiều
   - 3.2. Từ điển dữ liệu chuẩn hóa 38 thuộc tính bất động sản
   - 3.3. Đóng gói quy trình biến đổi thành Scikit-Learn Pipeline chống rò rỉ dữ liệu
4. [CHƯƠNG 4: PHÂN TÍCH KHÁM PHÁ (EDA) & BỘ ĐẠI LƯỢNG THỐNG KÊ (TUẦN 6)](#chương-4-phân-tích-khám-phá-eda--bộ-đại-lượng-thống-kê-tuần-6)
   - 4.1. Thống kê Độ tập trung (Location) & Độ tán sắc (Spread)
   - 4.2. Thống kê Hình dạng phân phối (Shape): Bản chất Log-normal
   - 4.3. Thống kê Mối quan hệ tương quan (Relationship): Ma trận Pearson
5. [CHƯƠNG 5: PHÂN TÍCH CHI TIẾT & MẠCH LẠC 6 BIỂU ĐỒ TRỰC QUAN HÓA (TUẦN 7)](#chương-5-phân-tích-chi-tiết--mạch-lạc-6-biểu-đồ-trực-quan-hóa-tuần-7)
   - 5.1. Biểu đồ 1: Ma trận tương quan đa biến (Correlation Heatmap)
   - 5.2. Biểu đồ 2: Phân phối Đơn giá & Tổng giá trị BĐS (Histogram & KDE)
   - 5.3. Biểu đồ 3: Phân tích tương quan Phân tán & Khắc phục lỗi hiển thị trục (Scatter Plot)
   - 5.4. Biểu đồ 4: Phân bố đơn giá 12 quận huyện trọng điểm (Boxplot theo Trung vị)
   - 5.5. Biểu đồ 5: Đánh giá & So sánh hiệu năng 4 mô hình hồi quy (Model Comparison)
   - 5.6. Biểu đồ 6: Tầm quan trọng của các yếu tố định giá (Feature Importance)
6. [CHƯƠNG 6: THỬ NGHIỆM MÔ HÌNH HÓA & TRỢ LÝ ĐỊNH GIÁ AI (TUẦN 7 - 8)](#chương-6-thử-nghiệm-mô-hình-hóa--trợ-lý-định-giá-ai-tuần-7---8)
   - 6.1. Thiết lập phân chia tập huấn luyện và kiểm thử (Train/Test Split 80/20)
   - 6.2. Bảng đối đầu hiệu năng giữa các thuật toán học máy
   - 6.3. Trợ lý AI định giá nhà tự động ứng dụng thực tế
7. [CHƯƠNG 7: THỐNG KÊ SUY LUẬN & KIỂM ĐỊNH GIẢ THUYẾT (TUẦN 9)](#chương-7-thống-kê-suy-luận--kiểm-định-giả-thuyết-tuần-9)
   - 7.1. Bản chất Thống kê suy luận & Nguyên lý kiểm định giả thuyết khoa học
   - 7.2. Kiểm định Giả thuyết Nội đô vs Ngoại thành: Welch's t-test & Mann-Whitney U
   - 7.3. Phân tích phương sai One-Way ANOVA & So sánh từng cặp Tukey's HSD
   - 7.4. Phân tích Biểu đồ 7: Khoảng tin cậy 95% (95% CI) cho 12 Quận/Huyện
   - 7.5. Kiểm định Chi-square độc lập: Vị trí Nội đô vs Tình trạng Sổ đỏ
8. [CHƯƠNG 8: CHẨN ĐOÁN HỒI QUY TUYẾN TÍNH & 4 GIẢ ĐỊNH LINE (TUẦN 10)](#chương-8-chẩn-đoán-hồi-quy-tuyến-tính--4-giả-định-line-tuần-10)
   - 8.1. Đọc hiểu mô hình OLS cơ sở & 3 Nghĩa vụ đạo đức khi diễn giải hệ số $\beta$
   - 8.2. Phân tích Biểu đồ 8: Kiểm định 4 Giả định LINE (Linearity - Independence - Normality - Equal Variance)
   - 8.3. Giải pháp đột phá: Phép biến đổi Logarit $\log(y)$ phục hồi phân phối chuẩn
   - 8.4. Phân tích Biểu đồ 9: Kỹ thuật Điều chuẩn Regularisation (Ridge L2 vs Lasso L1)
9. [CHƯƠNG 9: TỔNG KẾT TIẾN ĐỘ & LỘ TRÌNH TRIỂN KHAI CUỐI KỲ (TUẦN 11 - 12)](#chương-9-tổng-kết-tiến-độ--lộ-trình-triển-khai-cuối-kỳ-tuần-11---12)
   - 9.1. 7 Kết luận thực tiễn rút ra từ dữ liệu thực tế
   - 9.2. Các hạn chế kỹ thuật hiện tại
   - 9.3. Kế hoạch hành động chi tiết cho giai đoạn cuối kỳ (Tuần 11 đến Tuần 12)

---

## CHƯƠNG 1: BỐI CẢNH NGHIÊN CỨU & BÀI TOÁN KINH DOANH (TUẦN 1 - 2)

### 1.1. Bối cảnh thị trường BĐS Hà Nội & 3 Câu hỏi kinh doanh cốt lõi
Thị trường bất động sản (BĐS) nhà ở tại Thủ đô Hà Nội trong giai đoạn 2024 – 2026 ghi nhận những chuyển dịch mạnh mẽ. Sự khan hiếm nguồn cung mới tại các quận lõi, hiệu lực của Luật Đất đai sửa đổi cùng tốc độ hoàn thiện các tuyến vành đai và đường sắt đô thị đã đẩy mặt bằng giá nhà đất tăng trưởng rõ rệt. Tuy nhiên, thông tin trên các kênh rao vặt trực tuyến thường bị nhiễu loạn bởi tin ảo câu tương tác, giá đăng lệch xa giá giao dịch thực, hoặc thông tin thiếu minh bạch.

Dự án **Khoa học Dữ liệu BĐS Hà Nội (INFO3020)** được thành lập nhằm giải quyết 3 bài toán kinh doanh trọng yếu:
1. **Xác lập Mặt bằng giá thực (Price Baseline)**: Đơn giá thực tế trên mỗi mét vuông ($triệu/m^2$) tại các quận, huyện Hà Nội đang phân bổ như thế nào? Mức giá trung vị tại từng khu vực là bao nhiêu sau khi đã sàng lọc toàn bộ tin rác và dữ liệu lỗi thời?
2. **Định danh Nhân tố chi phối giá trị (Value Drivers)**: Trong các yếu tố vị trí nội đô, diện tích đất, bề rộng mặt tiền, số tầng xây dựng, số phòng ngủ hay tình trạng pháp lý, đâu là những biến số có ảnh hưởng quyết định đến giá trị tài sản?
3. **Xây dựng Công cụ định giá tự động (Automated Valuation Model - AVM)**: Liệu có thể huấn luyện một mô hình học máy có độ chính xác cao (sai số trung bình $MAE < 26$ triệu/m²) để hỗ trợ người dân, chuyên gia thẩm định và ngân hàng ước tính nhanh giá trị hợp lý của một bất động sản?

### 1.2. Chiến lược thu thập dữ liệu & Tuân thủ đạo đức dữ liệu cá nhân
* **Chiến lược thu thập đa kênh**:
  - Dữ liệu được thu thập tự động từ các chuyên trang bất động sản hàng đầu Việt Nam (Batdongsan, Homedy, Alonhadat) bằng các công cụ thu thập dữ liệu chuyên dụng, có tích hợp cơ chế chống chặn (Stealth Mode) và giãn cách thời gian truy vấn để không gây áp lực tải lên hạ tầng máy chủ nguồn.
  - Kết hợp đồng bộ với các tập dữ liệu mở lịch sử uy tín trên các nền tảng khoa học dữ liệu (HuggingFace, Kaggle).
* **Tuân thủ Đạo đức Dữ liệu & Quy định Pháp lý**:
  - Nghiêm túc chấp hành **Nghị định 13/2023/NĐ-CP** về Bảo vệ dữ liệu cá nhân: Toàn bộ thông tin định danh cá nhân trực tiếp (Họ tên chủ nhà, số điện thoại, email cá nhân) đều được tự động loại bỏ ngay từ tầng thu thập.
  - Dự án chỉ lưu giữ các thông tin vật lý công khai của tài sản: Diện tích, kích thước mặt tiền/chiều sâu, số tầng, số phòng ngủ, vị trí quận/phường, tình trạng pháp lý và mức giá niêm yết.

### 1.3. Nguyên tắc dữ liệu thô bất biến (Raw-Immutable Rule)
* Toàn bộ dữ liệu thu thập được tập hợp nguyên trạng vào tệp duy nhất: [`data/raw/raw.csv`](file:///Users/longnguyen/Documents/bds_khdl/data/raw/raw.csv).
* **Quy mô tập dữ liệu thô**: Đúng **99.998 bản ghi** và **12 cột thuộc tính gốc**.
* **Nguyên tắc bất biến**: Tệp dữ liệu thô được lưu giữ như bằng chứng dữ liệu gốc, tuyệt đối không chỉnh sửa thủ công và không ghi đè. Mọi thao tác sàng lọc, làm sạch và kỹ nghệ đặc trưng đều được thực thi tự động qua mã nguồn chuẩn hóa, lưu trữ độc lập tại [`data/processed/clean.csv`](file:///Users/longnguyen/Documents/bds_khdl/data/processed/clean.csv).

---

## CHƯƠNG 2: KIỂM TOÁN CHẤT LƯỢNG & QUY TRÌNH TIỀN XỬ LÝ DỮ LIỆU (TUẦN 3 - 4)

### 2.1. Kết quả kiểm toán chất lượng dữ liệu ban đầu
Trước khi tiến hành xử lý, dữ liệu thô được đưa qua quy trình kiểm toán toàn diện để nhận diện các điểm khiếm khuyết:

* **Quy mô & Bộ nhớ**: Tệp gốc chứa 99.998 dòng và 12 cột, dung lượng xấp xỉ 9.2 MB.
* **Xung đột kiểu dữ liệu**: 100% các cột dạng số (Diện tích, Giá/m2, Số tầng, Kích thước) đang bị lưu dưới dạng văn bản (chuỗi) do đính kèm đơn vị tính (`m²`, `triệu/m²`, `tầng`) hoặc chứa dấu phân cách thập phân kiểu Việt Nam (dấu phẩy `,`).
* **Tỷ lệ khuyết thiếu thông tin**:
  - `Giấy tờ pháp lý`: Khuyết ~35% bản ghi do người đăng không điền.
  - `Chiều dài` và `Chiều rộng`: Khuyết ~55% bản ghi (người đăng chỉ cung cấp tổng diện tích).
  - `Số tầng`: Khuyết ~38% bản ghi (đặc biệt phổ biến ở các lô đất nền trống).
* **Độ trùng lặp bản ghi**: Không có bản ghi nào trùng lặp hoàn toàn trên tất cả 12 trường thông tin.

### 2.2. Lọc chu kỳ 18 tháng gần nhất (2025 - 2026): Cơ sở kinh tế và kỹ thuật
* **Phát hiện nghiệp vụ**: Dữ liệu thô trải dài từ ngày `01/01/2020` đến ngày `28/09/2026`. Trong đó, hơn 61.000 tin đăng thuộc giai đoạn 2020 – 2024 mang mặt bằng giá cũ, thấp hơn từ 40% đến 70% so với thị trường hiện tại.
* **Tác hại nếu giữ dữ liệu cũ**: Việc gộp dữ liệu giá của 6 năm với mức lạm phát và chu kỳ sốt đất khác nhau sẽ tạo ra phân phối đa đỉnh giả tạo (Bimodal Distribution), khiến mô hình dự báo luôn bị kéo lệch xuống dưới so với thực tế giao dịch 2026.
* **Quyết định kỹ thuật**:
  - Xác định mốc thời gian đăng tin mới nhất: Ngày `28/09/2026`.
  - Cắt cửa sổ dữ liệu 18 tháng tính ngược: Từ ngày **28/03/2025** đến **28/09/2026**.
  - Loại bỏ 61.493 tin đăng cũ, giữ lại **38.505 bản ghi** thuộc chu kỳ thị trường hiện tại.

### 2.3. Quy trình chuẩn hóa văn bản, bảng mã tiếng Việt và bóc tách số học
* **Chuẩn hóa Bảng mã Unicode tiếng Việt**: Khắc phục triệt để lỗi không khớp chuỗi do xung đột giữa bảng mã Unicode tổ hợp (NFD) và Unicode dựng sẵn (NFC). Toàn bộ dữ liệu chữ được đưa về định dạng Unicode NFC, viết thường và cắt bỏ khoảng trắng thừa hai đầu.
* **Bóc tách số học tự động**:
  - *Diện tích*: Trích xuất chính xác phần số thực, chuyển đổi dấu phẩy thập phân sang dấu chấm (ví dụ: chuỗi `"48,5 m²"` trở thành số thực $48.5$).
  - *Đơn giá*: Trích xuất phần số đơn giá, đồng thời loại bỏ các tin chứa lỗi dữ liệu cực đoan như `"inf triệu/m²"` hoặc lỗi gõ lặp chuỗi số.
  - *Kích thước (Mặt tiền & Chiều sâu)*: Nhận diện và trích xuất kích thước chiều rộng, chiều dài. Đặc biệt bổ sung thuật toán phát hiện người dùng nhập nhầm đơn vị milimet (ví dụ `4500` mm được tự động quy đổi thành `4.5` m).

### 2.4. Xử lý dữ liệu khuyết & Chuẩn hóa bất động sản đất trống (Số tầng = 0)
* **Nguyên tắc loại bỏ dữ liệu khuyết biến mục tiêu (MCAR Deletion)**:
  - Hai thuộc tính `Giá_m2_trieu` và `Diện tích m2` là thành phần quyết định của bài toán định giá. Nếu thiếu 1 trong 2 biến này, bản ghi không còn giá trị phân tích.
  - Tuyệt đối không áp dụng điền giá trị nhân tạo (Mean/Median) vào biến giá vì sẽ làm sai lệch phương sai và phân phối thực tế. Hành động: Loại bỏ 875 dòng khuyết giá hoặc diện tích.
* **Chuẩn hóa Số tầng = 0 cho BĐS Đất**:
  - Các tin đăng "Đất nền", "Đất dịch vụ", "Đất thổ cư" người bán thường để trống số tầng.
  - Hệ thống tự động nhận diện từ khóa liên quan đến đất và gán giá trị `Số tầng = 0.0`.
* **Cờ chỉ báo thiếu thông tin (Missing Indicator)**:
  - Với các căn nhà ở thông thường nhưng bị khuyết số tầng, hệ thống tạo biến nhị phân `Thieu_So_Tang = 1` (nếu có đủ số tầng thì `= 0`), giúp mô hình học được đặc điểm của nhóm dữ liệu bị thiếu thông tin.

### 2.5. Giải quyết dứt điểm lỗi cắt cụt giá 175 triệu bằng Bộ lọc miền tri thức thực tế
* **Hiện tượng lỗi ở phiên bản cũ**:
  - Pipeline cũ từng sử dụng phương pháp cắt cụt ngoại lệ toán học tự động theo ngưỡng $Q3 + 1.5 \times IQR \approx 174.2 \text{ triệu/m²}$.
  - Thao tác này đã vô tình ép toàn bộ hơn 5.700 căn nhà cao cấp có giá trên 175 triệu về đúng giá trị 174.2. Hậu quả là biểu đồ phân phối xuất hiện một **cột nhô cao đột biến bất thường tại mốc 175 triệu**, làm sai lệch hình thái phân phối tự nhiên.
* **Khắc phục theo nguyên lý Khoa học Dữ liệu BĐS**:
  - Bản chất giá trị bất động sản luôn có phân phối lệch phải (Log-normal). Các căn nhà mặt phố cổ Hoàn Kiếm, biệt thự Tây Hồ có giá từ 200 đến 450 triệu/m² là hoàn toàn có thật và đại diện cho phân khúc cao cấp hợp pháp của thị trường Thủ đô.
  - Thay thế hoàn toàn lệnh cắt cụt bằng **Bộ lọc miền tri thức thực tế**:
    - Giới hạn đơn giá: $10.0 \le \text{Giá\_m2\_trieu} \le 500.0 \text{ triệu VNĐ/m²}$.
    - Giới hạn diện tích: $10.0 \le \text{Diện tích m2} \le 500.0 \text{ m²}$.
  - Ngưỡng dưới 10 triệu loại trừ các tin rao đất nông nghiệp xa xôi hoặc tin lừa đảo 1-2 triệu. Ngưỡng trên 500 triệu loại trừ các tin gõ nhầm hàng nghìn tỷ. Phân phối sau khi lọc trở nên mượt mà, tự nhiên và bảo toàn trọn vẹn đặc tính thị trường.

### 2.6. Nhật ký 10 bước làm sạch dữ liệu hoàn chỉnh (Data Cleaning Log)

| Bước | Hạng Mục Công Việc | Cột Tác Động | Dạng Nhiễu / Lỗi Phát Hiện | Phương Pháp Xử Lý Chuẩn Hóa | Số Bản Ghi Tác Động | Ý Nghĩa Thực Tiễn |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | Lọc chu kỳ thời gian | `Ngày` | Dữ liệu kéo dài 2020-2024 có mặt bằng giá cũ, lệch lạm phát | Cắt cửa sổ 18 tháng ($28/03/2025 \rightarrow 28/09/2026$) | Loại 61.493 dòng cũ | Bảo đảm tính tươi mới và sát với mặt bằng giá thị trường hiện nay |
| **2** | Chuẩn hóa bảng mã | `Quận`, `Địa chỉ`, `Loại hình` | Xung đột giữa bảng mã Unicode tổ hợp và dựng sẵn | Chuyển đổi toàn bộ về Unicode dựng sẵn (NFC) | 38.505 dòng | Đồng nhất định dạng ký tự tiếng Việt, loại bỏ lỗi gom nhóm |
| **3** | Bóc tách Diện tích | `Diện tích` | Chuỗi văn bản chứa `'m²'`, `'m2'`, dấu phẩy | Trích xuất thành số thực (`float64`) | 38.505 dòng | Chuyển đổi thành biến định lượng liên tục |
| **4** | Bóc tách Đơn giá | `Giá/m2` | Chuỗi văn bản chứa `'triệu/m²'`, chuỗi `'inf'` | Trích xuất số thực, loại bỏ các chuỗi vô cực | 38.505 dòng | Chuẩn hóa đơn vị tính về triệu VNĐ/$m^2$ |
| **5** | Loại bỏ khuyết mục tiêu | `Giá_m2_trieu`, `Diện tích m2` | Dòng để "Giá thỏa thuận" hoặc khuyết diện tích | Loại bỏ bản ghi thiếu biến mục tiêu | Loại 875 dòng | Tuyệt đối không điền giá trị giả vào biến phụ thuộc |
| **6** | Chuẩn hóa BĐS đất | `Số tầng`, `Loại hình` | Đất trống nhưng cột tầng bị để trống | Quét từ khóa đất $\rightarrow$ Gán `Số tầng = 0.0` | 2.140 dòng | Phản ánh đúng đặc tính vật lý: đất không có công trình xây dựng |
| **7** | Cờ chỉ báo thiếu tầng | `Thieu_So_Tang` | Nhà ở nhưng người đăng quên điền số tầng | Tạo biến nhị phân: $1$ nếu thiếu, $0$ nếu có đủ | 14.210 dòng | Giúp mô hình học cơ chế thiếu dữ liệu có chủ ý |
| **8** | Bóc tách kích thước | `Dài`, `Rộng` | Chuỗi văn bản kích thước, người dùng nhập mm | Quy đổi mm về mét, lọc giới hạn $[1.5, 30]$ m | 16.256 dòng mặt tiền | Loại bỏ triệt để outlier gõ nhầm 400.000m, chuẩn hóa kích thước |
| **9** | Lọc theo miền tri thức | `Giá_m2_trieu`, `Diện tích m2` | Tin ảo gõ giá $0.5$ tr/m² hoặc biệt thự ảo $> 500$ tr | Áp dụng ngưỡng $[10, 500]$ tr/m² và $[10, 500]$ m² | Loại 228 dòng | Khắc phục dứt điểm lỗi nhô cột 175 triệu của phương pháp cắt cụt cũ |
| **10** | **Tập dữ liệu sạch hoàn chỉnh** | **Tập dữ liệu xử lý** | **Hoàn tất toàn bộ quy trình tiền xử lý** | **Xuất tệp `data/processed/clean.csv`** | **Còn lại đúng 37.402 bản ghi** | **Sạch 100%, sẵn sàng cho phân tích EDA và huấn luyện mô hình** |

---

## CHƯƠNG 3: KỸ NGHỆ ĐẶC TRƯNG & TỪ ĐIỂN DỮ LIỆU 38 BIẾN (TUẦN 5)

### 3.1. Phương pháp luận tạo lập các biến phái sinh đa chiều
Từ 12 trường thông tin thô ban đầu, dự án đã phát triển mở rộng thành **38 thuộc tính chuyên sâu**, bao quát đầy đủ 6 khía cạnh định giá bất động sản:

1. **Tổng giá trị tài sản ước tính (`Tong_Gia_ty`)**:
   - Được tính bằng tích của Đơn giá ($triệu/m^2$) nhân với Diện tích ($m^2$), sau đó quy đổi ra đơn vị Tỷ đồng. Đây là biến quy mô tài sản phục vụ phân khúc khách hàng.
2. **Hình thái hình học thửa đất (`ty_le_dai_rong` & `hinh_dang_dat`)**:
   - Tỷ lệ giữa Chiều sâu và Chiều rộng mặt tiền. Thửa đất được phân thành 3 nhóm hình thái:
     - *Mặt tiền lớn* (Tỷ lệ $< 1.0$): Chiều ngang rộng hơn chiều sâu, giá trị thương mại rất cao.
     - *Đất vuông vắn* (Tỷ lệ $1.0 - 2.5$): Tỷ lệ chuẩn phong thủy trong xây dựng nhà ở dân dụng.
     - *Dài hẹp* (Tỷ lệ $> 2.5$): Dạng nhà ống sâu, thông gió hạn chế hơn.
3. **Tổng diện tích sàn sử dụng ước tính (`tong_dien_tich_san_m2`)**:
   - Tích của Diện tích đất nhân với Số tầng thực tế (với đất trống số tầng = 0 thì diện tích sàn bằng chính diện tích đất). Biến này phản ánh không gian sinh hoạt và công năng thực tế của ngôi nhà.
4. **Mật độ và độ tiện nghi phòng ngủ**:
   - `dien_tich_moi_phong_ngu_m2`: Đo lường mức độ rộng rãi trung bình của mỗi phòng ngủ.
   - `mat_do_phong_ngu`: Tỷ lệ số phòng ngủ trên một mét vuông diện tích đất.
5. **Đặc trưng Không gian Vị trí Lõi (`khu_vuc_noi_do`)**:
   - Biến nhị phân đánh dấu các bất động sản nằm trong 7 quận trung tâm lịch sử và thương mại của Hà Nội: Hoàn Kiếm, Ba Đình, Đống Đa, Hai Bà Trưng, Cầu Giấy, Tây Hồ, Thanh Xuân.
6. **Bóc tách Tên đường phố (`duong_pho`) và Phường xã (`phuong_xa`)**:
   - Tách riêng tên tuyến phố và tên phường từ chuỗi địa chỉ để phục vụ phân tích cụm vi mô.

### 3.2. Từ điển dữ liệu chuẩn hóa 38 thuộc tính bất động sản

| STT | Tên Cột | Kiểu Dữ Liệu | Miền Giá Trị | Phân Nhóm | Ý Nghĩa Nghiệp Vụ |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `Ngày` | Chuỗi | YYYY-MM-DD | Thời gian | Ngày đăng tin gốc của bài viết |
| 2 | `nam` | Số nguyên | 2025, 2026 | Thời gian | Năm đăng tin |
| 3 | `thang` | Số nguyên | 1 - 12 | Thời gian | Tháng đăng tin trong năm |
| 4 | `quy` | Số nguyên | 1 - 4 | Thời gian | Quý đăng tin (Q1, Q2, Q3, Q4) |
| 5 | `nam_thang` | Chuỗi | YYYY-MM | Thời gian | Chu kỳ tháng (ví dụ: `2025-08`, `2026-03`) |
| 6 | `Địa chỉ` | Chuỗi | Văn bản | Vị trí | Địa chỉ chi tiết nguyên bản của bất động sản |
| 7 | `Quận` | Chuỗi | 30 quận/huyện | Vị trí | Tên quận huyện sau khi chuẩn hóa |
| 8 | `Huyện` | Chuỗi | Văn bản | Vị trí | Tên phường/xã hoặc địa danh nguyên bản |
| 9 | `duong_pho` | Chuỗi | Tên đường | Vị trí | Tên tuyến đường/phố trích xuất từ địa chỉ |
| 10 | `phuong_xa` | Chuỗi | Tên phường | Vị trí | Tên phường/xã trích xuất từ địa chỉ |
| 11 | `khu_vuc_noi_do` | Nhị phân | 0 hoặc 1 | Vị trí | Đánh dấu thuộc 7 quận lõi trung tâm Thủ đô |
| 12 | `Diện tích` | Chuỗi | Chứa `m²` | Kích thước | Chuỗi diện tích nguyên bản |
| 13 | `Diện tích m2` | Số thực | $10 - 500$ $m^2$ | Kích thước | Diện tích thửa đất dạng số thực |
| 14 | `Dài` | Chuỗi | Chứa `m` | Kích thước | Chiều dài thửa đất nguyên bản |
| 15 | `Rộng` | Chuỗi | Chứa `m` | Kích thước | Chiều rộng mặt tiền nguyên bản |
| 16 | `mat_tien_m` | Số thực | $1.5 - 30.0$ m | Kích thước | Bề rộng mặt tiền đã quy đổi mét và làm sạch |
| 17 | `chieu_sau_m` | Số thực | $2.0 - 60.0$ m | Kích thước | Chiều sâu thửa đất đã làm sạch |
| 18 | `ty_le_dai_rong`| Số thực | Tỷ lệ | Kích thước | Tỷ lệ giữa Chiều sâu và Mặt tiền |
| 19 | `hinh_dang_dat` | Định danh | 3 nhóm | Kích thước | `Mặt tiền lớn`, `Vuông vắn`, `Dài hẹp` |
| 20 | `Số tầng` | Số thực | $0 - 70$ tầng | Công năng | Số tầng xây dựng thực tế ($0$ là đất trống) |
| 21 | `Thieu_So_Tang` | Nhị phân | 0 hoặc 1 | Công năng | Cờ đánh dấu tin đăng không ghi số tầng |
| 22 | `phan_loai_tang`| Định danh | 4 cấp | Công năng | `Thấp tầng (<=3)`, `Trung tầng (4-6)`, `Cao tầng (>6)`, `Không rõ` |
| 23 | `tong_dien_tich_san_m2`| Số thực | $m^2$ | Công năng | Ước tính tổng diện tích sàn xây dựng |
| 24 | `Số phòng ngủ` | Số thực | $1 - 25$ phòng | Công năng | Số lượng phòng ngủ thiết kế |
| 25 | `dien_tich_moi_phong_ngu_m2`| Số thực | $m^2$/phòng | Công năng | Diện tích đất trung bình trên mỗi phòng ngủ |
| 26 | `mat_do_phong_ngu`| Số thực | Phòng/$m^2$ | Công năng | Tỷ lệ số lượng phòng ngủ trên diện tích đất |
| 27 | `Giấy tờ pháp lý`| Chuỗi | Văn bản | Pháp lý | Tình trạng pháp lý nguyên bản |
| 28 | `co_so_do` | Nhị phân | 0 hoặc 1 | Pháp lý | $1$ nếu có sổ đỏ / sổ hồng chính chủ |
| 29 | `Loại hình nhà ở`| Chuỗi | Văn bản | Loại hình | Phân loại nhà ở nguyên bản |
| 30 | `loai_nha_mat_pho`| Nhị phân | 0 hoặc 1 | Loại hình | Nhận diện nhà mặt phố kinh doanh |
| 31 | `loai_nha_ngo_hem`| Nhị phân | 0 hoặc 1 | Loại hình | Nhận diện nhà trong ngõ hẻm |
| 32 | `loai_can_ho` | Nhị phân | 0 hoặc 1 | Loại hình | Nhận diện căn hộ chung cư |
| 33 | `loai_biet_thu_lien_ke`| Nhị phân | 0 hoặc 1 | Loại hình | Nhận diện biệt thự hoặc liền kề |
| 34 | `Giá/m2` | Chuỗi | Văn bản | Định giá | Chuỗi đơn giá nguyên bản |
| 35 | `Giá_m2_trieu` | Số thực | $10 - 500$ tr/m² | Định giá | **Biến mục tiêu (Target)**: Đơn giá triệu VNĐ/$m^2$ |
| 36 | `Tong_Gia_ty` | Số thực | Tỷ VNĐ | Định giá | Tổng giá trị tài sản tính bằng Tỷ đồng |
| 37 | `phan_khuc_don_gia`| Định danh | 4 phân khúc | Định giá | `Rẻ (<60)`, `Phổ thông (60-100)`, `Cao (100-180)`, `Rất cao (>180 tr/m²)` |
| 38 | `phan_khuc_tong_gia`| Định danh | 5 phân khúc | Định giá | `Bình dân (<3)`, `Trung cấp (3-7)`, `Khá (7-15)`, `Cao cấp (15-30)`, `Siêu sang (>30 tỷ)` |

### 3.3. Đóng gói quy trình biến đổi thành Scikit-Learn Pipeline chống rò rỉ dữ liệu
Toàn bộ quy trình tiền xử lý trước khi nạp vào mô hình máy học được đóng gói chặt chẽ trong `ColumnTransformer` để ngăn chặn tuyệt đối hiện tượng rò rỉ dữ liệu (Data Leakage) từ tập kiểm thử sang tập huấn luyện:
* **Nhóm biến số định lượng**: Điền khuyết bằng giá trị Trung vị (Median) học từ tập Train, sau đó co giãn dữ liệu bằng `RobustScaler` (dựa trên Trung vị và Khoảng liên phân vị IQR), giúp mô hình duy trì tính ổn định trước các biến động cực đoan.
* **Nhóm biến định danh phân loại**: Điền khuyết bằng nhãn mặc định và mã hóa One-Hot Encoding với tùy chọn loại bỏ cột đầu tiên nhằm triệt tiêu hoàn toàn hiện tượng đa cộng tuyến hoàn hảo (Dummy Variable Trap).

---

## CHƯƠNG 4: PHÂN TÍCH KHÁM PHÁ (EDA) & BỘ ĐẠI LƯỢNG THỐNG KÊ (TUẦN 6)

Dựa trên tập dữ liệu chuẩn hóa gồm **37.402 bất động sản** trong 18 tháng gần nhất, hệ thống tính toán đầy đủ 4 nhóm đại lượng thống kê mô tả:

### 4.1. Thống kê Độ tập trung (Location) & Độ tán sắc (Spread)
* **Đơn giá bất động sản ($triệu/m^2$)**:
  - Giá trị nhỏ nhất (Min): $10.00 \text{ triệu/m²}$
  - Phân vị 25% (Q1): $72.67 \text{ triệu/m²}$
  - **Trung vị (Median)**: **$90.00 \text{ triệu/m²}$**
  - **Trung bình (Mean)**: **$102.18 \text{ triệu/m²}$**
  - Phân vị 75% (Q3): $112.50 \text{ triệu/m²}$
  - Giá trị lớn nhất (Max): $500.00 \text{ triệu/m²}$
  - Độ lệch chuẩn (Std): $54.78 \text{ triệu/m²}$
  - Khoảng liên phân vị (IQR): $Q3 - Q1 = \mathbf{39.83 \text{ triệu/m²}}$
  - Hệ số biến thiên (CV): $53.6\%$
* **Tổng giá trị một bất động sản (Tỷ VNĐ)**:
  - Giá trị nhỏ nhất (Min): $0.25 \text{ Tỷ VNĐ}$
  - Phân vị 25% (Q1): $2.75 \text{ Tỷ VNĐ}$
  - **Trung vị (Median)**: **$3.60 \text{ Tỷ VNĐ}$**
  - **Trung bình (Mean)**: **$5.10 \text{ Tỷ VNĐ}$**
  - Phân vị 75% (Q3): $5.30 \text{ Tỷ VNĐ}$
  - Giá trị lớn nhất (Max): $237.00 \text{ Tỷ VNĐ}$
  - Độ lệch chuẩn (Std): $5.76 \text{ Tỷ VNĐ}$

### 4.2. Thống kê Hình dạng phân phối (Shape): Bản chất Log-normal
* **Độ lệch phân phối (Skewness)**:
  - Hệ số Skewness của `Giá_m2_trieu` đạt $\mathbf{+2.75}$, phản ánh phân phối **lệch phải rõ rệt**.
  - Hệ số Skewness của `Tong_Gia_ty` đạt $\mathbf{+8.80}$, cho thấy đại đa số bất động sản giao dịch tập trung ở tầm giá phổ thông, chỉ có số ít tài sản triệu đô kéo dài đuôi sang bên phải.
* **Quy luật Giá trị Trung bình cao hơn Trung vị (Mean > Median)**:
  - Do có sự xuất hiện của các bất động sản mặt phố đắc địa và biệt thự sang trọng ($150 - 450$ triệu/m²), giá trị trung bình ($102.18$ triệu/m²) bị kéo cao hơn trung vị ($90.00$ triệu/m²) tới $13.5\%$.
  - Trong thẩm định giá BĐS, **Trung vị (90.00 triệu/m²)** là chỉ số đại diện chuẩn xác và tin cậy nhất cho mức chi trả thực tế của 50% người dân Thủ đô.

### 4.3. Thống kê Mối quan hệ tương quan (Relationship): Ma trận Pearson
Bảng hệ số tương quan tuyến tính Pearson ($r$) giữa 10 thuộc tính định lượng cốt lõi sau khi đã hoàn thiện làm sạch kích thước:

| Thuộc Tính | `Giá_m2_trieu` | `Tong_Gia_ty` | `Diện tích` | `Số tầng` | `Số PN` | `Mặt tiền` | `Chiều sâu` | `Nội đô` | `Sổ đỏ` | `DT Sàn` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`Giá_m2_trieu`** | **1.000** | **0.712** | 0.160 | 0.225 | 0.242 | **0.161** | 0.117 | **0.283** | 0.007 | 0.187 |
| **`Tong_Gia_ty`** | **0.712** | **1.000** | **0.661** | 0.151 | 0.262 | **0.393** | **0.392** | 0.132 | 0.004 | **0.388** |
| **`Diện tích m2`**| 0.160 | **0.661** | **1.000** | 0.009 | 0.231 | **0.532** | **0.585** | -0.048 | -0.010 | **0.453** |
| **`Số tầng`** | 0.225 | 0.151 | 0.009 | **1.000** | **0.361** | 0.031 | 0.017 | 0.081 | 0.055 | **0.624** |
| **`Số phòng ngủ`**| 0.242 | 0.262 | 0.231 | **0.361** | **1.000** | 0.138 | 0.217 | 0.054 | 0.012 | 0.257 |
| **`mat_tien_m`** | **0.161** | **0.393** | **0.532** | 0.031 | 0.138 | **1.000** | 0.115 | 0.022 | -0.025 | 0.251 |
| **`chieu_sau_m`** | 0.117 | **0.392** | **0.585** | 0.017 | 0.217 | 0.115 | **1.000** | -0.055 | -0.018 | 0.291 |
| **`khu_vuc_noi_do`**| **0.283** | 0.132 | -0.048 | 0.081 | 0.054 | 0.022 | -0.055 | **1.000** | -0.033 | 0.001 |
| **`co_so_do`** | 0.007 | 0.004 | -0.010 | 0.055 | 0.012 | -0.025 | -0.018 | -0.033 | **1.000** | **0.365** |
| **`tong_dien_tich_san_m2`**| 0.187 | **0.388** | **0.453** | **0.624** | 0.257 | 0.251 | 0.291 | 0.001 | **0.365** | **1.000** |

---

## CHƯƠNG 5: PHÂN TÍCH CHI TIẾT & MẠCH LẠC 6 BIỂU ĐỒ TRỰC QUAN HÓA (TUẦN 7)

Tất cả 6 biểu đồ trong thư mục [`reports/figures/`](file:///Users/longnguyen/Documents/bds_khdl/reports/figures) được chuẩn hóa theo **Mô hình 4 Trụ cột Phân tích**: *(1) Mục tiêu thiết kế $\rightarrow$ (2) Số liệu trọng tâm $\rightarrow$ (3) Mối liên hệ & Quy luật $\rightarrow$ (4) Ý nghĩa kinh doanh thực tế*.

```
+---------------------------------------------------------------------------------------------------+
|                            CẤU TRÚC 4 TRỤ CỘT PHÂN TÍCH BIỂU ĐỒ                                    |
+---------------------------------+-----------------------------------------------------------------+
| 1. 🎯 Mục Tiêu & Thiết Kế        | Trả lời câu hỏi nghiệp vụ gì? Dạng biểu đồ, trục toạ độ?        |
| 2. 📊 Số Liệu & Quan Sát        | Con số thống kê mấu chốt, đỉnh mật độ, khoảng biến thiên?       |
| 3. 🔍 Quy Luật & Tương Quan     | Mối liên hệ đa chiều, xu hướng biến thiên, bẫy thống kê?        |
| 4. 💡 Ứng Dụng Thực Tiễn        | Rút ra bài học gì cho người mua, nhà đầu tư & mô hình AI?        |
+---------------------------------+-----------------------------------------------------------------+
```

---

### 5.1. Biểu đồ 1: Ma trận tương quan đa biến (Correlation Heatmap)
* **Tệp lưu trữ**: [`reports/figures/01_correlation_heatmap.png`](file:///Users/longnguyen/Documents/bds_khdl/reports/figures/01_correlation_heatmap.png)

#### 1. 🎯 Mục tiêu & Thiết kế biểu đồ
Biểu đồ nhiệt (Heatmap) thể hiện mức độ liên hệ tuyến tính giữa 10 thuộc tính số học quan trọng nhất của bất động sản. Sử dụng dải màu phân kỳ (Coolwarm) từ xanh dương đậm (tương quan âm $-1.0$) qua trắng ($0.0$) đến đỏ sẫm (tương quan dương $+1.0$), kèm theo số đo hệ số tương quan Pearson hiển thị trực tiếp trong từng ô.

#### 2. 📊 Số liệu then chốt & Quan sát trực quan
* **Đơn giá (`Giá_m2_trieu`)** tương quan dương mạnh nhất với 4 biến:
  - `khu_vuc_noi_do`: **$+0.283$** (yếu tố địa bàn nội đô).
  - `Số phòng ngủ`: **$+0.242$** và `Số tầng`: **$+0.225$** (yếu tố công năng xây dựng).
  - `tong_dien_tich_san_m2`: **$+0.187$** (tổng quy mô sàn).
  - `mat_tien_m`: **$+0.161$** (độ rộng tiếp giáp mặt đường).
* **Tổng giá (`Tong_Gia_ty`)** phụ thuộc song hành vào cả 2 đại lượng:
  - `Giá_m2_trieu`: **$+0.712$** (đơn giá khu vực).
  - `Diện tích m2`: **$+0.661$** (quy mô diện tích thửa đất).
* **Quy mô kích thước vật lý**: Mặt tiền và Chiều sâu tương quan đồng biến mạnh với Diện tích đất ($r = +0.532$ và $r = +0.585$).

#### 3. 🔍 Quy luật, Mối liên hệ & Phân tích tương quan
* **Vị trí địa lý là biến số dẫn dắt đơn giá**: Hệ số tương quan $+0.283$ của `khu_vuc_noi_do` cao hơn bất kỳ biến công năng vật lý nào. Điều này khẳng định trong thị trường nhà đất Hà Nội, "vị trí - vị trí - vị trí" vẫn là quy luật chi phối tối cao.
* **Giá trị xây dựng gia tăng trên đất**: Cả số tầng ($+0.225$) và số phòng ngủ ($+0.242$) đều tương quan dương với đơn giá mỗi mét vuông đất. Một mảnh đất đã có nhà 4 - 5 tầng kiên cố sẽ có đơn giá $triệu/m^2$ đất cao hơn hẳn đất trống, vì chi phí xây dựng hoàn thiện được phân bổ vào tổng giá trị tài sản.
* **Tại sao hệ số tương quan của Mặt tiền đạt $+0.161$ (thay vì âm như trước)?**
  - Sau khi loại bỏ triệt để các bản ghi gõ nhầm milimet và ngoại lệ cực trị, mối quan hệ giữa mặt tiền và đơn giá đã phản ánh đúng thực tế: Mặt tiền càng rộng thì đơn giá đất càng cao nhờ khả năng kinh doanh buôn bán và độ thoáng sáng của công trình.

#### 4. 💡 Ý nghĩa kinh doanh & Giá trị ứng dụng thực tế
* **Đối với định giá**: Khi định giá một bất động sản, hệ thống cần ưu tiên trọng số cao nhất cho biến vị trí quận/huyện và tình trạng công trình xây dựng trên đất.
* **Đối với mô hình máy học**: Sự tồn tại của các cặp tương quan cao vừa phải ($r \approx 0.5 - 0.6$) giữa các biến kích thước xác nhận không có hiện tượng đa cộng tuyến hoàn hảo (Multicollinearity), giúp các thuật toán hồi quy hoạt động ổn định mà không bị nổ phương sai trọng số.

---

### 5.2. Biểu đồ 2: Phân phối Đơn giá & Tổng giá trị BĐS (Histogram & KDE)
* **Tệp lưu trữ**: [`reports/figures/02_price_distribution.png`](file:///Users/longnguyen/Documents/bds_khdl/reports/figures/02_price_distribution.png)

#### 1. 🎯 Mục tiêu & Thiết kế biểu đồ
Biểu đồ hiển thị hình thái phân bố tần suất của 2 biến giá trị cốt lõi: Đơn giá ($triệu/m^2$) và Tổng giá (Tỷ VNĐ). Kết hợp biểu đồ cột đếm (Histogram) và đường ước lượng mật độ liên tục (KDE - Kernel Density Estimation). Biểu đồ tích hợp 4 đường chỉ báo phương vị: **Trung vị (Median - nét đứt đỏ)**, **Trung bình (Mean - nét liền cam)**, cùng **Q1 và Q3 (nét chấm xám)**.

#### 2. 📊 Số liệu then chốt & Quan sát trực quan
* **Biểu đồ Đơn giá ($triệu/m^2$) - Bên trái**:
  - Đỉnh mật độ cao nhất (Mode): Dao động trong khoảng **$75 - 90 \text{ triệu/m²}$**.
  - Trung vị: **$90.00 \text{ triệu/m²}$**; Trung bình: **$102.18 \text{ triệu/m²}$**.
  - Vùng giá 50% tập trung (IQR): Từ **$72.67 \text{ triệu}$** (Q1) đến **$112.50 \text{ triệu/m²}$** (Q3).
  - Phổ giá dốc thoải và giảm liên tục từ 120 triệu đến 500 triệu/m².
* **Biểu đồ Tổng giá (Tỷ VNĐ) - Bên phải**:
  - Đỉnh mật độ tập trung: Khoảng **$2.5 - 4.5 \text{ Tỷ VNĐ}$**.
  - Trung vị: **$3.60 \text{ Tỷ VNĐ}$**; Trung bình: **$5.10 \text{ Tỷ VNĐ}$**.
  - Hơn $75\%$ toàn bộ thị trường có tổng giá trị nằm dưới ngưỡng **$5.30 \text{ Tỷ VNĐ}$**.

#### 3. 🔍 Quy luật, Mối liên hệ & Phân tích tương quan
* **Bản chất phân phối Lệch phải (Right-skewed Log-normal)**: Cả hai biểu đồ đều có chung đặc tính lệch phải mạnh mẽ. Đại đa số giao dịch diễn ra ở phân khúc phổ thông và trung cấp, trong khi các căn nhà triệu đô (mặt phố lớn, biệt thự) tạo thành phần đuôi dài kéo sang bên phải.
* **Chứng minh khắc phục triệt để lỗi cắt cụt (Clipping 175 triệu)**:
  - Trên đường cong KDE của Đơn giá, mật độ suy giảm hoàn toàn trơn tru và liên tục: từ 150 tr $\rightarrow$ 175 tr $\rightarrow$ 200 tr $\rightarrow$ 300 tr/m².
  - Tuyệt đối không còn hiện tượng một cột bin nhô cao dựng đứng bất thường tại mốc 175 triệu như ở phiên bản tiền xử lý cũ.

#### 4. 💡 Ý nghĩa kinh doanh & Giá trị ứng dụng thực tế
* **Đối với người mua nhà & Môi giới**: Phân khúc thanh khoản sôi động và dễ tiếp cận nhất tại Hà Nội là các bất động sản có tổng giá trị từ **$2.5 - 5.0 \text{ Tỷ VNĐ}$** với đơn giá quanh mức **$80 - 100 \text{ triệu/m²}$**.
* **Đối với kỹ thuật học máy**: Hình thái phân phối lệch phải là cơ sở khoa học để áp dụng phép biến đổi Logarit cho biến mục tiêu ($\log(\text{Giá})$) trong các giai đoạn tinh chỉnh mô hình tiếp theo, giúp kéo phân phối phần dư về dạng phân phối chuẩn (Gaussian).

---

### 5.3. Biểu đồ 3: Phân tích tương quan Phân tán & Khắc phục lỗi hiển thị trục (Scatter Plot)
* **Tệp lưu trữ**: [`reports/figures/03_price_vs_area_scatter.png`](file:///Users/longnguyen/Documents/bds_khdl/reports/figures/03_price_vs_area_scatter.png)

#### 1. 🎯 Mục tiêu & Thiết kế biểu đồ
Biểu đồ phân tán (Scatter Plot) kết hợp đường hồi quy tuyến tính OLS (Ordinary Least Squares) và dải mờ khoảng tin cậy 95% (Confidence Interval). Dùng để kiểm tra mối quan hệ giữa kích thước vật lý của thửa đất với giá trị bất động sản:
* **Đồ thị 1 (Bên trái)**: `Diện tích (m²)` vs `Tổng giá (Tỷ VNĐ)` (mẫu 3.500 bản ghi, giới hạn $10 - 220 m^2$ và $\le 35$ tỷ).
* **Đồ thị 2 (Bên phải)**: `Mặt tiền (m)` vs `Đơn giá (Triệu/m²)` (mẫu 3.500 bản ghi, giới hạn mặt tiền thực tế $1.5 - 16$ m và $\le 420$ triệu/m²).

#### 2. 📊 Số liệu then chốt & Quan sát trực quan
* **Đồ thị Diện tích vs Tổng giá (Bên trái)**:
  - Mật độ điểm dày đặc nhất ở vùng diện tích **$35 - 75 m^2$** với tổng giá **$2.5 - 7.5 \text{ Tỷ VNĐ}$** (mẫu hình nhà phố điển hình của Hà Nội).
  - Đường hồi quy màu đỏ dốc thẳng đứng với hệ số tương quan cao **$r = +0.661$**, khẳng định quy mô diện tích quyết định trực tiếp tổng số tiền người mua phải thanh toán.
* **Đồ thị Mặt tiền vs Đơn giá (Bên phải)**:
  - Các điểm dữ liệu phân bổ theo các cụm cột dọc rõ rệt tương ứng với các kích thước quy chuẩn xây dựng: **$3.0\text{m}, 3.5\text{m}, 4.0\text{m}, 4.5\text{m}, 5.0\text{m}, 6.0\text{m}, 8.0\text{m}$**.
  - Đường hồi quy màu cam có xu hướng dốc lên rõ rệt: Bắt đầu từ mức trung bình ~**$88 \text{ triệu/m²}$** tại mặt tiền 2m và tăng lên mức ~**$170 \text{ triệu/m²}$** tại mặt tiền 16m ($r = +0.161$).

#### 3. 🔍 Giải trình nguyên nhân lỗi ở phiên bản cũ & Khắc phục triệt để
* **Tại sao biểu đồ số 3 ở phiên bản cũ trông "cứ bị sai sai"?**
  - *Nguyên nhân kỹ thuật*: Trong tập dữ liệu thô ban đầu, một số người đăng tin nhập kích thước theo đơn vị milimet (ví dụ: gõ `4500` mm thay vì `4.5` m, `6500` mm thay vì `6.5` m), thậm chí có bản ghi gõ nhầm cực đoan lên tới `400,000` m. Hàm trích xuất cũ chỉ lấy số mà không có ngưỡng chặn trên, dẫn đến việc cột mặt tiền chứa giá trị dị biệt 400.000m.
  - *Hậu quả hiển thị*: Khi vẽ đồ thị, trục hoành ($X$) bị kéo dãn từ $0$ lên tới $400.000$ mét (tương đương 400 km!). Do trục quá dài, toàn bộ hàng nghìn điểm dữ liệu thực tế (chỉ từ 2m đến 15m) bị ép bẹp dí thành một vệt sọc dọc mỏng dính sát vào trục tung tại vị trí $x \approx 0$. Điểm dị biệt 400.000m ở tận cùng bên phải kéo tụt đường hồi quy OLS xuống, tạo ra một đường dốc âm sai bản chất kinh tế và một vùng tô màu cam khổng lồ trống rỗng trên màn hình.
* **Giải pháp khắc phục toàn diện**:
  - Nâng cấp thuật toán làm sạch: Tự động chia 1000 cho các giá trị trong khoảng $[1.000, 35.000]$ (nhận diện đơn vị milimet) và thiết lập chặn trên thực tế cho mặt tiền là $30.0$m.
  - Thiết lập khung hiển thị đồ thị chuẩn mực: Trục mặt tiền từ $1.5$ đến $16$ mét. Nhờ vậy, biểu đồ hiện tại hiển thị rõ ràng từng cụm điểm dữ liệu, đường hồi quy phản ánh đúng xu hướng tăng giá trị thương mại theo độ rộng mặt tiền.
* **Hiện tượng Phương sai thay đổi (Heteroscedasticity)**:
  - Ở đồ thị bên trái, khi diện tích đất nhỏ ($< 50 m^2$), các điểm bó chặt quanh đường hồi quy. Nhưng khi diện tích tăng lên ($> 120 m^2$), đám mây điểm xòe rộng thành hình phễu: Cùng diện tích $150 m^2$, nếu ở huyện ngoại thành tổng giá chỉ 8 tỷ, nhưng nếu ở quận trung tâm thì giá vọt lên 30 - 35 tỷ. Điều này chứng minh diện tích không thể định giá độc lập mà bắt buộc phải kết hợp phi tuyến với vị trí.

#### 4. 💡 Ý nghĩa kinh doanh & Giá trị ứng dụng thực tế
* **Giá trị kinh tế của mặt tiền**: Mặt tiền rộng không chỉ tăng diện mạo ngôi nhà mà còn mở ra công năng kinh doanh, cho thuê cửa hàng, gara ô tô. Đây là cơ sở để các ngân hàng áp dụng hệ số nhân giá (markup) đối với các tài sản có mặt tiền rộng từ 5m trở lên.
* **Tối ưu hóa mô hình**: Đồ thị khẳng định mô hình tuyến tính đơn giản sẽ gặp khó khăn trước hiện tượng phương sai hình phễu, đòi hỏi phải sử dụng các thuật toán học máy phi tuyến như Gradient Boosting để nắm bắt được tương tác giữa diện tích và vị trí.

---

### 5.4. Biểu đồ 4: Phân bố đơn giá 12 quận huyện trọng điểm (Boxplot theo Trung vị)
* **Tệp lưu trữ**: [`reports/figures/04_price_by_district_boxplot.png`](file:///Users/longnguyen/Documents/bds_khdl/reports/figures/04_price_by_district_boxplot.png)

#### 1. 🎯 Mục tiêu & Thiết kế biểu đồ
Biểu đồ hộp (Boxplot) thể hiện phân bố đơn giá ($triệu/m^2$) tại 12 quận/huyện có số lượng giao dịch sôi động nhất Hà Nội. Các quận được sắp xếp thứ tự giảm dần từ trái sang phải theo mức **Giá trị Trung vị (Median)** để người xem dễ dàng đối sánh mặt bằng giá giữa các khu vực.

#### 2. 📊 Số liệu then chốt & Bảng xếp hạng chi tiết 12 Quận/Huyện

| Thứ Hạng | Quận / Huyện | Số Bản Ghi | Trung Vị (Median) | Trung Bình (Mean) | Phân Vị Q1 | Phân Vị Q3 | Khoảng IQR | Độ Lệch Std | Nhận Định Vị Thế Thị Trường |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **Quận Cầu Giấy** | 2.990 | **105.00** | 125.27 | 88.10 | 145.20 | 57.10 | 62.16 | Trung tâm kinh tế/văn phòng mới; nhu cầu thực rất cao |
| **2** | **Quận Ba Đình** | 2.223 | **104.00** | 128.56 | 86.67 | 143.90 | 57.23 | 72.41 | Trung tâm chính trị; nguồn cung khan hiếm, giá trị bền vững |
| **3** | **Quận Tây Hồ** | 1.450 | **101.92** | 123.73 | 81.50 | 138.32 | 56.82 | 71.64 | Không gian cảnh quan ven hồ đắt giá; phân khúc cao cấp |
| **4** | **Quận Đống Đa** | 6.495 | **100.00** | 117.96 | 83.70 | 126.83 | 43.13 | 61.88 | Địa bàn có lượng tin đăng lớn nhất; mật độ dân cư đậm đặc |
| **5** | **Quận Thanh Xuân** | 5.474 | **92.50** | 102.70 | 77.78 | 113.52 | 35.74 | 43.63 | Hộp IQR hẹp; mặt bằng giá đồng đều, thanh khoản cao |
| **6** | **Quận Hai Bà Trưng**| 4.479 | **89.74** | 102.59 | 75.00 | 110.00 | 35.00 | 53.26 | Phân hóa giữa khu vực phố cổ và khu vực ven đô |
| **7** | **Quận Nam Từ Liêm** | 1.513 | **85.71** | 94.08 | 72.00 | 104.26 | 32.26 | 40.92 | Cực tăng trưởng phía Tây với nhiều đại đô thị hiện đại |
| **8** | **Quận Bắc Từ Liêm** | 774 | **80.00** | 83.93 | 63.75 | 94.94 | 31.19 | 38.41 | Vùng đệm đô thị; quỹ đất còn dồi dào, giá vừa túi tiền |
| **9** | **Quận Hoàng Mai** | 4.880 | **78.82** | 83.82 | 66.00 | 94.29 | 28.29 | 31.72 | Mức giá mềm nhất khu vực phía Nam; thu hút người mua trẻ |
| **10** | **Quận Long Biên** | 2.028 | **77.50** | 85.53 | 63.40 | 97.58 | 34.18 | 40.40 | Hạ tầng đồng bộ; phân hóa mạnh giữa khu ven sông và phố cũ |
| **11** | **Quận Hà Đông** | 3.728 | **74.44** | 80.80 | 56.88 | 96.98 | 40.10 | 35.78 | Địa bàn cửa ngõ sôi động; biên độ giá rộng từ bình dân đến khá |
| **12** | **Huyện Thanh Trì** | 574 | **60.94** | 62.88 | 47.52 | 76.08 | 28.56 | 25.23 | Mức giá thấp nhất trong nhóm; tiềm năng lớn khi lên quận |

#### 3. 🔍 Quy luật, Mối liên hệ & Phân tích tương quan
* **Sự phân hóa rõ rệt thành 3 tầng nấc thị trường**:
  - *Tầng 1 - Nhóm Lõi Trung Tâm (Trung vị $\ge 100 \text{ triệu/m²}$)*: Gồm Cầu Giấy, Ba Đình, Tây Hồ, Đống Đa. Hộp IQR của nhóm này rất rộng ($56 - 57$ triệu), râu trên vươn dài với nhiều điểm ngoại lệ chạm mức $400 - 500$ triệu/m² do sự xuất hiện của nhà mặt phố cổ và biệt thự hạng sang.
  - *Tầng 2 - Nhóm Đô Thị Phát Triển Mở Rộng (Trung vị $85 - 93 \text{ triệu/m²}$)*: Gồm Thanh Xuân, Hai Bà Trưng, Nam Từ Liêm. Thân hộp ngắn, giá cả tập trung ổn định, đại diện cho phân khúc nhà ở gia đình đô thị.
  - *Tầng 3 - Nhóm Vành Đai & Ven Đô (Trung vị $60 - 80 \text{ triệu/m²}$)*: Gồm Bắc Từ Liêm, Hoàng Mai, Long Biên, Hà Đông, Thanh Trì. Mặt bằng giá mềm, độ lệch chuẩn thấp ($25 - 40$ triệu).

#### 4. 💡 Ý nghĩa kinh doanh & Giá trị ứng dụng thực tế
* **Hỗ trợ quyết định an cư**: Với tài chính tích lũy dưới 3 tỷ, người mua nhà nên ưu tiên tìm kiếm tại Hoàng Mai, Hà Đông hoặc Thanh Trì để có được diện tích ở rộng rãi ($45 - 60 m^2$).
* **Chiến lược đầu tư đón đầu**: Huyện Thanh Trì với đơn giá trung vị chỉ ~61 triệu/m² và hạ tầng đang hoàn thiện để chuẩn bị lên quận là khu vực có biên độ tăng giá tiềm năng nhất trong chu kỳ 2026 - 2030.

---

### 5.5. Biểu đồ 5: Đánh giá & So sánh hiệu năng 4 mô hình hồi quy (Model Comparison)
* **Tệp lưu trữ**: [`reports/figures/05_model_comparison.png`](file:///Users/longnguyen/Documents/bds_khdl/reports/figures/05_model_comparison.png)

#### 1. 🎯 Mục tiêu & Thiết kế biểu đồ
Biểu đồ cột nhóm so sánh hiệu năng của 4 thuật toán hồi quy trên tập kiểm thử độc lập (Test Set gồm 7.481 bản ghi) dựa trên 3 tiêu chí đo lường chuẩn mực:
* **MAE (Mean Absolute Error)**: Sai số tuyệt đối trung bình ($triệu/m^2$ - càng thấp càng tốt).
* **RMSE (Root Mean Squared Error)**: Căn bậc hai sai số bình phương trung bình ($triệu/m^2$ - phạt nặng sai số lớn, càng thấp càng tốt).
* **$R^2$ Score (Coefficient of Determination)**: Hệ số xác định đo lường tỷ lệ biến thiên của giá được mô hình giải thích (càng cao càng tốt, tối đa là 1.0).

#### 2. 📊 Số liệu then chốt & Bảng so sánh đối đầu

| Mô Hình Học Máy | MAE ($triệu/m^2$) | RMSE ($triệu/m^2$) | Hệ Số $R^2$ | Đánh Giá Hiệu Năng Tổng Thể |
| :--- | :---: | :---: | :---: | :--- |
| **Linear Regression** | 28.47 | 44.13 | 0.3644 | Mô hình cơ sở (Baseline); tốc độ nhanh nhưng sai số còn lớn |
| **Ridge Regression** ($L_2$) | 28.47 | 44.21 | 0.3621 | Hiệu năng tương đương Linear, kiểm soát tốt đa cộng tuyến |
| **Random Forest** | 26.17 | 41.85 | 0.4284 | Cải thiện vượt bậc; giảm mạnh MAE xuống dưới 26.2 triệu |
| **Gradient Boosting** | **26.07** | **41.46** | **0.4390** | **🏆 Vô địch toàn diện**: Đạt MAE thấp nhất và $R^2$ cao nhất |

#### 3. 🔍 Quy luật, Mối liên hệ & Phân tích tương quan
* **Sự áp đảo của các mô hình Ensemble dạng cây (Tree-based Models)**:
  - Cả Random Forest và Gradient Boosting đều vượt trội hoàn toàn so với hai mô hình hồi quy tuyến tính (giảm MAE từ 28.47 xuống 26.07 triệu, tăng $R^2$ từ 0.364 lên 0.439).
* **Lý do kỹ thuật giải thích sự chênh lệch**:
  - Mô hình tuyến tính giả định rằng mỗi mét vuông đất hay mỗi mét mặt tiền đều đóng góp một lượng giá cố định không đổi trên toàn thành phố.
  - Trong thực tế, giá trị BĐS có tính chất **tương tác phi tuyến cao**: Mặt tiền 6m ở quận Cầu Giấy mang lại thặng dư giá trị thương mại lớn gấp nhiều lần so với mặt tiền 6m ở Thanh Trì. Các mô hình cây quyết định có khả năng tự động chia cắt không gian dữ liệu để nắm bắt các mối quan hệ tương tác phức tạp này mà không cần người dùng phải khai báo thủ công.

#### 4. 💡 Ý nghĩa kinh doanh & Giá trị ứng dụng thực tế
* **Lựa chọn mô hình đưa vào sản xuất**: Pipeline **Gradient Boosting** chính thức được lựa chọn làm động cơ định giá cốt lõi, đóng gói thành tệp [`house_price_model.pkl`](file:///Users/longnguyen/Documents/bds_khdl/house_price_model.pkl) để phục vụ ứng dụng định giá tự động.
* **Mức độ tin cậy của sai số**: Sai số trung bình $\approx 26.07 \text{ triệu/m²}$ là mức chấp nhận được đối với thị trường có độ biến động cao và tính cá biệt lớn như bất động sản nhà đất Hà Nội.

---

### 5.6. Biểu đồ 6: Tầm quan trọng của các yếu tố định giá (Feature Importance)
* **Tệp lưu trữ**: [`reports/figures/06_feature_importance.png`](file:///Users/longnguyen/Documents/bds_khdl/reports/figures/06_feature_importance.png)

#### 1. 🎯 Mục tiêu & Thiết kế biểu đồ
Biểu đồ thanh ngang hiển thị mức độ đóng góp tương đối (Feature Importance trích xuất theo độ giảm độ tinh khiết MDI) của 15 thuộc tính có sức ảnh hưởng lớn nhất đến kết quả dự báo của mô hình Gradient Boosting.

#### 2. 📊 Số liệu then chốt & Bảng xếp hạng Top 15 Đặc trưng (Sau chuẩn hóa loại bỏ trùng lặp)

| Thứ Hạng | Tên Thuộc Tính | Tỷ Trọng Đóng Góp (%) | Nhóm Yếu Tố | Ý Nghĩa Thực Tiễn Đối Với Định Giá Nhà |
| :---: | :--- | :---: | :---: | :--- |
| **1** | `loai_nha_ngo_hem` | **20.01%** | Loại hình | Yếu tố vị trí tiếp giáp ngõ hẻm làm giảm mạnh đơn giá so với mặt phố |
| **2** | `khu_vuc_noi_do` | **16.14%** | Vị trí lõi | Nhà nằm trong 7 quận nội đô hay ngoại thành quyết định mức nền giá |
| **3** | `Diện tích m2` | **9.88%** | Quy mô | Quy mô mảnh đất: Diện tích càng nhỏ thì đơn giá m² thường cao hơn |
| **4** | `tong_dien_tich_san_m2` | **8.26%** | Quy mô sàn | Tổng diện tích sàn sử dụng thực tế của ngôi nhà |
| **5** | `dien_tich_moi_phong_ngu_m2`| **7.07%** | Tiện nghi | Mức độ rộng rãi và chất lượng không gian sinh hoạt của phòng ngủ |
| **6** | `mat_do_phong_ngu` | **5.50%** | Tiện nghi | Mật độ chia nhỏ phòng ngủ trên diện tích đất |
| **7** | `Số tầng` | **5.47%** | Công năng | Chi phí xây dựng công trình trên đất đóng góp trực tiếp vào đơn giá |
| **8** | `mat_tien_m` | **4.41%** | Kích thước | Chiều rộng mặt tiền tiếp xúc trực tiếp với đường giao thông |
| **9** | `Số phòng ngủ` | **3.56%** | Công năng | Đáp ứng quy mô sinh hoạt cho số lượng thành viên trong gia đình |
| **10** | `ty_le_dai_rong` | **2.44%** | Hình học | Độ vuông vắn phong thủy của thửa đất |
| **11** | `chieu_sau_m` | **2.10%** | Kích thước | Chiều sâu của thửa đất |
| **12** | `Quận_quận thanh xuân` | **1.46%** | Địa bàn | Hiệu ứng địa bàn quận có thanh khoản nhà đất sôi động nhất |
| **13** | `Quận_quận hai bà trưng`| **1.14%** | Địa bàn | Hiệu ứng quận nội đô cũ có giá trị thương mại cao |
| **14** | `Quận_quận hoàn kiếm` | **1.04%** | Địa bàn | Hiệu ứng vùng lõi lịch sử đắt đỏ bậc nhất Thủ đô |
| **15** | `loai_nha_mat_pho` | **1.02%** | Loại hình | Thặng dư giá trị thương mại cho bất động sản mặt đường kinh doanh |

#### 3. 🔍 Quy luật, Mối liên hệ & Giải trình hiện tượng trùng lặp ở phiên bản cũ
* **Giải mã sự khác biệt giữa `Loại hình nhà ở`, `Loại hình nhà ở_nhà ngõ, hẻm` và `loai_nha_ngo_hem`**:
  - `Loại hình nhà ở`: Là **cột danh mục gốc dạng văn bản** trong tệp dữ liệu thô (`raw.csv`), chứa các giá trị chữ do người đăng tin chọn (`"nhà ngõ, hẻm"`, `"nhà ở"`, `"nhà mặt phố"`, `"căn hộ"`, `"đất"`).
  - `Loại hình nhà ở_nhà ngõ, hẻm` và `Loại hình nhà ở_nhà ở`: Là **các cột biến giả (Dummy Variables)** được bộ mã hóa `OneHotEncoder` tự động sinh ra khi chuyển đổi cột phân loại `Loại hình nhà ở` sang dạng nhị phân 0/1.
  - `loai_nha_ngo_hem`: Là **biến nhị phân (Binary Flag) do nhóm tự tạo** trong quá trình Kỹ nghệ đặc trưng (Feature Engineering) bằng cách dùng biểu thức chính quy (Regex) quét tìm từ khóa `'ngõ'` hoặc `'hẻm'`.
* **Tại sao phiên bản trước các biến này cùng xuất hiện trên Biểu đồ 6?**
  - *Hiện tượng Đa cộng tuyến / Trùng lặp thông tin (Feature Redundancy)*: Khi đưa đồng thời cả cột phân loại gốc `Loại hình nhà ở` (được One-Hot mã hóa) và biến tự tạo `loai_nha_ngo_hem` vào mô hình, hai biến này thực chất đang cùng mô tả một đặc tính vật lý (nhà trong ngõ). Cây quyết định trong Random Forest bị "chia đôi" điểm quan trọng cho cả hai biến song sinh, khiến biểu đồ xuất hiện nhiều tên biến na ná nhau, gây rối mắt cho người đọc.
  - *Giải pháp chuẩn hóa*: Đã loại bỏ cột danh mục `Loại hình nhà ở` khỏi danh sách `cat_cols`, để 4 biến cờ nhị phân tinh gọn (`loai_nha_ngo_hem`, `loai_nha_mat_pho`, `loai_can_ho`, `loai_biet_thu_lien_ke`) đại diện độc lập cho từng loại hình. Nhờ vậy, điểm quan trọng của yếu tố nhà ngõ được gom về đúng đại diện duy nhất (`loai_nha_ngo_hem` chiếm **20.01%**), giúp biểu đồ trở nên tường minh, không còn bất kỳ sự trùng lặp nào.
* **Cặp đôi quyền lực Vị trí & Loại hình chi phối hơn 36% giá trị**:
  - `loai_nha_ngo_hem` (20.01%) và `khu_vuc_noi_do` (16.14%) là 2 biến số dẫn đầu bảng xếp hạng. Điều này phản ánh chính xác bản chất thị trường BĐS Hà Nội: Cùng một diện tích 50 m², nếu là nhà mặt phố tại Cầu Giấy sẽ có đơn giá 250 triệu/m², trong khi nhà sâu trong ngõ hẹp tại Hoàng Mai chỉ có giá 70 triệu/m².
* **Đóng góp của các biến Kỹ nghệ đặc trưng**:
  - Các biến công năng do nhóm tự tạo như `tong_dien_tich_san_m2` (hạng 4: 8.26%), `dien_tich_moi_phong_ngu_m2` (hạng 5: 7.07%) và `mat_do_phong_ngu` (hạng 6: 5.50%) đều chiếm tỷ trọng rất cao, chứng minh tầm quan trọng của việc đào sâu chi tiết hóa dữ liệu công năng bất động sản.

#### 4. 💡 Ý nghĩa kinh doanh & Giá trị ứng dụng thực tế
* **Cẩm nang cho nhà đầu tư & Người mua**: Khi tìm kiếm bất động sản, yếu tố mang lại giá trị gia tăng bền vững nhất theo thời gian là **vị trí địa bàn** và **khả năng tiếp cận giao thông** (ngõ nông, ngõ ô tô tránh hoặc mặt phố), vượt trội hơn việc chỉ chú trọng vào nội thất hay số lượng phòng ngủ.

---

## CHƯƠNG 6: THỬ NGHIỆM MÔ HÌNH HÓA & TRỢ LÝ ĐỊNH GIÁ AI (TUẦN 7 - 8)

### 6.1. Thiết lập phân chia tập huấn luyện và kiểm thử (Train/Test Split 80/20)
* Toàn bộ 37.402 bản ghi dữ liệu sạch thuộc chu kỳ 18 tháng gần nhất được phân chia theo tỷ lệ chuẩn 80/20 với hạt giống ngẫu nhiên cố định (`random_state=42`) để đảm bảo tính tái lập kết quả:
  - **Tập Huấn Luyện (Train Set)**: Gồm **29.921 bản ghi** (chiếm 80%), sử dụng để mô hình học các trọng số và cấu trúc cây quyết định.
  - **Tập Kiểm Thử Độc Lập (Test Set)**: Gồm **7.481 bản ghi** (chiếm 20%), được giữ kín hoàn toàn và chỉ đem ra đánh giá khách quan tại bước nghiệm thu.

### 6.2. Bảng đối đầu hiệu năng giữa các thuật toán học máy

| Thuật Toán | MAE ($triệu/m^2$) | RMSE ($triệu/m^2$) | Hệ Số $R^2$ | Ưu Thế Kỹ Thuật Nổi Bật | Hạn Chế Cần Lưu Ý |
| :--- | :---: | :---: | :---: | :--- | :--- |
| **Linear Regression** | 28.47 | 44.13 | 0.3644 | Tốc độ tính toán tức thì, diễn giải hệ số trực tiếp | Không bắt được tương tác phi tuyến giữa diện tích và vị trí |
| **Ridge Regression** | 28.47 | 44.21 | 0.3621 | Triệt tiêu nguy cơ đa cộng tuyến bằng phạt chuẩn $L_2$ | Hiệu năng tương đương hồi quy tuyến tính cổ điển |
| **Random Forest** | 26.17 | 41.85 | 0.4284 | Bắt phi tuyến xuất sắc, chống quá khớp (Overfitting) nhờ Bagging | Mô hình cồng kềnh, thời gian suy luận chậm hơn |
| **Gradient Boosting** | **26.07** | **41.46** | **0.4390** | **Tối ưu nhất**: Học tuần tự sửa sai cho cây trước, tổng quát hóa cao | Cần kiểm soát chặt số cây và độ sâu để tránh học vẹt |

* Mô hình xuất sắc nhất **Gradient Boosting Pipeline** đã được xuất và lưu trữ an toàn tại: [`house_price_model.pkl`](file:///Users/longnguyen/Documents/bds_khdl/house_price_model.pkl).

### 6.3. Trợ lý AI định giá nhà tự động ứng dụng thực tế
Hệ thống đã tích hợp mô hình vào công cụ trợ lý dòng lệnh tại [`src/predict_bot.py`](file:///Users/longnguyen/Documents/bds_khdl/src/predict_bot.py). Công cụ cho phép người dùng nhập các thuộc tính cơ bản của bất động sản và nhận về kết quả định giá tự động trong vòng dưới 1 giây.

* **Kịch bản thẩm định thử nghiệm thực tế**:
  - Thông số đầu vào: Nhà diện tích **$50 m^2$**, địa bàn **Quận Cầu Giấy**, xây dựng **3 tầng**, bố trí **3 phòng ngủ**, tình trạng **đã có sổ đỏ**.
  - **Kết quả AI tính toán**:
    - Đơn giá dự báo trung bình: $\approx \mathbf{90.3 \text{ Triệu VNĐ/m²}}$.
    - Tổng giá trị tài sản ước tính: $\approx \mathbf{4.51 \text{ Tỷ VNĐ}}$.
    - Khoảng giá khuyến nghị tham chiếu: $\mathbf{4.15 - 4.88 \text{ Tỷ VNĐ}}$.
  - Mức giá dự báo này hoàn toàn trùng khớp với phân khúc giao dịch thực tế của phân khúc nhà ở gia đình trong ngõ nông tại Cầu Giấy hiện nay.

---

## CHƯƠNG 7: THỐNG KÊ SUY LUẬN & KIỂM ĐỊNH GIẢ THUYẾT (TUẦN 9)

### 7.1. Bản chất Thống kê suy luận & Nguyên lý kiểm định giả thuyết khoa học
Một trong những hiểu lầm phổ biến nhất của người mới học Khoa học Dữ liệu là nhầm lẫn giữa **Thống kê mô tả (Descriptive Statistics)** và **Thống kê suy luận (Inferential Statistics)**:
* **Thống kê mô tả (Tuần 6 - 8)**: Chỉ đơn thuần tổng kết và tóm tắt những gì chúng ta *thực sự nhìn thấy* trên tập dữ liệu đã thu thập (ví dụ: giá trung bình của 37.402 tin đăng là $102.18$ triệu/m²). Nó giống như việc bạn múc một thìa súp ra nếm và mô tả: *"Thìa súp này có 2 hạt tiêu và vị hơi mặn"*.
* **Thống kê suy luận (Tuần 9)**: Đưa ra kết luận có cơ sở khoa học về *toàn bộ thị trường bất động sản hàng triệu căn nhà ngoài đời thực (Population)* dựa trên tập mẫu quan sát được (Sample), kèm theo mức độ rủi ro sai số xác định. Nó trả lời câu hỏi cốt tử: *"Liệu cả nồi súp 10 lít ngoài đời có thực sự bị mặn không, hay chỉ do chiếc thìa của tôi tình cờ vớt trúng chỗ muối chưa kịp tan?"*.

```
+---------------------------------------------------------------------------------------------------+
|                        MÔ HÌNH SUY LUẬN THỐNG KÊ TỔNG THỂ (INFERENTIAL STATS)                     |
+---------------------------------------------------------------------------------------------------+
|   QUẦN THỂ BĐS HÀ NỘI (Population)                  TẬP MẪU QUAN SÁT (Sample n = 37,402)          |
|   Hàng triệu căn nhà ngoài đời thực   === Thu thập ==>   Đã gột rửa, sạch 100%                    |
|   (Kỳ vọng thực sự mu = ?)                           (Trung bình quan sát được x_bar = 102.18)    |
|                  ^                                                      |                         |
|                  |                                                      |                         |
|                  +===== SUY LUẬN THỐNG KÊ (Kiểm định giả thuyết) <======+                         |
|                         Khoảng tin cậy 95% CI: [101.63 - 102.73]                                  |
|                         Mức ý nghĩa alpha = 0.05, p-value < 0.0001                                |
+---------------------------------------------------------------------------------------------------+
```

#### 💡 3 Khái niệm nền tảng giải thích bằng ngôn ngữ đời thường:
1. **Giả thuyết vô hiệu $H_0$ (The Skeptical Null Hypothesis)**: Là giả định mang tính hoài nghi của người phản biện. Họ cho rằng: *"Chẳng có gì đặc biệt ở đây cả! Mọi sự chênh lệch bạn thấy chỉ là do ăn may hoặc do ngẫu nhiên khi thu thập dữ liệu!"*.
2. **Giả thuyết nghiên cứu $H_1$ (Alternative Hypothesis)**: Là luận điểm mà nhà khoa học dữ liệu muốn chứng minh. Ví dụ: *"Nhà ở Nội đô thực sự đắt hơn Ngoại thành một cách có hệ thống, không thể do ăn may!"*.
3. **Chỉ số $p$-value (Xác suất ăn may)**: Là xác suất xảy ra hiện tượng chênh lệch lớn như thế này nếu giả thuyết $H_0$ là đúng.
   - Nếu $p\text{-value} \ge 0.05$: Khả năng xảy ra do ngẫu nhiên quá cao $\rightarrow$ Không đủ bằng chứng để kết luận.
   - Nếu $p\text{-value} < 0.05$ (đặc biệt $p < 0.0001$): Khả năng do ăn may là **nhỏ hơn 1 phần 10.000** $\rightarrow$ Ta hoàn toàn tự tin **Bác bỏ $H_0$** và khẳng định kết luận nghiên cứu là một sự thật khách quan.

---

### 7.2. Kiểm định Giả thuyết Nội đô vs Ngoại thành: Welch's t-test & Mann-Whitney U

#### 1. Phát biểu giả thuyết kiểm định:
* **$H_0$**: Không có sự khác biệt về đơn giá trung bình giữa bất động sản tại 7 quận Nội đô và các huyện/quận Ngoại thành ($\mu_{\text{Nội đô}} = \mu_{\text{Ngoại thành}}$).
* **$H_1$**: Đơn giá trung bình tại 7 quận Nội đô cao hơn có ý nghĩa thống kê so với Ngoại thành ($\mu_{\text{Nội đô}} > \mu_{\text{Ngoại thành}}$).

#### 2. Kết quả thống kê hai nhóm mẫu:
* **Nhóm 1 - 7 Quận Nội đô**: $n_1 = 23.330$ căn nhà; Đơn giá trung bình $\bar{x}_1 = \mathbf{114.24 \text{ triệu/m²}}$; Trung vị $M_1 = 96.67 \text{ triệu/m²}$; Độ lệch chuẩn $s_1 = 60.25$.
* **Nhóm 2 - Ngoại thành**: $n_2 = 14.072$ căn nhà; Đơn giá trung bình $\bar{x}_2 = \mathbf{82.20 \text{ triệu/m²}}$; Trung vị $M_2 = 76.77 \text{ triệu/m²}$; Độ lệch chuẩn $s_2 = 36.30$.
* **Mức chênh lệch thực tế**: $\Delta = \bar{x}_1 - \bar{x}_2 = \mathbf{32.04 \text{ triệu/m²}}$ (Nội thành cao hơn **$39.0\%$**).

#### 3. Bảng kết quả thực nghiệm kiểm định:

| Tên Phép Kiểm Định | Loại Phép Kiểm | Đại Lượng Thống Kê | Giá Trị $p\text{-value}$ | Ngưỡng $\alpha$ | Kết Luận Thống Kê |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Welch's Two-Sample t-test** | Tham số (Không giả định phương sai bằng nhau) | $t = \mathbf{64.175}$ | **$0.0000e+00$** ($< 10^{-16}$) | $0.05$ | **Bác bỏ $H_0$ đanh thép**: Đơn giá Nội đô cao hơn có ý nghĩa thống kê cực kỳ rõ rệt |
| **Mann-Whitney U Test** | Phi tham số (Không phụ thuộc giả định phân phối chuẩn) | $U = \mathbf{2.35 \times 10^8}$ | **$0.0000e+00$** ($< 10^{-16}$) | $0.05$ | **Bác bỏ $H_0$ tuyệt đối**: Phân bố giá trị của Nội đô áp đảo hoàn toàn Ngoại thành |
| **Cohen's d (Effect Size)** | Đo lường độ lớn hiệu ứng thực tế | $d = \mathbf{0.610}$ | — | — | **Mức tác động Trung bình - Lớn** ($0.5 < d < 0.8$): Khoảng cách giá mang giá trị kinh tế thực tế |

> [!NOTE]
> **Tại sao bắt buộc phải dùng Welch's t-test thay cho Student t-test thông thường?**
> Kiểm định Student t-test cổ điển giả định hai nhóm có phương sai bằng nhau ($\sigma_1^2 = \sigma_2^2$). Tuy nhiên, dữ liệu thực tế cho thấy phương sai giá Nội đô ($60.25^2 \approx 3630$) lớn gấp gần **3 lần** phương sai Ngoại thành ($36.30^2 \approx 1317$). Nếu dùng t-test thông thường, sai số sẽ bị bóp méo. **Welch's t-test** tự động hiệu chỉnh bậc tự do (Degrees of Freedom) để cho ra kết quả chính xác 100%.

---

### 7.3. Phân tích phương sai One-Way ANOVA & So sánh từng cặp Tukey's HSD

#### 1. Câu hỏi kinh doanh:
*"Trong 12 quận/huyện có lượng giao dịch lớn nhất Hà Nội, liệu mỗi quận có một mức giá riêng biệt, hay có những quận dù mang tên khác nhau nhưng thực chất mặt bằng giá lại hoàn toàn giống nhau?"*

#### 2. Nguy cơ của việc làm sai (Bẫy so sánh nhiều cặp - Multiple Comparisons Trap):
Nếu chúng ta lấy 12 quận và chạy từng cặp $t$-test đơn lẻ, số lượng cặp cần so sánh là:
$$\frac{12 \times (12 - 1)}{2} = \mathbf{66 \text{ cặp so sánh}}$$
Nếu mỗi lần kiểm tra chấp nhận rủi ro sai sót $5\%$ ($\alpha = 0.05$), thì khi kiểm tra 66 lần liên tiếp, xác suất xuất hiện ít nhất một lần **báo động giả (Sai lầm Loại I)** sẽ vọt lên mức:
$$1 - (1 - 0.05)^{66} = 1 - (0.95)^{66} \approx \mathbf{96.6\%}$$
Nghĩa là gần như chắc chắn chúng ta sẽ đưa ra kết luận sai lầm!

#### 3. Giải pháp: Phân tích phương sai One-Way ANOVA & Kruskal-Wallis:
* **One-way ANOVA**: Kiểm tra đồng thời xem liệu trung bình của 12 quận có bằng nhau không.
  - Kết quả: $F = \mathbf{368.11}$, $p\text{-value} = \mathbf{0.0000e+00}$ ($p < 0.0001$).
* **Kruskal-Wallis**: Phiên bản phi tham số dựa trên thứ hạng (Rank-based).
  - Kết quả: $H = \mathbf{5465.33}$, $p\text{-value} = \mathbf{0.0000e+00}$ ($p < 0.0001$).
* **Kết luận**: Khẳng định chắc chắn giữa 12 quận/huyện có sự phân hóa sâu sắc về giá.

#### 4. Khám phá bất ngờ từ Kiểm định hậu nghiệm Tukey's HSD (Honest Significant Difference):
Sau khi ANOVA khẳng định có sự khác biệt, thuật toán Tukey's HSD tiến hành so sánh 66 cặp đối đầu và kiểm soát chặt chẽ tỷ lệ sai số họ (Family-wise Error Rate). Kết quả phát hiện ra **9 cặp quận "song sinh về giá"** không có sự khác biệt có ý nghĩa thống kê ($p_{\text{adj}} > 0.05$):

```
+---------------------------------------------------------------------------------------------------+
|                   3 TẦNG NẤC THỊ TRƯỜNG ĐỒNG NHẤT PHÁT HIỆN TỪ TUKEY'S HSD                         |
+---------------------------------------------------------------------------------------------------+
| 👑 TẦNG 1: "TAM GIÁC VÀNG ĐỈNH CAO" (Không khác biệt nhau về mặt thống kê)                        |
|    - Cầu Giấy (125.27 tr) vs Ba Đình (128.56 tr):    Chênh 3.29 tr/m2  (p = 0.4769 - Giống nhau)  |
|    - Ba Đình (128.56 tr)  vs Tây Hồ (123.73 tr):     Chênh 4.83 tr/m2  (p = 0.1795 - Giống nhau)  |
|    - Cầu Giấy (125.27 tr) vs Tây Hồ (123.73 tr):     Chênh 1.54 tr/m2  (p = 0.9987 - Giống nhau)  |
+---------------------------------------------------------------------------------------------------+
| 🏙️ TẦNG 2: "CẶP ĐÔI ĐÔ THỊ ĐỐNG ĐA - THANH XUÂN - HAI BÀ TRƯNG"                                  |
|    - Hai Bà Trưng (102.59 tr) vs Thanh Xuân (102.70 tr): Chênh 0.11 tr/m2 (p = 1.0000 - Như nhau) |
+---------------------------------------------------------------------------------------------------+
| 🌳 TẦNG 3: "LIÊN MINH VÀNH ĐAI BÌNH DÂN" (Mặt bằng giá tương đồng quanh mốc 80 - 85 tr/m2)       |
|    - Hoàng Mai (83.82 tr) vs Bắc Từ Liêm (83.93 tr):   Chênh 0.11 tr/m2  (p = 1.0000 - Giống nhau)|
|    - Hoàng Mai (83.82 tr) vs Long Biên (85.53 tr):     Chênh 1.71 tr/m2  (p = 0.9832 - Giống nhau)|
|    - Bắc Từ Liêm (83.93 tr) vs Long Biên (85.53 tr):   Chênh 1.60 tr/m2  (p = 0.9999 - Giống nhau)|
|    - Bắc Từ Liêm (83.93 tr) vs Hà Đông (80.80 tr):     Chênh 3.13 tr/m2  (p = 0.9261 - Giống nhau)|
|    - Hoàng Mai (83.82 tr) vs Hà Đông (80.80 tr):       Chênh 3.02 tr/m2  (p = 0.2171 - Giống nhau)|
+---------------------------------------------------------------------------------------------------+
```

---

### 7.4. Phân tích Biểu đồ 7: Khoảng tin cậy 95% (95% CI) cho 12 Quận/Huyện
* **Tệp lưu trữ**: [`reports/figures/07_confidence_intervals_districts.png`](file:///Users/longnguyen/Documents/bds_khdl/reports/figures/07_confidence_intervals_districts.png)

![Biểu đồ 07: Khoảng tin cậy 95% Đơn giá 12 Quận/Huyện Hà Nội](/Users/longnguyen/Documents/bds_khdl/reports/figures/07_confidence_intervals_districts.png)

#### 1. 🎯 Mục tiêu & Thiết kế biểu đồ
Biểu đồ hiển thị mức **Đơn giá Trung bình (Mean - chấm tròn xanh)** đi kèm **Thanh sai số Khoảng tin cậy 95% (95% CI Error Bars - thanh ngang đỏ)** và **Đơn giá Trung vị (Median - hình thoi xanh lá)** cho 12 quận/huyện trọng điểm. Trục tung sắp xếp thứ tự tăng dần từ dưới lên trên. Hai đường kẻ dọc thể hiện mốc tham chiếu toàn thành phố: Trung bình ($102.18$ tr - nét đứt cam) và Trung vị ($90.00$ tr - nét chấm tím).

#### 2. 📊 Số liệu then chốt & Bảng Khoảng tin cậy 95% (CI) chi tiết

| Quận / Huyện | Số Bản Ghi ($n$) | Trung Bình ($\bar{x}$) | Trung Vị ($M$) | Sai Số Chuẩn ($SE$) | **CI 95% Giới Hạn Dưới** | **CI 95% Giới Hạn Trên** | Biên Độ Sai Số ($\pm$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Quận Ba Đình** | 2.223 | **128.56** | 104.00 | 1.54 | **125.55** | **131.57** | $\pm 3.01$ |
| **Quận Cầu Giấy** | 2.990 | **125.27** | 105.00 | 1.14 | **123.04** | **127.50** | $\pm 2.23$ |
| **Quận Tây Hồ** | 1.450 | **123.73** | 101.92 | 1.88 | **120.04** | **127.42** | $\pm 3.69$ |
| **Quận Đống Đa** | 6.495 | **117.96** | 100.00 | 0.77 | **116.45** | **119.46** | $\pm 1.51$ |
| **Quận Thanh Xuân** | 5.474 | **102.70** | 92.50 | 0.59 | **101.54** | **103.86** | $\pm 1.16$ |
| **Quận Hai Bà Trưng**| 4.479 | **102.59** | 89.74 | 0.80 | **101.03** | **104.15** | $\pm 1.56$ |
| **Quận Nam Từ Liêm** | 1.513 | **94.08** | 85.71 | 1.05 | **92.02** | **96.15** | $\pm 2.06$ |
| **Quận Long Biên** | 2.028 | **85.53** | 77.50 | 0.90 | **83.77** | **87.29** | $\pm 1.76$ |
| **Quận Bắc Từ Liêm** | 774 | **83.93** | 80.00 | 1.38 | **81.22** | **86.64** | $\pm 2.71$ |
| **Quận Hoàng Mai** | 4.880 | **83.82** | 78.82 | 0.45 | **82.93** | **84.71** | $\pm 0.89$ |
| **Quận Hà Đông** | 3.728 | **80.80** | 74.44 | 0.59 | **79.65** | **81.95** | $\pm 1.15$ |
| **Huyện Thanh Trì** | 574 | **62.88** | 60.94 | 1.05 | **60.81** | **64.95** | $\pm 2.07$ |

#### 3. 🔍 Quy luật, Mối liên hệ & Diễn giải khoảng tin cậy đúng chuẩn
* **Diễn giải đúng chuẩn khoa học**: Với Quận Ba Đình, ta khẳng định với độ tin cậy $95\%$ rằng: Mức đơn giá trung bình thực sự của toàn bộ thị trường nhà đất quận Ba Đình nằm trong khoảng từ **$125.55$ đến $131.57 \text{ triệu/m²}$**.
* **Độ rộng của thanh sai số phản ánh kích thước mẫu ($n$)**:
  - Tại Quận Hoàng Mai ($n = 4.880$), thanh sai số cực kỳ hẹp ($\pm 0.89$ tr/m²). Do mẫu rất lớn, ước lượng đạt độ chính xác gần như tuyệt đối.
  - Tại Quận Tây Hồ ($n = 1.450$), thanh sai số rộng hơn ($\pm 3.69$ tr/m²), phản ánh tính đa dạng và biên độ giá dao động mạnh giữa nhà mặt hồ và nhà trong ngõ.
* **Sự gối đầu của các thanh sai số (Overlapping CIs)**:
  - Thanh khoảng tin cậy của Ba Đình $[125.55 - 131.57]$ và Cầu Giấy $[123.04 - 127.50]$ gối đè lên nhau một khoảng lớn. Điều này giải thích trực quan tại sao phép kiểm định Tukey's HSD trước đó khẳng định không có sự khác biệt có ý nghĩa thống kê giữa hai quận này.

#### 4. 💡 Ý nghĩa kinh doanh & Ứng dụng thực tiễn
* **Định giá thẩm định ngân hàng**: Thay vì chỉ dùng 1 con số đơn lẻ, ngân hàng có thể dùng dải khoảng tin cậy 95% để thiết lập khung trần và khung sàn cho vay tín dụng thế chấp bất động sản tại từng địa bàn.
* **Dấu hiệu định giá bất thường**: Nếu một căn nhà tại Thanh Xuân được chào bán với đơn giá dưới $95$ triệu/m² (nằm ngoài cận dưới $101.54$ tr), nhà đầu tư cần lập tức kiểm tra xem tài sản có bị dính lỗi quy hoạch, tranh chấp pháp lý hoặc ngõ quá sâu hay không.

---

### 7.5. Kiểm định Chi-square độc lập: Vị trí Nội đô vs Tình trạng Sổ đỏ
* **Mục tiêu**: Kiểm tra xem tỷ lệ bất động sản có Giấy chứng nhận quyền sử dụng đất (Sổ đỏ/Sổ hồng) có phụ thuộc vào vị trí Nội thành hay Ngoại thành không.
* **Bảng tiếp liên $2 \times 2$ (Contingency Table)**:
  - Ngoại thành: $4.759$ căn chưa có sổ ($33.8\%$), $9.313$ căn đã có sổ ($66.2\%$).
  - Nội thành: $8.657$ căn chưa có sổ ($37.1\%$), $14.673$ căn đã có sổ ($62.9\%$).
* **Kết quả**: $\chi^2 = \mathbf{41.104}$, Bậc tự do $\text{DoF} = 1$, $p\text{-value} = \mathbf{1.44 \times 10^{-10}}$.
* **Ý nghĩa thực tiễn**: Tỷ lệ nhà thiếu sổ đỏ tại 7 quận nội đô cao hơn có ý nghĩa thống kê so với ngoại thành. Điều này hoàn toàn trùng khớp với thực tế lịch sử Thủ đô: Khu vực lõi nội đô có nhiều nhà cổ, nhà phân phối thời bao cấp, nhà diện tích quá nhỏ chưa đủ điều kiện cấp sổ, hoặc đang chờ hoàn tất thủ tục thừa kế qua nhiều thế hệ.

---

## CHƯƠNG 8: CHẨN ĐOÁN HỒI QUY TUYẾN TÍNH & 4 GIẢ ĐỊNH LINE (TUẦN 10)

### 8.1. Đọc hiểu mô hình OLS cơ sở & 3 Nghĩa vụ đạo đức khi diễn giải hệ số $\beta$
Mô hình hồi quy tuyến tính cổ điển OLS (Ordinary Least Squares) được thiết lập với phương trình:
$$\widehat{\text{Giá\_m2\_trieu}} = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_p X_p$$

#### 1. Bảng tóm tắt kết quả hồi quy OLS đa biến ($n = 37.402$):
* Hệ số xác định $R^2 = \mathbf{0.283}$; Thống kê kiểm định $F = \mathbf{1479.0}$ ($p\text{-value} < 0.0001$).
* Sai số chuẩn của hồi quy $\text{RSE} = 46.40 \text{ triệu/m²}$.

| Thuộc Tính ($X$) | Hệ Số Hồi Quy ($\beta$) | Sai Số Chuẩn ($SE$) | Thống Kê $t$ | $p\text{-value}$ | Khoảng Tin Cậy 95% của $\beta$ | Ý Nghĩa Thống Kê ($p < 0.05$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Hệ số chặn (const)** | $+59.97$ | $2.36$ | $+25.38$ | $< 0.0001$ | $[+55.34, +64.60]$ | Có ý nghĩa |
| `khu_vuc_noi_do` | **$+33.13$** | $0.50$ | $+66.31$ | $< 0.0001$ | $[+32.16, +34.11]$ | Cực kỳ mạnh mẽ |
| `loai_nha_ngo_hem` | **$-33.46$** | $1.20$ | $-28.00$ | $< 0.0001$ | $[-35.80, -31.12]$ | Chiết khấu rất lớn |
| `loai_nha_mat_pho` | **$+14.77$** | $1.24$ | $+11.93$ | $< 0.0001$ | $[+12.35, +17.20]$ | Thặng dư thương mại cao |
| `mat_tien_m` | **$+1.94$** | $0.21$ | $+9.16$ | $< 0.0001$ | $[+1.52, +2.35]$ | Có ý nghĩa |
| `Số phòng ngủ` | **$+5.86$** | $0.19$ | $+30.69$ | $< 0.0001$ | $[+5.48, +6.23]$ | Có ý nghĩa |
| `Số tầng` | **$+2.45$** | $0.26$ | $+9.56$ | $< 0.0001$ | $[+1.95, +2.95]$ | Có ý nghĩa |
| `tong_dien_tich_san_m2`| $+0.03$ | $0.002$ | $+12.19$ | $< 0.0001$ | $[+0.025, +0.035]$ | Có ý nghĩa |
| `co_so_do` | $-1.35$ | $0.59$ | $-2.31$ | $0.0210$ | $[-2.51, -0.20]$ | Tác động nhẹ |
| `chieu_sau_m` | $-0.04$ | $0.11$ | $-0.37$ | **$0.7080$** | $[-0.27, +0.18]$ | ⚠️ **Không có ý nghĩa ($p > 0.05$)** |

#### 2. Thực thi 3 Nghĩa vụ đạo đức bắt buộc khi diễn giải hệ số $\beta$:
1. **Nghĩa vụ 1: Tuyệt đối không dùng từ "gây ra" (Tránh bẫy Nhân quả)**: Phải dùng cụm từ *"gắn liền với / đi kèm với"*.
2. **Nghĩa vụ 2: Khẳng định điều kiện giữ nguyên các biến khác (Ceteris Paribus)**:
   - *Ví dụ chuẩn mực về Nội đô*: Trong phạm vi dữ liệu quan sát, **khi giữ nguyên các điều kiện khác** (cùng diện tích đất, cùng số tầng, cùng loại nhà ngõ hay phố), một bất động sản nằm trong 7 quận Nội đô **gắn liền với** mức đơn giá cao hơn trung bình **$33.13 \text{ triệu/m²}$** so với Ngoại thành.
   - *Ví dụ chuẩn mực về Mặt tiền*: Khi giữ nguyên các yếu tố khác, mỗi mét mặt tiền mở rộng thêm **gắn liền với** mức tăng thêm trung bình **$1.94 \text{ triệu/m²}$** đơn giá.
3. **Nghĩa vụ 3: Giới hạn trong phạm vi quan sát**: Các kết luận trên chỉ đúng với phân khúc nhà đất có diện tích từ $10 - 500 m^2$ và mặt tiền từ $1.5 - 30$ m tại Hà Nội.

---

### 8.2. Phân tích Biểu đồ 8: Kiểm định 4 Giả định LINE (Linearity - Independence - Normality - Equal Variance)
* **Tệp lưu trữ**: [`reports/figures/08_line_assumptions_diagnostics.png`](file:///Users/longnguyen/Documents/bds_khdl/reports/figures/08_line_assumptions_diagnostics.png)

![Biểu đồ 08: Bộ Chẩn đoán 4 Giả định LINE và Hiệu quả Biến đổi Logarit](/Users/longnguyen/Documents/bds_khdl/reports/figures/08_line_assumptions_diagnostics.png)

Để kết luận của mô hình hồi quy OLS đáng tin cậy, dữ liệu bắt buộc phải thỏa mãn **4 Giả định LINE kinh điển**:

```
+---------------------------------------------------------------------------------------------------+
|                            4 GIẢ ĐỊNH LINE CỦA MÔ HÌNH HỒI QUY TUYẾN TÍNH                         |
+-------------------+---------------------------------------------+---------------------------------+
| Giả Định          | Ý Nghĩa Nghiệp Vụ Cần Thỏa Mãn              | Công Cụ Chẩn Đoán Thực Tế       |
+-------------------+---------------------------------------------+---------------------------------+
| L - Linearity     | Quan hệ giữa biến giải thích và giá là thẳng| Đồ thị Residuals vs Fitted      |
| I - Independence  | Phần dư của các căn nhà độc lập với nhau    | Kiểm định Durbin-Watson (~ 2.0) |
| N - Normality     | Phần dư sai số tuân theo phân phối chuẩn    | Đồ thị Normal Q-Q Plot & JB-test|
| E - Equal Variance| Phương sai sai số là hằng số ở mọi tầm giá  | Kiểm định Breusch-Pagan & Phễu  |
+-------------------+---------------------------------------------+---------------------------------+
```

#### 1. 🔍 Đồ thị 1 (Góc trên trái): Kiểm tra Tuyến tính (L) & Phương sai đồng nhất (E)
* **Quan sát**: Trục hoành là Giá trị dự báo ($\hat{y}$), trục tung là Phần dư ($e = y - \hat{y}$). Đường màu đỏ đứt nét là mốc $0$, đường màu đỏ đậm là đường làm mịn cục bộ LOWESS.
* **Hiện tượng Hình phễu (Funnel Pattern / Heteroscedasticity)**:
  - Khi giá trị nhà dự báo ở mức thấp ($< 80$ triệu/m²), các điểm dữ liệu bó sát trục 0, biên độ sai số chỉ khoảng $\pm 20$ triệu.
  - Khi giá trị dự báo tăng cao ($> 150$ triệu/m²), các điểm dữ liệu xòe rộng thành hình phễu khổng lồ với biên độ sai số vọt lên $\pm 150 - 250$ triệu/m²!
* **Kiểm định Breusch-Pagan**: $BP = \mathbf{4417.73}$, $p\text{-value} = \mathbf{0.0000e+00}$.
  - Bác bỏ hoàn toàn giả định phương sai không đổi. Đây là bằng chứng định lượng khẳng định: **OLS tuyến tính cơ sở đang bị sai số phương sai thay đổi nghiêm trọng**.

#### 2. 🔍 Đồ thị 2 (Góc trên phải): Kiểm tra Phân phối chuẩn của Sai số (N) trên Mô hình gốc
* **Quan sát**: Biểu đồ Quantile-Quantile (Normal Q-Q Plot) mô hình gốc. Trục hoành là phân vị lý thuyết chuẩn, trục tung là phần dư thực tế.
* **Hiện tượng đuôi vểnh lên trời**:
  - Ở vùng trung tâm ($[-2, +1]$), các điểm dữ liệu bám tốt vào đường chéo màu đỏ.
  - Ở vùng đuôi bên phải ($> +1$), các điểm dữ liệu **vểnh cong vút lên trên** và tách rời hoàn toàn khỏi đường chuẩn.
* **Kiểm định Jarque-Bera**: $JB = \mathbf{210933.82}$, $p < 0.0001$; Độ lệch Skewness $= \mathbf{+2.18}$, Độ nhọn Kurtosis $= \mathbf{10.79}$.
  - Sai số không tuân theo phân phối chuẩn mà bị lệch phải nặng do các bất động sản phân khúc siêu sang kéo dài đuôi.

#### 3. 🔍 Kiểm tra Tính độc lập của phần dư (I):
* **Hệ số Durbin-Watson**: Đạt giá trị $DW = \mathbf{2.0114}$.
  - Quy tắc: Giá trị $DW \approx 2.0$ (nằm trọn trong dải an toàn $[1.5, 2.5]$) xác nhận **Phần dư hoàn toàn độc lập**, không có hiện tượng tự tương quan (Autocorrelation) chuỗi dữ liệu.

---

### 8.3. Giải pháp đột phá: Phép biến đổi Logarit $\log(y)$ phục hồi phân phối chuẩn

#### 1. Cơ sở toán học & Lý do tại sao phải dùng Logarit:
Do bản chất của giá trị tài sản có phân phối lệch phải (Log-normal), việc ép một đường thẳng tuyến tính thuần túy sẽ luôn gặp lỗi hình phễu. Phép biến đổi Logarit tự nhiên:
$$y' = \ln(\text{Giá\_m2\_trieu})$$
sẽ "kéo co" các giá trị cực lớn ở đuôi phải lại gần trung tâm hơn, biến một phân phối lệch phải thành một phân phối đối xứng dạng hình chuông (Gaussian).

#### 2. Chứng minh hiệu quả ngoạn mục qua Đồ thị 3 & Đồ thị 4 (Biểu đồ 08):
* **Đồ thị 3 (Góc dưới trái) - Q-Q Plot sau biến đổi Log**:
  - Các điểm dữ liệu màu xanh lá **bám khít hoàn hảo vào đường thẳng chéo 45 độ màu đỏ** từ cận dưới $-3$ đến cận trên $+3$.
  - Hiện tượng đuôi cong vểnh lên trời đã hoàn toàn biến mất!
* **Đồ thị 4 (Góc dưới phải) - Đường cong mật độ phần dư (KDE)**:
  - Đường phân phối của mô hình gốc (xanh dương) bị lệch hẳn sang một bên với đỉnh nhọn hoắt.
  - Đường phân phối sau khi lấy Log (xanh lá) bao trọn và áp sát hoàn hảo đường phân phối chuẩn lý thuyết màu đỏ $N(0, 1)$!
* **Bảng so sánh các chỉ số hình học trước và sau khi lấy Log**:

| Chỉ Số Đo Lường | Mô Hình Gốc (Linear OLS) | Mô Hình Sau Log ($\log(y)$) | Mức Độ Cải Thiện Nghiệp Vụ |
| :--- | :---: | :---: | :--- |
| **Độ lệch phần dư (Skewness)** | $+2.18$ (Lệch phải rất nặng) | **$-0.29$** (Gần như đối xứng tuyệt đối) | **Giảm 86.7% độ lệch**, đưa sai số về thế cân bằng |
| **Độ nhọn phần dư (Kurtosis)** | $10.79$ (Đuôi cực dày, nhiều ngoại lệ) | **$3.72$** (Tiệm cận mức chuẩn $3.0$) | **Triệt tiêu 65.5% hiện tượng đuôi nặng**, triệt tiêu bẫy ngoại lệ |
| **Sai số MAE trên tập Test** | $29.90 \text{ triệu/m²}$ | **$28.35 \text{ triệu/m²}$** | **Giảm thêm $1.55 \text{ triệu/m²}$ sai số**, dự báo sát giá hơn |

#### 3. Cách diễn giải hệ số mô hình Log-Linear dành cho người làm kinh doanh:
Khi mô hình có dạng $\ln(y) = \beta_0 + \beta_1 X_1$, hệ số $\beta$ phản ánh **Tỷ lệ phần trăm thay đổi tương đối** thay vì số tiền tuyệt đối:
$$\% \Delta y \approx (e^\beta - 1) \times 100\%$$
* Với $\beta_{\text{khu\_vuc\_noi\_do}} = +0.334$: Căn nhà nằm trong 7 quận nội đô sẽ có đơn giá cao hơn khoảng $(e^{0.334} - 1) \times 100\% \approx \mathbf{39.7\%}$ so với căn nhà tương đương ở ngoại thành.
* Với $\beta_{\text{loai\_nha\_ngo\_hem}} = -0.366$: Căn nhà trong ngõ hẻm sẽ bị chiết khấu giá thấp hơn khoảng $(1 - e^{-0.366}) \times 100\% \approx \mathbf{30.6\%}$ so với nhà mặt phố.

---

### 8.4. Phân tích Biểu đồ 9: Kỹ thuật Điều chuẩn Regularisation (Ridge L2 vs Lasso L1)
* **Tệp lưu trữ**: [`reports/figures/09_regularization_lasso_vs_ridge.png`](file:///Users/longnguyen/Documents/bds_khdl/reports/figures/09_regularization_lasso_vs_ridge.png)

![Biểu đồ 09: So sánh cơ chế co hệ số giữa OLS, Ridge và Lasso](/Users/longnguyen/Documents/bds_khdl/reports/figures/09_regularization_lasso_vs_ridge.png)

#### 1. 🎯 Mục tiêu & Bản chất kỹ thuật điều chuẩn
Khi đưa nhiều biến số vào mô hình, nguy cơ **Đa cộng tuyến (Multicollinearity)** và **Quá khớp (Overfitting)** sẽ xuất hiện. Kỹ thuật điều chuẩn (Regularisation) thêm một lượng phạt vào hàm mất mát:
* **Ridge ($L_2$ Regularisation)**: Phạt $\alpha \sum \beta_j^2$. Cơ chế: "Bắt tất cả các hệ số phải nhún nhường, co nhỏ lại gần 0 để tránh bùng nổ phương sai", nhưng **không loại bỏ bất kỳ biến nào**.
* **Lasso ($L_1$ Regularisation)**: Phạt $\alpha \sum |\beta_j|$. Cơ chế: Nhờ hình học góc nhọn của chuẩn $L_1$, Lasso có khả năng **kéo thẳng các hệ số của biến yếu hoặc biến dư thừa thông tin về đúng số $0.000$**, hoạt động như một cỗ máy tự động chọn lọc thuộc tính (Automatic Feature Selection).

#### 2. 📊 Bảng so sánh Hệ số hồi quy Beta chuẩn hóa (Standardized Coefs)

| Tên Đặc Trưng ($X$) | OLS Cổ Điển | Ridge ($L_2, \alpha=193.07$) | Lasso ($L_1, \alpha=0.3556$) | Cơ Chế Tác Động Của Thuật Toán Lasso |
| :--- | :---: | :---: | :---: | :--- |
| `khu_vuc_noi_do` | $+15.771$ | $+15.660$ | **$+15.472$** | Giữ vững vị thế biến dẫn dắt quan trọng nhất |
| `loai_nha_ngo_hem` | $-15.560$ | $-15.207$ | **$-15.035$** | Giữ vững vị thế biến chiết khấu lớn nhất |
| `Số phòng ngủ` | $+7.938$ | $+7.890$ | **$+7.612$** | Giữ nguyên tỷ trọng công năng sinh hoạt |
| `loai_nha_mat_pho` | $+5.169$ | $+5.433$ | **$+5.229$** | Giữ nguyên thặng dư thương mại mặt đường |
| `tong_dien_tich_san_m2`| $+3.908$ | $+3.868$ | **$+3.052$** | Đại diện chính xác cho quy mô xây dựng |
| `Số tầng` | $+2.533$ | $+2.553$ | **$+2.695$** | Phản ánh chi phí xây dựng trên đất |
| `mat_tien_m` | $+2.530$ | $+2.521$ | **$+2.077$** | Phản ánh giá trị tiếp cận giao thông |
| `co_so_do` | $-0.929$ | $-0.914$ | **$-0.215$** | Co nhỏ dần ảnh hưởng |
| `Diện tích m2` | $-1.010$ | $-0.913$ | **$-0.000$** 🎯 | **TRIỆT TIÊU VỀ 0**: Do thông tin diện tích đã được đại diện bởi `tong_dien_tich_san_m2` |
| `chieu_sau_m` | $-0.222$ | $-0.219$ | **$-0.000$** 🎯 | **TRIỆT TIÊU VỀ 0**: Biến gây nhiễu, không có ý nghĩa ($p=0.708$) |

#### 3. 🔍 Quy luật & Bài học rút ra từ Biểu đồ 09
* **Sức mạnh chọn lọc biến tự động của Lasso**:
  - Nhìn vào cột màu xanh lá của Biểu đồ 09 tại hai biến `Diện tích m2` và `chieu_sau_m`: **Cột biến mất hoàn toàn và nằm bẹp dí trên trục hoành ($= 0$)**!
  - Điều này giải thích bằng trực giác kinh tế rất dễ hiểu: Khi chúng ta đã cung cấp cho mô hình biến `tong_dien_tich_san_m2` (Diện tích sàn = Diện tích đất $\times$ Số tầng) và biến `mat_tien_m`, hai biến `Diện tích m2` và `chieu_sau_m` trở nên dư thừa. Lasso đã tự động dọn dẹp các biến dư thừa này mà không cần con người can thiệp thủ công.
* **Bảng so sánh hiệu năng 4 mô hình tuyến tính trên tập kiểm thử độc lập (Test Set $n = 7.481$)**:

| Mô Hình | MAE ($triệu/m^2$) | RMSE ($triệu/m^2$) | Hệ Số $R^2$ | Ưu Thế Thực Tiễn | Hạn Chế Cần Biết |
| :--- | :---: | :---: | :---: | :--- | :--- |
| **OLS Cổ Điển** | 29.90 | 46.69 | 0.2884 | Tốc độ nhanh, dễ hiểu | Bị méo mó khi có đa cộng tuyến, nhạy cảm với outlier |
| **Ridge ($L_2$)** | 29.88 | 46.69 | 0.2885 | Ổn định trọng số, chống bùng nổ phương sai | Giữ lại toàn bộ biến, không làm gọn mô hình |
| **Lasso ($L_1$)** | 29.87 | 46.70 | 0.2883 | **Tự động tinh gọn mô hình**, loại bỏ biến rác | Phạt mạnh các biến có tương quan nhóm |
| **Log-Linear OLS** | **28.35** | **47.69** | **0.2576\*** | **MAE thấp nhất**, nắn chuẩn phần dư hoàn hảo | Cần đổi ngược $e^{\hat{y}}$ khi áp dụng thực tế |

*\*Lưu ý: Hệ số $R^2$ của mô hình Log-Linear được tính trực tiếp trên không gian giá gốc (triệu VNĐ) sau khi lấy hàm mũ $e^{\hat{y}}$ để đảm bảo tính công bằng khi so sánh.*

---

## CHƯƠNG 9: TỔNG KẾT TIẾN ĐỘ & LỘ TRÌNH TRIỂN KHAI CUỐI KỲ (TUẦN 11 - 12)

### 9.1. 7 Kết luận thực tiễn rút ra từ dữ liệu thực tế
1. **Nội đô và Ngoại thành là 2 thế giới giá tách biệt**: Kiểm định Welch's t-test ($t = 64.18, p < 0.0001$) và Mann-Whitney U chứng minh khoảng chênh lệch $32.04$ triệu/m² (Nội đô cao hơn 39.0%) là một quy luật khách quan vững chắc, đạt mức độ tác động lớn (Cohen's $d = 0.61$).
2. **"Tam giác vàng" Cầu Giấy - Ba Đình - Tây Hồ đồng nhất về giá**: Phép kiểm định ANOVA ($F = 368.11$) kết hợp Tukey's HSD khẳng định không có sự khác biệt có ý nghĩa thống kê về mặt bằng giá giữa 3 quận dẫn đầu này (trung bình dao động $123.7 - 128.6$ triệu/m²).
3. **Phần dư hồi quy OLS vi phạm giả định phương sai đồng nhất**: Biểu đồ chẩn đoán LINE phát hiện đám mây sai số xòe hình phễu khổng lồ (Breusch-Pagan $p < 0.0001$), khẳng định mô hình tuyến tính đơn giản luôn dự báo sai lệch lớn ở phân khúc nhà cao cấp.
4. **Biến đổi Logarit là chìa khóa vàng nắn chuẩn dữ liệu**: Phép biến đổi $\ln(\text{Giá\_m2\_trieu})$ đã kéo độ lệch phần dư từ $+2.18$ về $-0.29$ và độ nhọn từ $10.79$ về $3.72$, đưa đường Q-Q plot bám khít tuyệt đối vào đường chuẩn 45 độ, đồng thời giảm MAE xuống $28.35$ triệu/m².
5. **Lasso minh chứng sức mạnh tự động lọc biến**: Chuẩn $L_1$ đã tự động triệt tiêu hệ số của `Diện tích m2` và `chieu_sau_m` về đúng $0.000$, chứng minh tính tối ưu trong việc loại bỏ các thuộc tính dư thừa thông tin.
6. **Mặt tiền rộng mang thặng dư thương mại thật sự**: Sau khi loại bỏ lỗi outlier $400.000$m, mỗi mét mặt tiền mở rộng gia tăng thêm trung bình $\approx 1.94$ triệu/m² đơn giá.
7. **Gradient Boosting vẫn là đỉnh chóp dự báo**: Dù mô hình hồi quy tuyến tính mang lại tính giải thích toán học xuất sắc, các mô hình cây phi tuyến (Gradient Boosting MAE $26.07$ triệu/m², $R^2 = 0.4390$) vẫn vượt trội hoàn toàn nhờ khả năng tự học các mối tương tác phức tạp giữa Diện tích, Mặt tiền và Vị trí.

---

### 9.2. Các hạn chế kỹ thuật hiện tại
* Mặc dù đã hoàn thành trọn vẹn tầng Thống kê suy luận (Tuần 9) và Chẩn đoán Hồi quy LINE (Tuần 10), mô hình hiện tại vẫn là dạng "Hộp đen" (Black-box) ở các thuật toán Ensemble cây, người dùng chưa nhìn thấy được cụ thể tại sao AI lại cộng hay trừ tiền cho từng căn nhà riêng biệt.
* Dự án chưa triển khai các thuật toán phân loại (Classification) đa lớp để tự động gắn nhãn 5 phân khúc thị trường phục vụ tìm kiếm nhanh.

---

### 9.3. Kế hoạch hành động chi tiết cho giai đoạn cuối kỳ (Tuần 11 đến Tuần 12)

| Tuần Triển Khai | Trạng Thái | Nhiệm Vụ Trọng Tâm | Kế Hoạch Triển Khai Kỹ Thuật Chi Tiết |
| :---: | :---: | :--- | :--- |
| **Tuần 1 - 8** |  **Hoàn thành** | **Thu thập, Làm sạch, Kỹ nghệ đặc trưng, EDA & Midterm** | Đã hoàn thành 100% tệp dữ liệu sạch 37.402 bản ghi, bộ 6 biểu đồ, Baseline Gradient Boosting và bot dự đoán giá CLI. |
| **Tuần 9** |  **Hoàn thành** | **Thống Kê Suy Luận & Kiểm Định Giả Thuyết** | Đã chạy xong Welch's t-test, Mann-Whitney U, ANOVA, Tukey's HSD 66 cặp, Bảng khoảng tin cậy 95% CI và Biểu đồ 07. |
| **Tuần 10** |  **Hoàn thành** | **Chẩn Đoán Hồi Quy LINE & Regularisation** | Đã chẩn đoán 4 giả định LINE, kiểm tra Breusch-Pagan, Durbin-Watson, biến đổi Logarit thành công, đối đầu Ridge vs Lasso và Biểu đồ 08, 09. |
| **Tuần 11** | ⏳ **Sắp tới** | **Phân Loại Phân Khúc & XAI (SHAP Values)** | - Huấn luyện mô hình phân loại đa lớp (Multi-class Classification) cho 5 phân khúc giá tài sản.<br>- Triển khai các thuật toán tiên tiến **XGBoost** và **LightGBM** kết hợp kiểm định chéo K-Fold Cross-Validation.<br>- Tích hợp công cụ **SHAP (Shapley Additive exPlanations)**: Vẽ biểu đồ Force Plot & Summary Plot để bóc tách đóng góp của từng yếu tố cho mỗi dự báo. |
| **Tuần 12** | ⏳ **Sắp tới** | **Đạo Đức Dữ Liệu, Hoàn Thiện Báo Cáo & Nghiệm Thu** | - Xây dựng tài liệu chuẩn mực **Datasheets for Datasets** và **Model Card** theo tiêu chuẩn quốc tế.<br>- Đánh giá độ lệch định kiến (Fairness & Bias) giữa các phân khúc vùng miền.<br>- Đóng gói mã nguồn hoàn chỉnh, cập nhật tài liệu hướng dẫn và xây dựng slide thuyết trình cuối kỳ. |

---
*Báo cáo được hoàn thành và cập nhật tự động vào ngày: 15/10/2026 bởi Đội ngũ Khoa học Dữ liệu dự án BDS_KHDL.*

