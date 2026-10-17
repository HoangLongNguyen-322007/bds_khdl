import os
import sys
import re
import psycopg2
from typing import Dict, Any, Optional

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database_ops import DatabaseManager

class DataNormalizer:
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        
    def parse_price(self, price_str: str) -> Optional[float]:
        """Convert '2.5 tỷ', '300 triệu' into raw float VND"""
        if not price_str:
            return None
            
        price_str = str(price_str).lower().replace(',', '.')
        
        # Extract number
        match = re.search(r'([0-9\.]+)', price_str)
        if not match:
            return None
            
        try:
            val = float(match.group(1))
            
            if 'tỷ' in price_str or 'ty' in price_str:
                return val * 1_000_000_000
            elif 'triệu' in price_str or 'trieu' in price_str or 'tr' in price_str:
                return val * 1_000_000
            elif 'nghìn' in price_str or 'nghin' in price_str:
                return val * 1_000
                
            return val
        except:
            return None
            
    def parse_area(self, area_str: str) -> Optional[float]:
        """Convert '120m2', '120 m²' into raw float"""
        if not area_str:
            return None
            
        area_str = str(area_str).replace(',', '.')
        match = re.search(r'([0-9\.]+)', area_str)
        if match:
            try:
                return float(match.group(1))
            except:
                return None
        return None
        
    def extract_district(self, text: str) -> Optional[str]:
        """Extract district from address"""
        if not text:
            return None
        
        text_lower = text.lower()
        
        # Danh sách 30 Quận Huyện Hà Nội
        hanoi_districts = {
            "ba đình": "Quận Ba Đình", "hoàn kiếm": "Quận Hoàn Kiếm", "tây hồ": "Quận Tây Hồ", 
            "long biên": "Quận Long Biên", "cầu giấy": "Quận Cầu Giấy", "đống đa": "Quận Đống Đa", 
            "hai bà trưng": "Quận Hai Bà Trưng", "hoàng mai": "Quận Hoàng Mai", "thanh xuân": "Quận Thanh Xuân", 
            "nam từ liêm": "Quận Nam Từ Liêm", "bắc từ liêm": "Quận Bắc Từ Liêm", "hà đông": "Quận Hà Đông",
            "sơn tây": "Thị xã Sơn Tây",
            "sóc sơn": "Huyện Sóc Sơn", "đông anh": "Huyện Đông Anh", "gia lâm": "Huyện Gia Lâm", 
            "thanh trì": "Huyện Thanh Trì", "mê linh": "Huyện Mê Linh", "ba vì": "Huyện Ba Vì", 
            "phúc thọ": "Huyện Phúc Thọ", "đan phượng": "Huyện Đan Phượng", "hoài đức": "Huyện Hoài Đức", 
            "quốc oai": "Huyện Quốc Oai", "thạch thất": "Huyện Thạch Thất", "chương mỹ": "Huyện Chương Mỹ", 
            "thanh oai": "Huyện Thanh Oai", "thường tín": "Huyện Thường Tín", "phú xuyên": "Huyện Phú Xuyên", 
            "ứng hòa": "Huyện Ứng Hòa", "mỹ đức": "Huyện Mỹ Đức"
        }
        
        # 1. Tìm theo cụm từ đầy đủ (có chữ Quận/Huyện)
        match = re.search(r'(Quận\s+[A-ZÀ-Ỹa-zà-ỹ\s]+|Huyện\s+[A-ZÀ-Ỹa-zà-ỹ\s]+)', text, re.IGNORECASE)
        if match:
            district = match.group(1).strip()
            return district.split(',')[0].strip()
            
        # 2. Tìm theo tên không có chữ Quận/Huyện (đặc biệt cho Kaggle)
        for key, value in hanoi_districts.items():
            if f" {key}," in text_lower or text_lower.endswith(f" {key}") or f",{key}," in text_lower.replace(" ", ""):
                return value
                
        return None

    def normalize_and_save(self):
        print("==================================================")
        print("🌟 BẮT ĐẦU CHUẨN HÓA DỮ LIỆU (PHASE 4) 🌟")
        print("==================================================")
        
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        # 1. Fetch unprocessed raw listings including dates
        cursor.execute("SELECT id, title_raw, description_raw, price_raw, area_raw, address_raw, url, source, collected_at, published_at_raw FROM raw_listings WHERE is_processed = FALSE")
        raw_rows = cursor.fetchall()
        
        print(f"-> Tìm thấy {len(raw_rows)} bản ghi chưa chuẩn hóa.")
        
        processed_count = 0
        for row in raw_rows:
            raw_id, title, desc, price_r, area_r, address_r, url, source, collected_at, published_at_raw = row
            
            # Normalize
            price_vnd = self.parse_price(price_r)
            area_m2 = self.parse_area(area_r)
            price_per_m2 = None
            if price_vnd and area_m2 and area_m2 > 0:
                price_per_m2 = price_vnd / area_m2
                
            district = self.extract_district(address_r)
            
            # Determine the best date
            # Try to parse published_at_raw if it exists (Kaggle has dates like DD/MM/YYYY)
            final_date = collected_at
            if published_at_raw:
                try:
                    from datetime import datetime
                    if "T" in published_at_raw: # ISO format from HuggingFace like 2026-06-01T05:12:56
                        # Cắt bỏ phần microseconds nếu có
                        clean_iso = published_at_raw.split('.')[0]
                        final_date = datetime.strptime(clean_iso, "%Y-%m-%dT%H:%M:%S")
                    elif "-" in published_at_raw: # YYYY-MM-DD
                        final_date = datetime.strptime(published_at_raw.split()[0], "%Y-%m-%d")
                    elif "/" in published_at_raw: # DD/MM/YYYY
                        final_date = datetime.strptime(published_at_raw, "%d/%m/%Y")
                except Exception as e:
                    pass
            
            # Insert into properties table
            insert_sql = """
                INSERT INTO properties 
                (price_vnd, area_m2, price_per_m2, address, old_district, city, published_at, collected_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            try:
                cursor.execute(insert_sql, (
                    price_vnd, area_m2, price_per_m2, 
                    address_r, district, "Hà Nội", final_date, collected_at
                ))
                
                # Update raw_listings
                cursor.execute("UPDATE raw_listings SET is_processed = TRUE WHERE id = %s", (raw_id,))
                
                processed_count += 1
                if processed_count % 100 == 0:
                    print(f"   ✅ Đã chuẩn hóa {processed_count} bản ghi...")
                    conn.commit()
                    
            except Exception as e:
                print(f"Lỗi khi insert property {url}: {e}")
                conn.rollback()
                
        conn.commit()
        cursor.close()
        conn.close()
        
        print(f"🚀 HOÀN TẤT! Đã chuẩn hóa thành công {processed_count}/{len(raw_rows)} BĐS.")
        print("Dữ liệu giờ đã sẵn sàng cho Model Machine Learning!")
        print("==================================================")

if __name__ == "__main__":
    DB_CONN = "dbname=bds_khdl user=longnguyen host=localhost port=5432"
    db = DatabaseManager(DB_CONN)
    normalizer = DataNormalizer(db)
    normalizer.normalize_and_save()
