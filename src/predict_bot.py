import os
import sys
import joblib
import pandas as pd
import numpy as np

def predict_price(area_m2: float, district: str, prop_type: str = 'nhà ngõ, hẻm', legal: str = 'đã có sổ', floors: float = 3.0, bedrooms: float = 3.0):
    print("==================================================")
    print("🤖 AI CHUYÊN GIA DỰ ĐOÁN GIÁ BẤT ĐỘNG SẢN HÀ NỘI")
    print("==================================================")
    
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(root_dir, 'house_price_model.pkl')
    
    if not os.path.exists(model_path):
        print("⚠️ Lỗi: Chưa tìm thấy Model AI tại house_price_model.pkl. Hãy chạy src/run_pipeline_eda_modeling.py trước.")
        return
        
    model = joblib.load(model_path)
    
    # Chuẩn hóa tên quận
    clean_district = str(district).strip().lower()
    if not clean_district.startswith("quận ") and not clean_district.startswith("huyện ") and not clean_district.startswith("thị xã "):
        clean_district = f"quận {clean_district}"
        
    noi_do = ['quận ba đình', 'quận hoàn kiếm', 'quận tây hồ', 'quận đống đa', 'quận hai bà trưng', 'quận cầu giấy', 'quận thanh xuân']
    khu_vuc_noi_do = 1 if any(d in clean_district for d in noi_do) else 0
    co_so_do = 1 if 'sổ' in str(legal).lower() else 0
    loai_nha_mat_pho = 1 if ('mặt phố' in str(prop_type).lower() or 'mặt tiền' in str(prop_type).lower()) else 0
    loai_nha_ngo_hem = 1 if ('ngõ' in str(prop_type).lower() or 'hẻm' in str(prop_type).lower()) else 0
    loai_can_ho = 1 if ('căn hộ' in str(prop_type).lower() or 'chung cư' in str(prop_type).lower()) else 0
    loai_biet_thu_lien_ke = 1 if ('biệt thự' in str(prop_type).lower() or 'liền kề' in str(prop_type).lower()) else 0
    
    input_df = pd.DataFrame([{
        'Diện tích m2': float(area_m2),
        'Số phòng ngủ': float(bedrooms) if bedrooms else np.nan,
        'Số tầng': float(floors) if floors else np.nan,
        'Thieu_So_Tang': 0 if floors else 1,
        'mat_tien_m': np.nan,
        'chieu_sau_m': np.nan,
        'ty_le_dai_rong': np.nan,
        'khu_vuc_noi_do': khu_vuc_noi_do,
        'co_so_do': co_so_do,
        'tong_dien_tich_san_m2': float(area_m2) * (float(floors) if floors else 1.0),
        'dien_tich_moi_phong_ngu_m2': float(area_m2) / float(bedrooms) if bedrooms and float(bedrooms) > 0 else np.nan,
        'mat_do_phong_ngu': float(bedrooms) / float(area_m2) if bedrooms and float(area_m2) > 0 else np.nan,
        'loai_nha_mat_pho': loai_nha_mat_pho,
        'loai_nha_ngo_hem': loai_nha_ngo_hem,
        'loai_can_ho': loai_can_ho,
        'loai_biet_thu_lien_ke': loai_biet_thu_lien_ke,
        'Quận': clean_district,
        'Loại hình nhà ở': prop_type.strip().lower(),
        'Giấy tờ pháp lý': legal.strip().lower(),
        'hinh_dang_dat': 'Không xác định',
        'phan_loai_tang': 'Thấp tầng (<=3)' if (floors and float(floors) <= 3) else ('Trung tầng (4-6)' if (floors and float(floors) <= 6) else 'Không rõ')
    }])
    
    # Dự đoán đơn giá (triệu/m2) từ Pipeline
    predicted_price_m2 = model.predict(input_df)[0]
    total_price_ty = (predicted_price_m2 * float(area_m2)) / 1000.0
    
    print(f"🏠 Thông tin bất động sản:")
    print(f"   - Khu vực: {clean_district.title()}")
    print(f"   - Diện tích: {area_m2} m²")
    print(f"   - Loại hình: {prop_type} | Pháp lý: {legal}")
    print(f"   - Thiết kế: {floors} tầng, {bedrooms} phòng ngủ")
    print("--------------------------------------------------")
    print(f"💰 Đơn giá ước tính (18 tháng gần nhất): ~ {predicted_price_m2:.1f} Triệu/m²")
    print(f"💎 Tổng giá trị ước tính: ~ {total_price_ty:.2f} Tỷ VNĐ")
    print("==================================================")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Cú pháp: python src/predict_bot.py <Diện_tích_m2> '<Tên_Quận>'")
        print("Ví dụ: python src/predict_bot.py 50 'Cầu Giấy'")
    else:
        area = float(sys.argv[1])
        district = sys.argv[2]
        predict_price(area, district)
