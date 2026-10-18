import os
import sys
import time
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database_ops import DatabaseManager

PROJECTS = [
    "ban-can-ho-vinhomes-ocean-park",
    "ban-nha-biet-thu-lien-ke-vinhomes-ocean-park",
    "ban-can-ho-ciputra-hanoi",
    "ban-nha-biet-thu-lien-ke-ciputra-hanoi",
    "ban-can-ho-vinhomes-royal-city",
    "ban-can-ho-times-city",
    "ban-can-ho-vinhomes-smart-city",
    "ban-nha-biet-thu-lien-ke-vinhomes-smart-city",
    "ban-can-ho-ecopark",
    "ban-nha-biet-thu-lien-ke-ecopark"
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

db = DatabaseManager("dbname=bds_khdl user=longnguyen host=localhost port=5432")

def fetch_page(project: str, page: int):
    url = f"https://homedy.com/{project}/p{page}" if page > 1 else f"https://homedy.com/{project}"
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            return 0
            
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('div', class_='product-item')
        
        if not items:
            return 0
            
        success_count = 0
        for item in items:
            try:
                title_elem = item.find('a', class_='thumb-image')
                if not title_elem:
                    continue
                    
                title = title_elem.get('title', '').strip()
                link = title_elem.get('href', '')
                full_url = "https://homedy.com" + link
                
                price_elem = item.find('strong', class_='price')
                price = price_elem.text.strip() if price_elem else ""
                
                # Cấu trúc homedy thường có .distance hoặc span chứa diện tích
                spans = item.find_all('span')
                area = ""
                for span in spans:
                    if 'm2' in span.text.lower():
                        area = span.text.strip()
                        break
                        
                address = f"Dự án {project.replace('-', ' ')}, Hà Nội"
                
                data = {
                    "source": "homedy_projects",
                    "title_raw": title,
                    "price_raw": price,
                    "area_raw": area,
                    "address_raw": address,
                    "city_raw": "Hà Nội",
                    "url": full_url
                }
                
                if db.insert_raw_listing(data):
                    success_count += 1
                    
            except Exception:
                continue
                
        return success_count
    except Exception as e:
        return 0

def crawl_project(project: str):
    print(f"Bắt đầu cào dự án: {project}")
    total = 0
    empty_pages = 0
    # Cào tối đa 50 trang mỗi dự án
    for page in range(1, 51):
        added = fetch_page(project, page)
        total += added
        if added == 0:
            empty_pages += 1
            if empty_pages >= 2: # Nếu 2 trang liên tiếp trống thì dừng dự án này
                break
        else:
            empty_pages = 0
        time.sleep(0.5)
    print(f"✅ Dự án {project}: Đã cào được {total} bản ghi mới.")
    return total

def run_all():
    print("🚀 ĐANG KHỞI ĐỘNG CỖ MÁY CÀO CÁC DỰ ÁN VIP...")
    total_new = 0
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(crawl_project, p) for p in PROJECTS]
        for future in as_completed(futures):
            total_new += future.result()
            
    print("==================================================")
    print(f"🎉 TỔNG KẾT: Đã thu thập thêm {total_new} bản ghi VIP vào Database.")
    print("==================================================")

if __name__ == "__main__":
    run_all()
