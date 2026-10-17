import psycopg2
from psycopg2.extras import Json
from typing import Dict, Any

class DatabaseManager:
    def __init__(self, conn_str: str):
        self.conn_str = conn_str
        
    def get_connection(self):
        return psycopg2.connect(self.conn_str)
        
    def insert_raw_listing(self, data: Dict[str, Any]):
        """
        Inserts a raw listing into the raw_listings table.
        Ignores duplicates based on source and source_listing_id (or url).
        """
        query = """
            INSERT INTO raw_listings (
                source, source_listing_id, url, title_raw, description_raw, 
                price_raw, area_raw, address_raw, district_raw, ward_raw, 
                city_raw, published_at_raw, raw_content
            ) VALUES (
                %(source)s, %(source_listing_id)s, %(url)s, %(title_raw)s, %(description_raw)s,
                %(price_raw)s, %(area_raw)s, %(address_raw)s, %(district_raw)s, %(ward_raw)s,
                %(city_raw)s, %(published_at_raw)s, %(raw_content)s
            ) ON CONFLICT (url) DO NOTHING;
        """
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cursor:
                    # Convert dict to JSON string for the raw_content jsonb field
                    if 'raw_content' in data and isinstance(data['raw_content'], dict):
                        data['raw_content'] = Json(data['raw_content'])
                    else:
                        data['raw_content'] = Json({})
                        
                    # Provide defaults for missing fields
                    keys = ['source', 'source_listing_id', 'url', 'title_raw', 'description_raw',
                            'price_raw', 'area_raw', 'address_raw', 'district_raw', 'ward_raw', 'city_raw', 'published_at_raw']
                    for k in keys:
                        if k not in data:
                            data[k] = None
                            
                    cursor.execute(query, data)
                    conn.commit()
                    return True
        except Exception as e:
            print(f"DB Insert Error: {e}")
            return False
