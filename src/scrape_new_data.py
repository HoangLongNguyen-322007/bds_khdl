import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import os
from datetime import datetime

# Các User-Agent đa dạng để tránh bị nhận diện là bot
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
]

def get_random_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

def scrape_bds123(max_pages=2):
    """Cào dữ liệu từ bds123.vn"""
    print(f"\n--- Đang cào dữ liệu từ BDS123 (Tối đa {max_pages} trang) ---")
    data = []
    base_url = "https://bds123.vn/ban-nha-ha-noi.html?page={}"
    
    for page in range(1, max_pages + 1):
        print(f"-> Đang cào trang {page} của BDS123...")
        url = base_url.format(page)
        
        try:
            response = requests.get(url, headers=get_random_headers(), timeout=10)
            if response.status_code != 200:
                print(f"Lỗi truy cập trang {page}. HTTP Code: {response.status_code}")
                continue
                
            soup = BeautifulSoup(response.text, 'html.parser')
            items = soup.find_all('li', class_='post-item')
            
            for item in items:
                try:
                    title_elem = item.find('h3', class_='post-title')
                    title = title_elem.text.strip() if title_elem else "N/A"
                    
                    price_elem = item.find('span', class_='post-price')
                    price = price_elem.text.strip() if price_elem else "N/A"
                    
                    area_elem = item.find('span', class_='post-acreage')
                    area = area_elem.text.strip() if area_elem else "N/A"
                    
                    loc_elem = item.find('span', class_='post-location')
                    location = loc_elem.text.strip() if loc_elem else "N/A"
                    
                    data.append({
                        "Ngày": datetime.now().strftime("%Y-%m-%d"),
                        "Nguồn": "BDS123",
                        "Tiêu đề": title,
                        "Địa chỉ": location,
                        "Giá": price,
                        "Diện tích": area,
                        "Quận/Huyện": location.split(',')[-2].strip() if len(location.split(',')) > 1 else "Hà Nội"
                    })
                except Exception as e:
                    pass
            
            # NGỦ NGẪU NHIÊN ĐỂ TRÁNH BỊ CHẶN IP
            sleep_time = random.uniform(2, 5)
            print(f"Ngủ {sleep_time:.2f}s để tránh Anti-bot...")
            time.sleep(sleep_time)
            
        except Exception as e:
            print(f"Lỗi: {e}")
            time.sleep(5)
            
    return data

def scrape_nhadat24h(max_pages=2):
    """Cào dữ liệu từ Nhadat24h.net"""
    print(f"\n--- Đang cào dữ liệu từ NhaDat24h (Tối đa {max_pages} trang) ---")
    data = []
    base_url = "https://nhadat24h.net/ban-nha-rieng-ha-noi/page{}"
    
    for page in range(1, max_pages + 1):
        print(f"-> Đang cào trang {page} của NhaDat24h...")
        url = base_url.format(page)
        
        try:
            response = requests.get(url, headers=get_random_headers(), timeout=10)
            if response.status_code != 200:
                print(f"Lỗi truy cập trang {page}. HTTP Code: {response.status_code}")
                continue
                
            soup = BeautifulSoup(response.text, 'html.parser')
            items = soup.find_all('div', class_='pnItem')
            
            for item in items:
                try:
                    title_elem = item.find('a', class_='a-title')
                    title = title_elem.text.strip() if title_elem else "N/A"
                    
                    price_elem = item.find('label', class_='a-price')
                    price = price_elem.text.strip() if price_elem else "N/A"
                    
                    area_elem = item.find('label', class_='a-area')
                    area = area_elem.text.strip() if area_elem else "N/A"
                    
                    loc_elem = item.find('span', class_='margin-left-5')
                    location = loc_elem.text.strip() if loc_elem else "N/A"
                    
                    data.append({
                        "Ngày": datetime.now().strftime("%Y-%m-%d"),
                        "Nguồn": "NhaDat24h",
                        "Tiêu đề": title,
                        "Địa chỉ": location,
                        "Giá": price,
                        "Diện tích": area,
                        "Quận/Huyện": location.split('-')[-1].strip() if '-' in location else "Hà Nội"
                    })
                except Exception as e:
                    pass
                    
            sleep_time = random.uniform(2, 5)
            print(f"Ngủ {sleep_time:.2f}s để tránh Anti-bot...")
            time.sleep(sleep_time)
            
        except Exception as e:
            print(f"Lỗi: {e}")
            time.sleep(5)
            
    return data

def main():
    print("BẮT ĐẦU CÀO DỮ LIỆU ĐA NGUỒN CHỐNG CHẶN IP...")
    
    # Số trang muốn cào (mỗi trang khoảng 15-20 tin)
    PAGES_TO_SCRAPE = 3
    
    all_data = []
    
    # 1. Cào từ BDS123
    bds123_data = scrape_bds123(max_pages=PAGES_TO_SCRAPE)
    all_data.extend(bds123_data)
    
    # 2. Cào từ Nhadat24h
    nhadat24h_data = scrape_nhadat24h(max_pages=PAGES_TO_SCRAPE)
    all_data.extend(nhadat24h_data)
    
    # Tạo DataFrame và lưu
    df = pd.DataFrame(all_data)
    
    if len(df) > 0:
        os.makedirs("data/raw", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = f"data/raw/bds_crawled_multi_{timestamp}.csv"
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
        print(f"\n[THÀNH CÔNG] Đã cào được {len(df)} bản ghi mới nhất.")
        print(f"Dữ liệu đã được lưu tại: {file_path}")
        print("Dưới đây là một vài dòng dữ liệu vừa cào:")
        print(df.head())
    else:
        print("\n[THẤT BẠI] Không cào được dữ liệu nào. Có thể cấu trúc HTML đã thay đổi hoặc bị IP block mạnh.")

if __name__ == "__main__":
    main()
