import time
import os
import sys
from playwright.sync_api import sync_playwright

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database_ops import DatabaseManager

def scrape_batdongsan_com_vn():
    print("==================================================")
    print("🌟 BOT CÀO DỮ LIỆU BATDONGSAN.COM.VN (CHẾ ĐỘ HIỂN THỊ) 🌟")
    print("==================================================")
    print("Lưu ý: Batdongsan.com.vn có hệ thống chặn Bot rất mạnh.")
    print("Trình duyệt sẽ mở lên. Nếu thấy yêu cầu xác minh Captcha (Tick chọn 'I am human'),")
    print("bạn hãy dùng chuột click vào để vượt qua nhé! Sau đó Bot sẽ tự động làm việc.")
    print("==================================================")
    
    DB_CONN = "dbname=bds_khdl user=longnguyen host=localhost port=5432"
    db = DatabaseManager(DB_CONN)
    
    total_inserted = 0
    
    with sync_playwright() as p:
        # Mở trình duyệt CÓ HIỂN THỊ (headless=False) để người dùng có thể tự qua mặt Captcha
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        for page_num in range(1, 101): # Cào 100 trang
            url = f"https://batdongsan.com.vn/ban-nha-dat-ha-noi/p{page_num}"
            if page_num == 1:
                url = "https://batdongsan.com.vn/ban-nha-dat-ha-noi"
                
            print(f"-> Đang tải trang {page_num}: {url}")
            page.goto(url)
            
            # Đợi 10 giây ở trang đầu tiên để bạn kịp click Captcha nếu có
            if page_num == 1:
                print("⏳ Đang chờ 10 giây để bạn giải quyết Captcha (nếu có)...")
                time.sleep(10)
            else:
                time.sleep(3)
                
            # Lấy toàn bộ card BĐS
            cards = page.query_selector_all(".js__pr-item")
            
            if not cards:
                print("⚠️ Không tìm thấy BĐS nào! Có thể bạn chưa giải Captcha hoặc web đã đổi cấu trúc.")
                break
                
            for card in cards:
                try:
                    title_elem = card.query_selector(".js__pr-title")
                    price_elem = card.query_selector(".re__card-config-price")
                    area_elem = card.query_selector(".re__card-config-area")
                    loc_elem = card.query_selector(".re__card-location")
                    
                    title = title_elem.inner_text().strip() if title_elem else None
                    price = price_elem.inner_text().strip() if price_elem else None
                    area = area_elem.inner_text().strip() if area_elem else None
                    location = loc_elem.inner_text().strip() if loc_elem else None
                    
                    if title:
                        data = {
                            "source": "batdongsan.com.vn",
                            "title_raw": title,
                            "price_raw": price,
                            "area_raw": area,
                            "address_raw": location,
                            "city_raw": "Hà Nội",
                            "url": f"batdongsan-{hash(title)}"
                        }
                        success = db.insert_raw_listing(data)
                        if success:
                            total_inserted += 1
                except Exception as e:
                    pass
                    
            print(f"   ✅ Đã lấy & lưu {total_inserted} BĐS từ Batdongsan.com.vn vào Database.")
            
        browser.close()
        print(f"🚀 Hoàn tất! Đã thu thập {total_inserted} BĐS từ Batdongsan.com.vn.")

if __name__ == "__main__":
    scrape_batdongsan_com_vn()
