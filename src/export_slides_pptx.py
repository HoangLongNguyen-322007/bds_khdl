"""
Xuất toàn bộ Slide thuyết trình tiến độ KHDL (Tuần 1 - 10) sang định dạng Microsoft PowerPoint (.pptx).
Bản nâng cấp toàn diện:
- Hệ thống bố cục đa dạng (8 archetypes): 3 Cột Trụ, Phễu Quy Trình Ngang, Ma Trận 2x2, Hero Chart To Toàn Diện (7.5" - 11.7"), Bảng Toàn Màn Hình, Đối Sánh Trước/Sau.
- Tự động căn chỉnh tỷ lệ khung hình biểu đồ (Aspect Ratio Fitting), giữ biểu đồ lớn, sắc nét tuyệt đối.
- Cỡ chữ to rõ ràng đạt chuẩn hội trường: Tiêu đề 22-24pt, Thẻ 15-16pt, Gạch đầu dòng 13.5-14.5pt, Số liệu KPI 30-36pt.
- Đồng bộ thương hiệu Executive Luxury: Dark Blue (#0F2240) + Accent Gold (#D97706) + Arial font.
"""

import os
from PIL import Image
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG_DIR = os.path.join(ROOT_DIR, 'reports', 'figures')
OUTPUT_PPTX = os.path.join(ROOT_DIR, 'BAO_CAO_TIEN_DO_SLIDES.pptx')

# Bảng màu chủ đạo sang trọng & tương phản cao
NAVY = RGBColor(26, 54, 93)          # #1A365D - Navy quyền lực
DARK_BLUE = RGBColor(15, 34, 64)     # #0F2240 - Nền Header
GOLD = RGBColor(217, 119, 6)         # #D97706 - Gold điểm nhấn
CHARCOAL = RGBColor(30, 41, 59)      # #1E293B - Chữ chính dễ đọc
WHITE = RGBColor(255, 255, 255)
LIGHT_BG = RGBColor(248, 250, 252)   # #F8FAFC
LIGHT_BLUE = RGBColor(234, 243, 254) # #EAF3FE
BORDER_GRAY = RGBColor(203, 213, 225)# #CBD5E1
MUTED_TEXT = RGBColor(71, 85, 105)
GREEN_ACCENT = RGBColor(22, 101, 52) # #166534


def add_fitted_picture(slide, fig_path, left_in, top_in, max_w_in, max_h_in):
    """Thêm hình ảnh vào slide với tỷ lệ khung hình gốc (không méo), căn giữa trong khung bao."""
    if not os.path.exists(fig_path):
        return None
    with Image.open(fig_path) as img:
        img_w, img_h = img.size
    ratio = img_w / img_h
    box_ratio = max_w_in / max_h_in
    if ratio >= box_ratio:
        w = max_w_in
        h = max_w_in / ratio
        top = top_in + (max_h_in - h) / 2
        left = left_in
    else:
        h = max_h_in
        w = max_h_in * ratio
        left = left_in + (max_w_in - w) / 2
        top = top_in
    return slide.shapes.add_picture(fig_path, Inches(left), Inches(top), width=Inches(w), height=Inches(h))


def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def add_header(slide, title_text):
        """Header tinh gọn, font chữ 22pt bold, dải viền Gold tinh tế."""
        header_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.05))
        header_shape.fill.solid()
        header_shape.fill.fore_color.rgb = DARK_BLUE
        header_shape.line.fill.background()

        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(1.02), Inches(13.333), Inches(0.04))
        bar.fill.solid()
        bar.fill.fore_color.rgb = GOLD
        bar.line.fill.background()

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.16), Inches(11.733), Inches(0.72))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.name = "Arial"
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = WHITE
        p_title.vertical_anchor = MSO_ANCHOR.MIDDLE

    def add_card(slide, left, top, width, height, title=None, header_bg=NAVY, header_color=WHITE, bg_color=WHITE, border_color=BORDER_GRAY):
        """Hộp thẻ chứa nội dung phẳng, viền xám tinh tế, có thanh tiêu đề phân cấp nổi bật."""
        base_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
        base_shape.fill.solid()
        base_shape.fill.fore_color.rgb = bg_color
        base_shape.line.color.rgb = border_color
        base_shape.line.width = Pt(1)

        body_top = top
        body_height = height

        if title:
            # Tự động tính chiều cao header nếu tiêu đề dài để không bị tràn chữ
            is_long = len(title) > 28 or (width < Inches(4.5) and len(title) > 22)
            h_height = Inches(0.66) if is_long else Inches(0.48)
            f_size = Pt(12.5) if is_long else Pt(13.5)

            hbar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, h_height)
            hbar.fill.solid()
            hbar.fill.fore_color.rgb = header_bg
            hbar.line.fill.background()

            tb_h = slide.shapes.add_textbox(left + Inches(0.18), top + Inches(0.04), width - Inches(0.36), h_height - Inches(0.08))
            tf_h = tb_h.text_frame
            tf_h.word_wrap = True
            p_h = tf_h.paragraphs[0]
            p_h.text = title
            p_h.font.name = "Arial"
            p_h.font.size = f_size
            p_h.font.bold = True
            p_h.font.color.rgb = header_color
            p_h.vertical_anchor = MSO_ANCHOR.MIDDLE

            body_top = top + h_height
            body_height = height - h_height

        tb_body = slide.shapes.add_textbox(left + Inches(0.20), body_top + Inches(0.10), width - Inches(0.40), body_height - Inches(0.20))
        tf_body = tb_body.text_frame
        tf_body.word_wrap = True
        return tf_body

    def create_left_chart_slide(slide, title, fig_path, badge_title, bullets):
        """Layout A: Hero Chart lớn bên trái (7.4" x 5.65") + Khung Insight bên phải (chữ 13 - 14pt)."""
        add_header(slide, title)

        fig_w, fig_h = 7.4, 5.65
        fig_card = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.35), Inches(fig_w), Inches(fig_h))
        fig_card.fill.solid()
        fig_card.fill.fore_color.rgb = WHITE
        fig_card.line.color.rgb = BORDER_GRAY
        fig_card.line.width = Pt(1)

        add_fitted_picture(slide, fig_path, 0.88, 1.43, fig_w - 0.16, fig_h - 0.16)

        right_left = 0.8 + fig_w + 0.25
        right_w = 13.333 - 0.8 - right_left
        tf_right = add_card(slide, Inches(right_left), Inches(1.35), Inches(right_w), Inches(fig_h), badge_title, header_bg=NAVY)

        for idx, (b_title, b_desc) in enumerate(bullets):
            pt = tf_right.paragraphs[0] if idx == 0 else tf_right.add_paragraph()
            pt.text = b_title
            pt.font.name = "Arial"
            pt.font.size = Pt(13.5)
            pt.font.bold = True
            pt.font.color.rgb = GOLD
            if idx > 0:
                pt.space_before = Pt(10)

            pd = tf_right.add_paragraph()
            pd.text = b_desc
            pd.font.name = "Arial"
            pd.font.size = Pt(12.5)
            pd.font.color.rgb = CHARCOAL
            pd.space_before = Pt(3)

    def create_top_chart_slide(slide, title, fig_path, cards_info):
        """Layout B: Hero Chart rộng toàn màn hình ở trên (11.73" x 3.85") + 3 Thẻ Insight bên dưới (chữ 13pt)."""
        add_header(slide, title)

        chart_w, chart_h = 11.733, 3.85
        chart_card = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.35), Inches(chart_w), Inches(chart_h))
        chart_card.fill.solid()
        chart_card.fill.fore_color.rgb = WHITE
        chart_card.line.color.rgb = BORDER_GRAY
        chart_card.line.width = Pt(1)

        add_fitted_picture(slide, fig_path, 0.88, 1.43, chart_w - 0.16, chart_h - 0.16)

        bottom_top = 1.35 + chart_h + 0.20
        bottom_h = 7.5 - bottom_top - 0.35
        card_w = (chart_w - 0.40) / 3.0

        for idx, (c_title, c_desc) in enumerate(cards_info):
            c_left = 0.8 + idx * (card_w + 0.20)
            tf_c = add_card(slide, Inches(c_left), Inches(bottom_top), Inches(card_w), Inches(bottom_h), c_title, header_bg=NAVY)
            p = tf_c.paragraphs[0]
            p.text = c_desc
            p.font.name = "Arial"
            p.font.size = Pt(13)
            p.font.color.rgb = CHARCOAL
            p.space_before = Pt(4)

    # ==========================================
    # SLIDE 1: TRANG BÌA (EXECUTIVE LUXURY COVER)
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = DARK_BLUE
    bg1.line.fill.background()

    gold_stripe = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.1), Inches(11.733), Inches(0.06))
    gold_stripe.fill.solid()
    gold_stripe.fill.fore_color.rgb = GOLD
    gold_stripe.line.fill.background()

    tb_t = s1.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(11.733), Inches(2.2))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True

    p0 = tf_t.paragraphs[0]
    p0.text = "BÁO CÁO TIẾN ĐỘ DỰ ÁN KHOA HỌC DỮ LIỆU"
    p0.font.name = "Arial"
    p0.font.size = Pt(32)
    p0.font.bold = True
    p0.font.color.rgb = GOLD

    p1 = tf_t.add_paragraph()
    p1.text = "PHÂN TÍCH KHÁM PHÁ, SUY LUẬN THỐNG KÊ & MÔ HÌNH HÓA GIÁ BẤT ĐỘNG SẢN HÀ NỘI"
    p1.font.name = "Arial"
    p1.font.size = Pt(19)
    p1.font.bold = True
    p1.font.color.rgb = WHITE
    p1.space_before = Pt(12)

    p2 = tf_t.add_paragraph()
    p2.text = "Dữ liệu thực nghiệm: 33.456 tin rao bán • Tiền xử lý & Làm sạch • Thống kê suy luận • Mô hình hóa & Đánh giá"
    p2.font.name = "Arial"
    p2.font.size = Pt(13.5)
    p2.font.color.rgb = RGBColor(203, 213, 225)
    p2.space_before = Pt(8)

    # Khung Giảng viên
    c_gv = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(4.3), Inches(5.67), Inches(2.3))
    c_gv.fill.solid()
    c_gv.fill.fore_color.rgb = NAVY
    c_gv.line.color.rgb = GOLD
    c_gv.line.width = Pt(1)
    tf_gv = c_gv.text_frame
    tf_gv.word_wrap = True
    p_gv_h = tf_gv.paragraphs[0]
    p_gv_h.text = "🏛️ HỘI ĐỒNG & GIẢNG VIÊN HƯỚNG DẪN"
    p_gv_h.font.name = "Arial"
    p_gv_h.font.size = Pt(14.5)
    p_gv_h.font.bold = True
    p_gv_h.font.color.rgb = GOLD
    p_gv_c = tf_gv.add_paragraph()
    p_gv_c.text = "• Môn học: Khoa Học Dữ Liệu Thực Hành (Tuần 1 - 10)\n• Bộ môn: Khoa Học Dữ Liệu & Trí Tuệ Nhân Tạo\n• Mục tiêu: Nghiệm thu báo cáo tiến độ & Mô hình hóa định giá BĐS"
    p_gv_c.font.name = "Arial"
    p_gv_c.font.size = Pt(13)
    p_gv_c.font.color.rgb = WHITE
    p_gv_c.space_before = Pt(10)

    # Khung Sinh viên
    c_sv = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.86), Inches(4.3), Inches(5.67), Inches(2.3))
    c_sv.fill.solid()
    c_sv.fill.fore_color.rgb = NAVY
    c_sv.line.color.rgb = GOLD
    c_sv.line.width = Pt(1)
    tf_sv = c_sv.text_frame
    tf_sv.word_wrap = True
    p_sv_h = tf_sv.paragraphs[0]
    p_sv_h.text = "👨‍💻 NHÓM SINH VIÊN THỰC HIỆN DỰ ÁN"
    p_sv_h.font.name = "Arial"
    p_sv_h.font.size = Pt(14.5)
    p_sv_h.font.bold = True
    p_sv_h.font.color.rgb = GOLD
    p_sv_c = tf_sv.add_paragraph()
    p_sv_c.text = "• Sinh viên thực hiện: Hoàng Long & Cộng sự\n• Chuyên ngành: Khoa Học Dữ Liệu / Trí Tuệ Nhân Tạo\n• Thời gian nghiệm thu: Tháng 10/2026\n• Phạm vi nghiên cứu: 30 Quận / Huyện TP. Hà Nội"
    p_sv_c.font.name = "Arial"
    p_sv_c.font.size = Pt(13)
    p_sv_c.font.color.rgb = WHITE
    p_sv_c.space_before = Pt(10)

    # ==========================================
    # SLIDE 2: BỐI CẢNH & 3 BÀI TOÁN KINH DOANH (LAYOUT: 3 CỘT TRỤ)
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Bối Cảnh Thị Trường & 3 Bài Toán Khoa Học Dữ Liệu")

    col_w = Inches(3.64)
    gap = Inches(0.40)
    top_pos = Inches(1.35)
    h_pos = Inches(5.65)

    pillars = [
        ("01", "BÀI TOÁN 1: DỰ BÁO GIÁ", "GIẢI MÃ TÍNH PHI TUYẾN", [
            ("Thực trạng thị trường:", "Thị trường BĐS Hà Nội biến động mạnh, chênh lệch giữa các quận lên tới 10 lần."),
            ("Mục tiêu kỹ thuật:", "Xây dựng thuật toán Machine Learning (GBDT, Random Forest) dự báo đơn giá m² chính xác."),
            ("Chỉ số kỳ vọng:", "Đạt sai số MAE < 28 triệu/m² và hệ số xác định R² > 0.40 trên tập kiểm thử độc lập.")
        ]),
        ("02", "BÀI TOÁN 2: THẨM ĐỊNH", "QUẢN TRỊ RỦI RO TÍN DỤNG", [
            ("Thực trạng tài chính:", "Ngân hàng và nhà đầu tư đối mặt rủi ro nợ xấu khi định giá tài sản sai lệch."),
            ("Mục tiêu kỹ thuật:", "Thống kê suy luận (Welch's T-Test, ANOVA) và khoảng tin cậy 95% Bootstrap."),
            ("Chỉ số kỳ vọng:", "Xác lập biên độ định giá an toàn (Lower-Upper Bound) cho 30 Quận/Huyện.")
        ]),
        ("03", "BÀI TOÁN 3: ĐẦU TƯ", "PHÂN KHÚC & QUẬN SONG SINH", [
            ("Thực trạng đầu tư:", "Nhà đầu tư khó nhận diện phân khúc giá và các khu vực có tỷ suất sinh lời tương đương."),
            ("Mục tiêu kỹ thuật:", "Phân tích phương sai ANOVA & Tukey HSD tìm kiếm 9 cặp quận tương đồng giá (Substitute Assets)."),
            ("Chỉ số kỳ vọng:", "Xác lập bản đồ phân khúc giá 30 Quận/Huyện phục vụ chiến lược dịch chuyển dòng vốn đầu tư.")
        ])
    ]

    for idx, (p_num, p_title, p_sub, p_items) in enumerate(pillars):
        c_left = Inches(0.8) + idx * (col_w + gap)
        tf_p = add_card(s2, c_left, top_pos, col_w, h_pos, p_title, header_bg=NAVY)

        p_sub_h = tf_p.paragraphs[0]
        p_sub_h.text = f"🎯 {p_sub}"
        p_sub_h.font.name = "Arial"
        p_sub_h.font.size = Pt(13.5)
        p_sub_h.font.bold = True
        p_sub_h.font.color.rgb = GOLD

        for it_idx, (it_lbl, it_val) in enumerate(p_items):
            pt = tf_p.add_paragraph()
            pt.text = f"• {it_lbl}"
            pt.font.name = "Arial"
            pt.font.size = Pt(13)
            pt.font.bold = True
            pt.font.color.rgb = NAVY
            pt.space_before = Pt(14)

            pd = tf_p.add_paragraph()
            pd.text = it_val
            pd.font.name = "Arial"
            pd.font.size = Pt(12.5)
            pd.font.color.rgb = CHARCOAL
            pd.space_before = Pt(3)

    # ==========================================
    # SLIDE 3: PHỄU SÀNG LỌC & LÀM SẠCH DỮ LIỆU (LAYOUT: FUNNEL FLOW + BẢNG CHI TIẾT)
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Phễu Sàng Lọc & Làm Sạch Dữ Liệu (33.456 ➔ 21.142 Bản Ghi)")

    # 4 Khối Funnel ngang ở trên
    step_w = Inches(2.78)
    step_gap = Inches(0.20)
    funnel_steps = [
        ("BƯỚC 1: DỮ LIỆU THÔ", "33.456", "100.0%", "Thu thập đa nguồn"),
        ("BƯỚC 2: LỌC MISSING", "29.478", "88.1%", "Loại khuyết giá/diện tích"),
        ("BƯỚC 3: XỬ LÝ OUTLIERS", "25.500", "76.2%", "Cắt tỉa IQR & Z-score"),
        ("BƯỚC 4: DỮ LIỆU SẠCH", "21.142", "63.2%", "Chuẩn hóa hoàn tất")
    ]
    for s_idx, (s_name, s_num, s_pct, s_note) in enumerate(funnel_steps):
        s_left = Inches(0.8) + s_idx * (step_w + step_gap)
        sc = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, s_left, Inches(1.35), step_w, Inches(1.50))
        sc.fill.solid()
        sc.fill.fore_color.rgb = DARK_BLUE if s_idx == 3 else NAVY
        sc.line.color.rgb = GOLD if s_idx == 3 else BORDER_GRAY
        sc.line.width = Pt(1.5) if s_idx == 3 else Pt(1)

        tf_sc = sc.text_frame
        tf_sc.word_wrap = True
        p_sc0 = tf_sc.paragraphs[0]
        p_sc0.text = s_name
        p_sc0.font.name = "Arial"
        p_sc0.font.size = Pt(11)
        p_sc0.font.bold = True
        p_sc0.font.color.rgb = GOLD

        p_sc1 = tf_sc.add_paragraph()
        p_sc1.text = s_num
        p_sc1.font.name = "Arial"
        p_sc1.font.size = Pt(24)
        p_sc1.font.bold = True
        p_sc1.font.color.rgb = WHITE
        p_sc1.space_before = Pt(2)

        p_sc2 = tf_sc.add_paragraph()
        p_sc2.text = f"{s_pct} • {s_note}"
        p_sc2.font.name = "Arial"
        p_sc2.font.size = Pt(11)
        p_sc2.font.color.rgb = RGBColor(226, 232, 240)
        p_sc2.space_before = Pt(2)

    # Bảng chi tiết 4 lỗi bên dưới
    tbl_shape = s3.shapes.add_table(5, 4, Inches(0.8), Inches(3.10), Inches(11.733), Inches(3.90))
    table = tbl_shape.table
    table.columns[0].width = Inches(2.20)
    table.columns[1].width = Inches(1.50)
    table.columns[2].width = Inches(1.30)
    table.columns[3].width = Inches(6.733)

    data_errors = [
        ["Hạng Mục Xử Lý", "Bản Ghi Loại", "Tỷ Lệ %", "Nguyên Nhân Thực Tế & Tác Động Thuật Toán"],
        ["Thiếu thông tin (Missing)", "3.978", "11.9%", "Tin rao ghi 'Thỏa thuận', thiếu diện tích/giá -> Buộc loại bỏ để tránh biến thiên giả."],
        ["Bất thường (Outliers)", "3.978", "11.9%", "Tin rác (diện tích 1m², giá 1 tỷ/m² hoặc 1 triệu) -> Lọc theo IQR (10-500m², 15-500 tr/m²)."],
        ["Tin trùng lặp (Duplicates)", "2.358", "7.0%", "Một BĐS được nhiều môi giới đăng lại nhiều lần -> Giữ bản ghi duy nhất theo địa chỉ & diện tích."],
        ["Nhiễu mô tả (Noise Text)", "2.000", "6.0%", "Chữ viết hoa lẫn lộn, ký hiệu lạ -> Xóa bỏ ký tự thừa, chuẩn hóa về dạng chữ số chuẩn."]
    ]

    for r_idx, row in enumerate(data_errors):
        for c_idx, val in enumerate(row):
            cell = table.cell(r_idx, c_idx)
            cell.text = val
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = cell.text_frame.paragraphs[0]
            p.font.name = "Arial"
            if r_idx == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = NAVY
                p.font.bold = True
                p.font.size = Pt(13)
                p.font.color.rgb = WHITE
                p.alignment = PP_ALIGN.CENTER
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = WHITE if r_idx % 2 == 1 else LIGHT_BG
                p.font.size = Pt(12.5)
                p.font.color.rgb = CHARCOAL
                if c_idx in [1, 2]:
                    p.alignment = PP_ALIGN.CENTER
                    p.font.bold = True

    # ==========================================
    # SLIDE 4: KỸ NGHỆ ĐẶC TRƯNG (LAYOUT: 3 CỘT TRỤ ĐẶC TRƯNG)
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Kỹ Nghệ Đặc Trưng 3 Trụ Cột (Feature Engineering)")

    feat_cols = [
        ("KHÔNG GIAN & VỊ TRÍ", [
            ("Mã hóa One-Hot 30 Quận/Huyện:", "Chuyển đổi biến phân loại vị trí thành vector nhị phân, loại bỏ thứ tự giả định sai lệch."),
            ("Khoảng cách tới Trung tâm:", "Tính bán kính hình học từ tọa độ tâm quận tới Hồ Hoàn Kiếm (0km - 35km)."),
            ("Phân tầng 3 Vùng Kinh Tế:", "Lõi di sản (Hoàn Kiếm, Ba Đình), Cận trung tâm (Cầu Giấy, Đống Đa), và Vành đai ven đô.")
        ]),
        ("QUY MÔ HÌNH HỌC", [
            ("Chuẩn hóa Đơn giá m²:", "Tạo biến mục tiêu chuẩn hóa `price_per_m2 = total_price / area` giúp loại trừ sai lệch diện tích."),
            ("Tỷ lệ Chiều rộng / Chiều sâu:", "Nhận diện thế đất vuông vức hay nở hậu, ảnh hưởng trực tiếp đến giá trị thương mại."),
            ("Tương tác Diện tích & Tầng:", "Tính tổng diện tích sàn sử dụng thực tế (GFA = area * floors).")
        ]),
        ("PHÁP LÝ & TIỆN ÍCH", [
            ("Trạng thái Pháp lý:", "Biến nhị phân nhận diện Sổ đỏ / Sổ hồng sẵn sàng giao dịch so với nhà đang chờ cấp."),
            ("Vị trí Mặt tiền vs Ngõ hẻm:", "Biến phân loại `is_frontage` phân tách rõ BĐS kinh doanh và BĐS an cư trong ngõ ngách."),
            ("Khả năng tiếp cận Giao thông:", "Độ rộng ngõ vào (ô tô đỗ cửa, tránh nhau, xe máy), quyết định thanh khoản.")
        ])
    ]

    for idx, (f_title, f_items) in enumerate(feat_cols):
        c_left = Inches(0.8) + idx * (col_w + gap)
        tf_f = add_card(s4, c_left, top_pos, col_w, h_pos, f"NHÓM {idx+1}: {f_title}", header_bg=NAVY)

        for it_idx, (it_lbl, it_val) in enumerate(f_items):
            pt = tf_f.paragraphs[0] if it_idx == 0 else tf_f.add_paragraph()
            pt.text = f"• {it_lbl}"
            pt.font.name = "Arial"
            pt.font.size = Pt(13.5)
            pt.font.bold = True
            pt.font.color.rgb = GOLD
            if it_idx > 0:
                pt.space_before = Pt(18)

            pd = tf_f.add_paragraph()
            pd.text = it_val
            pd.font.name = "Arial"
            pd.font.size = Pt(12.5)
            pd.font.color.rgb = CHARCOAL
            pd.space_before = Pt(4)

    # ==========================================
    # SLIDE 5: THIẾT KẾ SCIKIT-LEARN PIPELINE (LAYOUT: HORIZONTAL FLOW + 2 NGUYÊN TẮC)
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Thiết Kế Scikit-Learn Pipeline & Chống Rò Rỉ Dữ Liệu")

    # Flow ngang 4 block
    pipe_w = Inches(2.78)
    pipe_gap = Inches(0.20)
    pipe_steps = [
        ("ĐẦU VÀO DỮ LIỆU", "Raw DataFrame", "21.142 bản ghi sạch"),
        ("TIỀN XỬ LÝ ĐẶC TRƯNG", "ColumnTransformer", "Imputer + Scaler + OneHot"),
        ("MÔ HÌNH DỰ BÁO", "GBDT / Random Forest", "Huấn luyện trên X_train"),
        ("ĐÁNH GIÁ ĐỘC LẬP", "K-Fold Cross-Val", "5 Folds kiểm thử không rò rỉ")
    ]
    for p_idx, (p_st, p_md, p_nt) in enumerate(pipe_steps):
        p_left = Inches(0.8) + p_idx * (pipe_w + pipe_gap)
        box = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, p_left, Inches(1.35), pipe_w, Inches(1.65))
        box.fill.solid()
        box.fill.fore_color.rgb = DARK_BLUE if p_idx == 2 else NAVY
        box.line.color.rgb = GOLD if p_idx == 2 else BORDER_GRAY
        box.line.width = Pt(1.5) if p_idx == 2 else Pt(1)

        tf_b = box.text_frame
        tf_b.word_wrap = True
        pb0 = tf_b.paragraphs[0]
        pb0.text = f"BƯỚC {p_idx+1}: {p_st}"
        pb0.font.name = "Arial"
        pb0.font.size = Pt(10.5)
        pb0.font.bold = True
        pb0.font.color.rgb = GOLD

        pb1 = tf_b.add_paragraph()
        pb1.text = p_md
        pb1.font.name = "Arial"
        pb1.font.size = Pt(16)
        pb1.font.bold = True
        pb1.font.color.rgb = WHITE
        pb1.space_before = Pt(4)

        pb2 = tf_b.add_paragraph()
        pb2.text = p_nt
        pb2.font.name = "Arial"
        pb2.font.size = Pt(11)
        pb2.font.color.rgb = RGBColor(226, 232, 240)
        pb2.space_before = Pt(4)

    # 2 Thẻ nguyên tắc bên dưới
    half_w = Inches(5.67)
    gap_half = Inches(0.393)
    tf_l5 = add_card(s5, Inches(0.8), Inches(3.25), half_w, Inches(3.75), "TRIỆT TIÊU RÒ RỈ DỮ LIỆU (DATA LEAKAGE)", header_bg=NAVY)
    l5_items = [
        ("Nguyên tắc 'Chỉ học trên Train':", "Toàn bộ tham số trung bình, trung vị (Imputer) và độ lệch chuẩn (StandardScaler) chỉ được tính trên tập Train."),
        ("Độc lập kiểm thử hoàn toàn:", "Tập Test được giữ nguyên vẹn như dữ liệu tương lai chưa từng thấy, chỉ biến đổi bằng `.transform()`."),
        ("Độ tin cậy của chỉ số:", "Đảm bảo điểm số R² và sai số MAE phản ánh chính xác năng lực thực chiến, không bị thổi phồng giả tạo.")
    ]
    for it_idx, (it_h, it_b) in enumerate(l5_items):
        pt = tf_l5.paragraphs[0] if it_idx == 0 else tf_l5.add_paragraph()
        pt.text = f"• {it_h}"
        pt.font.name = "Arial"
        pt.font.size = Pt(13)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(12)
        pd = tf_l5.add_paragraph()
        pd.text = it_b
        pd.font.name = "Arial"
        pd.font.size = Pt(12.5)
        pd.font.color.rgb = CHARCOAL
        pd.space_before = Pt(2)

    tf_r5 = add_card(s5, Inches(0.8) + half_w + gap_half, Inches(3.25), half_w, Inches(3.75), "ĐÓNG GÓI SẢN PHẨM SẴN SÀNG TRIỂN KHAI", header_bg=NAVY)
    r5_items = [
        ("Tính nhất quán (Reproducibility):", "Pipeline tích hợp đóng gói toàn bộ luồng xử lý và mô hình thành 1 tệp nhị phân duy nhất (`pipeline.pkl`)."),
        ("Khả năng mở rộng (Scalability):", "Dễ dàng thay thế mô hình lõi từ GBDT sang LightGBM hoặc XGBoost mà không làm gãy luồng xử lý."),
        ("Sẵn sàng cho Suy Diễn (Inference Pipeline):", "Hàm pipeline.predict() nhận trực tiếp dữ liệu thô, tự động tiền xử lý và dự báo giá trong 0.05 giây.")
    ]
    for it_idx, (it_h, it_b) in enumerate(r5_items):
        pt = tf_r5.paragraphs[0] if it_idx == 0 else tf_r5.add_paragraph()
        pt.text = f"• {it_h}"
        pt.font.name = "Arial"
        pt.font.size = Pt(13)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(12)
        pd = tf_r5.add_paragraph()
        pd.text = it_b
        pd.font.name = "Arial"
        pd.font.size = Pt(12.5)
        pd.font.color.rgb = CHARCOAL
        pd.space_before = Pt(2)

    # ==========================================
    # SLIDE 6: THỐNG KÊ MÔ TẢ 4 HỌ DỮ LIỆU (LAYOUT: MA TRẬN 2x2)
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Thống Kê Mô Tả 4 Họ Dữ Liệu Bất Động Sản")

    m_w = Inches(5.67)
    m_h = Inches(2.65)
    m_gap_x = Inches(0.393)
    m_gap_y = Inches(0.35)

    matrix_cards = [
        ("HỌ 1: ĐỊNH DANH & LOẠI HÌNH BĐS", [
            ("Quy mô mẫu:", "21.142 bản ghi sạch đại diện toàn diện thị trường Hà Nội."),
            ("Cơ cấu loại hình:", "68.4% Nhà riêng / Liền kề, 22.1% Căn hộ chung cư, 9.5% Nhà mặt phố thương mại."),
            ("Ý nghĩa phân tích:", "Cần phân tầng mô hình theo loại hình để đạt độ chính xác tối ưu.")
        ]),
        ("HỌ 2: KHÔNG GIAN ĐỊA LÝ (30 QUẬN/HUYỆN)", [
            ("Mật độ tập trung:", "54% giao dịch tập trung tại Cầu Giấy, Đống Đa, Nam Từ Liêm, Hà Đông."),
            ("Bán kính đô thị:", "Từ 0km (Hoàn Kiếm) đến 35km (Ba Vì, Sóc Sơn)."),
            ("Ý nghĩa phân tích:", "Vị trí địa lý giải thích tới 28% độ biến thiên giá trị tài sản.")
        ]),
        ("HỌ 3: QUY MÔ HÌNH HỌC (DIỆN TÍCH & MẶT TIỀN)", [
            ("Diện tích đất:", "Trung vị 52 m² (IQR: 38 - 85 m²), trung bình 64.2 m²."),
            ("Chiều rộng mặt tiền:", "Trung vị 4.2m, dao động phổ biến từ 3.2m đến 5.5m."),
            ("Ý nghĩa phân tích:", "Diện tích tương quan mạnh nhất với tổng giá trị (r = 0.72).")
        ]),
        ("HỌ 4: PHÂN PHỐI GIÁ & ĐƠN GIÁ M²", [
            ("Tổng giá trị tài sản:", "Trung vị 4.8 tỷ VNĐ (Dao động từ 1.2 tỷ đến 35 tỷ sau lọc)."),
            ("Đơn giá m²:", "Trung vị 92.5 triệu/m², phân phối lệch phải (Skewness = 3.84)."),
            ("Ý nghĩa phân tích:", "Cần log-transform để đưa phân phối về chuẩn hóa Gauss.")
        ])
    ]

    for idx, (m_title, m_items) in enumerate(matrix_cards):
        row_i = idx // 2
        col_i = idx % 2
        m_left = Inches(0.8) + col_i * (m_w + m_gap_x)
        m_top = Inches(1.35) + row_i * (m_h + m_gap_y)

        tf_m = add_card(s6, m_left, m_top, m_w, m_h, m_title, header_bg=NAVY)
        for it_idx, (it_h, it_b) in enumerate(m_items):
            pt = tf_m.paragraphs[0] if it_idx == 0 else tf_m.add_paragraph()
            pt.text = f"• {it_h} "
            pt.font.name = "Arial"
            pt.font.size = Pt(12.5)
            pt.font.bold = True
            pt.font.color.rgb = GOLD
            if it_idx > 0:
                pt.space_before = Pt(8)

            pd = pt
            run_b = pd.add_run()
            run_b.text = it_b
            run_b.font.name = "Arial"
            run_b.font.size = Pt(12)
            run_b.font.bold = False
            run_b.font.color.rgb = CHARCOAL

    # ==========================================
    # SLIDE 7: [BIỂU ĐỒ 01] MA TRẬN TƯƠNG QUAN PEARSON (LAYOUT: LEFT HERO CHART)
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    fig1_path = os.path.join(FIG_DIR, "01_correlation_heatmap.png")
    create_left_chart_slide(
        s7,
        "Biểu Đồ 1: Ma Trận Tương Quan Tuyến Tính Giữa Các Đặc Trưng",
        fig1_path,
        "TƯƠNG QUAN TUYẾN TÍNH (BĐ 01)",
        [
            ("Tác Dụng & Mục Đích Biểu Đồ:",
             "Đo lường mức độ liên kết tuyến tính (hệ số Pearson r) giữa các biến định lượng: Diện tích, Số phòng ngủ, Số tầng, Mặt tiền và Giá."),
            ("Phát Hiện Trọng Tâm (Key Insight):",
             "Diện tích (area) có tương quan dương mạnh nhất với Tổng giá trị tài sản (r = 0.72), khẳng định quy mô diện tích là nhân tố gốc chi phối giá."),
            ("Cảnh Báo Đa Cộng Tuyến (Multicollinearity):",
             "Số phòng ngủ và Diện tích có mức tương quan r = 0.68 -> Cần kiểm soát chỉ số VIF để tránh mô hình tuyến tính bị thổi phồng phương sai."),
            ("Ý Nghĩa Ứng Dụng Thực Tiễn:",
             "Loại bỏ các biến dư thừa có tương quan nội bộ cao, giữ lại các đặc trưng độc lập mạnh nhất cho thuật toán Machine Learning.")
        ]
    )

    # ==========================================
    # SLIDE 8: [BIỂU ĐỒ 02] PHÂN PHỐI GIÁ & LOGARIT (LAYOUT: TOP-WIDE HERO CHART)
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    fig2_path = os.path.join(FIG_DIR, "02_price_distribution.png")
    create_top_chart_slide(
        s8,
        "Biểu Đồ 2: Phân Phối Giá BĐS & Đột Phá Sau Biến Đổi Logarit",
        fig2_path,
        [
            ("1. PHÂN PHỐI GỐC (LỆCH PHẢI)",
             "Độ lệch Skewness ban đầu = 3.84 cực kỳ cao. Đa số BĐS tập trung ở mức 2 - 6 tỷ nhưng đuôi kéo dài tới 35 tỷ, gây nhiễu sai số lớn."),
            ("2. GIẢI PHÁP LOG-TRANSFORM",
             "Biến đổi logarit đưa Skewness về 0.18, nén biên độ dao động và tạo ra đường cong phân phối chuẩn đối xứng lý tưởng (chuông Gauss)."),
            ("3. Ý NGHĨA KHOA HỌC DỮ LIỆU",
             "Giúp các mô hình nhạy cảm với ngoại lệ (Linear, Ridge) đạt độ hội tụ ổn định, giảm hiện tượng phương sai dư sai thay đổi (Heteroscedasticity).")
        ]
    )

    # ==========================================
    # SLIDE 9: [BIỂU ĐỒ 03] TÁN XẠ MẶT TIỀN VS GIÁ (LAYOUT: TOP-WIDE HERO CHART)
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    fig3_path = os.path.join(FIG_DIR, "03_price_vs_area_scatter.png")
    create_top_chart_slide(
        s9,
        "Biểu Đồ 3: Tương Quan Tán Xạ Giữa Diện Tích & Giá Trị BĐS",
        fig3_path,
        [
            ("1. QUAN HỆ ĐỒNG BIẾN RÕ NÉT",
             "Đường hồi quy thực nghiệm có độ dốc dương rõ ràng: Diện tích càng lớn thì tổng giá trị tài sản càng tăng theo quy luật tuyến tính chủ đạo."),
            ("2. TÍNH PHI TUYẾN & ĐỘ PHÂN TÁN",
             "Tại cùng diện tích 50m², giá nhà dao động mạnh từ 3 tỷ (ngoại thành) đến 15 tỷ (trung tâm), phản ánh trọng số cực lớn của vị trí địa lý."),
            ("3. KHUYẾN NGHỊ MÔ HÌNH HÓA",
             "Thuật toán tuyến tính đơn thuần không thể bao quát toàn bộ độ phân tán này; bắt buộc phải dùng Gradient Boosting để bắt tương tác phi tuyến.")
        ]
    )

    # ==========================================
    # SLIDE 10: [BIỂU ĐỒ 04] BOXPLOT GIÁ 30 QUẬN HUYỆN (LAYOUT: TOP-WIDE HERO CHART)
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    fig4_path = os.path.join(FIG_DIR, "04_price_by_district_boxplot.png")
    create_top_chart_slide(
        s10,
        "Biểu Đồ 4: Phân Bố Đơn Giá (triệu/m²) Chi Tiết 30 Quận / Huyện Hà Nội",
        fig4_path,
        [
            ("1. TOP 3 QUẬN ĐẮT ĐỎ NHẤT",
             "Hoàn Kiếm (trung vị >280 tr/m²), Ba Đình (195 tr/m²), Hai Bà Trưng (175 tr/m²). Nguồn cung khan hiếm, giá trị bảo toàn cao."),
            ("2. TOP 3 VÙNG GIÁ DỄ TIẾP CẬN",
             "Ba Vì (22 tr/m²), Sóc Sơn (26 tr/m²), Mê Linh (31 tr/m²). Biên độ tăng trưởng dài hạn lớn gắn liền quy hoạch hạ tầng vành đai."),
            ("3. ĐỘ PHÂN TÁN NỘI BỘ (IQR)",
             "Các quận trung tâm có 'râu hộp' (whisker) rất dài, phản ánh sự phân hóa sâu sắc giữa phân khúc nhà mặt phố và nhà ngõ sâu.")
        ]
    )

    # ==========================================
    # SLIDE 11: THỬ NGHIỆM MÔ HÌNH HÓA (LAYOUT: FULL-WIDTH TABLE + BOTTOM BANNER)
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Thử Nghiệm & So Sánh 5 Mô Hình Machine Learning")

    t11_shape = s11.shapes.add_table(6, 6, Inches(0.8), Inches(1.35), Inches(11.733), Inches(3.60))
    t11 = t11_shape.table
    t11.columns[0].width = Inches(2.333)
    t11.columns[1].width = Inches(1.50)
    t11.columns[2].width = Inches(1.80)
    t11.columns[3].width = Inches(1.80)
    t11.columns[4].width = Inches(1.80)
    t11.columns[5].width = Inches(2.50)

    models_data = [
        ["Mô Hình ML", "R² Score", "MAE (tr/m²)", "RMSE (tr/m²)", "Thời Gian Train", "Đánh Giá Toàn Diện"],
        ["Linear Regression", "0.3820", "28.45", "38.12", "0.15 giây", "Baseline cơ bản; sai số cao ở phân khúc đắt."],
        ["Ridge Regression (L2)", "0.3824", "28.42", "38.10", "0.18 giây", "Khống chế đa cộng tuyến nhưng vẫn tuyến tính."],
        ["Decision Tree", "0.3150", "30.12", "41.50", "0.45 giây", "Dễ quá khớp (Overfitting), ranh giới cắt bậc thang."],
        ["Gradient Boosting (GBDT)", "0.4390", "26.07", "35.80", "1.20 giây", "🏆 TỐT NHẤT TOÀN DIỆN: R² cao nhất, MAE thấp nhất."],
        ["Random Forest", "0.4280", "26.55", "36.20", "2.85 giây", "Ổn định cao nhưng thời gian train gấp 2.4 lần GBDT."]
    ]

    for r_idx, row in enumerate(models_data):
        for c_idx, val in enumerate(row):
            cell = t11.cell(r_idx, c_idx)
            cell.text = val
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = cell.text_frame.paragraphs[0]
            p.font.name = "Arial"
            if r_idx == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = NAVY
                p.font.bold = True
                p.font.size = Pt(13)
                p.font.color.rgb = WHITE
                p.alignment = PP_ALIGN.CENTER
            elif r_idx == 4:
                cell.fill.solid()
                cell.fill.fore_color.rgb = LIGHT_BLUE
                p.font.bold = True
                p.font.size = Pt(12.5)
                p.font.color.rgb = NAVY
                if c_idx in [1, 2, 3, 4]:
                    p.alignment = PP_ALIGN.CENTER
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = WHITE if r_idx % 2 == 1 else LIGHT_BG
                p.font.size = Pt(12)
                p.font.color.rgb = CHARCOAL
                if c_idx in [1, 2, 3, 4]:
                    p.alignment = PP_ALIGN.CENTER

    # Banner Takeaway ở đáy
    b_banner = s11.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(5.25), Inches(11.733), Inches(1.75))
    b_banner.fill.solid()
    b_banner.fill.fore_color.rgb = DARK_BLUE
    b_banner.line.color.rgb = GOLD
    b_banner.line.width = Pt(1.5)
    tf_b = b_banner.text_frame
    tf_b.word_wrap = True
    pb0 = tf_b.paragraphs[0]
    pb0.text = "🏆 KẾT LUẬN CHIẾN LƯỢC MÔ HÌNH HÓA"
    pb0.font.name = "Arial"
    pb0.font.size = Pt(14)
    pb0.font.bold = True
    pb0.font.color.rgb = GOLD
    pb1 = tf_b.add_paragraph()
    pb1.text = "• Gradient Boosting (GBDT) được lựa chọn làm mô hình sản xuất chính: Giảm 8.4% sai số MAE so với Linear Regression nhờ khả năng học tương tác phi tuyến giữa diện tích và vị trí quận.\n• Thời gian huấn luyện siêu nhanh (1.20 giây) đáp ứng hoàn hảo yêu cầu cập nhật lại mô hình định kỳ (Retraining Pipeline) và đóng gói triển khai suy diễn tự động."
    pb1.font.name = "Arial"
    pb1.font.size = Pt(13)
    pb1.font.color.rgb = WHITE
    pb1.space_before = Pt(8)

    # ==========================================
    # SLIDE 12: [BIỂU ĐỒ 05] ĐÁNH GIÁ MÔ HÌNH (LAYOUT: TOP-WIDE HERO CHART)
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    fig5_path = os.path.join(FIG_DIR, "05_model_comparison.png")
    create_top_chart_slide(
        s12,
        "Biểu Đồ 5: So Sánh Hiệu Năng Các Mô Hình (MAE & R² Score)",
        fig5_path,
        [
            ("1. GBDT QUÁN QUÂN TUYỆT ĐỐI",
             "Đạt R² = 0.4390 cao nhất và MAE = 26.07 triệu/m² thấp nhất toàn bộ thử nghiệm, giảm 8.4% sai số so với mô hình Linear."),
            ("2. BẢN CHẤT PHI TUYẾN",
             "Chuỗi cây quyết định liên tiếp học phần dư sai của các cây trước, giải quyết triệt để tính phi tuyến và tương tác vị trí."),
            ("3. Ý NGHĨA KHOA HỌC DỮ LIỆU",
             "Khẳng định mô hình học máy dạng cây tăng cường là sự lựa chọn tối ưu, đủ cơ sở khoa học để đưa vào sản xuất thực tế.")
        ]
    )

    # ==========================================
    # SLIDE 13: [BIỂU ĐỒ 06] TẦM QUAN TRỌNG ĐẶC TRƯNG (LAYOUT: LEFT HERO CHART)
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    fig6_path = os.path.join(FIG_DIR, "06_feature_importance.png")
    create_left_chart_slide(
        s13,
        "Biểu Đồ 6: Tầm Quan Trọng Của Các Đặc Trưng Trong Mô Hình GBDT",
        fig6_path,
        "TẦM QUAN TRỌNG ĐẶC TRƯNG (BĐ 06)",
        [
            ("Tác Dụng & Mục Đích Biểu Đồ:",
             "Xếp hạng đóng góp tương đối (Relative Feature Importance) của các đặc trưng vào quyết định dự báo giá của mô hình Gradient Boosting."),
            ("🥇 Đặc Trưng Số 1: Diện Tích (42%):",
             "Chiếm tỷ trọng áp đảo, khẳng định quy luật bất biến: quy mô diện tích luôn là nhân tố nền tảng quyết định giá trị bất động sản."),
            ("🥈 Đặc Trưng Số 2: Vị Trí Địa Lý (28%):",
             "Các biến Quận/Huyện đóng góp 28% tổng trọng số, phản ánh tính chất 'nhất vị, nhị hướng' của thị trường thủ đô."),
            ("🥉 Mặt Tiền & Số Tầng (15%):",
             "Chiều rộng mặt tiền tạo ra giá trị thặng dư thương mại lớn, trong khi số tầng quyết định tổng không gian sử dụng thực tế.")
        ]
    )

    # ==========================================
    # SLIDE 14: KHUNG SUY LUẬN THỐNG KÊ & CÂY CHỌN PHÉP KIỂM (TUẦN 9)
    # ==========================================
    s14 = prs.slides.add_slide(blank_layout)
    add_header(s14, "Khung Suy Luận Thống Kê & Quy Trình Kiểm Định Giả Thuyết (Tuần 9)")

    tf_l14 = add_card(s14, Inches(0.8), Inches(1.35), half_w, Inches(5.65), "CÂY QUYẾT ĐỊNH CHỌN PHÉP KIỂM ĐỊNH", header_bg=DARK_BLUE, bg_color=NAVY)
    l14_items = [
        ("Bản chất Thống kê Suy luận:",
         "Thống kê mô tả chỉ tóm tắt 21.142 mẫu quan sát được; Thống kê suy luận kiểm định các quy luật trên toàn thể thị trường kèm mức độ không chắc chắn."),
        ("1. So sánh 2 nhóm độc lập (Mặt phố vs Ngõ):",
         "Phương sai hai nhóm không đồng nhất (s₁² ≠ s₂²) ➔ Bắt buộc dùng Welch's t-test (equal_var=False) để triệt tiêu sai lầm Loại I."),
        ("2. So sánh 3+ nhóm định lượng (30 Quận/Huyện):",
         "Phân tích phương sai One-way ANOVA ➔ Kết hợp kiểm định hậu nghiệm Tukey's HSD Post-hoc phát hiện các cặp quận tương đồng giá."),
        ("3. Dữ liệu phân phối lệch & Ngoại lệ:",
         "Dùng kỹ thuật tái lấy mẫu phi tham số Bootstrap 1.000 lần xác lập khoảng tin cậy 95% (CI) không phụ thuộc giả định chuẩn hóa.")
    ]
    for it_idx, (it_h, it_b) in enumerate(l14_items):
        pt = tf_l14.paragraphs[0] if it_idx == 0 else tf_l14.add_paragraph()
        pt.text = f"• {it_h}"
        pt.font.name = "Arial"
        pt.font.size = Pt(13)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(10)
        pd = tf_l14.add_paragraph()
        pd.text = it_b
        pd.font.name = "Arial"
        pd.font.size = Pt(12)
        pd.font.color.rgb = WHITE
        pd.space_before = Pt(2)

    tf_r14 = add_card(s14, Inches(0.8) + half_w + gap_half, Inches(1.35), half_w, Inches(5.65), "QUY TRÌNH 5 BƯỚC & BẢN CHẤT P-VALUE", header_bg=NAVY, bg_color=WHITE)
    r14_items = [
        ("Quy trình 5 bước kiểm định giả thuyết chuẩn:",
         "1. Phát biểu H₀ (Không khác biệt) và H₁ (Có khác biệt thực sự).\n2. Thiết lập mức ý nghĩa α = 0.05 TRƯỚC KHI quan sát số liệu.\n3. Kiểm tra giả định (Normality, Homoscedasticity) & chọn phép kiểm.\n4. Tính Test-statistic, p-value, Khoảng tin cậy CI và Effect Size.\n5. Đưa ra kết luận: Bác bỏ H₀ nếu p-value < α."),
        ("Bản chất p-value & 4 ngộ nhận cần tránh:",
         "p-value là xác suất quan sát dữ liệu cực đoan như vậy với giả định H₀ đúng; KHÔNG PHẢI là xác suất H₀ đúng. p < 0.05 không đồng nghĩa hiệu ứng lớn."),
        ("Kiểm soát 2 loại sai lầm thống kê:",
         "• Sai lầm Loại I (α): Bác bỏ H₀ khi H₀ đúng (Báo động giả).\n• Sai lầm Loại II (β): Không bác bỏ H₀ khi H₀ sai; Power = 1 - β ≥ 0.8.")
    ]
    for it_idx, (it_h, it_b) in enumerate(r14_items):
        pt = tf_r14.paragraphs[0] if it_idx == 0 else tf_r14.add_paragraph()
        pt.text = f"• {it_h}"
        pt.font.name = "Arial"
        pt.font.size = Pt(13)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(12)
        pd = tf_r14.add_paragraph()
        pd.text = it_b
        pd.font.name = "Arial"
        pd.font.size = Pt(12)
        pd.font.color.rgb = CHARCOAL
        pd.space_before = Pt(2)

    # ==========================================
    # SLIDE 15: THỐNG KÊ SUY LUẬN - WELCH'S T-TEST (LAYOUT: SPLIT CONTRAST)
    # ==========================================
    s15 = prs.slides.add_slide(blank_layout)
    add_header(s15, "Thống Kê Suy Luận: Welch's T-Test (Mặt Tiền vs Trong Ngõ)")

    tf_l15 = add_card(s15, Inches(0.8), Inches(1.35), half_w, Inches(4.20), "NHÓM 1: BẤT ĐỘNG SẢN MẶT PHỐ", header_bg=NAVY)
    l15_items = [
        ("Đơn giá trung bình thực nghiệm:", "162.8 triệu/m² (Độ lệch chuẩn: 42.5 triệu/m²)."),
        ("Đặc tính kinh tế vượt trội:", "Khả năng khai thác thương mại, mở showroom, cửa hàng kinh doanh tạo dòng tiền thụ động."),
        ("Thanh khoản thị trường:", "Nhu cầu mua giữ tài sản lớn, tốc độ tăng giá ổn định trước biến động lạm phát."),
        ("Quy mô mẫu phân tích:", "3.420 bản ghi BĐS mặt phố trên toàn địa bàn Hà Nội.")
    ]
    for it_idx, (it_h, it_b) in enumerate(l15_items):
        pt = tf_l15.paragraphs[0] if it_idx == 0 else tf_l15.add_paragraph()
        pt.text = f"• {it_h}"
        pt.font.name = "Arial"
        pt.font.size = Pt(13.5)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(12)
        pd = tf_l15.add_paragraph()
        pd.text = it_b
        pd.font.name = "Arial"
        pd.font.size = Pt(12.5)
        pd.font.color.rgb = CHARCOAL
        pd.space_before = Pt(2)

    tf_r15 = add_card(s15, Inches(0.8) + half_w + gap_half, Inches(1.35), half_w, Inches(4.20), "NHÓM 2: BẤT ĐỘNG SẢN TRONG NGÕ NGÁCH", header_bg=NAVY)
    r15_items = [
        ("Đơn giá trung bình thực nghiệm:", "114.2 triệu/m² (Độ lệch chuẩn: 31.8 triệu/m²)."),
        ("Đặc tính an cư:", "Không gian yên tĩnh, phục vụ mục đích ở thuần túy, phụ thuộc vào độ rộng ngõ và khả năng đỗ ô tô."),
        ("Chênh lệch giá trị tuyệt đối:", "Thấp hơn nhà mặt phố trung bình 48.6 triệu/m² (chênh lệch ~30% giá trị)."),
        ("Quy mô mẫu phân tích:", "17.722 bản ghi BĐS trong ngõ ngách sau làm sạch.")
    ]
    for it_idx, (it_h, it_b) in enumerate(r15_items):
        pt = tf_r15.paragraphs[0] if it_idx == 0 else tf_r15.add_paragraph()
        pt.text = f"• {it_h}"
        pt.font.name = "Arial"
        pt.font.size = Pt(13.5)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(12)
        pd = tf_r15.add_paragraph()
        pd.text = it_b
        pd.font.name = "Arial"
        pd.font.size = Pt(12.5)
        pd.font.color.rgb = CHARCOAL
        pd.space_before = Pt(2)

    # Bottom Banner T-Test
    b_ttest = s15.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(5.75), Inches(11.733), Inches(1.35))
    b_ttest.fill.solid()
    b_ttest.fill.fore_color.rgb = DARK_BLUE
    b_ttest.line.color.rgb = GOLD
    b_ttest.line.width = Pt(1.5)
    tf_tt = b_ttest.text_frame
    tf_tt.word_wrap = True
    ptt0 = tf_tt.paragraphs[0]
    ptt0.text = "🔬 KẾT QUẢ KIỂM ĐỊNH WELCH'S T-TEST (PHƯƠNG SAI KHÔNG ĐỒNG NHẤT)"
    ptt0.font.name = "Arial"
    ptt0.font.size = Pt(13.5)
    ptt0.font.bold = True
    ptt0.font.color.rgb = GOLD
    ptt1 = tf_tt.add_paragraph()
    ptt1.text = "• T-statistic = 42.18 | P-value = 1.2e-85 (< 0.001) -> BÁC BỎ HOÀN TOÀN GIẢ THUYẾT H0 (HAI NHÓM CÓ GIÁ BẰNG NHAU).\n• Khẳng định với độ tin cậy > 99.99%: Nhà mặt phố tại Hà Nội có giá trị cao hơn có ý nghĩa thống kê so với nhà trong ngõ."
    ptt1.font.name = "Arial"
    ptt1.font.size = Pt(12.5)
    ptt1.font.color.rgb = WHITE
    ptt1.space_before = Pt(6)

    # ==========================================
    # SLIDE 16: ANOVA & 9 CẶP QUẬN SONG SINH (LAYOUT: TOP SUMMARY + 2 SEGMENT CARDS)
    # ==========================================
    s16 = prs.slides.add_slide(blank_layout)
    add_header(s16, "ANOVA Phân Tích Phương Sai & 9 Cặp Quận 'Song Sinh' Giá")

    # Top Card ANOVA
    tf_top16 = add_card(s16, Inches(0.8), Inches(1.35), Inches(11.733), Inches(1.85), "KẾT QUẢ PHÂN TÍCH PHƯƠNG SAI ANOVA 30 QUẬN/HUYỆN", header_bg=NAVY)
    top16_items = [
        ("F-statistic = 186.42 | P-value < 0.001:", "Bác bỏ giả thuyết H0; vị trí địa lý tạo nên sự phân hóa đơn giá có ý nghĩa thống kê cực kỳ mạnh mẽ."),
        ("Ý nghĩa kiểm định hậu nghiệm (Tukey HSD Post-hoc):", "Xác định chính xác những cặp quận nào có giá thực sự khác biệt và những cặp quận nào có mức giá tương đương nhau.")
    ]
    for it_idx, (it_h, it_b) in enumerate(top16_items):
        pt = tf_top16.paragraphs[0] if it_idx == 0 else tf_top16.add_paragraph()
        pt.text = f"• {it_h} "
        pt.font.name = "Arial"
        pt.font.size = Pt(13)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(8)
        run_b = pt.add_run()
        run_b.text = it_b
        run_b.font.name = "Arial"
        run_b.font.size = Pt(12.5)
        run_b.font.color.rgb = CHARCOAL

    # 2 Cards Cặp quận song sinh bên dưới
    tf_l16 = add_card(s16, Inches(0.8), Inches(3.40), half_w, Inches(3.65), "9 CẶP QUẬN 'SONG SINH' TƯƠNG ĐỒNG GIÁ", header_bg=NAVY)
    pairs_list = [
        ("Cầu Giấy ≈ Đống Đa:", "Chênh lệch trung vị < 2.5% (p = 0.82), hai trung tâm giáo dục & văn phòng."),
        ("Thanh Xuân ≈ Nam Từ Liêm:", "Chênh lệch < 3.2% (p = 0.76), trục phát triển đô thị phía Tây sôi động."),
        ("Hà Đông ≈ Hoàng Mai:", "Chênh lệch < 2.1% (p = 0.88), phân khúc giá vừa túi tiền cho gia đình trẻ."),
        ("Long Biên ≈ Tây Hồ (vùng ngoài):", "Tương đồng về biên độ tăng trưởng phân khúc nhà vườn/biệt thự.")
    ]
    for it_idx, (it_h, it_b) in enumerate(pairs_list):
        pt = tf_l16.paragraphs[0] if it_idx == 0 else tf_l16.add_paragraph()
        pt.text = f"• {it_h} "
        pt.font.name = "Arial"
        pt.font.size = Pt(13)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(10)
        run_b = pt.add_run()
        run_b.text = it_b
        run_b.font.name = "Arial"
        run_b.font.size = Pt(12)
        run_b.font.color.rgb = CHARCOAL

    tf_r16 = add_card(s16, Inches(0.8) + half_w + gap_half, Inches(3.40), half_w, Inches(3.65), "Ý NGHĨA KINH DOANH & TỐI ƯU DANH MỤC ĐẦU TƯ", header_bg=NAVY)
    strat_list = [
        ("Chiến lược hàng hóa thay thế (Substitute Assets):", "Khi giá tại Cầu Giấy bị đẩy lên quá cao, nhà đầu tư có thể chuyển dịch vốn sang Đống Đa hoặc Nam Từ Liêm với kỳ vọng tỷ suất sinh lời tương đương."),
        ("Phòng ngừa rủi ro định giá sai (Arbitrage):", "Phát hiện ngay những căn nhà bị định giá lệch khỏi mức cân bằng của cặp quận song sinh để thực hiện chiến lược mua gom."),
        ("Khuyến nghị cho sàn môi giới:", "Đa dạng hóa rổ sản phẩm liên quận, tư vấn linh hoạt cho khách hàng có ngân sách cố định.")
    ]
    for it_idx, (it_h, it_b) in enumerate(strat_list):
        pt = tf_r16.paragraphs[0] if it_idx == 0 else tf_r16.add_paragraph()
        pt.text = f"• {it_h}"
        pt.font.name = "Arial"
        pt.font.size = Pt(13)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(10)
        pd = tf_r16.add_paragraph()
        pd.text = it_b
        pd.font.name = "Arial"
        pd.font.size = Pt(12)
        pd.font.color.rgb = CHARCOAL
        pd.space_before = Pt(2)
    # SLIDE 17: [BIỂU ĐỒ 07] KHOẢNG TIN CẬY 95% BOOTSTRAP (LAYOUT: LEFT HERO CHART)
    # ==========================================
    s17 = prs.slides.add_slide(blank_layout)
    fig7_path = os.path.join(FIG_DIR, "07_confidence_intervals_districts.png")
    create_left_chart_slide(
        s17,
        "Biểu Đồ 7: Khoảng Tin Cậy 95% Bootstrap Đơn Giá Từng Quận",
        fig7_path,
        "KHOẢNG TIN CẬY 95% (BĐ 07)",
        [
            ("Tác Dụng & Mục Đích Biểu Đồ:",
             "Sử dụng kỹ thuật tái lấy mẫu không hoàn lại Bootstrap 1.000 lần để xác định dải dao động 95% tin cậy của đơn giá m² từng quận."),
            ("Miễn Nhiễm Với Giả Định Phân Phối:",
             "Bootstrap không đòi hỏi dữ liệu phải tuân theo phân phối chuẩn, bảo toàn độ chính xác tuyệt đối ngay cả ở các quận có độ lệch cao."),
            ("Ứng Dụng Quản Trị Rủi Ro Tín Dụng:",
             "Ngân hàng có thể sử dụng cận dưới (Lower Bound 95%) làm mức định giá trần an toàn khi duyệt hạn mức cho vay thế chấp."),
            ("Ý Nghĩa Với Người Mua Nhà:",
             "Giúp khách hàng nhận diện nhanh giao dịch đang mua là đắt hay rẻ so với biên độ dao động thống kê chuẩn mực của khu vực.")
        ]
    )

    # ==========================================
    # SLIDE 18: ĐỌC HIỂU OLS & 3 NGHĨA VỤ ĐẠO ĐỨC (LAYOUT: ASYMMETRIC SPLIT)
    # ==========================================
    s18 = prs.slides.add_slide(blank_layout)
    add_header(s18, "Phân Tích Hồi Quy Tuyến Tính OLS & 3 Nghĩa Vụ Đạo Đức AI")

    tf_l18 = add_card(s18, Inches(0.8), Inches(1.35), Inches(4.30), Inches(5.65), "ĐỌC HIỂU HỆ SỐ HỒI QUY OLS", header_bg=NAVY)
    l18_items = [
        ("Độ giải thích R² = 0.382:", "Mô hình OLS giải thích được 38.2% độ biến thiên giá trị; phần còn lại thuộc về yếu tố phi tuyến và vi vị trí."),
        ("Hệ số Diện tích (Area):", "Beta chuẩn hóa = +0.58 (p < 0.001) - Biến số có sức ảnh hưởng mạnh nhất đến tổng giá."),
        ("Hệ số Mặt tiền (Frontage):", "Beta chuẩn hóa = +0.24 (p < 0.001) - Tăng thêm giá trị thặng dư thương mại độc lập."),
        ("Cảnh báo Đa cộng tuyến (VIF):", "Biến số phòng ngủ có VIF > 4.2 khi kết hợp với diện tích -> Cần loại bỏ để tránh ước lượng sai số.")
    ]
    for it_idx, (it_h, it_b) in enumerate(l18_items):
        pt = tf_l18.paragraphs[0] if it_idx == 0 else tf_l18.add_paragraph()
        pt.text = f"• {it_h}"
        pt.font.name = "Arial"
        pt.font.size = Pt(13)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(12)
        pd = tf_l18.add_paragraph()
        pd.text = it_b
        pd.font.name = "Arial"
        pd.font.size = Pt(12.5)
        pd.font.color.rgb = CHARCOAL
        pd.space_before = Pt(2)

    # 3 Thẻ Đạo Đức Dữ Liệu bên phải
    right_left_18 = Inches(0.8) + Inches(4.30) + Inches(0.35)
    right_w_18 = Inches(7.083)
    card_h_18 = Inches(1.72)
    gap_y_18 = Inches(0.24)

    ethics_cards = [
        ("1. TÍNH MINH BẠCH & KHẢ NĂNG GIẢI THÍCH (TRANSPARENCY)",
         "Không sử dụng mô hình 'hộp đen' khó hiểu. Mọi kết quả định giá từ mô hình đều phải giải trình rõ ràng đóng góp biên của các đặc trưng (SHAP/Feature Importance) cho các bên liên quan."),
        ("2. PHÒNG CHỐNG ĐỊNH KIẾN THUẬT TOÁN (FAIRNESS)",
         "Đảm bảo mô hình không áp đặt định kiến tiêu cực lên các quận ven đô (Đông Anh, Gia Lâm, Mê Linh). Luôn cập nhật tốc độ phát triển hạ tầng thực tế vào thuật toán."),
        ("3. BẢO MẬT DỮ LIỆU & QUYỀN RIÊNG TƯ (DATA PRIVACY)",
         "Ẩn danh hóa hoàn toàn số nhà, tên chủ hộ, thông tin liên lạc cá nhân theo đúng Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân.")
    ]
    for e_idx, (e_title, e_desc) in enumerate(ethics_cards):
        e_top = Inches(1.35) + e_idx * (card_h_18 + gap_y_18)
        tf_e = add_card(s18, right_left_18, e_top, right_w_18, card_h_18, e_title, header_bg=NAVY)
        p = tf_e.paragraphs[0]
        p.text = e_desc
        p.font.name = "Arial"
        p.font.size = Pt(12.5)
        p.font.color.rgb = CHARCOAL
        p.space_before = Pt(4)

    # ==========================================
    # SLIDE 19: [BIỂU ĐỒ 08] KIỂM ĐỊNH 4 GIẢ ĐỊNH LINE (LAYOUT: LEFT HERO CHART)
    # ==========================================
    s19 = prs.slides.add_slide(blank_layout)
    fig8_path = os.path.join(FIG_DIR, "08_line_assumptions_diagnostics.png")
    create_left_chart_slide(
        s19,
        "Biểu Đồ 8: Kiểm Định 4 GiẢ Định Hồi Quy Tuyến Tính (LINE Diagnostics)",
        fig8_path,
        "CHẨN ĐOÁN 4 GIẢ ĐỊNH (BĐ 08)",
        [
            ("Tác Dụng & Mục Đích Biểu Đồ:",
             "Kiểm tra tính hợp lệ của mô hình OLS qua 4 giả định cốt lõi: Tuyến tính (Linearity), Độc lập (Independence), Chuẩn hóa (Normality), và Phương sai đồng nhất (Equal variance)."),
            ("Vi Phạm Giả Định Phương Sai (Heteroscedasticity):",
             "Đồ thị Residuals vs Fitted phình to hình phễu ở nhóm giá cao; phương sai sai số không đồng nhất làm lệch khoảng tin cậy của OLS."),
            ("Độ Lệch Chuẩn Ở Q-Q Plot:",
             "Đường Q-Q uốn cong mạnh ở hai đầu đuôi (heavy tails), phản ánh sự hiện diện của các biệt thự hạng sang có mức giá cá biệt."),
            ("Định Hướng Khắc Phục Triệt Để:",
             "Minh chứng rõ ràng lý do tại sao phải chuyển sang mô hình phi tuyến GBDT hoặc áp dụng biến đổi Logarit toàn diện.")
        ]
    )

    # ==========================================
    # SLIDE 20: ĐỘT PHÁ SAU BIẾN ĐỔI LOGARIT (LAYOUT: BEFORE VS AFTER CONTRAST)
    # ==========================================
    s20 = prs.slides.add_slide(blank_layout)
    add_header(s20, "So Sánh Hiệu Quả Trước & Sau Khi Biến Đổi Logarit")

    tf_l20 = add_card(s20, Inches(0.8), Inches(1.35), half_w, Inches(5.65), "TRƯỚC BIẾN ĐỔI LOGARIT (THANG ĐO GỐC)", header_bg=NAVY)
    l20_items = [
        ("Phân phối lệch phải cực nặng:", "Độ lệch Skewness = 3.84; hàm mục tiêu bị kéo lệch bởi nhóm BĐS cao cấp."),
        ("Hiệu năng mô hình tuyến tính yếu:", "R² dừng lại ở 0.382; sai số RMSE lên tới 38.1 triệu/m² do nhạy cảm với ngoại lệ."),
        ("Dư sai vi phạm nặng giả định LINE:", "Biểu đồ phần dư có hiện tượng phương sai thay đổi rõ nét, làm giảm độ tin cậy khi suy luận thống kê."),
        ("Khó khăn khi tối ưu hóa Gradient:", "Thuật toán học máy hội tụ chậm và dễ bị kẹt tại các cực tiểu cục bộ do dải giá trị biến thiên quá rộng.")
    ]
    for it_idx, (it_h, it_b) in enumerate(l20_items):
        pt = tf_l20.paragraphs[0] if it_idx == 0 else tf_l20.add_paragraph()
        pt.text = f"• {it_h}"
        pt.font.name = "Arial"
        pt.font.size = Pt(13.5)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(16)
        pd = tf_l20.add_paragraph()
        pd.text = it_b
        pd.font.name = "Arial"
        pd.font.size = Pt(12.5)
        pd.font.color.rgb = CHARCOAL
        pd.space_before = Pt(3)

    tf_r20 = add_card(s20, Inches(0.8) + half_w + gap_half, Inches(1.35), half_w, Inches(5.65), "SAU BIẾN ĐỔI LOGARIT (LOG-TRANSFORMED)", header_bg=DARK_BLUE, bg_color=NAVY)
    r20_items = [
        ("Phân phối tiệm cận chuẩn Gauss lý tưởng:", "Độ lệch Skewness giảm sâu xuống 0.18, đối xứng hoàn hảo quanh trung vị."),
        ("Hiệu năng mô hình tăng vọt (+15.4%):", "R² tăng từ 0.382 lên 0.441; sai số phần trăm trung bình MAPE giảm về mức 12.8%."),
        ("Ổn định phương sai dư sai (Homoscedasticity):", "Sai số phân bổ đồng đều trên toàn bộ các phân khúc từ nhà giá rẻ đến biệt thự cao cấp."),
        ("Độ trễ tối ưu hóa giảm mạnh:", "Các thuật toán Gradient Descent hội tụ nhanh gấp 2 lần, gradient ổn định không bị hiện tượng bùng nổ.")
    ]
    for it_idx, (it_h, it_b) in enumerate(r20_items):
        pt = tf_r20.paragraphs[0] if it_idx == 0 else tf_r20.add_paragraph()
        pt.text = f"• {it_h}"
        pt.font.name = "Arial"
        pt.font.size = Pt(13.5)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(16)
        pd = tf_r20.add_paragraph()
        pd.text = it_b
        pd.font.name = "Arial"
        pd.font.size = Pt(12.5)
        pd.font.color.rgb = WHITE
        pd.space_before = Pt(3)

    # ==========================================
    # SLIDE 21: [BIỂU ĐỒ 09] REGULARIZATION LASSO VS RIDGE (LAYOUT: LEFT HERO CHART)
    # ==========================================
    s21 = prs.slides.add_slide(blank_layout)
    fig9_path = os.path.join(FIG_DIR, "09_regularization_lasso_vs_ridge.png")
    create_left_chart_slide(
        s21,
        "Biểu Đồ 9: Kiểm Soát Quá Khớp Với Regularization (Lasso L1 vs Ridge L2)",
        fig9_path,
        "REGULARIZATION (BĐ 09)",
        [
            ("Tác Dụng & Mục Đích Biểu Đồ:",
             "Quan sát đường cong thu hẹp hệ số (Shrinkage Path) khi tham số phạt alpha tăng dần từ 0.001 đến 100 trên hai kỹ thuật chuẩn hóa."),
            ("🎯 Lasso (L1 Penalty) - Tự Động Lựa Chọn Biến:",
             "Triệt tiêu hoàn toàn các hệ số biến nhiễu về chính xác 0, giữ lại tập đặc trưng tinh gọn nhất cho mô hình."),
            ("🛡️ Ridge (L2 Penalty) - Khống Chế Đa Cộng Tuyến:",
             "Thu nhỏ đồng đều tất cả hệ số mà không triệt tiêu về 0, giúp mô hình ổn định khi 30 quận/huyện có tương quan nội bộ cao."),
            ("Quyết Định Lựa Chọn Tối Ưu:",
             "Áp dụng kết hợp ElasticNet hoặc sử dụng Ridge trong các bài toán yêu cầu bảo toàn toàn bộ danh sách 30 Quận/Huyện.")
        ]
    )

    # ==========================================
    # SLIDE 22: 7 KẾT LUẬN THỰC TIỄN CHO DOANH NGHIỆP (LAYOUT: MA TRẬN 2x2 ACTION PILLARS)
    # ==========================================
    s22 = prs.slides.add_slide(blank_layout)
    add_header(s22, "7 Kết Luận Thực Tiễn Cho Doanh Nghiệp & Nhà Đầu Tư")

    action_pillars = [
        ("TRỤ CỘT 1: ĐỊNH GIÁ & GIAO DỊCH BĐS", [
            ("Tự động hóa định giá khách quan:", "Áp dụng thuật toán GBDT đạt sai số MAE ~26 tr/m², giảm 8.4% sai số so với Linear."),
            ("Độ chính xác vượt trội:", "Sai số thực tế chỉ ~26 tr/m², tin cậy cao trên tập kiểm thử."),
            ("Bảo vệ quyền lợi người mua:", "Phát hiện ngay tin rao khống giá hoặc lệch mặt bằng khu vực.")
        ]),
        ("TRỤ CỘT 2: ĐẦU TƯ & TỐI ƯU DANH MỤC", [
            ("Khai thác 9 cặp quận 'song sinh':", "Chuyển dịch dòng vốn sang quận lân cận có giá tương đồng."),
            ("Bắt đáy cơ hội tăng trưởng:", "Tận dụng các khu vực ven đô có quy hoạch vành đai và metro."),
            ("Tối ưu hóa lợi suất cho thuê:", "Lựa chọn nhà mặt phố có thặng dư thương mại cao.")
        ]),
        ("TRỤ CỘT 3: QUẢN TRỊ TÍN DỤNG NGÂN HÀNG", [
            ("Chốt chặn an toàn với Bootstrap:", "Áp dụng Lower Bound 95% làm ngưỡng giải ngân an toàn."),
            ("Giảm thiểu rủi ro nợ xấu:", "Phát hiện hiện tượng thổi giá cục bộ của giới đầu cơ."),
            ("Tự động hóa hồ sơ thế chấp:", "Tích hợp API định giá vào luồng phê duyệt tín dụng tự động.")
        ]),
        ("TRỤ CỘT 4: MINH BẠCH HÓA THỊ TRƯỜNG", [
            ("Chuẩn hóa dữ liệu toàn diện:", "Khắc phục triệt để tin rác, tin ảo, tin trùng lặp."),
            ("Tuân thủ chuẩn mực đạo đức AI:", "Minh bạch thuật toán, bảo vệ tuyệt đối dữ liệu người dùng."),
            ("Sẵn sàng cho sản phẩm thực tế:", "Đóng gói pipeline hoàn chỉnh, sẵn sàng mở rộng quy mô toàn quốc.")
        ])
    ]

    for idx, (a_title, a_items) in enumerate(action_pillars):
        row_i = idx // 2
        col_i = idx % 2
        a_left = Inches(0.8) + col_i * (m_w + m_gap_x)
        a_top = Inches(1.35) + row_i * (m_h + m_gap_y)

        tf_a = add_card(s22, a_left, a_top, m_w, m_h, a_title, header_bg=NAVY)
        for it_idx, (it_h, it_b) in enumerate(a_items):
            pt = tf_a.paragraphs[0] if it_idx == 0 else tf_a.add_paragraph()
            pt.text = f"• {it_h} "
            pt.font.name = "Arial"
            pt.font.size = Pt(12.5)
            pt.font.bold = True
            pt.font.color.rgb = GOLD
            if it_idx > 0:
                pt.space_before = Pt(8)
            run_b = pt.add_run()
            run_b.text = it_b
            run_b.font.name = "Arial"
            run_b.font.size = Pt(12)
            run_b.font.color.rgb = CHARCOAL

    # ==========================================
    # SLIDE 23: LỘ TRÌNH CUỐI KỲ & Q&A (LAYOUT: SPLIT HERO)
    # ==========================================
    s23 = prs.slides.add_slide(blank_layout)
    add_header(s23, "Lộ Trình Hoàn Thiện Cuối Kỳ (Tuần 11 - 12) & Hỏi - Đáp")

    plan_w = Inches(6.20)
    qa_w = Inches(5.133)

    tf_l23 = add_card(s23, Inches(0.8), Inches(1.35), plan_w, Inches(5.65), "3 MỤC TIÊU ĐỘT PHÁ TUẦN 11 - 12", header_bg=NAVY)
    plan_items = [
        ("1. Tinh Chỉnh & Mở Rộng Mô Hình (Tuần 11):",
         "Áp dụng Bayesian Optimization cho XGBoost/LightGBM và đánh giá Precision/Recall, PR-AUC cho bài toán phân loại phân khúc giá."),
        ("2. Trí Tuệ Nhân Tạo Có Thể Giải Thích (SHAP XAI - Tuần 12):",
         "Tích hợp thư viện SHAP (Shapley Additive exPlanations) để bóc tách chính xác lý do tại sao một căn nhà cụ thể được định giá tăng hoặc giảm."),
        ("3. Chuẩn Hóa Quản Trị & Đạo Đức Dữ Liệu (Tuần 12):",
         "Xây dựng Datasheets for Datasets và Model Cards theo chuẩn Google PAIR & Nghị định 13/2023/NĐ-CP, thiết lập cơ chế ẩn danh k-anonymity.")
    ]
    for it_idx, (it_h, it_b) in enumerate(plan_items):
        pt = tf_l23.paragraphs[0] if it_idx == 0 else tf_l23.add_paragraph()
        pt.text = it_h
        pt.font.name = "Arial"
        pt.font.size = Pt(13.5)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(18)
        pd = tf_l23.add_paragraph()
        pd.text = it_b
        pd.font.name = "Arial"
        pd.font.size = Pt(12.5)
        pd.font.color.rgb = CHARCOAL
        pd.space_before = Pt(4)

    # Khung Cảm ơn & Q&A
    b_qa = s23.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(7.40), Inches(1.35), qa_w, Inches(5.65))
    b_qa.fill.solid()
    b_qa.fill.fore_color.rgb = DARK_BLUE
    b_qa.line.color.rgb = GOLD
    b_qa.line.width = Pt(1.5)

    tb_qa = s23.shapes.add_textbox(Inches(7.60), Inches(2.2), Inches(4.733), Inches(4.0))
    tf_qa = tb_qa.text_frame
    tf_qa.word_wrap = True

    p_qa0 = tf_qa.paragraphs[0]
    p_qa0.text = "CẢM ƠN THẦY CÔ & HỘI ĐỒNG ĐÃ LẮNG NGHE!"
    p_qa0.font.name = "Arial"
    p_qa0.font.size = Pt(22)
    p_qa0.font.bold = True
    p_qa0.font.color.rgb = GOLD
    p_qa0.alignment = PP_ALIGN.CENTER

    p_qa1 = tf_qa.add_paragraph()
    p_qa1.text = "\n\nNHÓM DỰ ÁN SẴN SÀNG TRẢ LỜI MỌI CÂU HỎI VÀ TIẾP THU Ý KIẾN ĐÓNG GÓP TỪ HỘI ĐỒNG KHOA HỌC DỮ LIỆU."
    p_qa1.font.name = "Arial"
    p_qa1.font.size = Pt(14)
    p_qa1.font.color.rgb = WHITE
    p_qa1.space_before = Pt(16)
    p_qa1.alignment = PP_ALIGN.CENTER

    prs.save(OUTPUT_PPTX)
    print(f"🎉 Đã xuất thành công tệp PowerPoint tại: {OUTPUT_PPTX}")


if __name__ == '__main__':
    create_deck()
