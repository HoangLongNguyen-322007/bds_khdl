# THƯ MỤC LƯU TRỮ (ARCHIVE)

Thư mục này chứa các mã nguồn cũ từ giai đoạn **Tuần 1 - Tuần 3 (Thu thập dữ liệu thô)** được lưu trữ lại để làm minh chứng học phần khi cần:

- `crawlers/crawl_alonhadat.py`: Script cào dữ liệu từ alonhadat.com.vn.
- `crawlers/crawl_batdongsan_ui.py`: Script cào dữ liệu giao diện từ batdongsan.com.vn (Playwright).
- `crawlers/crawl_projects_homedy.py`: Script cào dự án chung cư từ homedy.com.
- `crawlers/crawl_urban_areas.py`: Script cào khu đô thị từ homedy.com.
- `crawlers/crawler_massive.py`: Script cào đa luồng 30 quận/huyện Hà Nội.

> **Ghi chú**: Dữ liệu thô thu thập được đã được kết xuất và bảo toàn bất biến tại `data/raw/raw.csv` (99.998 bản ghi). Toàn bộ luồng xử lý và mô hình hoá chính thức của dự án hiện hoạt động độc lập qua các pipeline trong thư mục `src/`.
