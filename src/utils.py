import pandas as pd
import numpy as np
import unicodedata

def audit_data(df: pd.DataFrame):
    """6 dòng lệnh kiểm tra bắt buộc (Mandatory Audit Lines)"""
    print("-" * 50)
    print("1. SHAPE (Dòng, Cột):", df.shape)
    print("-" * 50)
    print("2. INFO:")
    df.info()
    print("-" * 50)
    print("3. HEAD (5 dòng đầu):")
    print(df.head())
    print("-" * 50)
    print("4. DTYPES:")
    print(df.dtypes)
    print("-" * 50)
    print("5. MISSING VALUES:")
    print(df.isna().sum())
    print("-" * 50)
    print("6. DUPLICATES:")
    print("Số lượng dòng trùng lặp:", df.duplicated().sum())
    print("-" * 50)

def normalize_vn(text):
    """Chuẩn hóa chuỗi tiếng Việt (NFC, in thường, strip)"""
    if pd.isna(text):
        return text
    text = str(text)
    # Đưa về chuẩn NFC
    text = unicodedata.normalize('NFC', text)
    # Chữ thường và loại bỏ khoảng trắng thừa
    return text.lower().strip()

def clean_price(price_str):
    """Chuyển đổi các định dạng giá về đơn vị Tỷ VND"""
    if pd.isna(price_str):
        return np.nan
    
    price_str = str(price_str).lower().strip()
    
    # Missing giấu mặt
    if "thỏa thuận" in price_str or "không rõ" in price_str or price_str == "":
        return np.nan
    
    try:
        # Xử lý chứa chữ 'tỷ'
        if "tỷ" in price_str:
            num = float(price_str.replace("tỷ", "").strip())
            return num
        # Xử lý chứa chữ 'triệu'
        elif "triệu" in price_str:
            num = float(price_str.replace("triệu", "").strip())
            return num / 1000  # Quy đổi về tỷ
        else:
            return float(price_str)
    except:
        return np.nan

def clean_area(area_str):
    """Làm sạch định dạng m2 của diện tích"""
    if pd.isna(area_str):
        return np.nan
    area_str = str(area_str).lower().strip()
    if "khong ro" in area_str or area_str == "":
        return np.nan
    
    # Bỏ các chữ cái, ký hiệu
    area_str = area_str.replace("m2", "").replace("m²", "").strip()
    try:
        return float(area_str)
    except:
        return np.nan
