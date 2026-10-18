# 🏙️ HỆ THỐNG PHÂN TÍCH KHÔNG GIAN & DỰ ĐOÁN GIÁ BẤT ĐỘNG SẢN HÀ NỘI
> **Học phần:** Khoa Học Dữ Liệu (INFO3020)  
> **Quy mô dữ liệu:** 99.998 tin rao thu thập $\rightarrow$ 37.402 bất động sản chuẩn hóa 18 tháng gần nhất (2025 - 2026)  
> **Mô hình vô địch:** Gradient Boosting Regressor ($R^2 = 0.4390$, $\text{MAE} = 26.07\text{ triệu/m}^2$)

---

## 📌 1. TỔNG QUAN DỰ ÁN
Dự án tập trung giải quyết bài toán **bất đối xứng thông tin** và **định giá bất động sản tự động (Automated Valuation Model - AVM)** trên địa bàn Thủ đô Hà Nội. Thông qua quy trình Khoa học Dữ liệu chuẩn mực từ Tuần 1 đến Tuần 10, dự án đã:
1. **Thu thập & Chuẩn hóa dữ liệu lớn**: Xử lý 99.998 tin rao thô từ các nền tảng BĐS uy tín, sàng lọc qua phễu kỹ thuật 6 bước để giữ lại 37.402 bản ghi sạch đại diện cho 12 quận/huyện trọng điểm.
2. **Kỹ nghệ đặc trưng đa chiều**: Mở rộng từ 12 trường dữ liệu ban đầu thành 38 biến phái sinh sâu sắc (tỷ lệ mặt tiền/chiều sâu, tổng diện tích sàn, cờ thương mại, khoảng cách tâm hồ Hoàn Kiếm, phân vùng quy hoạch).
3. **Phân tích khám phá (EDA) & Trực quan hóa**: Xây dựng 9 biểu đồ chuyên sâu bóc tách phân phối lệch phải (Log-normal), ma trận tương quan đa biến, phân tầng giá 12 quận và hiện tượng phương sai hình phễu.
4. **Thống kê suy luận (Inferential Statistics)**: 
   - Kiểm định **Welch's t-test** khẳng định giá Nội đô đắt hơn Ngoại thành $32.04\text{ tr/m}^2$ ($+39.0\%$, $p < 10^{-16}$, Cohen's $d = 0.610$).
   - Phân tích phương sai **One-Way ANOVA** ($F = 368.11$) kết hợp kiểm định hậu nghiệm **Tukey's HSD** phát hiện **9 cặp quận "song sinh giá"** (điển hình: Cầu Giấy = Ba Đình = Tây Hồ với $p > 0.05$).
   - Ước lượng **Khoảng tin cậy 95% (95% CI)** cho đơn giá kỳ vọng của từng địa bàn.
5. **Chẩn đoán hồi quy LINE & Điều chuẩn**:
   - Vạch trần vi phạm phương sai đồng nhất của OLS gốc qua kiểm định Breusch-Pagan ($BP = 4.417,73$, $p < 0.0001$).
   - Biến đổi $\log(y)$ nắn chuẩn hoàn hảo phần dư (Skewness từ $+2.18 \rightarrow -0.29$, Kurtosis từ $10.79 \rightarrow 3.72$, giảm sai số MAE xuống $28.35\text{ tr/m}^2$).
   - Điều chuẩn **Lasso L1** minh chứng tính năng thưa hóa (Sparsity), tự động triệt tiêu các biến diện tích đất và chiều sâu thừa thãi về đúng $0.000$.
6. **Mô hình học máy & Đóng gói Pipeline**: Huấn luyện đối đầu 5 mô hình (Linear, Ridge, Lasso, Random Forest, Gradient Boosting). Gradient Boosting đạt quán quân hiệu năng và được đóng gói thành Scikit-Learn Pipeline hoàn chỉnh.

---

## 📁 2. CẤU TRÚC THƯ MỤC CHUẨN MỰC
Toàn bộ dự án tuân thủ nghiêm ngặt nguyên tắc **Dữ liệu thô bất biến (Raw-Immutable Rule)** và tính tái lập 100% (Reproducibility):

```text
bds_khdl/
├── README.md                          # Bản tài liệu kỹ thuật tổng thể (file này)
├── KIENTHUC_TONG_QUAN.md              # Khung lý thuyết & đề cương học phần INFO3020
├── BAO_CAO_TIEN_DO_KHDL.md            # Báo cáo tiến độ chi tiết dạng Markdown (Tuần 1 - 10)
├── BAO_CAO_TIEN_DO_KHDL.docx          # Báo cáo tiến độ chuẩn Word nộp bài (đầy đủ bảng & biểu đồ)
├── BAO_CAO_TIEN_DO_SLIDES.md          # Kịch bản trình chiếu Slide thuyết trình
├── BAO_CAO_TIEN_DO_SLIDES.pptx        # Bộ Slide thuyết trình Microsoft PowerPoint chuyên nghiệp
├── house_price_model.pkl              # Pipeline Gradient Boosting tốt nhất đã được huấn luyện
│
├── data/
│   ├── raw/raw.csv                    # Dữ liệu gốc thu thập ban đầu (99.998 dòng - Bất biến)
│   └── processed/clean.csv            # Dữ liệu sạch sau lọc chu kỳ & outlier (37.402 dòng)
│
├── notebooks/
│   └── bds_khdl_eda_modeling.ipynb    # Jupyter Notebook thực nghiệm từ Tiền xử lý đến Mô hình hóa
│
├── reports/figures/                   # 9 biểu đồ phân giải cao phục vụ báo cáo và thuyết trình
│   ├── 01_correlation_heatmap.png     # Ma trận tương quan đa biến Pearson
│   ├── 02_price_distribution.png      # Phân phối tần suất kép Đơn giá & Tổng giá (KDE)
│   ├── 03_price_vs_area_scatter.png   # Tương quan phân tán Diện tích & Mặt tiền vs Giá bán
│   ├── 04_price_by_district_boxplot.png # Biểu đồ hộp đơn giá 12 quận xếp theo Trung vị
│   ├── 05_model_comparison.png        # So sánh hiệu năng đối đầu 4 mô hình học máy
│   ├── 06_feature_importance.png      # Top 10 đặc trưng chi phối giá trích xuất từ GBDT
│   ├── 07_confidence_intervals_districts.png # Khoảng tin cậy 95% (95% CI) cho 12 quận/huyện
│   ├── 08_line_assumptions_diagnostics.png   # Bộ tứ chẩn đoán 4 giả định hồi quy LINE
│   └── 09_regularization_lasso_vs_ridge.png  # So sánh trọng số điều chuẩn OLS vs Ridge vs Lasso
│
├── src/                               # Toàn bộ mã nguồn thực thi đang hoạt động
│   ├── pipeline_hanoi.py              # Custom Scikit-Learn Transformers & Pipeline tiền xử lý
│   ├── run_pipeline_eda_modeling.py   # Thực thi Tuần 5 - 8: Làm sạch, EDA, vẽ hình 1-6, train ML
│   ├── run_week9_week10.py            # Thực thi Tuần 9 - 10: Thống kê suy luận, LINE, hình 7-9
│   ├── export_report_docx.py          # Script tự động tạo báo cáo Word hoàn chỉnh
│   └── export_slides_pptx.py          # Script tự động tạo Slide PowerPoint trình chiếu
│
└── archive/                           # Thư mục lưu trữ mã nguồn cào dữ liệu cũ
    ├── README.md                      # Ghi chú minh chứng thu thập dữ liệu Tuần 1 - 3
    └── crawlers/                      # Các script cào web thô ban đầu
```

---

## ⚙️ 3. CÀI ĐẶT MÔI TRƯỜNG & HƯỚNG DẪN THỰC THI

### 3.1. Kích hoạt môi trường ảo
```bash
# Kích hoạt virtualenv (đã tích hợp đầy đủ thư viện trong repo)
source venv/bin/activate
```

### 3.2. Chạy toàn bộ luồng xử lý và mô hình hóa
```bash
# 1. Chạy tiền xử lý dữ liệu, phân tích EDA và huấn luyện 5 mô hình ML (Tuần 5 - 8)
python src/run_pipeline_eda_modeling.py

# 2. Chạy thống kê suy luận, kiểm định Welch t-test, ANOVA, LINE diagnostics & Lasso (Tuần 9 - 10)
python src/run_week9_week10.py

# 3. Xuất báo cáo Word (.docx) và Slide PowerPoint (.pptx)
python src/export_report_docx.py
python src/export_slides_pptx.py
```

---

## 🏆 4. BẢNG HIỆU NĂNG MÔ HÌNH HỌC MÁY (TEST SET: 7.481 BẢN GHI)

| Thuật Toán | $R^2$ Score | MAE (Sai số tuyệt đối) | RMSE | Đánh Giá Thực Tiễn |
| :--- | :---: | :---: | :---: | :--- |
| **Linear Regression (Baseline)** | 0.3644 | 28.47 tr/m² | 44.13 tr/m² | Chuẩn cơ sở, chưa nắm bắt tương tác phi tuyến |
| **Ridge Regression (L2)** | 0.3621 | 28.47 tr/m² | 44.21 tr/m² | Ổn định trọng số, khắc phục đa cộng tuyến |
| **Lasso Regression (L1)** | 0.3638 | 28.43 tr/m² | 44.17 tr/m² | Triệt tiêu các biến diện tích/chiều sâu thừa về $0.000$ |
| **Random Forest (50 cây)** | 0.4284 | 26.17 tr/m² | 41.85 tr/m² | Bắt tương tác phi tuyến tốt, giảm 8.1% sai số |
| **Gradient Boosting (Champion)** | **0.4390** | **26.07 tr/m²** | **41.46 tr/m²** | **QUÁN QUÂN HIỆU NĂNG**: Sai số thấp nhất, tổng thể tối ưu |

---

## 💡 5. CÁC PHÁT HIỆN THỰC TIỄN NỔI BẬT DÀNH CHO THỊ TRƯỜNG
1. **Quy luật "Vị trí là số 1"**: Cờ nội đô tương quan dương cao nhất ($r = +0.283$), vị trí ngõ hẻm tương quan âm mạnh nhất ($r = -0.279$). Cự ly gần trung tâm chi phối $>36\%$ quyết định định giá của AI.
2. **Bước nhảy thương mại mặt tiền**: Mặt tiền $\ge 4\text{m}$ kết hợp đường rộng tạo bước nhảy vọt về đơn giá, kéo đường xu hướng OLS từ $88\text{ tr/m}^2$ lên $170\text{ tr/m}^2$.
3. **Phân tầng giá 3 lớp rõ nét**:
   - *Tầng 1 (Lõi di sản)*: Cầu Giấy ($105\text{ tr}$), Ba Đình ($104\text{ tr}$), Tây Hồ ($101.9\text{ tr}$), Đống Đa ($100\text{ tr/m}^2$).
   - *Tầng 2 (Đô thị mở rộng)*: Thanh Xuân ($92.5\text{ tr}$), Hai Bà Trưng ($89.7\text{ tr}$), Nam Từ Liêm ($85.7\text{ tr/m}^2$).
   - *Tầng 3 (Ven đô & Ngoại thành)*: Bắc Từ Liêm, Hoàng Mai, Long Biên, Hà Đông, Thanh Trì ($60 - 80\text{ tr/m}^2$).
4. **Cặp quận "song sinh giá"**: Kiểm định Tukey HSD chứng minh không có sự khác biệt thống kê ($p > 0.05$) giữa Ba Đình, Cầu Giấy và Tây Hồ $\rightarrow$ Người mua nhà có thể cân nhắc chuyển đổi tương đương giữa 3 quận này.
5. **Cứu cánh từ phép biến đổi Logarit**: Mô hình OLS với biến mục tiêu thô vi phạm nghiêm trọng giả định hồi quy (Breusch-Pagan $p < 0.0001$). Việc áp dụng $\log(y)$ đã nắn độ lệch Skewness từ $+2.18$ về $-0.29$ và độ nhọn Kurtosis từ $10.79$ về $3.72$, đảm bảo tính hợp lệ kinh tế lượng.
