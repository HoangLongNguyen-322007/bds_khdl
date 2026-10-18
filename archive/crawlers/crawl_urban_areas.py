import os
import sys
import time
import requests
from bs4 import BeautifulSoup
import urllib.parse
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database_ops import DatabaseManager

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
}

URBAN_AREAS = [
    "Vinhomes Ocean Park",
    "Vinhomes Smart City",
    "Ciputra",
    "Royal City",
    "Times City",
    "Starlake",
    "Gamuda Gardens",
    "Ecopark",
    "Vinhomes Riverside",
    "Khu đô thị Văn Quán",
    "Khu đô thị Linh Đàm",
    "Khu đô thị Mỹ Đình",
    "Khu đô thị Cầu Bươu",
    "Khu đô thị Xa La"
]

def fetch_page(query: str, page: int):
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://homedy.com/ban-nha-dat-ha-noi/p{page}?q={encoded_query}" if page > 1 else f"https://homedy.com/ban-nha-dat-ha-noi?q={encoded_query}"
    
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
                    "source": "homedy_urban_recent",
                    "title_raw": title,
                    "price_raw": price_tag.text.strip() if price_tag else None,
                    "area_raw": area_tag.text.strip() if area_tag else None,
                    "address_raw": loc_tag.text.strip() if loc_tag else None,
                    "url": "https://homedy.com" + a_tag['href'] if a_tag and a_tag.get('href') else f"homedy-{hash(title)}",
                    "published_at_raw": datetime.now().isoformat()
                })
        return results
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def main():
    print("==================================================")
    print("🏙️ BẮT ĐẦU CÀO BĐS CÁC KHU ĐÔ THỊ LỚN (MỚI NHẤT)")
    print("==================================================")
    
    db = DatabaseManager("dbname=bds_khdl user=longnguyen host=localhost port=5432")
    total_added = 0
    
    for area in URBAN_AREAS:
        print(f"\n📍 Đang quét khu đô thị: {area}")
        empty_pages = 0
        area_count = 0
        
        # Lấy 10 trang mới nhất cho mỗi khu (khoảng 200 căn mới nhất)
        for page in range(1, 11):
            items = fetch_page(area, page)
            if not items or len(items) == 0:
                empty_pages += 1
                if empty_pages >= 2:
                    break
            else:
                empty_pages = 0
                for item in items:
                    if db.insert_raw_listing(item):
                        total_added += 1
                        area_count += 1
            time.sleep(1) # politely sleep
            
        print(f"   => Đã lấy {area_count} căn mới nhất từ {area}.")
        
    print("==================================================")
    print(f"✅ Hoàn tất! Thu thập thêm {total_added} BĐS khu đô thị mới nhất.")
    print("==================================================")

if __name__ == "__main__":
    main()
