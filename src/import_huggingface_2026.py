import os
import sys
import uuid
import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database_ops import DatabaseManager

def import_hf_dataset():
    print("==================================================")
    print("🌟 ĐANG TẢI DỮ LIỆU TỪ HUGGINGFACE (SARAH HOOKER - 24 THÁNG QUA) 🌟")
    print("==================================================")
    
    try:
        from datasets import load_dataset
    except ImportError:
        print("Vui lòng cài đặt thư viện 'datasets': pip install datasets")
        return
        
    db = DatabaseManager("dbname=bds_khdl user=longnguyen host=localhost port=5432")
    
    # Load dataset
    ds = load_dataset('sarahooker/vietnam-real-estate-listings', split='train')
    
    total = 0
    inserted = 0
    
    print(f"-> Tổng số bản ghi trong Dataset: {len(ds)}")
    
    for row in ds:
        total += 1
        
        # Chỉ lấy Hà Nội
        if row.get('province_name') != 'Hà Nội':
            continue
            
        # Bỏ qua nếu không có tiêu đề
        title = row.get('name')
        if not title:
            continue
            
        # Lọc bài đăng thuộc năm 2024, 2025, 2026
        published_at = row.get('published_at')
        pub_str = str(published_at)
        if not published_at or ('2024' not in pub_str and '2025' not in pub_str and '2026' not in pub_str):
             continue
             
        # Lấy giá
        price_raw = str(row.get('price')) if row.get('price') is not None else ""
        
        # Lấy diện tích
        area_raw = str(row.get('area')) if row.get('area') is not None else ""
        
        # Lấy địa chỉ
        parts = []
        if row.get('street_name'): parts.append(str(row.get('street_name')))
        if row.get('ward_name'): parts.append(str(row.get('ward_name')))
        if row.get('district_name'): parts.append(str(row.get('district_name')))
        address_raw = ", ".join(parts)
        
        data = {
            "source": "huggingface_2026",
            "title_raw": title,
            "price_raw": price_raw,
            "area_raw": area_raw,
            "address_raw": address_raw,
            "city_raw": "Hà Nội",
            "url": f"hf-{uuid.uuid4()}",
            "published_at_raw": str(published_at)
        }
        
        if db.insert_raw_listing(data):
            inserted += 1
            
        if total % 5000 == 0:
            print(f"   Đã quét qua {total} bản ghi... (Đã lưu {inserted} bản ghi ở Hà Nội)")
            
    print("==================================================")
    print(f"✅ Hoàn tất! Đã nhập {inserted} bản ghi BĐS Hà Nội 24 tháng qua vào Database.")
    
if __name__ == "__main__":
    import_hf_dataset()
