import os
import sys
import time
import requests
from bs4 import BeautifulSoup
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database_ops import DatabaseManager

# 30 Quận Huyện Hà Nội trên Homedy
DISTRICTS = [
    "quan-ba-dinh", "quan-hoan-kiem", "quan-tay-ho", "quan-long-bien", "quan-cau-giay",
    "quan-dong-da", "quan-hai-ba-trung", "quan-hoang-mai", "quan-thanh-xuan", "huyen-soc-son",
    "huyen-dong-anh", "huyen-gia-lam", "quan-nam-tu-liem", "huyen-thanh-tri", "quan-bac-tu-liem",
    "huyen-me-linh", "quan-ha-dong", "thi-xa-son-tay", "huyen-ba-vi", "huyen-phuc-tho",
    "huyen-dan-phuong", "huyen-hoai-duc", "huyen-quoc-oai", "huyen-thach-that", "huyen-chuong-my",
    "huyen-thanh-oai", "huyen-thuong-tin", "huyen-phu-xuyen", "huyen-ung-hoa", "huyen-my-duc"
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
}

csv_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'master_raw_listings.csv')
db = DatabaseManager("dbname=bds_khdl user=longnguyen host=localhost port=5432")

def fetch_page(district: str, page: int):
    url = f"https://homedy.com/ban-nha-dat-{district}-ha-noi/p{page}" if page > 1 else f"https://homedy.com/ban-nha-dat-{district}-ha-noi"
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            return None
            
        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all('div', class_='product-item')
        
        results = []
        for card in cards:
            title_tag = card.find('h3')
            a_tag = card.find('a')
            price_tag = card.find(class_='price')
            area_tag = card.find(class_='acreage')
            loc_tag = card.find(class_='address')
            
            title = title_tag.text.strip() if title_tag else None
            if title:
                results.append({
                    "source": "homedy_massive",
                    "title_raw": title,
                    "price_raw": price_tag.text.strip() if price_tag else None,
                    "area_raw": area_tag.text.strip() if area_tag else None,
                    "address_raw": loc_tag.text.strip() if loc_tag else None,
                    "url": "https://homedy.com" + a_tag['href'] if a_tag and a_tag.get('href') else f"homedy-{hash(title)}"
                })
        return results
    except:
        return None

def main():
    print("==================================================")
    print("🚀 KÍCH HOẠT MASSIVE CRAWLER - MỤC TIÊU 200.000 BĐS 🚀")
    print("==================================================")
    print("Chiến thuật: Vượt giới hạn 500 trang bằng cách chia nhỏ cào từng Quận/Huyện.")
    
    # Mở file CSV mode append
    file_exists = os.path.exists(csv_file)
    with open(csv_file, mode='a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['source', 'title', 'price', 'area', 'address', 'url'])
            
        total_scraped = 0
        
        # Dùng ThreadPool để cào đa luồng siêu tốc
        with ThreadPoolExecutor(max_workers=5) as executor:
            for district in DISTRICTS:
                print(f"\n📍 Bắt đầu quét cạn kiệt: {district.upper()}")
                
                # Quét từ trang 1 đến 500 cho từng quận
                futures = {executor.submit(fetch_page, district, p): p for p in range(1, 501)}
                
                empty_pages = 0
                for future in as_completed(futures):
                    data = future.result()
                    if data:
                        for item in data:
                            # Ghi vào CSV
                            writer.writerow([
                                item['source'], item['title_raw'], item['price_raw'], 
                                item['area_raw'], item['address_raw'], item['url']
                            ])
                            
                            # Ghi vào DB
                            db.insert_raw_listing(item)
                            total_scraped += 1
                            
                        if total_scraped % 100 == 0:
                            print(f"   ⚡ Đã thu thập được {total_scraped} BĐS...")
                            f.flush()
                    else:
                        empty_pages += 1
                        # Nếu gặp 10 trang rỗng liên tiếp thì bỏ qua quận này (hết dữ liệu)
                        if empty_pages > 10:
                            break

    print("\n==================================================")
    print(f"🏁 ĐÃ HOÀN TẤT CHIẾN DỊCH! TỔNG THU HOẠCH: {total_scraped} BĐS.")
    print(f"📂 Dữ liệu đã được dồn tất cả vào: {csv_file}")
    print("==================================================")

if __name__ == "__main__":
    main()
