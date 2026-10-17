import os
import sys
import pandas as pd
import psycopg2
from tqdm import tqdm

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database_ops import DatabaseManager

def import_kaggle_dataset():
    print("==================================================")
    print("🌟 BẮT ĐẦU NẠP DỮ LIỆU KAGGLE (HN_Houseprice) VÀO HỆ THỐNG 🌟")
    print("==================================================")
    
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'raw_datasets', 'HN_Houseprice.csv')
    
    if not os.path.exists(file_path):
        print(f"Lỗi: Không tìm thấy file {file_path}")
        return

    # Load CSV
    try:
        df = pd.read_csv(file_path, on_bad_lines='skip', engine='python')
    except Exception as e:
        print(f"Lỗi đọc CSV: {e}")
        return
        
    print(f"-> Phân tích thấy {len(df)} dòng dữ liệu thô từ Kaggle.")
    
    # Kết nối DB
    db = DatabaseManager("dbname=bds_khdl user=longnguyen host=localhost port=5432")
    conn = db.get_connection()
    cursor = conn.cursor()
    
    success_count = 0
    duplicate_count = 0
    
    print("-> Bắt đầu chèn vào Database (sẽ tự động loại bỏ trùng lặp)...")
    
    # Import
    for index, row in tqdm(df.iterrows(), total=len(df)):
        try:
            # Map columns from Kaggle to our raw_listings schema
            title = str(row['Title']) if pd.notna(row['Title']) else ""
            address = str(row['Address']) if pd.notna(row['Address']) else ""
            district = str(row['District']) if pd.notna(row['District']) else ""
            price = str(row['Price']) if pd.notna(row['Price']) else ""
            area = str(row['Area']) if pd.notna(row['Area']) else ""
            
            # Since Kaggle doesn't have a URL, we generate a unique hash for the URL based on title + address
            unique_url = f"kaggle-{hash(title + address)}"
            
            data = {
                "source": "kaggle_2026",
                "title_raw": title,
                "price_raw": price,
                "area_raw": area,
                "address_raw": address,
                "city_raw": "Hà Nội",
                "url": unique_url
            }
            
            is_inserted = db.insert_raw_listing(data)
            if is_inserted:
                success_count += 1
            else:
                duplicate_count += 1
                
        except Exception as e:
            pass
            
    conn.close()
    
    print("\n==================================================")
    print(f"✅ Hoàn tất quá trình Import!")
    print(f"   - Số bản ghi chèn thành công: {success_count}")
    print(f"   - Số bản ghi bị trùng (bỏ qua): {duplicate_count}")
    print("👉 Hãy chạy `src/normalize_data.py` để chuẩn hóa đống dữ liệu này.")
    print("==================================================")

if __name__ == "__main__":
    import_kaggle_dataset()
