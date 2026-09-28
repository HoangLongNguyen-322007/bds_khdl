import os
import urllib.request
from datetime import datetime

def download_hanoi_dataset():
    print("Đang tải dữ liệu thực tế: Tập dữ liệu giá nhà Hà Nội (hơn 80.000 bản ghi)...")
    url = "https://raw.githubusercontent.com/phkhanhtrinh23/hanoi_housing_price/main/Hanoi_housing_dataset.csv"
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("data/raw", exist_ok=True)
    file_path = f"data/raw/bds_raw_hanoi_{timestamp}.csv"
    
    try:
        urllib.request.urlretrieve(url, file_path)
        print(f"Đã tải thành công tập dữ liệu thô và lưu tại: {file_path}")
    except Exception as e:
        print(f"Lỗi khi tải dữ liệu: {e}")
        
if __name__ == "__main__":
    download_hanoi_dataset()
