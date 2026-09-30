# TÀI LIỆU BÁO CÁO CHI TIẾT QUY TRÌNH TIỀN XỬ LÝ DỮ LIỆU BẤT ĐỘNG SẢN

Tài liệu này là Báo cáo Kỹ thuật (Technical Report) trình bày cặn kẽ và chuyên sâu về các hành động, phương pháp và chiến lược đã được thực thi để biến đổi bộ dữ liệu thô (Raw Data) thành một bộ dữ liệu sạch hoàn toàn (Clean Data). 

---

## 1. Bối Cảnh và Mục Tiêu
*   **Đầu vào:** Bộ dữ liệu cào từ các nền tảng rao vặt bất động sản (`raw.csv`). Dữ liệu ban đầu mang rất nhiều lỗi đặc trưng của người dùng nhập liệu tay (sai chính tả, dính chữ vào số, bỏ trống thông tin, hoặc rao giá ảo).
*   **Mục tiêu:** Xử lý triệt để các rác thải dữ liệu, đồng nhất định dạng và đóng gói toàn bộ quy trình thành một luồng tự động (Pipeline). Dữ liệu đầu ra phải đảm bảo tính trung thực và chuẩn mực cao nhất để phục vụ cho các báo cáo phân tích thống kê chuyên sâu.

---

## 2. Phân Tích Cặn Kẽ Các Hành Động Đã Thực Thi (Theo Trình Tự)

Quy trình làm sạch được thực thi nghiêm ngặt qua 6 phân đoạn sau:

### Phân đoạn 1: Khởi tạo và Khám bệnh Dữ liệu (Data Audit)
Trước khi tiến hành can thiệp vào cấu trúc bảng, hệ thống thực hiện một bước "kiểm toán" toàn diện để chẩn đoán mức độ nhiễu của dữ liệu.
*   **Chi tiết hành động thực thi:**
    1. **Quét kích thước ma trận:** Hệ thống đọc file `.csv` và đo lường chính xác tổng số dòng (số lượng bản ghi) và số cột (số lượng thuộc tính).
    2. **Phân tích Kiểu dữ liệu (Dtypes):** Kiểm tra xem hệ thống phân tích đang nhận diện từng cột là Chữ (Object) hay Số (Float/Int). (Tại bước này đã phát hiện cột "Giá" đang bị nhận nhầm là chữ do chứa ký tự).
    3. **Thống kê Lỗ hổng (Missing values):** Quét qua toàn bộ các ô, đếm chính xác số lượng ô chứa giá trị `NaN` (trống) tại từng cột để lên phương án xử lý (Cột nào trống nhiều, cột nào trống ít).
    4. **Dò tìm Bản sao (Duplicates):** Quét toàn ma trận để tìm ra số lượng các bản ghi giống hệt nhau 100% ở mọi cột.

### Phân đoạn 2: Dọn dẹp Cơ bản Cấu trúc Bảng
Nhằm làm nhẹ bộ nhớ và ngăn chặn các sai lệch trong tính toán thống kê cơ bản.
*   **Chi tiết hành động thực thi:**
    1. **Tiêu diệt Cột rác hệ thống:** Hệ thống dò tìm cột mang tên `Unnamed: 0` (đây là cột đếm số thứ tự sinh ra do lỗi lưu trữ index của file CSV trước đó). Khi phát hiện, lệnh gỡ bỏ (drop) được kích hoạt để xóa vĩnh viễn cột này khỏi trục dữ liệu.
    2. **Loại bỏ Tin rao trùng lặp:** Hệ thống thực thi quét đối chiếu chéo. Khi phát hiện từ 2 dòng dữ liệu trở lên có thông tin giống hệt nhau (trùng cả giá, diện tích, vị trí...), nó sẽ chỉ giữ lại dòng đầu tiên và xóa toàn bộ các dòng copy. Hành động này triệt tiêu nguy cơ thiên vị (bias) khi tính mức giá trung bình của một khu vực.

### Phân đoạn 3: Đồng nhất tính Nhất quán của Dữ liệu (Data Consistency)
Bước này can thiệp sâu vào từng ô dữ liệu để gọt giũa các lỗi do con người gõ phím sai.
*   **Chi tiết hành động thực thi với Dữ liệu Chữ (Văn bản):**
    1. Xây dựng một quy trình chuẩn hóa 3 lớp và áp dụng quét qua các cột `Quận`, `Loại hình nhà ở`, `Giấy tờ pháp lý`.
    2. **Lớp 1 (Chuẩn hóa Bảng mã):** Ép toàn bộ các chuỗi ký tự về chuẩn Unicode NFC. Hành động này nối các ký tự tiếng Việt bị đứt gãy (do gõ bằng các bộ gõ khác nhau) về chung một chuẩn, chống lỗi vỡ font chữ.
    3. **Lớp 2 (Đồng nhất Viết thường):** Ép toàn bộ các chữ cái (kể cả chữ in hoa) thành chữ viết thường (lowercase). Tránh việc "CẦU GIẤY" và "cầu giấy" bị đếm thành 2 quận.
    4. **Lớp 3 (Gọt khoảng trắng):** Cắt bỏ toàn bộ các dấu cách (space) vô tình bị thừa ở đầu và cuối chuỗi văn bản.
*   **Chi tiết hành động thực thi với Dữ liệu Số (Giá, Diện tích):**
    1. **Bóc tách:** Xóa bỏ hoàn toàn các chuỗi ký tự đi kèm như "triệu/m2", "triệu/m²" ra khỏi cột Giá. 
    2. **Chuẩn hóa hệ thập phân:** Tìm kiếm toàn bộ các dấu phẩy (`,`) và thay thế bằng dấu chấm (`.`) để tuân thủ đúng chuẩn định dạng số thập phân quốc tế.
    3. **Ép kiểu:** Sau khi đã gọt sạch chữ, hệ thống bắt buộc ép định dạng cột đó từ Văn bản sang Số thực (Float). Bất kỳ cụm từ nào quá lộn xộn không thể ép ra số sẽ bị cưỡng chế biến thành ô trống (`NaN`).

### Phân đoạn 4: Chiến lược Xử lý Dữ liệu Khuyết thiếu (Missing Imputation)
Tuyệt đối không điền bừa bãi. Hệ thống áp dụng 2 chiến lược song song tùy thuộc vào bản chất của cột dữ liệu:
*   **Chi tiết hành động thực thi (Chiến lược 1 - Cắt bỏ):** Áp dụng nghiêm ngặt cho 2 cột sinh tử là `Giá` và `Diện tích`. Hệ thống quét 2 cột này, hễ phát hiện ô nào là `NaN`, lập tức xóa bỏ hoàn toàn dòng bản ghi đó. Vì tự suy đoán (bịa) ra giá nhà sẽ phá hủy hoàn toàn độ tin cậy của báo cáo phân tích.
*   **Chi tiết hành động thực thi (Chiến lược 2 - Tạo Cờ hiệu):** Áp dụng cho cột `Số tầng`. Thực tế, một mảnh đất nền không có nhà thì sẽ không có số tầng. Việc thiếu dữ liệu lúc này mang một ý nghĩa đặc biệt. Do đó, hệ thống không xóa dòng, mà sinh ra một cột Cờ hiệu mới mang tên `Thieu_So_Tang`. Hệ thống sẽ điền số `1` nếu nhà đó khuyết số tầng, và điền số `0` nếu nhà đó có tầng.

### Phân đoạn 5: Xử lý Giá trị Ngoại lệ (Outliers)
Ngoại lệ là những tin đăng "ảo" phá hoại thị trường (Ví dụ: nhà 10m2 nhưng rao bán 100 tỷ).
*   **Chi tiết hành động thực thi:**
    1. **Đo lường bằng IQR:** Hệ thống tính toán điểm phân vị 25% và 75% của cột Giá, qua đó tìm ra "vùng phổ biến nhất" của thị trường. Từ đó, dùng công thức thống kê nội suy ra một mức **Giá Trần** (Upper bound) cao nhất có thể chấp nhận được.
    2. **Kỹ thuật Cắt ngọn (Winsorization/Clipping):** Thay vì xóa bỏ các căn nhà "tin ảo" này làm thất thoát lượng lớn dữ liệu, hệ thống dùng thuật toán quét dọc cột Giá. Bất kỳ căn nhà nào có giá vọt qua Mức Giá Trần, nó sẽ bị "ép" (ghì xuống) bằng đúng với Mức Giá Trần đó. Điều này giúp triệt tiêu sự vô lý của "tin ảo" nhưng vẫn giữ lại được dòng dữ liệu để phân tích các yếu tố khác (như diện tích, vị trí).

### Phân đoạn 6: Đóng gói Pipeline và Số hóa Dữ liệu
Bước can thiệp cuối cùng nhằm biến hóa dữ liệu sao cho các công cụ tính toán phức tạp nhất có thể hấp thụ được.
*   **Chi tiết hành động thực thi:**
    1. **Khởi tạo Dây chuyền (Pipeline):** Hệ thống tạo ra một luồng xử lý tự động (Scikit-Learn Pipeline) để đảm bảo dữ liệu không bị rò rỉ.
    2. **Với các cột dạng Số:** Hệ thống tự động tìm các ô còn trống sót lại và điền bằng giá trị Trung vị (Median). Sau đó, áp dụng thuật toán `RobustScaler` để kéo giãn/thu hẹp các con số siêu to (tiền tỷ) và siêu nhỏ (số tầng) về chung một hệ quy chiếu tỷ lệ chuẩn mực.
    3. **Với các cột dạng Chữ:** Hệ thống tự điền chữ "khong_ro" vào các ô trống. Sau đó, do các công cụ phân tích không biết đọc chữ "Quận Cầu Giấy", hệ thống áp dụng kỹ thuật `One-Hot Encoding` để đập vỡ cột Quận thành hàng chục cột nhỏ chứa mã nhị phân (chỉ có số 0 và 1).

---
**TỔNG KẾT:** 
Sau khi đi qua 6 phân đoạn kỹ thuật trên, bộ dữ liệu đã được gột rửa mọi tạp chất, đồng nhất 100% về cấu trúc và định dạng. Không một giá trị ảo hay nhiễu loạn nào còn tồn tại, dữ liệu hiện tại là một "mỏ vàng" sạch sẽ, sẵn sàng để khai phá các báo cáo phân tích chính xác nhất.
