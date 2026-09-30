# 🏙️ BẢN THIẾT KẾ KIẾN TRÚC TỔNG THỂ (MASTER BLUEPRINT)
**Dự án: Hệ thống Phân tích Không gian và Dự đoán Giá Bất động sản tại Hà Nội**

*(Tài liệu này đóng vai trò là "Bản vẽ kỹ thuật" chi tiết nhất, bóc tách toàn bộ các thành phần của hệ thống từ Database, luồng Dữ liệu, thuật toán ML cho đến Kiến trúc Web để đội ngũ bám sát định dạng trong quá trình phát triển).*

---

## 🏗️ 1. KIẾN TRÚC HỆ THỐNG PHẦN MỀM (SYSTEM ARCHITECTURE)
Hệ thống được thiết kế theo mô hình **Microservices Phân tán**, đảm bảo việc xử lý dữ liệu nặng (ML) không làm sập giao diện người dùng (Frontend).

### 1.1. Tầng Cơ sở dữ liệu (Database Layer)
*   **Công nghệ:** Supabase (PostgreSQL).
*   **Lõi mở rộng:** Cài đặt thêm Extension **PostGIS**.
*   **Chức năng chuyên sâu:** PostGIS cho phép lưu tọa độ dưới định dạng không gian (Geometry Point). Thay vì query `SELECT * FROM bds WHERE district='Cau Giay'`, hệ thống có thể query không gian phức tạp: *"Lấy tất cả căn hộ nằm trong bán kính 2km từ Hồ Gươm"* vô cùng nhanh chóng.

### 1.2. Tầng Trí tuệ Nhân tạo (Machine Learning Layer)
*   **Công nghệ:** Google Colab (Môi trường phát triển) + Scikit-Learn / XGBoost (Thư viện lõi).
*   **Chức năng chuyên sâu:** Nơi kỹ sư dữ liệu load dữ liệu từ DB, chạy thực nghiệm (Experiments), huấn luyện mô hình. Mô hình tốt nhất sẽ được xuất ra file nhị phân nén dạng `model.pkl` hoặc `model.joblib`.

### 1.3. Tầng Xử lý Logic (Backend API Layer)
*   **Công nghệ:** Python **FastAPI** (Triển khai trên Cloud Render / Railway).
*   **Chức năng chuyên sâu:** Là cầu nối trung gian. Nó chứa file `model.pkl`. 
*   **Thiết kế API Endpoints (Giao thức giao tiếp):**
    *   `GET /api/v1/map-data`: Trả về tọa độ hàng ngàn căn nhà để Frontend vẽ lên bản đồ.
    *   `GET /api/v1/stats`: Trả về dữ liệu thống kê (giá trung bình, số lượng) khi user click vào một quận.
    *   `POST /api/v1/predict`: Nhận cục payload (Ví dụ: `{dien_tich: 70, quan: "Cầu Giấy", so_tang: 10}`), đưa vào mô hình ML và trả về số tiền dự đoán `2.5 tỷ`.

### 1.4. Tầng Giao diện Người dùng (Frontend Layer)
*   **Công nghệ:** ReactJS (TypeScript) + TailwindCSS + Leaflet Map (Triển khai trên Vercel).
*   **Chức năng chuyên sâu:** Nhận dữ liệu từ Backend và render lên màn hình. Leaflet Map chịu trách nhiệm vẽ các điểm màu (Heatmap) theo tọa độ. TailwindCSS chịu trách nhiệm thiết kế giao diện Glassmorphism hiện đại, mượt mà.

---

## 🗄️ 2. LUỒNG DỮ LIỆU & FEATURE ENGINEERING (DATA PIPELINE)
Tuân thủ mô hình chuẩn **Medallion Architecture** (Bronze $\rightarrow$ Silver $\rightarrow$ Gold) để dữ liệu không bao giờ bị rác.

### 2.1. Bronze Layer (Dữ liệu thô - Raw Data)
*   Web Scraping thu về file `raw.csv`. Dữ liệu cực bẩn, sai chính tả, chứa HTML tags. Tuyệt đối không phân tích trên tập này.

### 2.2. Silver Layer (Dữ liệu đã gột rửa - Processed Data)
*   Thực thi luồng làm sạch tự động (như file `pipeline_hanoi.py`).
*   Khử nhiễu, điền missing values, ép kiểu số, gọt rác Unicode.

### 2.3. Gold Layer (Dữ liệu Đặc trưng - Feature Engineered Data)
Đây là giai đoạn "chế biến" tạo ra giá trị gia tăng cao nhất cho mô hình AI:
*   **Tính toán tọa độ (Geocoding):** Gửi tên đường/quận lên Google API để lấy Kinh độ/Vĩ độ.
*   **Đặc trưng khoảng cách (Distance Features):** Dùng công thức Haversine tính toán khoảng cách đường chim bay từ căn nhà đến: `Trung_tam_Ho_Guom`, `Ben_tau_Metro`, `Dai_hoc_Quoc_Gia`.
*   **Đặc trưng thống kê chéo (Target Encoding):** Tạo ra các cột như `Gia_Trung_Binh_Cua_Quan_Do`, `Gia_Trung_Binh_Cua_Khu_Do_Thi_Do` giúp mô hình AI có một hệ quy chiếu "giá nền" của khu vực.

---

## 🤖 3. CHIẾN LƯỢC HUẤN LUYỆN MÔ HÌNH (ML BLUEPRINT)
*   **Bài toán:** Hồi quy (Regression) - Dự đoán một con số liên tục (Giá tiền).
*   **Thuật toán thi đấu:** 
    1. *Linear Regression:* Dùng làm Baseline (Mức chuẩn cơ sở).
    2. *Random Forest:* Bắt đầu học được các quy luật phi tuyến tính.
    3. *XGBoost / LightGBM:* "Trùm cuối" cho dữ liệu bảng (Tabular Data). Xử lý cực tốt các biến phân loại (Categorical) như tên Quận, tên Phường, tên Khu Đô Thị.
*   **Đánh giá mô hình (Metrics):**
    *   **RMSE (Root Mean Square Error):** Phạt nặng các dự đoán sai lệch quá lớn.
    *   **MAE (Mean Absolute Error):** Cho biết trung bình mô hình dự đoán lệch bao nhiêu tiền (Ví dụ: Lệch 150 triệu VNĐ/căn).
    *   **R² (R-Squared):** Đo lường xem mô hình giải thích được bao nhiêu % sự biến động của thị trường.
*   **Giải Thích Mô Hình (XAI - Explainable AI):** Không được thiết kế theo kiểu "Hộp đen" (Blackbox). Bắt buộc phải tích hợp thư viện **SHAP**. Khi AI phán căn nhà giá 3 Tỷ, SHAP phải bóc tách được: Khởi điểm là 2 Tỷ, cộng thêm 800 triệu vì có nội thất, cộng thêm 200 triệu vì nằm gần bến Metro.

---

## 📁 4. CẤU TRÚC THƯ MỤC CHUẨN (REPOSITORY FORMAT)
Dự án phải tuân thủ nghiêm ngặt cấu trúc cây thư mục sau đây để đảm bảo tính chuyên nghiệp và dễ bảo trì:

```text
hanoi-realestate-analytics/
│
├── data/                   # Nơi chứa toàn bộ dữ liệu (Tuyệt đối không push lên Github)
│   ├── raw/                # Dữ liệu cào nguyên bản (Bronze)
│   ├── processed/          # Dữ liệu đã làm sạch (Silver)
│   └── feature/            # Dữ liệu đã thêm tọa độ, khoảng cách (Gold)
│
├── notebooks/              # Các file Jupyter (.ipynb) để thử nghiệm
│   ├── 01_data_audit.ipynb
│   ├── 02_eda_spatial.ipynb
│   └── 03_model_training.ipynb
│
├── src/                    # Mã nguồn chính của luồng xử lý
│   ├── data_cleaning/      # Chứa pipeline_hanoi.py
│   ├── feature_engineering/
│   └── models/             # Chứa code train và file model.pkl
│
├── backend/                # Source code của API Server (FastAPI)
│   ├── main.py
│   └── routers/
│
├── frontend/               # Source code của giao diện Web (React)
│   ├── components/         # Các mảnh ghép UI (Map, Charts)
│   └── pages/
│
├── requirements.txt        # Danh sách thư viện Python (Pandas, Sklearn, FastAPI...)
└── README.md               # Bản thiết kế tổng thể (Chính là file này)
```

---

## 🛤️ 5. LỘ TRÌNH THỰC THI CHI TIẾT (MILESTONES)

*   **Milestone 1 (Data Foundation):** Hoàn thiện 100% việc cào dữ liệu, chạy qua Pipeline làm sạch (file `pipeline_hanoi.py`), lưu vào CSDL Supabase.
*   **Milestone 2 (Geospatial & EDA):** Chạy API lấy tọa độ cho toàn bộ dữ liệu. Thực hiện vẽ biểu đồ Heatmap đầu tiên trên Jupyter Notebook để thấy luồng nhiệt giá đất Hà Nội.
*   **Milestone 3 (AI Core):** Xây dựng các đặc trưng khoảng cách. Bỏ dữ liệu vào huấn luyện XGBoost. Chốt được mô hình có MAE thấp nhất và xuất file `model.pkl`.
*   **Milestone 4 (Backend API):** Code FastAPI load `model.pkl`. Test API bằng Postman đảm bảo gửi request lên lấy được giá trả về dưới 1 giây.
*   **Milestone 5 (Frontend Map):** Code ReactJS, tích hợp Leaflet vẽ bản đồ. Gắn thanh Filter (lọc theo quận, giá). 
*   **Milestone 6 (Integration & Release):** Ghép Frontend gọi API Backend. Hoàn thiện bảng Dashboard Thống kê và Form Dự đoán Giá có giải thích SHAP. Deploy lên mạng Internet.
