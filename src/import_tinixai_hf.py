import os
import sys
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database_ops import DatabaseManager

def import_tinixai():
    print("==================================================")
    print("🌊 KÍCH HOẠT MÁY BƠM DỮ LIỆU TỪ HUGGINGFACE (TINIXAI - 24 THÁNG QUA) 🌊")
    print("==================================================")
    
    try:
        from datasets import load_dataset
    except ImportError:
        print("Vui lòng cài đặt thư viện 'datasets'")
        return
        
    db = DatabaseManager("dbname=bds_khdl user=longnguyen host=localhost port=5432")
    
    print("-> Đang kết nối luồng Streaming...")
    ds = load_dataset('tinixai/vietnam-real-estates', split='train', streaming=True)
    
    total_scanned = 0
    inserted = 0
    TARGET_RECORDS = 30000  # Hút 30.000 căn nhà lịch sử
    
    for row in ds:
        total_scanned += 1
        
        # Chỉ lấy Hà Nội
        province = row.get('province_name')
        if not province or 'Hà Nội' not in province:
            continue
            
        title = row.get('name')
        if not title:
            continue
            
        published_at = str(row.get('published_at', ''))
        # Lọc bài đăng thuộc năm 2024, 2025, 2026
        if '2024' not in published_at and '2025' not in published_at and '2026' not in published_at:
             continue
             
        # Gộp địa chỉ
        parts = []
        if row.get('street_name'): parts.append(str(row.get('street_name')))
        if row.get('ward_name'): parts.append(str(row.get('ward_name')))
        if row.get('district_name'): parts.append(str(row.get('district_name')))
        address_raw = ", ".join(parts) if parts else "Hà Nội"
        
        # Giá và diện tích
        price = row.get('price')
        area = row.get('area')
        
        price_str = f"{price} VNĐ" if price else ""
        area_str = f"{area} m2" if area else ""
        
        data = {
            "source": "hf_tinixai_history",
            "title_raw": title,
            "price_raw": price_str,
            "area_raw": area_str,
            "address_raw": address_raw,
            "city_raw": "Hà Nội",
            "url": f"tinixai-{uuid.uuid4()}",
            "published_at_raw": published_at
        }
        
        if db.insert_raw_listing(data):
            inserted += 1
            
        if inserted % 1000 == 0 and inserted > 0:
            print(f"   ⚡ Đã hút thành công {inserted} bản ghi BĐS Hà Nội (Quét qua {total_scanned} tin)")
            
        if inserted >= TARGET_RECORDS:
            break
            
    print("==================================================")
    print(f"🏁 XONG! Đã thu thập thành công {inserted} bản ghi lịch sử vào Database.")
    print("==================================================")
    
if __name__ == "__main__":
    import_tinixai()
