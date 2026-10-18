# 🖥️ SLIDE DECK: BÁO CÁO TIẾN ĐỘ DỰ ÁN KHOA HỌC DỮ LIỆU
## ĐỀ TÀI: PHÂN TÍCH KHÔNG GIAN VÀ DỰ ĐOÁN GIÁ BẤT ĐỘNG SẢN TẠI HÀ NỘI
*(Tài liệu trình chiếu Slide thuyết trình — Tổng hợp tiến độ triển khai từ Tuần 1 đến Tuần 10)*

---

```
====================================================================================================
                                      CẤU TRÚC BỘ SLIDE THUYẾT TRÌNH
================PHẦN 1: BỐI CẢNH & PHỄU DỮ LIỆU (TUẦN 1 - 4)
  - Trang Bìa Đề Tài & Thông Tin Dự Án
  - Bối Cảnh Thị Trường & 3 Bài Toán Kinh Doanh Trọng Yếu
  - Phễu Sàng Lọc Dữ Liệu: Từ 99.998 Xuống 37.402 Bản Ghi & Phân Tích Lỗi Kỹ Thuật

PHẦN 2: KỸ NGHỆ ĐẶC TRƯNG & THIẾT KẾ PIPELINE (TUẦN 5)
  - Kỹ Nghệ Đặc Trưng Đa Chiều: 6 Nhóm Biến Cốt Lõi (12 -> 38 Biến)
  - Thiết Kế Scikit-Learn Pipeline & Cơ Chế Chống Rò Rỉ Dữ Liệu (Data Leakage)

PHẦN 3: PHÂN TÍCH KHÁM PHÁ EDA & BỘ BIỂU ĐỒ TRỰC QUAN HÓA (TUẦN 6 - 7)
  - Bức Tranh Thống Kê Mô Tả 4 Họ & Hiện Tượng Phân Phối Lệch Phải Log-Normal
  - [Biểu Đồ 01] Ma Trận Tương Quan Đa Biến Giữa Giá & Các Thuộc Tính
  - [Biểu Đồ 02] Phân Phối Đơn Giá & Tổng Giá Trị Bất Động Sản (KDE)
  - [Biểu Đồ 03] Tương Quan Phân Tán & Bước Nhảy Thương Mại Của Mặt Tiền
  - [Biểu Đồ 04] Phân Bố Đơn Giá 12 Quận/Huyện Trọng Điểm Theo Trung Vị

PHẦN 4: THỬ NGHIỆM MÔ HÌNH HÓA (TUẦN 10 - 11)
  - Huấn Luyện 80/20 & Bảng Đối Đầu Hiệu Năng 4 Thuật Toán Học Máy
  - [Biểu Đồ 05 & 06] Đánh Giá Hiệu Năng Mô Hình & Top 10 Đặc Trưng Chi Phối

PHẦN 5: THỐNG KÊ SUY LUẬN & KIỂM ĐỊNH GIẢ THUYẾT (TUẦN 9)
  - Khung Suy Luận Thống Kê & Cây Quyết Định Chọn Phép Kiểm
  - Welch's t-test So Sánh Nội Đô vs Ngoại Thành & Độ Lớn Hiệu Ứng (Cohen's d)
  - Phân Tích Phương Sai ANOVA & 9 Cặp Quận "Song Sinh Giá" (Tukey's HSD)
  - [Biểu Đồ 07] Khoảng Tin Cậy 95% (95% CI) Cho Đơn Giá 12 Quận/Huyện Hà Nội

PHẦN 6: CHẨN ĐOÁN HỒI QUY LINE & KỸ THUẬT ĐIỀU CHUẨN (TUẦN 10)
  - Đọc Hiểu OLS Đa Biến & 3 Nghĩa Vụ Đạo Đức Khi Diễn Giải Hệ Số Beta
  - [Biểu Đồ 08] Bộ Chẩn Đoán 4 Giả Định LINE Của Hồi Quy Kinh Tế Lượng
  - Hiệu Quả Đột Phá Sau Biến Đổi Logarit: Nắn Chuẩn Phần Dư Tuyệt Đối
  - [Biểu Đồ 09] Kỹ Thuật Điều Chuẩn: Lasso L1 Tự Động Triệt Tiêu Biến Rác Về 0

PHẦN 7: TỔNG KẾT & KẾ HOẠCH BỨT PHÁ (TUẦN 11 - 12)
  - 7 Kết Luận Thực Tiễn Rút Ra Từ Dữ Liệu Thực Tế Thị Trường
  - Lộ Trình Hoàn Thiện Cuối Kỳ (Tuần 11 - 12) & Sẵn Sàng Trả Lời Câu Hỏi
====================================================================================================
```

---

<!-- slide -->
# 🎯 TRANG BÌA & THÔNG TIN DỰ ÁN

## ĐỀ TÀI: PHÂN TÍCH KHÔNG GIAN VÀ DỰ ĐOÁN GIÁ BẤT ĐỘNG SẢN TẠI HÀ NỘI
### Học Phần: Khoa Học Dữ Liệu (INFO3020) — Báo Cáo Tiến Độ Tuần 1 Đến Tuần 10

* **Quy mô tập dữ liệu**: 99.998 tin rao thu thập $\rightarrow$ 37.402 bản ghi chuẩn hóa 18 tháng gần nhất (2025 – 2026).
* **Công cụ cốt lõi**: Python, Scikit-Learn, Statsmodels, SciPy, Matplotlib & Seaborn.
* **Mục tiêu**: Xây dựng bức tranh toàn cảnh về giá BĐS Hà Nội, kiểm định giả thuyết thị trường bằng thống kê suy luận, chẩn đoán mô hình hồi quy và đóng gói pipeline suy diễn chuẩn mực.

---

<!-- slide -->
# 🎯 BỐI CẢNH THỊ TRƯỜNG & 3 BÀI TOÁN KINH DOANH TRỌNG YẾU

### 1. Bối Cảnh Thị Trường BĐS Hà Nội (2025 - 2026):
* Luật Đất đai mới có hiệu lực cùng tốc độ hoàn thiện các tuyến vành đai và metro đẩy mặt bằng giá nhà đất tăng mạnh.
* Thị trường tin rao trực tuyến bị nhiễu loạn bởi tin ảo câu tương tác, giá "hét" chênh lệch xa giao dịch thực tế, hoặc dùng mặt bằng giá lỗi thời của 5 năm trước.

### 2. 3 Câu Hỏi Kinh Doanh Cốt Lõi:
```
+----------------------------------------------------------------------------------------------------+
| ❓ 1. MẶT BẰNG GIÁ THỰC (Baseline Price):                                                          |
|    Đơn giá thực tế (triệu/m²) tại các quận, huyện là bao nhiêu sau khi lọc bỏ 100% tin rác và cũ?  |
+----------------------------------------------------------------------------------------------------+
| ❓ 2. NHÂN TỐ DẪN DẮT GIÁ TRỊ (Value Drivers):                                                     |
|    Trong các yếu tố: Vị trí nội đô, Mặt tiền, Diện tích, Số tầng, Pháp lý - đâu là biến số chi phối |
|    quyết định nhất đến giá trị tài sản?                                                            |
+----------------------------------------------------------------------------------------------------+
| ❓ 3. CÔNG CỤ ĐỊNH GIÁ TỰ ĐỘNG (Automated Valuation Model - AVM):                                  |
|    Liệu có thể xây dựng mô hình AI với sai số MAE < 26 triệu/m² để hỗ trợ người dân và ngân hàng    |
|    ước tính nhanh giá trị nhà trong vòng dưới 1 giây?                                              |
+----------------------------------------------------------------------------------------------------+
```

---

<!-- slide -->
# 🎯 PHỄU SÀNG LỌC DỮ LIỆU: TỪ 99.998 XUỐNG 37.402 BẢN GHI & PHÂN TÍCH LỖI KỸ THUẬT

### 1. 📊 Bảng Tổng Quan Phễu Sàng Lọc Dữ Liệu (Data Cleaning Funnel):

| Bước Sàng Lọc | Quy Mô Bản Ghi | Số Lượng Lọc Bỏ | Tỷ Lệ Sụt Giảm | Lý Do Nghiệp Vụ & Cơ Sở Khoa Học |
| :--- | :---: | :---: | :---: | :--- |
| **1. Dữ liệu thô ban đầu** | **99.998 dòng** | — | — | Thu thập đa kênh: Batdongsan, Homedy, Alonhadat + Dữ liệu mở Kaggle/HuggingFace. |
| **2. Lọc chu kỳ 18 tháng** | **38.505 dòng** | **Loại 61.493 dòng** | Giảm **61.5%** | Dữ liệu cũ 2020-2024 có giá thấp hơn 40-70%, loại bỏ để tránh **bẫy phân phối đa đỉnh (Bimodal)**. |
| **3. Xóa khuyết mục tiêu** | **37.630 dòng** | **Loại 875 dòng** | Giảm **2.3%** | Thiếu Giá/m2 ("giá thỏa thuận", chuỗi `inf`) hoặc thiếu Diện tích (không được điền giá trị giả). |
| **4. Lọc Outlier tri thức** | **37.402 dòng** | **Loại 228 dòng** | Giảm **0.6%** | Đơn giá ảo $< 10$ tr hoặc $> 500$ tr/m² (tin lừa đảo cọc hoặc gõ nhầm hàng chục số 0). |
| **👉 TẬP SẠCH CUỐI CÙNG** | **37.402 dòng** | **Đạt chuẩn 100%** | **Giữ lại 37.4%** | Sạch hoàn hảo, đúng chu kỳ giá 2025 - 2026, sẵn sàng cho EDA & huấn luyện mô hình. |

---

### 2. 🔍 Bảng Bóc Tách Chi Tiết Từng Lỗi Missing, Outlier & Nhiễu Nhập Liệu:

| Nhóm Lỗi | Thuộc Tính Bị Lỗi | Số Bản Ghi Lỗi | Tỷ Lệ Mẫu (%) | Nguyên Nhân Gốc Rễ Phát Sinh Lỗi | Phương Pháp & Nguyên Lý Xử Lý Chuẩn Hóa |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **Missing** | `Giá/m2`, `Diện tích` | **875 dòng** | **2.27%** | Người đăng cố tình ghi *"Giá thỏa thuận"* để câu inbox, hoặc lỗi parser ra chuỗi `inf`. | **Xóa bỏ hoàn toàn (MCAR Deletion)**; tuyệt đối không điền giá trị giả vào biến mục tiêu. |
| **Missing** | `Số tầng` (Đất nền) | **2.140 dòng** | **5.56%** | Đặc thù vật lý: Đất nền, đất dịch vụ trống **chưa có công trình**, người bán để trống số tầng. | **Chuẩn hóa giá trị thực**: Tự động quét từ khóa đất $\rightarrow$ Gán `Số tầng = 0.0`. |
| **Missing** | `Số tầng` (Nhà ở) | **14.210 dòng** | **36.91%** | Nhà ở thực tế có tầng nhưng người đăng lười điền do biểu mẫu web không bắt buộc. | Điền trung vị tập train kèm tạo biến cờ chỉ báo **`Thieu_So_Tang = 1`**. |
| **Missing** | Kích thước (`Dài`, `Rộng`)| **21.178 dòng** | **55.00%** | Người bán chỉ nhớ tổng diện tích sổ đỏ, lười đo đạc kích thước hình học chi tiết từng cạnh. | Giữ nguyên dữ liệu để tránh mất 55% mẫu; đưa vào Pipeline điền `SimpleImputer(Median)`. |
| **Missing** | `Giấy tờ pháp lý` | **13.476 dòng** | **35.00%** | Tâm lý e ngại công khai pháp lý chưa hoàn chỉnh (nhà chờ cấp sổ, đất xen kẹt, đang cắm ngân hàng). | Gán nhãn `'Chưa xác định'` và tạo biến cờ nhị phân `co_so_do = 1 / 0`. |
| **Outlier** | `Đơn giá` cực đoan | **228 dòng** | **0.59%** | Tin lừa đảo cọc (rao nhà $1-2$ tr) hoặc gõ nhầm hàng chục số 0 (bán 50 tỷ gõ nhầm 5.000 tỷ). | **Bộ lọc miền tri thức**: Giới hạn $[10, 500] \text{ tr/m²}$ và $[10, 500] \text{ m²}$ (xóa bẫy cắt cụt 174M cũ). |
| **Nhiễu số** | `Mặt tiền` dạng mm | **1.420 dòng** | **3.69%** | Người dùng quen nhập theo bản vẽ kỹ thuật bằng đơn vị **milimet** (gõ `4500` mm thay vì `4.5` m). | **Quy đổi tự động**: Nhận diện dải $[1.000, 35.000]$ và tự động chia $1.000$ đưa về mét chuẩn. |
| **Outlier** | `Mặt tiền` dị biệt | **12 dòng** | **0.03%** | Lỗi kẹt phím gõ nhầm mặt tiền lên tới $400.000$ m (kéo dãn trục hoành scatter plot lên 400km). | **Chặn trần vật lý**: Thiết lập kích thước mặt tiền tối đa là $30.0$ m. |
| **Nhiễu chữ** | `Quận`, `Địa chỉ` (Text) | **38.505 dòng** | **100%** | Xung đột Unicode tổ hợp (NFD) và dựng sẵn (NFC) do người đăng dùng các bộ gõ Unikey khác nhau. | **Chuẩn hóa Unicode NFC**: Chuyển đổi toàn bộ văn bản về Unicode NFC dựng sẵn. |
| **Trùng lặp** | Toàn bộ 12 trường | **0 dòng** | **0.00%** | Không có bản ghi nào trùng khớp $100\%$ tất cả các trường thông tin. | Bảo toàn nguyên vẹn tính duy nhất của từng thực thể bài đăng. |

---

<!-- slide -->
# 🎯 KỸ NGHỆ ĐẶC TRƯNG ĐA CHIỀU: 6 NHÓM BIẾN CỐT LÕI (12 ➔ 38 BIẾN)
### Từ 12 Trường Thuộc Tính Gốc Phát Triển Thành 38 Biến Chuyên Sâu

Thay vì để dữ liệu ở dạng thô, dự án trích xuất và thiết lập các biến phái sinh bao quát 6 góc độ định giá:

```
+----------------------------------------------------------------------------------------------------+
| 6 NHÓM ĐẶC TRƯNG ĐẠI DIỆN PHÁI SINH TIÊU BIỂU                                                      |
+--------------------+--------------------------------+----------------------------------------------+
| Nhóm Đặc Trưng     | Biến Số Phái Sinh Tiêu Biểu     | Ý Nghĩa Nghiệp Vụ Kinh Doanh                  |
+--------------------+--------------------------------+----------------------------------------------+
| 1. Quy mô tài sản  | Tong_Gia_ty (Tỷ VNĐ)           | Đơn giá * Diện tích / 1000                   |
| 2. Hình thái đất   | ty_le_dai_rong & hinh_dang_dat | Tỷ lệ Sâu / Mặt tiền (Mặt tiền lớn / Vuông)  |
| 3. Công năng sàn   | tong_dien_tich_san_m2          | Diện tích đất * Số tầng (Không gian ở thực)  |
| 4. Tiện nghi phòng | dien_tich_moi_phong_ngu_m2     | Diện tích đất / Số phòng ngủ                 |
| 5. Vị trí lõi      | khu_vuc_noi_do (0 hoặc 1)      | Cờ nhị phân đánh dấu 7 quận trung tâm lịch sử|
| 6. Loại hình nhà   | loai_nha_ngo_hem & mat_pho     | Tách riêng cờ nhận diện nhà trong ngõ vs phố |
+--------------------+--------------------------------+----------------------------------------------+
```

* **Hình thái đất**: Tỷ lệ $< 1.0$ (Mặt tiền lớn, giá trị kinh doanh cao), $1.0 - 2.5$ (Đất vuông vắn chuẩn phong thủy), $> 2.5$ (Nhà ống dài hẹp).
* **Công năng thực**: Biến `tong_dien_tich_san_m2` phản ánh diện tích sử dụng thực tế của ngôi nhà thay vì chỉ nhìn vào diện tích đất thô.

---

<!-- slide -->
# 🎯 THIẾT KẾ SCIKIT-LEARN PIPELINE & CƠ CHẾ CHỐNG RÒ RỈ DỮ LIỆU (DATA LEAKAGE)

Để đảm bảo kết quả đánh giá khách quan và mô hình không bị "học vẹt", toàn bộ quy trình tiền xử lý được đóng gói trong `ColumnTransformer`:

```
                 TẬP DỮ LIỆU HUẤN LUYỆN (TRAIN SET - 80%)
                                   │
         ┌─────────────────────────┴─────────────────────────┐
         ▼                                                   ▼
┌─────────────────────────────────┐       ┌─────────────────────────────────┐
│     BIẾN ĐỊNH LƯỢNG (NUMERIC)   │       │   BIẾN ĐỊNH DANH (CATEGORICAL)  │
│  - SimpleImputer (Median)       │       │  - SimpleImputer (Most Frequent)│
│  - RobustScaler (Dựa trên IQR)  │       │  - OneHotEncoder (drop='first') │
└─────────────────────────────────┘       └─────────────────────────────────┘
         │                                                   │
         └─────────────────────────┬─────────────────────────┘
                                   ▼
               ĐẶC TRƯNG ĐÃ ĐƯỢC CHUẨN HÓA SẠCH
                                   │
                                   ▼
                 MÔ HÌNH HỌC MÁY (MACHINE LEARNING)
```

* **RobustScaler**: Chuẩn hóa dữ liệu bằng Trung vị (Median) và Khoảng liên phân vị (IQR), giúp mô hình duy trì tính ổn định, không bị kéo lệch bởi các căn nhà triệu đô.
* **OneHotEncoder (`drop='first'`)**: Triệt tiêu hoàn toàn bẫy biến giả (Dummy Variable Trap).
* **Quy tắc chống rò rỉ (Data Leakage)**: Mọi tham số trung vị hay thang đo đều chỉ được học (fit) trên tập Train (80%), sau đó mới áp dụng (transform) sang tập Test (20%).

---

<!-- slide -->
# 🎯 BỨC TRANH THỐNG KÊ MÔ TẢ 4 HỌ & HIỆN TƯỢNG PHÂN PHỐI LỆCH PHẢI LOG-NORMAL

Dựa trên **37.402 bản ghi sạch**, hệ thống tính toán đầy đủ 4 nhóm đại lượng thống kê:

```
+----------------------------------------------------------------------------------------------------+
| BẢNG ĐẠI LƯỢNG THỐNG KÊ CỐT LÕI (N = 37,402 BẢN GHI SẠCH)                                          |
+------------------------------------+--------------------------+------------------------------------+
| Chỉ Số Đo Lường / Phân Tầng        | Đơn Giá (Triệu VNĐ/m²)   | Tổng Giá Trị Tài Sản (Tỷ VNĐ)      |
+------------------------------------+--------------------------+------------------------------------+
| 1. LOCATION (Độ tập trung)         |                          |                                    |
|    - Giá trị nhỏ nhất (Min)        | 10.00 triệu/m²           | 0.25 Tỷ VNĐ                        |
|    - Phân vị Q1 (25%)              | 72.67 triệu/m²           | 2.75 Tỷ VNĐ                        |
|    - TRUNG VỊ (Median - Chuẩn)     | 90.00 triệu/m² 🎯        | 3.60 Tỷ VNĐ 🎯                    |
|    - TRUNG BÌNH (Mean)             | 102.18 triệu/m²          | 5.10 Tỷ VNĐ                        |
|    - Phân vị Q3 (75%)              | 112.50 triệu/m²          | 5.30 Tỷ VNĐ                        |
|    - Giá trị lớn nhất (Max)        | 500.00 triệu/m²          | 237.00 Tỷ VNĐ                      |
+------------------------------------+--------------------------+------------------------------------+
| 2. SPREAD (Độ tán sắc)             |                          |                                    |
|    - Khoảng liên phân vị (IQR)     | 39.83 triệu/m²           | 2.55 Tỷ VNĐ                        |
|    - Độ lệch chuẩn (Std)           | 54.78 triệu/m²           | 5.76 Tỷ VNĐ                        |
+------------------------------------+--------------------------+------------------------------------+
| 3. SHAPE (Hình dạng phân phối)     |                          |                                    |
|    - Hệ số Skewness (Độ lệch)      | +2.75 (Lệch phải mạnh)   | +8.80 (Lệch phải cực lớn)          |
+------------------------------------+--------------------------+------------------------------------+
```

### 💡 Quy Luật Kinh Tế: Mean Luôn Cao Hơn Median
* Do sự xuất hiện của các bất động sản mặt phố đắc địa ($150 - 450$ tr/m²), giá trị trung bình ($102.18$ tr) bị kéo cao hơn trung vị ($90.00$ tr) tới **$13.5\%$**.
* **Kết luận nghiệp vụ**: Trong định giá BĐS, **Trung vị (90.00 triệu/m²)** là thước đo đại diện sát thực tế nhất cho mức chi trả của 50% người dân Thủ đô.

---

<!-- slide -->
# 🎯 [BIỂU ĐỒ 01] MA TRẬN TƯƠNG QUAN ĐA BIẾN GIỮA GIÁ & CÁC THUỘC TÍNH

![Biểu đồ 01: Ma trận tương quan đa biến](/Users/longnguyen/Documents/bds_khdl/reports/figures/01_correlation_heatmap.png)

### 📌 Phân Tích Chuyên Sâu 4 Trọng Tâm:
1. **Biểu đồ gì**: Ma trận tương quan đa biến (Correlation Heatmap Matrix) hiển thị hệ số tương quan tuyến tính Pearson ($r \in [-1, +1]$) giữa các cặp thuộc tính.
2. **Có tác dụng gì**:
   - Quét đồng thời toàn bộ mối quan hệ giữa biến mục tiêu (`Đơn giá tr/m²`, `Tổng giá tỷ`) với các biến độc lập.
   - Nhận diện sớm hiện tượng đa cộng tuyến (Multicollinearity) giữa các đặc trưng trước khi đưa vào mô hình hồi quy.
   - Sàng lọc nhanh các yếu tố chi phối mạnh nhất để định hướng kỹ nghệ đặc trưng.
3. **Đang biểu diễn thứ gì**:
   - **Hai trục X và Y**: Danh mục các đặc trưng (Đơn giá, Tổng giá, Diện tích, Mặt tiền, Chiều sâu, Số tầng, Số phòng ngủ, Cờ nội đô, Cờ ngõ hẻm, Cờ mặt phố).
   - **Thang màu (Color bar)**: Dải gradient từ xanh lam đậm ($r = -1.0$, tương quan nghịch tuyệt đối) qua trắng ($r = 0$, không tương quan) đến đỏ cam đậm ($r = +1.0$, tương quan thuận tuyệt đối).
   - **Số hiển thị trong từng ô**: Giá trị chính xác của hệ số Pearson $r$.
4. **Mang lại ý nghĩa gì**:
   - *Vị trí và loại hình là nhân tố tối cao*: `khu_vuc_noi_do` đạt tương quan dương cao nhất với đơn giá ($r = +0.283$), trong khi `loai_nha_ngo_hem` tương quan âm mạnh nhất ($r = -0.279$). Bất động sản trong ngõ hẻm luôn chịu mức chiết khấu giá rất sâu.
   - *Đặc trưng công năng vật lý gia tăng giá trị*: Số phòng ngủ ($r = +0.242$) và Số tầng ($r = +0.225$) đồng biến mạnh với đơn giá đất vì chi phí xây dựng hoàn thiện được kết tinh vào giá chào bán.
   - *Thặng dư thương mại mặt tiền*: Sau khi sửa triệt để lỗi milimet, mặt tiền có tương quan dương ($r = +0.161$) – mặt tiền càng rộng thì đơn giá đất càng cao nhờ khả năng kinh doanh buôn bán.
   - *Cảnh báo đa cộng tuyến*: Diện tích đất và Tổng diện tích sàn tương quan với nhau rất cao ($r = 0.88$), cảnh báo mô hình tuyến tính sẽ bị bất ổn định nếu không dùng Regularization.

---

<!-- slide -->
# 🎯 [BIỂU ĐỒ 02] PHÂN PHỐI ĐƠN GIÁ & TỔNG GIÁ TRỊ BẤT ĐỘNG SẢN (KDE)

![Biểu đồ 02: Phân phối Đơn giá & Tổng giá trị](/Users/longnguyen/Documents/bds_khdl/reports/figures/02_price_distribution.png)

### 📌 Phân Tích Chuyên Sâu 4 Trọng Tâm:
1. **Biểu đồ gì**: Biểu đồ phân phối tần suất kép (Dual Distribution Plot) gồm Histogram dạng cột ghép đôi kết hợp đường cong ước lượng mật độ hạt nhân trơn (Kernel Density Estimation - KDE).
2. **Có tác dụng gì**:
   - Kiểm tra trực quan hình thái phân phối thực tế của biến mục tiêu (Đơn giá tr/m² và Tổng giá bán tỷ VNĐ).
   - Đo lường mức độ bất đối xứng (Skewness) và độ nhọn (Kurtosis), từ đó xác minh xem dữ liệu có tuân theo phân phối chuẩn Gaussian hay không.
   - Nhận diện phân khúc thanh khoản tập trung nhất trên thị trường giao dịch thực tế.
3. **Đang biểu diễn thứ gì**:
   - **Đồ thị bên trái (Đơn giá)**: Trục hoành X là Đơn giá (triệu VNĐ/m², từ $10$ đến $500$ tr/m²); Trục tung Y là Mật độ xác suất (Density). Cột histogram xanh lam biểu diễn tần suất phân tổ; đường cam KDE biểu diễn hàm mật độ liên tục.
   - **Đồ thị bên phải (Tổng giá trị)**: Trục hoành X là Tổng giá trị (Tỷ VNĐ, từ $0.25$ đến $50$ Tỷ); Trục tung Y là Mật độ xác suất.
   - **Vị trí đỉnh sóng KDE**: Đại diện cho điểm tập trung giao dịch đông đảo nhất (Mode).
4. **Mang lại ý nghĩa gì**:
   - *Bản chất phân phối Lệch phải tự nhiên (Right-Skewed / Log-Normal)*: Đuôi phải kéo dài sang các bất động sản giá siêu đắt ($300 - 500$ tr/m² và $20 - 50$ tỷ VNĐ). Skewness đơn giá là $+2.75$ và Tổng giá là $+8.80$.
   - *Tâm chấn thanh khoản thị trường*: Đỉnh mật độ đơn giá tập trung ở $75 - 90$ tr/m²; tổng giá tập trung ở $2.5 - 5.0$ tỷ VNĐ. Đây là phân khúc cốt lõi đáp ứng nhu cầu ở thực của đại đa số gia đình trung lưu Thủ đô.
   - *Quyết định kỹ thuật sống còn*: Chứng minh biến mục tiêu vi phạm giả định chuẩn, bắt buộc phải sử dụng phép biến đổi $\log(y)$ khi huấn luyện các mô hình hồi quy tuyến tính OLS, Ridge, Lasso.

---

<!-- slide -->
# 🎯 [BIỂU ĐỒ 03] TƯƠNG QUAN PHÂN TÁN & BƯỚC NHẢY THƯƠNG MẠI CỦA MẶT TIỀN

![Biểu đồ 03: Tương quan phân tán diện tích & mặt tiền](/Users/longnguyen/Documents/bds_khdl/reports/figures/03_price_vs_area_scatter.png)

### 📌 Phân Tích Chuyên Sâu 4 Trọng Tâm:
1. **Biểu đồ gì**: Biểu đồ phân tán đám mây điểm 2 chiều (Bivariate Scatter Plot) kết hợp đường xu hướng hồi quy tuyến tính OLS màu đỏ và dải phân tán mật độ điểm.
2. **Có tác dụng gì**:
   - Khảo sát mối quan hệ giữa các biến hình học vật lý cốt lõi (Diện tích đất, Chiều rộng mặt tiền) với giá cả.
   - Phát hiện hiện tượng phương sai sai số thay đổi (Heteroscedasticity) trực quan qua hình thái đám mây điểm.
   - Kiểm chứng giả thuyết: "Mặt tiền càng rộng thì đơn giá mỗi mét vuông đất càng tăng vọt do giá trị thương mại".
3. **Đang biểu diễn thứ gì**:
   - **Đồ thị bên trái (Diện tích vs Tổng giá)**: Trục hoành X là Diện tích ($m^2$, từ 20 đến 300 $m^2$); Trục tung Y là Tổng giá bán (Tỷ VNĐ, từ 1 đến 50 Tỷ). Đường hồi quy đỏ dốc lên tuyến tính.
   - **Đồ thị bên phải (Mặt tiền vs Đơn giá)**: Trục hoành X là Mặt tiền (mét, từ 1.5m đến 16m sau chuẩn hóa sạch); Trục tung Y là Đơn giá (triệu VNĐ/m², từ 10 đến 500 tr/m²). Điểm dữ liệu tập trung thành các dải sọc đứng ứng với các quy chuẩn xây dựng phổ biến: 3m, 3.5m, 4m, 4.5m, 5m, 6m.
4. **Mang lại ý nghĩa gì**:
   - *Hiện tượng phương sai hình phễu (Funnel Shape)*: Ở diện tích nhỏ ($< 50m^2$), các điểm tập trung rất sát đường hồi quy (sai số thấp). Khi diện tích tăng ($> 120m^2$), các điểm xòe rộng thành hình phễu từ 8 tỷ (ven đô) đến 35 tỷ (nhà phố trung tâm).
   - *Thặng dư thương mại mặt tiền*: Đường hồi quy mặt tiền dốc lên rõ rệt từ mức ~88 tr/m² (mặt tiền 2m) lên mức ~170 tr/m² (mặt tiền 16m).
   - *Ngưỡng bùng nổ thương mại (Break-even threshold)*: Tại mốc Mặt tiền = 4.0m, đơn giá có bước nhảy vọt. Nhà có mặt tiền $\ge 4.0m$ cho phép mở cửa hàng, kinh doanh tầng 1 hoặc cho thuê văn phòng, tạo ra dòng tiền đều đặn ngoài giá trị ở thuần túy.

---

<!-- slide -->
# 🎯 [BIỂU ĐỒ 04] PHÂN BỐ ĐƠN GIÁ 12 QUẬN/HUYỆN TRỌNG ĐIỂM THEO TRUNG VỊ

![Biểu đồ 04: Boxplot đơn giá 12 quận huyện](/Users/longnguyen/Documents/bds_khdl/reports/figures/04_price_by_district_boxplot.png)

### 📌 Phân Tích Chuyên Sâu 4 Trọng Tâm:
1. **Biểu đồ gì**: Biểu đồ hộp và râu đa nhóm (Multi-Group Box-and-Whisker Plot), được sắp xếp thứ tự giảm dần theo giá trị Trung vị (Median-Ordered Boxplot).
2. **Có tác dụng gì**:
   - So sánh trực quan đồng thời phân phối đơn giá của 12 quận/huyện trọng điểm tại Hà Nội mà không bị đánh lừa bởi giá trị ngoại lai.
   - Phân tích 5 số tóm tắt (Min, Q1, Median, Q3, Max) và độ phân tán (chiều dài hộp IQR) của từng địa bàn.
   - Phân tầng địa kinh tế và nhận diện các vùng giá dị biệt trên bản đồ Thủ đô.
3. **Đang biểu diễn thứ gì**:
   - **Trục hoành X**: 12 quận/huyện sắp xếp theo trung vị từ trái sang phải (Cầu Giấy, Ba Đình, Tây Hồ, Đống Đa, Thanh Xuân, Hai Bà Trưng, Nam Từ Liêm, Bắc Từ Liêm, Hoàng Mai, Long Biên, Hà Đông, Thanh Trì).
   - **Trục tung Y**: Đơn giá (triệu VNĐ/m²) từ 10 đến 500 tr/m².
   - **Thân hộp màu (Box)**: Biểu thị 50% dữ liệu ở giữa ($IQR = Q3 - Q1$). Đường vạch ngang bên trong hộp là Trung vị (Median).
   - **Râu (Whiskers)**: Kéo dài đến $1.5 \times IQR$. Các chấm tròn nằm ngoài râu là các căn nhà ngoại lai (Outliers - nhà mặt phố siêu đắt hoặc đất ngõ sâu).
4. **Mang lại ý nghĩa gì**:
   - *Phân định 3 tầng thứ bậc rõ nét*:
     + **Tầng 1 - Lõi di sản & phát triển (Trung vị $\ge 100$ tr/m²)**: Cầu Giấy (105 tr), Ba Đình (104 tr), Tây Hồ (101.9 tr), Đống Đa (100 tr). Hộp IQR rất cao và râu dài, thể hiện biên độ phân hóa lớn giữa nhà ngõ và mặt phố lớn.
     + **Tầng 2 - Đô thị phát triển năng động (Trung vị $85 - 93$ tr/m²)**: Thanh Xuân (92.5 tr), Hai Bà Trưng (89.7 tr), Nam Từ Liêm (85.7 tr). Thân hộp ngắn, giá cả đồng đều.
     + **Tầng 3 - Vành đai & Ven đô (Trung vị $60 - 80$ tr/m²)**: Bắc Từ Liêm (80 tr), Hoàng Mai (78.8 tr), Long Biên (77.5 tr), Hà Đông (74.4 tr), Thanh Trì (60.9 tr/m²). Mặt bằng giá mềm, phù hợp với gia đình trẻ.
   - *Giá trị thực tiễn*: Giúp người mua nhà định hình ngay ngân sách: Nếu chỉ có dưới 80 triệu/m², lựa chọn tối ưu là hướng sang Tầng 3 (Hà Đông, Hoàng Mai, Long Biên).

---

<!-- slide -->
# 🎯 HUẤN LUYỆN 80/20 & BẢNG ĐỐI ĐẦU HIỆU NĂNG 4 THUẬT TOÁN HỌC MÁY

Tập dữ liệu được phân chia theo tỷ lệ chuẩn Train/Test 80/20 (`random_state=42`):
* **Tập Huấn Luyện (Train)**: $29.921$ bản ghi ($80\%$).
* **Tập Kiểm Thử Độc Lập (Test)**: $7.481$ bản ghi ($20\%$).

### Bảng So Sánh Hiệu Năng Đối Đầu Trên Tập Test:
| Mô Hình Học Máy | MAE ($triệu/m^2$) | RMSE ($triệu/m^2$) | Hệ Số $R^2$ | Đánh Giá Kỹ Thuật |
| :--- | :---: | :---: | :---: | :--- |
| **Linear Regression** | 28.47 | 44.13 | 0.3644 | Baseline cơ sở, không bắt được tương tác phi tuyến |
| **Ridge Regression ($L_2$)** | 28.47 | 44.21 | 0.3621 | Kiểm soát đa cộng tuyến, hiệu năng tương đương Linear |
| **Random Forest** | 26.17 | 41.85 | 0.4284 | Cải thiện vượt bậc; giảm mạnh sai số MAE |
| **Gradient Boosting** | **26.07** | **41.46** | **0.4390** | **🏆 Vô địch toàn diện**: MAE thấp nhất, $R^2$ cao nhất |

* **Lý do thuật toán Cây (Tree-based) áp đảo Tuyến tính**: Giá trị BĐS có tính chất tương tác phi tuyến cao: Mặt tiền 6m ở Cầu Giấy mang lại thặng dư gấp nhiều lần mặt tiền 6m ở Thanh Trì. Các mô hình cây quyết định tự động phân vùng không gian để nắm bắt các mối liên hệ phức tạp này.

---

<!-- slide -->
# 🎯 [BIỂU ĐỒ 05 & 06] ĐÁNH GIÁ HIỆU NĂNG MÔ HÌNH & TOP 10 ĐẶC TRƯNG CHI PHỐI

| Biểu Đồ 05: So Sánh Hiệu Năng 4 Mô Hình | Biểu Đồ 06: Top 10 Đặc Trưng Quan Trọng Nhất |
| :---: | :---: |
| ![Model Comparison](/Users/longnguyen/Documents/bds_khdl/reports/figures/05_model_comparison.png) | ![Feature Importance](/Users/longnguyen/Documents/bds_khdl/reports/figures/06_feature_importance.png) |

### 📌 Phân Tích Chuyên Sâu 4 Trọng Tâm Cho [BIỂU ĐỒ 05]:
1. **Biểu đồ gì**: Biểu đồ cột nhóm ghép đôi (Dual-Metric Grouped Bar Chart) so sánh song song sai số tuyệt đối trung bình (MAE) và hệ số xác định ($R^2$ Score) trên tập kiểm thử độc lập (Test Set: 7.481 bản ghi).
2. **Có tác dụng gì**: Đánh giá khách quan năng lực học tập và khái quát hóa giữa 4 trường phái thuật toán (OLS, Ridge $L_2$, Random Forest, Gradient Boosting), tìm ra mô hình vô địch (Champion Model) có sai số dự báo nhỏ nhất.
3. **Đang biểu diễn thứ gì**:
   - **Trục hoành X**: 4 thuật toán học máy được đưa lên bàn cân đối đầu.
   - **Cột đỏ cam (Trục tung Y trái)**: Sai số MAE ($triệu/m^2$ - Càng thấp mô hình càng chuẩn xác).
   - **Cột xanh lam (Trục tung Y phải)**: Hệ số $R^2$ (Càng cao mô hình giải thích phương sai càng tốt).
   - **Số liệu gắn trên đầu cột**: Linear (MAE 28.47 tr, $R^2$ 0.364) $\rightarrow$ Ridge (MAE 28.47 tr, $R^2$ 0.362) $\rightarrow$ Random Forest (MAE 26.17 tr, $R^2$ 0.428) $\rightarrow$ **Gradient Boosting (MAE 26.07 tr, $R^2$ 0.439)**.
4. **Mang lại ý nghĩa gì**:
   - *Chiến thắng áp đảo của mô hình Cây (Tree-based Ensemble)*: GBDT giảm sai số MAE tới **$8.4\%$** và tăng $R^2$ thêm **$+20.5\%$** so với Linear Regression.
   - *Bản chất phi tuyến của thị trường BĐS*: Bất động sản có sự tương tác phi tuyến cực mạnh (mặt tiền 6m ở quận trung tâm có giá trị thương mại gấp nhiều lần mặt tiền 6m ở huyện ngoại thành). Mô hình cây tự động phân tách các vùng không gian đa chiều để khớp chính xác các mối quan hệ này.

---

### 📌 Phân Tích Chuyên Sâu 4 Trọng Tâm Cho [BIỂU ĐỒ 06]:
1. **Biểu đồ gì**: Biểu đồ thanh ngang xếp hạng tầm quan trọng đặc trưng (Horizontal Feature Importance Bar Chart) trích xuất từ mô hình quán quân Gradient Boosting dựa trên độ giảm độ vẩn đục Gini (Mức tăng thông tin).
2. **Có tác dụng gì**: Mở chiếc "hộp đen" (Black-box) của thuật toán học máy, minh bạch hóa các yếu tố cốt lõi nào đang dẫn dắt và định đoạt giá bán nhà tại Hà Nội.
3. **Đang biểu diễn thứ gì**:
   - **Trục tung Y**: Top 10 đặc trưng có lực chi phối mạnh nhất xếp từ cao xuống thấp.
   - **Trục hoành X**: Tỷ lệ phần trăm đóng góp tầm quan trọng (%) vào quyết định phân nhánh của các cây quyết định.
4. **Mang lại ý nghĩa gì**:
   - *Bộ đôi Vị trí & Loại hình chi phối trên 36% toàn bộ giá trị*: `loai_nha_ngo_hem` chiếm **$20.01\%$** (yếu tố tiếp giáp ngõ hẻm làm giảm giá trị nhiều nhất), tiếp theo là `khu_vuc_noi_do` chiếm **$16.14\%$** (thuộc 7 quận lõi quyết định mức sàn giá).
   - *Minh chứng sức mạnh của Kỹ nghệ đặc trưng*: Biến phái sinh `tong_dien_tich_san_m2` ($8.26\%$) và `dien_tich_moi_phong_ngu_m2` ($7.07\%$) xuất sắc lọt Top 5, vượt trội hoàn toàn so với biến diện tích đất thô.
   - *Ứng dụng thực tiễn*: Thẩm định viên chỉ cần tập trung kiểm chứng 5 yếu tố hàng đầu này là đã làm chủ trên $60\%$ cơ sở định giá của một tài sản.

---

<!-- slide -->
# 🎯 KHUNG SUY LUẬN THỐNG KÊ & QUY TRÌNH KIỂM ĐỊNH GIẢ THUYẾT (TUẦN 9)

### 1. Cây Quyết Định Lựa Chọn Phép Kiểm Định Thống Kê:
* **Bản chất Thống kê Suy luận**: Chuyển từ việc chỉ tóm tắt 21.142 mẫu quan sát được sang khẳng định các quy luật trên toàn thể thị trường bất động sản kèm mức độ không chắc chắn.
* **So sánh 2 nhóm độc lập (Mặt phố vs Ngõ)**: Phương sai hai nhóm không đồng nhất ($s_1^2 \neq s_2^2$) $\rightarrow$ Bắt buộc dùng **Welch's t-test** (`equal_var=False`) để triệt tiêu sai lầm Loại I.
* **So sánh 3+ nhóm định lượng (30 Quận/Huyện)**: Phân tích phương sai **One-way ANOVA** $\rightarrow$ Kết hợp kiểm định hậu nghiệm **Tukey's HSD Post-hoc** phát hiện các cặp quận tương đồng giá (tài sản thay thế).
* **Dữ liệu phân phối lệch & Ngoại lệ**: Dùng kỹ thuật tái lấy mẫu phi tham số **Bootstrap 1.000 lần** xác lập khoảng tin cậy 95% (CI) không phụ thuộc giả định chuẩn hóa.

### 2. Quy Trình 5 Bước & Bản Chất p-value:
* **Quy trình 5 bước kiểm định giả thuyết chuẩn mực**:
  1. Phát biểu $H_0$ (Không khác biệt) và $H_1$ (Có khác biệt thực sự).
  2. Thiết lập mức ý nghĩa $\alpha = 0.05$ TRƯỚC KHI quan sát số liệu.
  3. Kiểm tra giả định (Normality, Homoscedasticity) & chọn phép kiểm thích hợp.
  4. Tính Test-statistic, p-value, Khoảng tin cậy CI và Độ lớn hiệu ứng (Effect Size Cohen's d).
  5. Đưa ra kết luận: Bác bỏ $H_0$ nếu p-value $< \alpha$.
* **Bản chất p-value & 4 ngộ nhận cần tránh**: p-value là xác suất quan sát dữ liệu cực đoan như vậy với giả định $H_0$ đúng; KHÔNG PHẢI là xác suất $H_0$ đúng. $p < 0.05$ không đồng nghĩa hiệu ứng lớn.
* **Kiểm soát 2 loại sai lầm thống kê**:
  - *Sai lầm Loại I ($\alpha$)*: Bác bỏ $H_0$ khi $H_0$ đúng (Báo động giả).
  - *Sai lầm Loại II ($\beta$)*: Không bác bỏ $H_0$ khi $H_0$ sai; Đảm bảo Statistical Power $1 - \beta \ge 0.8$.

---

<!-- slide -->
# 🎯 WELCH'S T-TEST SO SÁNH NỘI ĐÔ VS NGOẠI THÀNH & ĐỘ LỚN HIỆU ỨNG (COHEN'S D)

Chuyển từ **Thống kê mô tả** (chỉ tóm tắt mẫu quan sát được) sang **Thống kê suy luận** (khẳng định bản chất của toàn bộ thị trường hàng triệu căn nhà ngoài đời thực):

```
+----------------------------------------------------------------------------------------------------+
| KIỂM ĐỊNH GIẢ THUYẾT: NỘI THÀNH (n=23.330) VS NGOẠI THÀNH (n=14.072)                               |
| - H0 (Hoài nghi): Giá đất Nội đô và Ngoại thành như nhau, chênh lệch thấy được chỉ là do ăn may.   |
| - H1 (Nghiên cứu): Giá đất Nội đô thực sự đắt hơn Ngoại thành có ý nghĩa thống kê.                |
+----------------------------------------------------------------------------------------------------+
```

### Bảng Kết Quả Thực Nghiệm:
* **Nội đô**: Mean = **$114.24$ tr/m²** ($s = 60.25$, Median = $96.67$)
* **Ngoại thành**: Mean = **$82.20$ tr/m²** ($s = 36.30$, Median = $76.77$)
* **Chênh lệch thực tế**: **$32.04$ triệu/m²** (Nội đô cao hơn **$39.0\%$**).

| Phép Kiểm Định | Đại Lượng Thống Kê | Giá Trị $p\text{-value}$ | Kết Luận Khoa Học |
| :--- | :---: | :---: | :--- |
| **Welch's Two-Sample t-test** | $t = \mathbf{64.18}$ | **$< 10^{-16}$** ($0.0000$) | **Bác bỏ $H_0$ đanh thép**: Đơn giá Nội đô cao hơn vượt trội |
| **Mann-Whitney U (Phi tham số)**| $U = \mathbf{2.35 \times 10^8}$| **$< 10^{-16}$** ($0.0000$) | Khẳng định không phụ thuộc giả định phân phối chuẩn |
| **Cohen's d (Effect Size)** | $d = \mathbf{0.610}$ | — | **Mức tác động Trung bình - Lớn**: Chênh lệch mang giá trị kinh tế |

---

<!-- slide -->
# 🎯 PHÂN TÍCH PHƯƠNG SAI ANOVA & 9 CẶP QUẬN "SONG SINH GIÁ" (TUKEY'S HSD)

* **Nguy cơ Bẫy so sánh nhiều cặp (Multiple Comparisons)**: Với 12 quận, có $66$ cặp so sánh. Nếu chạy 66 lần t-test đơn lẻ, xác suất báo động giả vọt lên: $1 - (0.95)^{66} \approx \mathbf{96.6\%}$!
* **Giải pháp**: Dùng **One-Way ANOVA** ($F = \mathbf{368.11}, p < 0.0001$) kết hợp kiểm định hậu nghiệm **Tukey's HSD** kiểm soát chặt chẽ sai số họ.

### Phát Hiện 9 Cặp Quận "Song Sinh Về Giá" ($p_{\text{adj}} > 0.05$):
```
+----------------------------------------------------------------------------------------------------+
| 👑 CỤM ĐỈNH CAO: Cầu Giấy (125.3 tr) - Ba Đình (128.6 tr) - Tây Hồ (123.7 tr)                      |
|    -> Ba Đình vs Cầu Giấy: Chênh 3.29 tr (p = 0.4769 - Không khác biệt)                            |
|    -> Ba Đình vs Tây Hồ:   Chênh 4.83 tr (p = 0.1795 - Không khác biệt)                            |
|    -> Cầu Giấy vs Tây Hồ:  Chênh 1.54 tr (p = 0.9987 - Không khác biệt)                            |
+----------------------------------------------------------------------------------------------------+
| 🏙️ CỤM ĐÔ THỊ ĐỐNG ĐA - THANH XUÂN - HAI BÀ TRƯNG:                                                 |
|    -> Hai Bà Trưng (102.59 tr) vs Thanh Xuân (102.70 tr): Chênh 0.11 tr (p = 1.0000 - Như nhau)    |
+----------------------------------------------------------------------------------------------------+
| 🌳 CỤM VÀNH ĐAI BÌNH DÂN (80 - 85 tr/m²):                                                          |
|    -> Hoàng Mai (83.82 tr) vs Bắc Từ Liêm (83.93 tr): Chênh 0.11 tr (p = 1.0000 - Như nhau)       |
|    -> Hoàng Mai (83.82 tr) vs Hà Đông (80.80 tr):     Chênh 3.02 tr (p = 0.2171 - Như nhau)       |
|    -> Hoàng Mai vs Long Biên (p = 0.983) | Bắc Từ Liêm vs Hà Đông (p = 0.926)                      |
+----------------------------------------------------------------------------------------------------+
```

---

<!-- slide -->
# 🎯 [BIỂU ĐỒ 07] KHOẢNG TIN CẬY 95% (95% CI) CHO ĐƠN GIÁ 12 QUẬN/HUYỆN HÀ NỘI

![Biểu đồ 07: Khoảng tin cậy 95% đơn giá 12 quận huyện](/Users/longnguyen/Documents/bds_khdl/reports/figures/07_confidence_intervals_districts.png)

### 📌 Phân Tích Chuyên Sâu 4 Trọng Tâm:
1. **Biểu đồ gì**: Biểu đồ khoảng tin cậy dạng thanh sai số (95% Confidence Interval Forest / Error Bar Plot), tính toán từ sai số chuẩn ($SE = \frac{s}{\sqrt{n}}$) dựa trên phân phối t-Student ($CI_{95\%} = \bar{x} \pm t_{\alpha/2, df} \times SE$).
2. **Có tác dụng gì**:
   - Chuyển từ thống kê mô tả trên mẫu (Sample) sang suy luận tổng thể (Population Inference): Tuyên bố với độ tin cậy 95% mức giá thật của từng quận ngoài thực tế nằm trong khoảng nào.
   - Kiểm tra trực quan hiện tượng chồng lấn (Overlapping Intervals) để xác minh các quận có cùng mặt bằng giá.
   - Đánh giá độ tin cậy của ước lượng theo quy mô mẫu dữ liệu thu thập ($n$).
3. **Đang biểu diễn thứ gì**:
   - **Trục hoành X**: 12 quận/huyện sắp xếp theo đơn giá trung bình mẫu giảm dần từ trái sang phải.
   - **Trục tung Y**: Đơn giá trung bình (triệu VNĐ/m²).
   - **Điểm tròn trung tâm**: Giá trị trung bình mẫu ($\bar{x}$).
   - **Thanh dọc có hai đầu mút (Error Bar)**: Khoảng tin cậy 95% $[Lower, Upper]$. Dải nền bóng mờ biểu thị vùng chồng lấn giữa các quận lân cận.
4. **Mang lại ý nghĩa gì**:
   - *Độ tin cậy khoa học vững chắc*: Ta tự tin $95\%$ rằng đơn giá trung bình thực sự của toàn bộ thị trường quận Ba Đình nằm trong khoảng $[125.55 - 131.57]$ tr/m², Cầu Giấy trong khoảng $[123.04 - 127.50]$ tr/m².
   - *Minh chứng thị giác cho 9 cặp quận "song sinh giá" (Tukey's HSD)*: Thanh CI của Ba Đình, Cầu Giấy và Tây Hồ gối đè lên nhau gần như hoàn toàn $\rightarrow$ Giải thích tại sao kiểm định ANOVA/Tukey khẳng định 3 quận này không có sự khác biệt có ý nghĩa thống kê về mặt bằng giá.
   - *Cỡ mẫu lớn mang lại độ chuẩn xác cao*: Quận Hoàng Mai có tới $4.880$ tin rao nên thanh CI cực hẹp ($\pm 0.89$ tr/m²), chứng minh kết quả ước lượng đạt độ tin cậy thực tế tuyệt đối.

---

<!-- slide -->
# 🎯 ĐỌC HIỂU OLS ĐA BIẾN & 3 NGHĨA VỤ ĐẠO ĐỨC KHI DIỄN GIẢI HỆ SỐ BETA

Mô hình hồi quy OLS cơ sở đạt $R^2 = \mathbf{0.283}$, $F = \mathbf{1479.0}$ ($p < 0.0001$):

### Bảng Hệ Số Hồi Quy $\beta$ & Tuân Thủ 3 Nghĩa VỤ Đạo Đức:
| Thuộc Tính ($X$) | Hệ Số $\beta$ | Giá Trị $p\text{-value}$ | Diễn Giải Chuẩn Mực Nghiệp Vụ (Ceteris Paribus) |
| :--- | :---: | :---: | :--- |
| `khu_vuc_noi_do` | **$+33.13$** | $< 0.0001$ | Cùng diện tích & số tầng, nhà nội đô **gắn liền với** mức giá cao hơn **$33.13$ tr/m²** |
| `loai_nha_ngo_hem`| **$-33.46$** | $< 0.0001$ | Nhà trong ngõ **gắn liền với** mức chiết khấu giảm **$33.46$ tr/m²** so với mặt phố |
| `loai_nha_mat_pho`| **$+14.77$** | $< 0.0001$ | Nhà mặt phố **gắn liền với** thặng dư thương mại tăng **$14.77$ tr/m²** |
| `Số phòng ngủ` | **$+5.86$** | $< 0.0001$ | Mỗi phòng ngủ bố trí thêm **gắn liền với** mức tăng **$5.86$ tr/m²** |
| `Số tầng` | **$+2.45$** | $< 0.0001$ | Mỗi tầng xây dựng thêm **gắn liền với** mức tăng **$2.45$ tr/m²** |
| `mat_tien_m` | **$+1.94$** | $< 0.0001$ | Mỗi mét mặt tiền mở rộng **gắn liền với** mức tăng **$1.94$ tr/m²** |
| `chieu_sau_m` | $-0.04$ | **$0.7080$** | ⚠️ Không có ý nghĩa thống kê ($p > 0.05$), biến dư thừa gây nhiễu |

* **3 Nghĩa Vụ Bắt Buộc**: (1) Dùng từ *"gắn liền với/đi kèm với"*, không dùng từ "gây ra"; (2) Khẳng định điều kiện giữ nguyên các biến khác trong mô hình; (3) Giới hạn trong phạm vi dữ liệu quan sát.

---

<!-- slide -->
# 🎯 [BIỂU ĐỒ 08] BỘ CHẨN ĐOÁN 4 GIẢ ĐỊNH LINE CỦA HỒI QUY KINH TẾ LƯỢNG

![Biểu đồ 08: Bộ chẩn đoán 4 giả định LINE](/Users/longnguyen/Documents/bds_khdl/reports/figures/08_line_assumptions_diagnostics.png)

### 📌 Phân Tích Chuyên Sâu 4 Trọng Tâm:
1. **Biểu đồ gì**: Tổ hợp ma trận 4 biểu đồ chẩn đoán vi phạm hồi quy kinh tế lượng (4-in-1 LINE Regression Diagnostic Matrix):
   - Đồ thị 1 (Góc trên trái): Phần dư theo giá trị dự báo (Residuals vs Fitted Values).
   - Đồ thị 2 (Góc trên phải): Đồ thị xác suất chuẩn (Normal Q-Q Plot) của mô hình OLS thô.
   - Đồ thị 3 (Góc dưới trái): Đồ thị Normal Q-Q Plot sau biến đổi Logarit $y' = \ln(y)$.
   - Đồ thị 4 (Góc dưới phải): Biểu đồ phân phối phần dư (Residual Density Distribution) trước vs sau Log.
2. **Có tác dụng gì**:
   - Kiểm tra 4 điều kiện cốt tử để mô hình hồi quy OLS có hiệu lực học thuật (LINE: Linearity, Independence, Normality, Equal Variance).
   - Phát hiện các căn bệnh vi phạm: Phương sai thay đổi hình phễu (Heteroscedasticity) và Phân phối đuôi dày ngoại lai (Heavy Tails).
   - Cung cấp bằng chứng thực nghiệm trực quan về sức mạnh của biến đổi Logarit trong việc khôi phục tính chuẩn xác của mô hình.
3. **Đang biểu diễn thứ gì**:
   - **Góc trên trái**: Trục X là Giá trị dự báo $\hat{y}$; Trục Y là Phần dư $e = y - \hat{y}$. Đường chấm ngang $y=0$ và đường cong trơn Lowess đỏ. Đám mây điểm xòe rộng thành hình phễu rõ nét khi giá trị dự báo tăng cao.
   - **Góc trên phải**: Q-Q Plot mô hình gốc với các điểm dữ liệu uốn cong vểnh lên trời ở hai đầu đuôi, lệch xa đường chéo đỏ $45^\circ$.
   - **Góc dưới trái**: Q-Q Plot sau Log với các điểm xanh bám khít $100\%$ vào đường thẳng đỏ $45^\circ$ từ $-3$ đến $+3$.
   - **Góc dưới phải**: Đường cong mật độ phần dư đỏ (gốc, lệch phải nhọn hoắt) so với đường cong xanh (sau Log, đối xứng chuẩn hình chuông Gauss).
4. **Mang lại ý nghĩa gì**:
   - *Vạch trần sai phạm của mô hình OLS gốc*: Kiểm định Breusch-Pagan cho $BP = \mathbf{4417.73}$ ($p < 0.0001$), khẳng định mô hình gốc vi phạm nghiêm trọng giả định Homoscedasticity (nhà rẻ tiền sai số $\pm 15$ triệu, nhưng nhà đắt tiền sai số vọt lên $\pm 200$ triệu).
   - *Sự kỳ diệu của Logarit*: Nắn Skewness phần dư từ $+2.18$ về **$-0.29$** (đối xứng lý tưởng); giảm Kurtosis từ $10.79$ về **$3.72$** (sát mức chuẩn $3.0$); giảm MAE từ $29.90$ xuống $28.35$ tr/m².
   - *Ý nghĩa pháp lý*: Bảo vệ tính hợp lệ của các kiểm định $t$ và $F$, đảm bảo kết quả định giá có căn cứ khoa học vững chắc.

---

<!-- slide -->
# 🎯 HIỆU QUẢ ĐỘT PHÁ SAU BIẾN ĐỔI LOGARIT: NẮN CHUẨN PHẦN DƯ TUYỆT ĐỐI

Do giá trị BĐS có phân phối lệch phải tự nhiên, áp dụng phép biến đổi: $y' = \ln(\text{Giá\_m2\_trieu})$ kéo co các giá trị cực lớn ở đuôi phải lại gần trung tâm.

### Minh Chứng Hiệu Quả Qua Đồ Thị 3 & 4 (Biểu Đồ 08):
* **Độ lệch phần dư (Skewness)**: Giảm từ $+2.18$ về **$-0.29$** (gần như đối xứng hoàn hảo)!
* **Độ nhọn phần dư (Kurtosis)**: Giảm từ $10.79$ về **$3.72$** (áp sát mức chuẩn $3.0$ của phân phối Gaussian).
* **Đường Q-Q plot sau Log (Góc dưới trái)**: **Bám khít 100% vào đường thẳng chéo 45 độ màu đỏ** từ cận dưới $-3$ đến cận trên $+3$, hiện tượng vểnh đuôi cong biến mất hoàn toàn!
* **Sai số MAE trên tập test**: Giảm từ $29.90$ xuống **$28.35 \text{ triệu/m²}$**.

### 💡 Diễn Giải Hệ Số Mô Hình Log-Linear Cho Nhà Đầu Tư:
Hệ số $\beta$ phản ánh tỷ lệ thay đổi phần trăm tương đối: $\% \Delta y \approx (e^\beta - 1) \times 100\%$:
* Căn nhà nằm trong 7 quận nội đô có đơn giá cao hơn khoảng $(e^{0.334} - 1) \times 100\% \approx \mathbf{39.7\%}$ so với căn nhà tương đương ở ngoại thành.
* Căn nhà trong ngõ hẻm bị chiết khấu giá thấp hơn khoảng $(1 - e^{-0.366}) \times 100\% \approx \mathbf{30.6\%}$ so với nhà mặt phố.

---

<!-- slide -->
# 🎯 [BIỂU ĐỒ 09] KỸ THUẬT ĐIỀU CHUẨN: LASSO L1 TỰ ĐỘNG TRIỆT TIÊU BIẾN RÁC VỀ 0

![Biểu đồ 09: Kỹ thuật điều chuẩn Ridge vs Lasso](/Users/longnguyen/Documents/bds_khdl/reports/figures/09_regularization_lasso_vs_ridge.png)

### 📌 Phân Tích Chuyên Sâu 4 Trọng Tâm:
1. **Biểu đồ gì**: Biểu đồ cột nhóm so sánh trọng số hồi quy chuẩn hóa (Multi-Model Regularization Coefficient Comparison Bar Chart) giữa 3 phương pháp: OLS cổ điển, Hồi quy sườn Ridge ($L_2$) và Hồi quy dây thòng lọng Lasso ($L_1$).
2. **Có tác dụng gì**:
   - Khắc phục triệt để vấn đề Đa cộng tuyến (Multicollinearity) giữa các biến hình học thửa đất (Diện tích đất vs Tổng diện tích sàn $r = 0.88$).
   - Minh chứng tính năng thưa hóa (Sparsity) và chọn lọc biến số tự động (Automatic Feature Selection) của hình học hàm phạt $L_1$.
   - Giúp kỹ sư dữ liệu loại bỏ các thuộc tính gây nhiễu, làm tinh giản mô hình để triển khai trên các hệ thống microservices tốc độ cao.
3. **Đang biểu diễn thứ gì**:
   - **Trục hoành X**: 8 đặc trưng cốt lõi (`khu_vuc_noi_do`, `loai_nha_ngo_hem`, `loai_nha_mat_pho`, `tong_dien_tich_san_m2`, `mat_tien_m`, `Số phòng ngủ`, `Dien_tich_m2`, `chieu_sau_m`).
   - **Trục tung Y**: Độ lớn hệ số hồi quy chuẩn hóa ($\beta$).
   - **3 cột màu sắc tại mỗi đặc trưng**: Cột xám (OLS thông thường), Cột xanh lam (Ridge $L_2$ với $\alpha = 4.2813$), Cột đỏ cam (Lasso $L_1$ với $\alpha = 0.3556$).
4. **Mang lại ý nghĩa gì**:
   - *Bản chất của Ridge ($L_2$)*: Phạt bình phương tổng hệ số ($\alpha \sum \beta^2$). Ridge co đều tất cả các hệ số nhỏ lại để giảm phương sai, nhưng KHÔNG CÓ biến nào bị loại bỏ hoàn toàn (không có hệ số nào bằng 0).
   - *Đột phá của Lasso ($L_1$)*: Phạt trị tuyệt đối tổng hệ số ($\alpha \sum |\beta|$). Nhờ cấu trúc hình học có các góc nhọn tiếp xúc với trục tọa độ, Lasso đã **tự động triệt tiêu hệ số của 2 biến `Dien_tich_m2` ($0.000$) và `chieu_sau_m` ($0.000$) về đúng số 0**!
   - *Giải thích kinh tế*: Khi mô hình đã sở hữu biến `tong_dien_tich_san_m2` (phản ánh toàn bộ công năng sàn ở thực) và biến `mat_tien_m` (phản ánh giá trị tiếp giáp thương mại), thì biến `Dien_tich_m2` và `chieu_sau_m` trở nên thừa thãi. Lasso đã thông minh "gạt bỏ" hai biến này khỏi phương trình định giá, giúp mô hình gọn gàng hơn mà độ chính xác không hề suy giảm.
---

<!-- slide -->
# 🎯 7 KẾT LUẬN THỰC TIỄN RÚT RA TỪ DỮ LIỆU THỰC TẾ THỊ TRƯỜNG

```
+----------------------------------------------------------------------------------------------------+
| 7 KẾT LUẬN THỰC TIỄN QUAN TRỌNG NHẤT DỰ ÁN                                                         |
+----------------------------------------------------------------------------------------------------+
| 1. VỊ TRÍ LÀ SỐ 1: Vị trí nội đô chi phối > 36% giá trị, đẩy đơn giá cao hơn 32.04 triệu/m² (+39%)  |
| 2. TAM GIÁC VÀNG ĐỒNG GIÁ: Cầu Giấy (125 tr), Ba Đình (128 tr), Tây Hồ (123 tr) tương đồng giá      |
| 3. PHÂN PHỐI LỆCH PHẢI LÀ TỰ NHIÊN: Lọc miền tri thức [10, 500] tr/m² cứu sống nhóm nhà cao cấp    |
| 4. GIÁ TRỊ THỰC CỦA MẶT TIỀN: Mỗi mét mặt tiền mở rộng giúp tăng trung bình ~1.94 triệu/m² đơn giá |
| 5. OLS VI PHẠM PHƯƠNG SAI ĐỒNG NHẤT: Mô hình tuyến tính đơn giản bị lỗi hình phễu ở phân khúc sang  |
| 6. BIẾN ĐỔI LOGARIT LÀ CHÌA KHÓA: Nắn chuẩn phần dư Skewness về -0.29, giảm MAE về 28.35 triệu    |
| 7. GRADIENT BOOSTING VÔ ĐỊCH: Xử lý xuất sắc tương tác phi tuyến, đạt MAE = 26.07 triệu/m²         |
+----------------------------------------------------------------------------------------------------+
```

> [!WARNING]
> **Ranh giới thực tế**: Mô hình đạt $R^2 \approx 44\%$, sai số $\pm 26$ triệu/m² $\rightarrow$ Đóng vai trò là **Công cụ tham chiếu sơ bộ (Price Guidance)**; người mua nhà cần trừ hao biên độ thương lượng từ $5\% - 10\%$ so với giá chào bán niêm yết trực tuyến.

---

<!-- slide -->
# 🎯 LỘ TRÌNH HOÀN THIỆN CUỐI KỲ (TUẦN 11 - 12) & SẴN SÀNG TRẢ LỜI CÂU HỎI

### Kế Hoạch Triển Khai Cho Tuần 11 & Tuần 12:
* **Tuần 11: Mô Hình Nâng Cao & Trí Tuệ Nhân Tạo Có Thể Giải Thích (XAI)**:
  - Huấn luyện mô hình tối tân **XGBoost** và **LightGBM** kết hợp K-Fold Cross-Validation để đẩy $R^2 > 0.50$.
  - Tích hợp thư viện **SHAP (Shapley Additive exPlanations)**: Vẽ biểu đồ thác nước (Waterfall plot) giải thích tường minh: *Tại sao căn nhà này được AI định giá 5 Tỷ (Cộng bao nhiêu vì ở Cầu Giấy, trừ bao nhiêu vì ngõ hẹp)*.
  - Bài toán phân loại: Tự động gắn nhãn 5 phân khúc giá tài sản.
* **Tuần 12: Đạo Đức Dữ Liệu, Hoàn Thiện & Nghiệm Thu**:
  - Xây dựng tài liệu chuẩn mực quốc tế **Datasheets for Datasets** và **Model Card**.
  - Kiểm toán độ lệch định kiến vùng miền (Fairness Audit).
  - Đóng gói hoàn thiện mã nguồn và báo cáo nghiệm thu cuối kỳ.

---

### 🎉 XIN TRÂN TRỌNG CẢM ƠN THẦY CÔ VÀ HỘI ĐỒNG ĐÃ LẮNG NGHE!
*Nhóm sẵn sàng tiếp thu các câu hỏi phản biện và đóng góp ý kiến (Q&A).*
