import os
import sys
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database_ops import DatabaseManager

def crawl_alonhadat_page(page_num, db_manager):
    url = f"https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/{page_num}/ha-noi.html"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"Lỗi truy cập trang {page_num}: Status {response.status_code}")
            return 0
            
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Alonhadat wraps listings in elements with class 'content-item'
        items = soup.find_all('div', class_='content-item')
        
        success_count = 0
        for item in items:
            try:
                title_tag = item.find('h3', class_='property-title')
                if not title_tag:
                    continue
                
                title = title_tag.text.strip()
                link_tag = item.find('a', class_='link')
                link = link_tag['href'] if link_tag else ""
                full_url = "https://alonhadat.com.vn" + link
                
                price_tag = item.find('span', class_='price')
                price = price_tag.text.strip().replace("Giá:", "").strip() if price_tag else ""
                
                area_tag = item.find('span', class_='square')
                area = area_tag.text.strip().replace("Diện tích:", "").strip() if area_tag else ""
                
                # Vị trí thường nằm trong một thẻ span hoặc div riêng
                address_tag = item.find('div', class_='ct_dis')
                if not address_tag:
                    address_tag = item.find('span', class_='location') # Alonhadat uses 'location'
                address = address_tag.text.strip() if address_tag else ""
                
                data = {
                    "source": "Alonhadat_2026",
                    "title_raw": title,
                    "price_raw": price,
                    "area_raw": area,
                    "address_raw": address,
                    "city_raw": "Hà Nội",
                    "url": full_url
                }
                
                is_inserted = db_manager.insert_raw_listing(data)
                if is_inserted:
                    success_count += 1
                    
            except Exception as e:
                continue
                
        return success_count
        
    except Exception as e:
        print(f"Lỗi tại trang {page_num}: {e}")
        return 0

def run_crawler():
    print("==================================================")
    print("🚀 BẮT ĐẦU CÀO DỮ LIỆU TỪ ALONHADAT.COM.VN 2026")
    print("==================================================")
    
    db = DatabaseManager("dbname=bds_khdl user=longnguyen host=localhost port=5432")
    
    total_added = 0
    # Scrape first 10 pages as a demo/start
    for page in range(1, 11):
        print(f"-> Đang quét trang {page}...")
        added = crawl_alonhadat_page(page, db)
        total_added += added
        print(f"   + Thêm mới được {added} bản ghi độc nhất.")
        time.sleep(2) # Lịch sự với Server
        
    print("==================================================")
    print(f"✅ Hoàn tất đợt cào mini! Thu thập thêm {total_added} BĐS mới nhất.")
    print("==================================================")

if __name__ == "__main__":
    run_crawler()
