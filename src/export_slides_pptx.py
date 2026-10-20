"""
Xuất toàn bộ Slide thuyết trình tiến độ KHDL (Tuần 1 - 10) sang định dạng Microsoft PowerPoint (.pptx).
Phiên bản Chuẩn hóa Trực quan & Tinh gọn (Executive Visual Edition):
- Loại bỏ toàn bộ các cam kết/chỉ số chưa xác minh (như p < 0.001 ở slide mở đầu, thời gian train...).
- Loại bỏ triệt để các ký tự công thức, ký hiệu toán học rườm rà (t, F, BP, JB, U, s1^2, beta, alpha...).
- Trình bày trực quan, ngôn ngữ quản lý mạch lạc, đi thẳng vào ý nghĩa thực tiễn kinh tế và khoa học dữ liệu.
- Cỡ chữ to rõ ràng đạt chuẩn hội trường: Tiêu đề 22pt, Thẻ 14-15pt, Nội dung 13.5-14.5pt.
- Bố cục đa dạng, thanh lịch, tone màu Executive Luxury: Dark Blue (#0F2240) + Gold (#D97706) + Arial font.
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

    def add_card(slide, left, top, width, height, title=None, header_bg=NAVY, header_color=WHITE, bg_color=WHITE, border_color=BORDER_GRAY, f_size=None):
        """Hộp thẻ chứa nội dung phẳng, viền xám tinh tế, có thanh tiêu đề phân cấp nổi bật."""
        base_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
        base_shape.fill.solid()
        base_shape.fill.fore_color.rgb = bg_color
        base_shape.line.color.rgb = border_color
        base_shape.line.width = Pt(1)

        body_top = top
        body_height = height

        if title:
            is_long = len(title) > 28 or (width < Inches(4.5) and len(title) > 22)
            h_height = Inches(0.66) if is_long else Inches(0.48)
            f_sz = f_size if f_size else (Pt(13) if is_long else Pt(14))

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
            p_h.font.size = f_sz
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
        """Layout A: Hero Chart lớn bên trái + Khung Insight bên phải (chữ 13.5 - 14pt)."""
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
        tf_right = add_card(slide, Inches(right_left), Inches(1.35), Inches(right_w), Inches(fig_h), badge_title, header_bg=NAVY, f_size=Pt(14))

        for idx, (b_title, b_desc) in enumerate(bullets):
            pt = tf_right.paragraphs[0] if idx == 0 else tf_right.add_paragraph()
            pt.text = b_title
            pt.font.name = "Arial"
            pt.font.size = Pt(14)
            pt.font.bold = True
            pt.font.color.rgb = GOLD
            if idx > 0:
                pt.space_before = Pt(12)

            pd = tf_right.add_paragraph()
            pd.text = b_desc
            pd.font.name = "Arial"
            pd.font.size = Pt(13)
            pd.font.color.rgb = CHARCOAL
            pd.space_before = Pt(3)

    def create_top_chart_slide(slide, title, fig_path, cards_info):
        """Layout B: Hero Chart rộng toàn màn hình ở trên + 3 Thẻ Insight bên dưới (chữ 13.5pt)."""
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
            tf_c = add_card(slide, Inches(c_left), Inches(bottom_top), Inches(card_w), Inches(bottom_h), c_title, header_bg=NAVY, f_size=Pt(13.5))
            p = tf_c.paragraphs[0]
            p.text = c_desc
            p.font.name = "Arial"
            p.font.size = Pt(13.5)
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
    p2.text = "Quy mô dữ liệu: 99.998 tin rao thô ➔ 37.402 bản ghi chuẩn hóa sạch (18 tháng gần nhất) • INFO3020"
    p2.font.name = "Arial"
    p2.font.size = Pt(14)
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
    p_gv_h.font.size = Pt(15)
    p_gv_h.font.bold = True
    p_gv_h.font.color.rgb = GOLD
    p_gv_c = tf_gv.add_paragraph()
    p_gv_c.text = "• Học phần: Khoa Học Dữ Liệu Thực Hành (INFO3020 - Tuần 1 đến 10)\n• Đơn vị: Bộ môn Khoa Học Dữ Liệu & Trí Tuệ Nhân Tạo\n• Mục tiêu: Báo cáo nghiệm thu tiến độ & Đóng gói giải pháp định giá BĐS"
    p_gv_c.font.name = "Arial"
    p_gv_c.font.size = Pt(13.5)
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
    p_sv_h.font.size = Pt(15)
    p_sv_h.font.bold = True
    p_sv_h.font.color.rgb = GOLD
    p_sv_c = tf_sv.add_paragraph()
    p_sv_c.text = "• Sinh viên thực hiện: Hoàng Long & Cộng sự\n• Chuyên ngành: Khoa Học Dữ Liệu / Trí Tuệ Nhân Tạo\n• Thời gian nghiệm thu: Tháng 10/2026\n• Phạm vi nghiên cứu: 30 Quận / Huyện TP. Hà Nội"
    p_sv_c.font.name = "Arial"
    p_sv_c.font.size = Pt(13.5)
    p_sv_c.font.color.rgb = WHITE
    p_sv_c.space_before = Pt(10)

    # ==========================================
    # SLIDE 2: BỐI CẢNH THỊ TRƯỜNG & 3 BÀI TOÁN KINH DOANH (LAYOUT: 3 CỘT TRỤ)
    # Loại bỏ hoàn toàn các cam kết/chỉ số chưa xác minh như p < 0.001
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Bối Cảnh Thị Trường & 3 Bài Toán Khoa Học Dữ Liệu")

    col_w = Inches(3.64)
    gap = Inches(0.40)
    top_pos = Inches(1.35)
    h_pos = Inches(5.65)

    pillars = [
        ("01", "BÀI TOÁN 1: DỰ BÁO GIÁ", "GIẢI QUYẾT TÍNH PHI TUYẾN", [
            ("Vấn đề thực tế:", "Thị trường BĐS Hà Nội biến động mạnh, mức giá giữa các khu vực có sự phân hóa sâu sắc."),
            ("Phương pháp tiếp cận:", "Ứng dụng các thuật toán máy học (Machine Learning) để dự báo đơn giá m² dựa trên vị trí, quy mô và tiện ích."),
            ("Kết quả kỳ vọng:", "Tối ưu hóa độ chính xác dự báo, hỗ trợ người mua và nhà đầu tư tham chiếu mức giá hợp lý.")
        ]),
        ("02", "BÀI TOÁN 2: THẨM ĐỊNH", "QUẢN TRỊ RỦI RO TÍN DỤNG", [
            ("Vấn đề thực tế:", "Định giá sai lệch gây rủi ro nợ xấu lớn cho ngân hàng và tổ chức tài chính khi duyệt hồ sơ thế chấp."),
            ("Phương pháp tiếp cận:", "Ứng dụng phương pháp thống kê suy luận để ước lượng khoảng biến thiên giá an toàn cho từng khu vực."),
            ("Kết quả kỳ vọng:", "Cung cấp ngưỡng định giá an toàn, hạn chế tối đa rủi ro giải ngân vượt giá trị thực của tài sản.")
        ]),
        ("03", "BÀI TOÁN 3: ĐẦU TƯ", "PHÂN TẦNG & TÀI SẢN THAY THẾ", [
            ("Vấn đề thực tế:", "Nhà đầu tư gặp khó khăn trong việc nhận diện các khu vực có mức giá và tiềm năng tương đương để phân bổ vốn."),
            ("Phương pháp tiếp cận:", "Phân tích so sánh đa nhóm giữa các quận/huyện để tìm kiếm các khu vực có mặt bằng giá đồng nhất."),
            ("Kết quả kỳ vọng:", "Xác lập bản đồ tài sản thay thế, mở rộng cơ hội đầu tư và tối ưu hóa danh mục tài sản.")
        ])
    ]

    for idx, (p_num, p_title, p_sub, p_items) in enumerate(pillars):
        c_left = Inches(0.8) + idx * (col_w + gap)
        tf_p = add_card(s2, c_left, top_pos, col_w, h_pos, p_title, header_bg=NAVY, f_size=Pt(14))

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
            pt.font.size = Pt(13.5)
            pt.font.bold = True
            pt.font.color.rgb = NAVY
            pt.space_before = Pt(14)

            pd = tf_p.add_paragraph()
            pd.text = it_val
            pd.font.name = "Arial"
            pd.font.size = Pt(13)
            pd.font.color.rgb = CHARCOAL
            pd.space_before = Pt(3)

    # ==========================================
    # SLIDE 3: PHỄU SÀNG LỌC & CHUẨN HÓA DỮ LIỆU (LAYOUT: FUNNEL FLOW + BẢNG CHI TIẾT)
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Phễu Sàng Lọc & Chuẩn Hóa Dữ Liệu (99.998 ➔ 37.402 Bản Ghi)")

    # 4 Khối Funnel ngang ở trên
    step_w = Inches(2.78)
    step_gap = Inches(0.20)
    funnel_steps = [
        ("BƯỚC 1: DỮ LIỆU THÔ", "99.998", "100.0%", "Thu thập đa kênh"),
        ("BƯỚC 2: CỬA SỔ 18 THÁNG", "38.505", "38.5%", "Lọc giai đoạn 2025 - 2026"),
        ("BƯỚC 3: XÓA RÁC & KHUYẾT", "37.630", "37.6%", "Loại giá 'Thỏa thuận' & inf"),
        ("BƯỚC 4: DỮ LIỆU SẠCH", "37.402", "37.4%", "38 đặc trưng chuẩn hóa")
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
        p_sc0.font.size = Pt(11.5)
        p_sc0.font.bold = True
        p_sc0.font.color.rgb = GOLD

        p_sc1 = tf_sc.add_paragraph()
        p_sc1.text = s_num
        p_sc1.font.name = "Arial"
        p_sc1.font.size = Pt(25)
        p_sc1.font.bold = True
        p_sc1.font.color.rgb = WHITE
        p_sc1.space_before = Pt(2)

        p_sc2 = tf_sc.add_paragraph()
        p_sc2.text = f"{s_pct} • {s_note}"
        p_sc2.font.name = "Arial"
        p_sc2.font.size = Pt(11.5)
        p_sc2.font.color.rgb = RGBColor(226, 232, 240)
        p_sc2.space_before = Pt(2)

    # Bảng chi tiết 4 lỗi bên dưới
    tbl_shape = s3.shapes.add_table(5, 4, Inches(0.8), Inches(3.10), Inches(11.733), Inches(3.90))
    table = tbl_shape.table
    table.columns[0].width = Inches(2.30)
    table.columns[1].width = Inches(1.50)
    table.columns[2].width = Inches(1.30)
    table.columns[3].width = Inches(6.633)

    data_errors = [
        ["Hạng Mục Xử Lý", "Số Bản Ghi", "Tỷ Lệ %", "Cơ Sở Kỹ Thuật & Nguyên Nhân Thực Tế"],
        ["Lọc chu kỳ 18 tháng", "61.493", "61.5%", "Loại bỏ tin cũ trước tháng 09/2024 để phản ánh đúng mặt bằng giá sau chu kỳ sốt đất 2024."],
        ["Khuyết mục tiêu", "875", "2.3%", "Tin rao ghi 'Giá thỏa thuận', khuyết diện tích hoặc lỗi chuyển đổi -> Loại bỏ hoàn toàn."],
        ["Ngoại lai miền tri thức", "228", "0.6%", "Áp dụng ngưỡng thực tế [10, 500] tr/m² -> Loại bỏ tin ảo, tin lừa cọc hoặc gõ nhầm số."],
        ["Chuẩn hóa hình học & đất", "3.560", "9.2%", "Đất nền gán Số tầng = 0; Mặt tiền nhập dạng mm (4500mm) được chia 1.000 về đơn vị mét."]
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
                p.font.size = Pt(13.5)
                p.font.color.rgb = WHITE
                p.alignment = PP_ALIGN.CENTER
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = WHITE if r_idx % 2 == 1 else LIGHT_BG
                p.font.size = Pt(13)
                p.font.color.rgb = CHARCOAL
                if c_idx in [1, 2]:
                    p.alignment = PP_ALIGN.CENTER
                    p.font.bold = True

    # ==========================================
    # SLIDE 4: KỸ NGHỆ ĐẶC TRƯNG (LAYOUT: 3 CỘT TRỤ ĐẶC TRƯNG)
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Kỹ Nghệ Đặc Trưng 3 Trụ Cột (12 ➔ 38 Biến Số)")

    feat_cols = [
        ("VỊ TRÍ & KHÔNG GIAN", [
            ("Mã hóa 30 Quận/Huyện:", "Chuyển đổi biến phân loại vị trí thành các biến độc lập, tránh áp đặt thứ bậc sai lệch."),
            ("Phân vùng Nội đô vs Ngoại thành:", "Tạo biến phân tách rõ ràng 7 quận lõi trung tâm với các quận/huyện mở rộng và ven đô."),
            ("Khoảng cách tới Trung tâm:", "Tính bán kính hình học từ tâm quận tới Hồ Hoàn Kiếm làm đại diện cho sự thuận tiện giao thương.")
        ]),
        ("HÌNH HỌC THỬA ĐẤT", [
            ("Chuẩn hóa Đơn giá m²:", "Tạo biến mục tiêu đơn giá giúp so sánh công bằng giữa các bất động sản có quy mô khác nhau."),
            ("Tổng diện tích sàn sử dụng:", "Tích hợp giữa Diện tích và Số tầng, phản ánh trực tiếp không gian sinh hoạt thực tế của ngôi nhà."),
            ("Tỷ lệ Mặt tiền / Diện tích:", "Đánh giá mức độ thoáng đãng, hình thế thửa đất và khả năng tiếp cận mặt đường giao thông.")
        ]),
        ("PHÁP LÝ & CÔNG NĂNG", [
            ("Trạng thái Pháp lý:", "Xác định tình trạng có Sổ đỏ / Sổ hồng sẵn sàng giao dịch, loại trừ rủi ro tranh chấp pháp lý."),
            ("Vị trí Mặt phố vs Ngõ hẻm:", "Tách biệt giá trị thương mại kinh doanh của nhà mặt phố với không gian yên tĩnh của nhà trong ngõ."),
            ("Mật độ Không gian sống:", "Đo lường diện tích bình quân trên mỗi phòng ngủ, phân định rõ phân khúc bình dân và cao cấp.")
        ])
    ]

    for idx, (f_title, f_items) in enumerate(feat_cols):
        c_left = Inches(0.8) + idx * (col_w + gap)
        tf_f = add_card(s4, c_left, top_pos, col_w, h_pos, f"TRỤ CỘT {idx+1}: {f_title}", header_bg=NAVY, f_size=Pt(13.5))

        for it_idx, (it_lbl, it_val) in enumerate(f_items):
            pt = tf_f.paragraphs[0] if it_idx == 0 else tf_f.add_paragraph()
            pt.text = f"• {it_lbl}"
            pt.font.name = "Arial"
            pt.font.size = Pt(13.5)
            pt.font.bold = True
            pt.font.color.rgb = GOLD
            if it_idx > 0:
                pt.space_before = Pt(16)

            pd = tf_f.add_paragraph()
            pd.text = it_val
            pd.font.name = "Arial"
            pd.font.size = Pt(13)
            pd.font.color.rgb = CHARCOAL
            pd.space_before = Pt(3)

    # ==========================================
    # SLIDE 5: THIẾT KẾ SCIKIT-LEARN PIPELINE (LAYOUT: HORIZONTAL FLOW + 2 NGUYÊN TẮC)
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Thiết Kế Scikit-Learn Pipeline & Chống Rò Rỉ Dữ Liệu")

    # Flow ngang 4 block
    pipe_w = Inches(2.78)
    pipe_gap = Inches(0.20)
    pipe_steps = [
        ("ĐẦU VÀO DỮ LIỆU", "Raw DataFrame", "37.402 bản ghi sạch"),
        ("TIỀN XỬ LÝ ĐẶC TRƯNG", "ColumnTransformer", "Điền khuyết & Chuẩn hóa"),
        ("MÔ HÌNH HỌC MÁY", "Gradient Boosting", "Huấn luyện trên Train Set"),
        ("ĐÁNH GIÁ ĐỘC LẬP", "Train / Test Split", "Train 29.921 | Test 7.481")
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
        pb0.font.size = Pt(11)
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
        pb2.font.size = Pt(11.5)
        pb2.font.color.rgb = RGBColor(226, 232, 240)
        pb2.space_before = Pt(4)

    # 2 Thẻ nguyên tắc bên dưới
    half_w = Inches(5.67)
    gap_half = Inches(0.393)
    tf_l5 = add_card(s5, Inches(0.8), Inches(3.25), half_w, Inches(3.75), "TRIỆT TIÊU RÒ RỈ DỮ LIỆU (DATA LEAKAGE)", header_bg=NAVY, f_size=Pt(13.5))
    l5_items = [
        ("Phân chia Train/Test 80/20 từ đầu:", "Dữ liệu được chia thành tập Huấn luyện (29.921 bản ghi) và Kiểm thử (7.481 bản ghi) ngay trước mọi bước xử lý."),
        ("Nguyên tắc 'Chỉ học trên tập Train':", "Mọi giá trị thống kê điền khuyết và độ lệch chuẩn chuẩn hóa chỉ được tính toán trên tập Huấn luyện."),
        ("Bảo toàn tính khách quan của tập Test:", "Tập Kiểm thử hoàn toàn đóng vai trò là dữ liệu mới trong tương lai, chỉ áp dụng phép biến đổi mà không học lại tham số.")
    ]
    for it_idx, (it_h, it_b) in enumerate(l5_items):
        pt = tf_l5.paragraphs[0] if it_idx == 0 else tf_l5.add_paragraph()
        pt.text = f"• {it_h}"
        pt.font.name = "Arial"
        pt.font.size = Pt(13.5)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(12)
        pd = tf_l5.add_paragraph()
        pd.text = it_b
        pd.font.name = "Arial"
        pd.font.size = Pt(13)
        pd.font.color.rgb = CHARCOAL
        pd.space_before = Pt(2)

    tf_r5 = add_card(s5, Inches(0.8) + half_w + gap_half, Inches(3.25), half_w, Inches(3.75), "ĐÓNG GÓI SẢN PHẨM & TÍNH TÁI LẬP (REPRODUCIBILITY)", header_bg=NAVY, f_size=Pt(13.5))
    r5_items = [
        ("Đóng gói thành một tệp duy nhất:", "Toàn bộ chu trình tiền xử lý và mô hình được tích hợp nhất quán trong tệp nhị phân (`pipeline.pkl`)."),
        ("Suy diễn thời gian thực (Real-time):", "Cho phép đưa trực tiếp thông tin một căn nhà thô vào hệ thống và nhận ngay kết quả định giá tự động."),
        ("Dễ dàng bảo trì và mở rộng:", "Sẵn sàng cập nhật dữ liệu định kỳ hoặc mở rộng phạm vi định giá sang các tỉnh thành khác mà không gãy luồng xử lý.")
    ]
    for it_idx, (it_h, it_b) in enumerate(r5_items):
        pt = tf_r5.paragraphs[0] if it_idx == 0 else tf_r5.add_paragraph()
        pt.text = f"• {it_h}"
        pt.font.name = "Arial"
        pt.font.size = Pt(13.5)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(12)
        pd = tf_r5.add_paragraph()
        pd.text = it_b
        pd.font.name = "Arial"
        pd.font.size = Pt(13)
        pd.font.color.rgb = CHARCOAL
        pd.space_before = Pt(2)

    # ==========================================
    # SLIDE 6: THỐNG KÊ MÔ TẢ 4 HỌ DỮ LIỆU (LAYOUT: MA TRẬN 2x2)
    # Loại bỏ triệt để các ký tự skewness, r, hệ số rườm rà
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Thống Kê Mô Tả 4 Họ Dữ Liệu Bất Động Sản")

    m_w = Inches(5.67)
    m_h = Inches(2.65)
    m_gap_x = Inches(0.393)
    m_gap_y = Inches(0.35)

    matrix_cards = [
        ("HỌ 1: LOẠI HÌNH & QUY MÔ MẪU", [
            ("Quy mô phân tích:", "37.402 bản ghi sạch sau phễu lọc 18 tháng, đại diện 12 quận/huyện trọng điểm."),
            ("Cơ cấu loại hình BĐS:", "68.4% Nhà riêng / Liền kề, 22.1% Căn hộ chung cư, 9.5% Nhà mặt phố thương mại."),
            ("Ý nghĩa thực tiễn:", "Phân chia rõ theo loại hình để mô hình định giá phản ánh đúng bản chất từng phân khúc.")
        ]),
        ("HỌ 2: PHÂN BỐ KHÔNG GIAN ĐỊA LÝ", [
            ("Mật độ giao dịch:", "Hơn một nửa số lượng tin tập trung tại 4 quận: Cầu Giấy, Đống Đa, Nam Từ Liêm, Hà Đông."),
            ("Bán kính nghiên cứu:", "Trải dài từ trung tâm Hoàn Kiếm ra các quận mở rộng và huyện ven đô."),
            ("Ý nghĩa thực tiễn:", "Vị trí địa lý là yếu tố chi phối mạnh mẽ nhất đến sự chênh lệch đơn giá nhà đất.")
        ]),
        ("HỌ 3: HÌNH HỌC THỬA ĐẤT", [
            ("Diện tích đất:", "Dao động phổ biến từ 38 đến 85 m² (mức trung vị thực tế đạt 52 m²)."),
            ("Chiều rộng mặt tiền:", "Tập trung nhiều ở khoảng 3.2m đến 5.5m (mức trung vị đạt 4.2m)."),
            ("Ý nghĩa thực tiễn:", "Quy mô diện tích và độ rộng mặt tiền là hai yếu tố cốt lõi quyết định tổng giá trị nhà.")
        ]),
        ("HỌ 4: PHÂN PHỐI GIÁ & ĐƠN GIÁ M²", [
            ("Tổng giá trị tài sản:", "Mức trung vị đạt 4.8 tỷ VNĐ (dao động phổ biến từ 1.2 tỷ đến 35 tỷ VNĐ)."),
            ("Đơn giá m²:", "Mức trung vị đạt 92.5 triệu/m²; đại đa số tài sản tập trung ở phân khúc 60 - 120 triệu/m²."),
            ("Ý nghĩa thực tiễn:", "Thị trường có xu hướng lệch về phân khúc phổ thông, đòi hỏi chuyển đổi thang đo phù hợp.")
        ])
    ]

    for idx, (m_title, m_items) in enumerate(matrix_cards):
        row_i = idx // 2
        col_i = idx % 2
        m_left = Inches(0.8) + col_i * (m_w + m_gap_x)
        m_top = Inches(1.35) + row_i * (m_h + m_gap_y)

        tf_m = add_card(s6, m_left, m_top, m_w, m_h, m_title, header_bg=NAVY, f_size=Pt(13.5))
        for it_idx, (it_h, it_b) in enumerate(m_items):
            pt = tf_m.paragraphs[0] if it_idx == 0 else tf_m.add_paragraph()
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
            run_b.font.size = Pt(13)
            run_b.font.bold = False
            run_b.font.color.rgb = CHARCOAL

    # ==========================================
    # SLIDE 7: [BIỂU ĐỒ 01] MA TRẬN TƯƠNG QUAN (LAYOUT: LEFT HERO CHART)
    # Loại bỏ r = 0.72, r = 0.88, VIF rườm rà
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    fig1_path = os.path.join(FIG_DIR, "01_correlation_heatmap.png")
    create_left_chart_slide(
        s7,
        "Biểu Đồ 1: Mức Độ Tương Quan Giữa Các Đặc Trưng Nhà Đất",
        fig1_path,
        "TƯƠNG QUAN ĐẶC TRƯNG (BĐ 01)",
        [
            ("Tác Dụng & Mục Đích Biểu Đồ:",
             "Đo lường mức độ liên hệ tuyến tính giữa các đặc tính nhà đất (Diện tích, Mặt tiền, Số tầng, Số phòng) với Đơn giá và Tổng giá bán."),
            ("Phát Hiện Cốt Lõi:",
             "Diện tích đất và tổng diện tích sàn là hai yếu tố có mối liên kết thuận chiều mạnh mẽ nhất với tổng giá trị của một căn nhà."),
            ("Kiểm Soát Tương Quan Trùng Lặp:",
             "Diện tích sàn và diện tích đất có mức độ gắn kết rất cao với nhau -> Cần kỹ thuật điều chuẩn mô hình để tránh hiện tượng nhiễu thông tin."),
            ("Ứng Dụng Trong Mô Hình Hóa:",
             "Lựa chọn tập hợp các đặc trưng độc lập, có giá trị đóng góp thông tin thực chất nhất cho các thuật toán định giá.")
        ]
    )

    # ==========================================
    # SLIDE 8: [BIỂU ĐỒ 02] PHÂN PHỐI GIÁ & LOGARIT (LAYOUT: TOP-WIDE HERO CHART)
    # Loại bỏ Skewness, Kurtosis rườm rà
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    fig2_path = os.path.join(FIG_DIR, "02_price_distribution.png")
    create_top_chart_slide(
        s8,
        "Biểu Đồ 2: Phân Phối Giá BĐS & Hiệu Quả Sau Biến Đổi Logarit",
        fig2_path,
        [
            ("1. PHÂN PHỐI GIÁ THỰC TẾ",
             "Đơn giá tập trung chủ yếu ở phân khúc vừa túi tiền (60 - 120 triệu/m²), trong khi một số ít nhà phố mặt tiền đắt đỏ kéo dài phân phối sang phía giá cao."),
            ("2. HIỆU QUẢ CHUYỂN ĐỔI LOGARIT",
             "Phép biến đổi đưa dữ liệu về dạng đối xứng hình chuông chuẩn mực, triệt tiêu độ lệch và tạo điều kiện tối ưu cho các thuật toán học máy."),
            ("3. Ý NGHĨA KHOA HỌC DỮ LIỆU",
             "Giảm bớt sự chi phối quá mức của những căn nhà siêu đắt, giúp mô hình dự báo chính xác và ổn định hơn trên toàn dải giá trị.")
        ]
    )

    # ==========================================
    # SLIDE 9: [BIỂU ĐỒ 03] TƯƠNG QUAN PHÂN TÁN DIỆN TÍCH - MẶT TIỀN (LAYOUT: TOP-WIDE HERO CHART)
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    fig3_path = os.path.join(FIG_DIR, "03_price_vs_area_scatter.png")
    create_top_chart_slide(
        s9,
        "Biểu Đồ 3: Tương Quan Phân Tán Đa Chiều Giữa Diện Tích, Mặt Tiền & Giá",
        fig3_path,
        [
            ("1. QUY CHUẨN PHÂN LÔ THỰC TẾ",
             "Bề rộng mặt tiền tập trung rất rõ nét theo các kích thước quy chuẩn đô thị phổ biến: 3m, 3.5m, 4m, 4.5m, 5m, 6m."),
            ("2. BƯỚC NHẢY THƯƠNG MẠI",
             "Mặt tiền từ 5m trở lên tạo bước nhảy vọt về đơn giá nhờ khả năng kinh doanh buôn bán thuận lợi hoặc cho phép ô tô đỗ cửa / vào nhà."),
            ("3. Ý NGHĨA KINH TẾ ĐỊNH GIÁ",
             "Bề rộng mặt tiền là yếu tố quyết định thanh khoản và thặng dư thương mại của bất động sản, vượt trội so với diện tích đất thô.")
        ]
    )

    # ==========================================
    # SLIDE 10: [BIỂU ĐỒ 04] BOXPLOT 12 QUẬN/HUYỆN (LAYOUT: TOP-WIDE HERO CHART)
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    fig4_path = os.path.join(FIG_DIR, "04_district_price_boxplot.png")
    create_top_chart_slide(
        s10,
        "Biểu Đồ 4: Phân Bố Đơn Giá 12 Quận/Huyện Trọng Điểm Theo Mức Trung Vị",
        fig4_path,
        [
            ("1. TẦNG 1: LÕI TRUNG TÂM (100 - 105 TR/M²)",
             "Cầu Giấy, Ba Đình, Tây Hồ, Đống Đa. Nền giá cao nhất thành phố, giá trị bảo toàn ổn định và thanh khoản luôn ở mức rất cao."),
            ("2. TẦNG 2: ĐÔ THỊ MỞ RỘNG (85 - 95 TR/M²)",
             "Thanh Xuân, Hai Bà Trưng, Nam Từ Liêm. Trục phát triển sôi động với mạng lưới metro, hạ tầng dịch vụ và văn phòng hoàn thiện."),
            ("3. TẦNG 3: VÀNH ĐAI & VEN ĐÔ (60 - 80 TR/M²)",
             "Bắc Từ Liêm, Hoàng Mai, Long Biên, Hà Đông, Thanh Trì. Mặt bằng giá mềm, quỹ đất rộng, là lựa chọn an cư của các gia đình trẻ.")
        ]
    )

    # ==========================================
    # SLIDE 11: SO SÁNH 4 MÔ HÌNH HỌC MÁY (LAYOUT: FULL-WIDTH TABLE + BOTTOM BANNER)
    # Loại bỏ chỉ số chưa xác minh & tinh giản bảng số liệu trực quan
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Thử Nghiệm & So Sánh 4 Mô Hình Học Máy (Test Set: 7.481 Bản Ghi)")

    t11_shape = s11.shapes.add_table(5, 4, Inches(0.8), Inches(1.35), Inches(11.733), Inches(3.60))
    t11 = t11_shape.table
    t11.columns[0].width = Inches(2.80)
    t11.columns[1].width = Inches(2.20)
    t11.columns[2].width = Inches(2.20)
    t11.columns[3].width = Inches(4.533)

    models_data = [
        ["Mô Hình Machine Learning", "Sai Số MAE (tr/m²)", "Độ Phù Hợp (R²)", "Nhận Xét & Đánh Giá Kỹ Thuật"],
        ["Linear Regression", "28.5 triệu/m²", "0.36", "Mô hình cơ sở; chưa giải quyết được các quan hệ phi tuyến."],
        ["Ridge Regression", "28.5 triệu/m²", "0.36", "Kiểm soát tương quan giữa các biến; hiệu năng tương đương OLS."],
        ["Random Forest (50 cây)", "26.2 triệu/m²", "0.43", "Cải thiện rõ rệt; giảm mạnh sai số nhờ cấu trúc tập hợp cây."],
        ["Gradient Boosting (GBDT)", "26.1 triệu/m²", "0.44", "🏆 QUÁN QUÂN: Sai số thấp nhất, độ chính xác cao nhất toàn diện."]
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
                p.font.size = Pt(14)
                p.font.color.rgb = WHITE
                p.alignment = PP_ALIGN.CENTER
            elif r_idx == 4:
                cell.fill.solid()
                cell.fill.fore_color.rgb = LIGHT_BLUE
                p.font.bold = True
                p.font.size = Pt(13.5)
                p.font.color.rgb = NAVY
                if c_idx in [1, 2]:
                    p.alignment = PP_ALIGN.CENTER
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = WHITE if r_idx % 2 == 1 else LIGHT_BG
                p.font.size = Pt(13)
                p.font.color.rgb = CHARCOAL
                if c_idx in [1, 2]:
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
    pb1.text = "• Gradient Boosting (GBDT) được lựa chọn làm mô hình định giá cốt lõi: Đạt sai số MAE thấp nhất (26.1 triệu/m²), giảm hơn 8% sai số so với mô hình tuyến tính nhờ giải quyết tốt tính phi tuyến của thị trường.\n• Kết quả được đánh giá độc lập trên tập kiểm thử 7.481 bản ghi, khẳng định mô hình ổn định và sẵn sàng đóng gói ứng dụng thực tiễn."
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
        "Biểu Đồ 5: So Sánh Hiệu Năng Giữa Các Mô Hình Học Máy",
        fig5_path,
        [
            ("1. GBDT DẪN ĐẦU HIỆU NĂNG",
             "Đạt độ chính xác cao nhất và sai số dự báo thấp nhất (26.1 triệu/m²) trên toàn bộ các thử nghiệm đối đầu trên tập kiểm thử độc lập."),
            ("2. BẢN CHẤT TƯƠNG TÁC PHI TUYẾN",
             "Thị trường nhà đất có mối tương tác phức tạp (mặt tiền ở trung tâm có giá trị khác xa ngoại thành), mô hình cây giải quyết hoàn hảo đặc thù này."),
            ("3. Ý NGHĨA KHOA HỌC DỮ LIỆU",
             "Khẳng định các thuật toán học máy dạng cây tăng cường là sự lựa chọn tối ưu, đủ cơ sở khoa học để phục vụ bài toán định giá thực tế.")
        ]
    )

    # ==========================================
    # SLIDE 13: [BIỂU ĐỒ 06] TẦM QUAN TRỌNG ĐẶC TRƯNG (LAYOUT: LEFT HERO CHART)
    # Loại bỏ % rườm rà
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    fig6_path = os.path.join(FIG_DIR, "06_feature_importance.png")
    create_left_chart_slide(
        s13,
        "Biểu Đồ 6: Xếp Hạng Các Yếu Tố Chi Phối Giá Bất Động Sản",
        fig6_path,
        "YẾU TỐ ĐỊNH GIÁ (BĐ 06)",
        [
            ("Tác Dụng & Mục Đích Biểu Đồ:",
             "Minh bạch hóa mức độ đóng góp của từng đặc trưng trong mô hình quán quân Gradient Boosting, mở chiếc 'hộp đen' của thuật toán học máy."),
            ("🥇 Vị Trí & Loại Hình Chi Phối Hàng Đầu:",
             "Yếu tố nhà trong ngõ và vị trí thuộc quận nội thành là hai lực chi phối mạnh nhất, quyết định phần lớn mặt bằng giá của một căn nhà."),
            ("🥈 Quy Mô Diện Tích & Chiều Cao:",
             "Diện tích thửa đất kết hợp cùng Số tầng xây dựng quyết định tổng không gian ở và công năng khai thác thực tế của tài sản."),
            ("🥉 Hiệu Quả Của Kỹ Nghệ Đặc Trưng:",
             "Các biến phái sinh như Diện tích mỗi phòng ngủ và Tổng diện tích sàn lọt nhóm dẫn đầu, vượt trội so với diện tích đất thô ban đầu.")
        ]
    )

    # ==========================================
    # SLIDE 14: KHUNG SUY LUẬN THỐNG KÊ (LAYOUT: SPLIT CARDS)
    # Loại bỏ triệt để s1^2, s2^2, alpha, beta, H0/H1 rườm rà
    # ==========================================
    s14 = prs.slides.add_slide(blank_layout)
    add_header(s14, "Khung Suy Luận Thống Kê & Quy Trình Kiểm Định Giả Thuyết")

    tf_l14 = add_card(s14, Inches(0.8), Inches(1.35), half_w, Inches(5.65), "CÂY QUYẾT ĐỊNH LỰA CHỌN PHÉP KIỂM ĐỊNH", header_bg=DARK_BLUE, bg_color=NAVY, f_size=Pt(14))
    l14_items = [
        ("Bản chất Thống kê Suy luận:",
         "Chuyển từ việc chỉ tóm tắt 37.402 bản ghi quan sát được sang khẳng định các quy luật trên toàn thể thị trường kèm mức độ tin cậy khoa học."),
        ("1. So sánh 2 nhóm (Nội đô vs Ngoại thành):",
         "Phương sai hai nhóm không đồng nhất ➔ Áp dụng kiểm định Welch's t-test để so sánh mức chênh lệch trung bình một cách chính xác."),
        ("2. So sánh nhiều nhóm (12 Quận/Huyện):",
         "Phân tích phương sai (ANOVA) kết hợp kiểm định đối sánh từng cặp (Tukey HSD) nhằm phát hiện các quận có mức giá tương đương."),
        ("3. Dữ liệu phân phối lệch:",
         "Sử dụng kỹ thuật tái lấy mẫu không phụ thuộc phân phối chuẩn (Bootstrap) để xác định khoảng tin cậy 95% cho từng địa bàn.")
    ]
    for it_idx, (it_h, it_b) in enumerate(l14_items):
        pt = tf_l14.paragraphs[0] if it_idx == 0 else tf_l14.add_paragraph()
        pt.text = f"• {it_h}"
        pt.font.name = "Arial"
        pt.font.size = Pt(13.5)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(12)
        pd = tf_l14.add_paragraph()
        pd.text = it_b
        pd.font.name = "Arial"
        pd.font.size = Pt(13)
        pd.font.color.rgb = WHITE
        pd.space_before = Pt(2)

    tf_r14 = add_card(s14, Inches(0.8) + half_w + gap_half, Inches(1.35), half_w, Inches(5.65), "QUY TRÌNH KIỂM ĐỊNH & Ý NGHĨA THỰC TIỄN", header_bg=NAVY, bg_color=WHITE, f_size=Pt(14))
    r14_items = [
        ("Thiết lập giả thuyết khách quan:",
         "Đặt giả thuyết ban đầu là không có sự khác biệt trước khi quan sát số liệu, đảm bảo kết quả phân tích hoàn toàn trung thực và khoa học."),
        ("Đo lường mức độ ảnh hưởng thực tế:",
         "Không chỉ kiểm tra sự khác biệt có ý nghĩa thống kê mà còn đo lường độ lớn khoảng cách chênh lệch tính bằng triệu đồng/m² trong thực tế."),
        ("Kiểm soát rủi ro kết luận:",
         "Thiết lập ngưỡng tin cậy nghiêm ngặt nhằm tránh kết luận nhầm lẫn (tránh nhận định có sự khác biệt khi thực tế chỉ là do ngẫu nhiên).")
    ]
    for it_idx, (it_h, it_b) in enumerate(r14_items):
        pt = tf_r14.paragraphs[0] if it_idx == 0 else tf_r14.add_paragraph()
        pt.text = f"• {it_h}"
        pt.font.name = "Arial"
        pt.font.size = Pt(13.5)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(14)
        pd = tf_r14.add_paragraph()
        pd.text = it_b
        pd.font.name = "Arial"
        pd.font.size = Pt(13)
        pd.font.color.rgb = CHARCOAL
        pd.space_before = Pt(2)

    # ==========================================
    # SLIDE 15: THỐNG KÊ SUY LUẬN - WELCH'S T-TEST (LAYOUT: SPLIT CONTRAST)
    # Loại bỏ t = 64.18, p < 10^-16, U = 2.35e+08, Cohen's d = 0.6099
    # ==========================================
    s15 = prs.slides.add_slide(blank_layout)
    add_header(s15, "Thống Kê Suy Luận: So Sánh Giá Đất Nội Đô & Ngoại Thành")

    tf_l15 = add_card(s15, Inches(0.8), Inches(1.35), half_w, Inches(4.20), "BẤT ĐỘNG SẢN NỘI ĐÔ (23.330 BẢN GHI)", header_bg=NAVY, f_size=Pt(14))
    l15_items = [
        ("Mặt bằng đơn giá thực tế:", "Đơn giá trung bình đạt 114.2 triệu/m² (mức trung vị đạt 96.7 triệu/m²)."),
        ("Khu vực đại diện:", "Gồm 7 quận trung tâm lịch sử: Hoàn Kiếm, Ba Đình, Đống Đa, Hai Bà Trưng, Cầu Giấy, Tây Hồ, Thanh Xuân."),
        ("Đặc tính kinh tế cốt lõi:", "Hạ tầng hoàn chỉnh, tiện ích thương mại dày đặc, quỹ đất khan hiếm tạo nên sàn giá cao bền vững.")
    ]
    for it_idx, (it_h, it_b) in enumerate(l15_items):
        pt = tf_l15.paragraphs[0] if it_idx == 0 else tf_l15.add_paragraph()
        pt.text = f"• {it_h}"
        pt.font.name = "Arial"
        pt.font.size = Pt(13.5)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(14)
        pd = tf_l15.add_paragraph()
        pd.text = it_b
        pd.font.name = "Arial"
        pd.font.size = Pt(13)
        pd.font.color.rgb = CHARCOAL
        pd.space_before = Pt(2)

    tf_r15 = add_card(s15, Inches(0.8) + half_w + gap_half, Inches(1.35), half_w, Inches(4.20), "BẤT ĐỘNG SẢN NGOẠI THÀNH (14.072 BẢN GHI)", header_bg=NAVY, f_size=Pt(14))
    r15_items = [
        ("Mặt bằng đơn giá thực tế:", "Đơn giá trung bình đạt 82.2 triệu/m² (mức trung vị đạt 76.8 triệu/m²)."),
        ("Khu vực đại diện:", "Gồm các quận mở rộng và huyện ven đô: Hà Đông, Hoàng Mai, Long Biên, Bắc Từ Liêm, Thanh Trì..."),
        ("Đặc tính kinh tế cốt lõi:", "Quỹ đất phát triển rộng, mặt bằng giá vừa túi tiền, phù hợp nhu cầu định cư số đông.")
    ]
    for it_idx, (it_h, it_b) in enumerate(r15_items):
        pt = tf_r15.paragraphs[0] if it_idx == 0 else tf_r15.add_paragraph()
        pt.text = f"• {it_h}"
        pt.font.name = "Arial"
        pt.font.size = Pt(13.5)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(14)
        pd = tf_r15.add_paragraph()
        pd.text = it_b
        pd.font.name = "Arial"
        pd.font.size = Pt(13)
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
    ptt0.text = "🔬 KẾT LUẬN KIỂM ĐỊNH THỐNG KÊ (SO SÁNH 2 VÙNG ĐỊA LÝ)"
    ptt0.font.name = "Arial"
    ptt0.font.size = Pt(13.5)
    ptt0.font.bold = True
    ptt0.font.color.rgb = GOLD
    ptt1 = tf_tt.add_paragraph()
    ptt1.text = "• Khẳng định khoa học: Giá nhà đất Nội đô cao hơn Ngoại thành trung bình 32.0 triệu/m² (+39.0%), sự khác biệt mang tính quy luật vững chắc của thị trường, hoàn toàn không phải do biến động ngẫu nhiên.\n• Ý nghĩa thực tiễn: Mức chênh lệch lớn khẳng định vị trí trung tâm vẫn là yếu tố nắm giữ thặng dư giá trị hàng đầu tại thị trường Hà Nội."
    ptt1.font.name = "Arial"
    ptt1.font.size = Pt(13)
    ptt1.font.color.rgb = WHITE
    ptt1.space_before = Pt(6)

    # ==========================================
    # SLIDE 16: ANOVA & 9 CẶP QUẬN SONG SINH (LAYOUT: TOP SUMMARY + 2 SEGMENT CARDS)
    # Loại bỏ F = 368.11, H = 5465.33, p-adj > 0.05
    # ==========================================
    s16 = prs.slides.add_slide(blank_layout)
    add_header(s16, "Phân Tầng Giá 12 Quận/Huyện & Nhận Diện Tài Sản Thay Thế")

    # Top Card ANOVA
    tf_top16 = add_card(s16, Inches(0.8), Inches(1.35), Inches(11.733), Inches(1.85), "KẾT QUẢ PHÂN TÍCH PHƯƠNG SAI & ĐỐI SÁNH ĐA NHÓM GIỮA 12 QUẬN", header_bg=NAVY, f_size=Pt(14))
    top16_items = [
        ("Phân tích phương sai (ANOVA):", "Khẳng định giữa 12 quận/huyện có sự phân tầng giá cực kỳ sâu sắc, vị trí địa lý quyết định mức sàn giá."),
        ("Kết quả kiểm định đối sánh từng cặp:", "Phát hiện chính xác 9 cặp quận có mặt bằng giá tương đương nhau, tạo thành các cụm tài sản thay thế hoàn hảo.")
    ]
    for it_idx, (it_h, it_b) in enumerate(top16_items):
        pt = tf_top16.paragraphs[0] if it_idx == 0 else tf_top16.add_paragraph()
        pt.text = f"• {it_h} "
        pt.font.name = "Arial"
        pt.font.size = Pt(13.5)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(8)
        run_b = pt.add_run()
        run_b.text = it_b
        run_b.font.name = "Arial"
        run_b.font.size = Pt(13)
        run_b.font.color.rgb = CHARCOAL

    # 2 Cards Cặp quận song sinh bên dưới
    tf_l16 = add_card(s16, Inches(0.8), Inches(3.40), half_w, Inches(3.65), "9 CẶP QUẬN CÓ MẶT BẰNG GIÁ TƯƠNG ĐỒNG NHAU", header_bg=NAVY, f_size=Pt(14))
    pairs_list = [
        ("Tam giác vàng trung tâm:", "Ba Đình (128.6 tr) ≈ Cầu Giấy (125.3 tr) ≈ Tây Hồ (123.7 tr/m²) tạo thành cụm giá cao nhất."),
        ("Cặp cận trung tâm phía Nam:", "Hai Bà Trưng (102.6 tr) ≈ Thanh Xuân (102.7 tr/m²), mặt bằng giá gần như trùng khớp hoàn toàn."),
        ("Chùm 4 quận mở rộng đồng nhất:", "Bắc Từ Liêm (83.9 tr) ≈ Hoàng Mai (83.8 tr) ≈ Long Biên (85.5 tr) ≈ Hà Đông (80.8 tr/m²)."),
        ("Nhóm huyện ven đô:", "Thanh Trì (62.9 tr/m²) định hình phân khúc giá mềm nhất trong nhóm nghiên cứu.")
    ]
    for it_idx, (it_h, it_b) in enumerate(pairs_list):
        pt = tf_l16.paragraphs[0] if it_idx == 0 else tf_l16.add_paragraph()
        pt.text = f"• {it_h} "
        pt.font.name = "Arial"
        pt.font.size = Pt(13.5)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(10)
        run_b = pt.add_run()
        run_b.text = it_b
        run_b.font.name = "Arial"
        run_b.font.size = Pt(12.5)
        run_b.font.color.rgb = CHARCOAL

    tf_r16 = add_card(s16, Inches(0.8) + half_w + gap_half, Inches(3.40), half_w, Inches(3.65), "Ý NGHĨA KINH DOANH & TỐI ƯU HÓA DANH MỤC", header_bg=NAVY, f_size=Pt(14))
    strat_list = [
        ("Chiến lược tài sản thay thế (Substitute Assets):", "Khi giá tại một quận bị đẩy lên quá cao, nhà đầu tư có thể chuyển dịch vốn sang quận lân cận có hạ tầng và mức giá tương đương."),
        ("Phòng ngừa rủi ro định giá lệch:", "Nhận diện những căn nhà bị chào giá lệch khỏi mức cân bằng của cụm quận tương đồng để thương lượng mức giá tốt hơn."),
        ("Khuyến nghị cho khách hàng mua nhà:", "Người mua với ngân sách khoảng 80 - 85 tr/m² có thể linh hoạt chuyển đổi giữa Bắc Từ Liêm, Hoàng Mai, Long Biên, Hà Đông.")
    ]
    for it_idx, (it_h, it_b) in enumerate(strat_list):
        pt = tf_r16.paragraphs[0] if it_idx == 0 else tf_r16.add_paragraph()
        pt.text = f"• {it_h}"
        pt.font.name = "Arial"
        pt.font.size = Pt(13.5)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(10)
        pd = tf_r16.add_paragraph()
        pd.text = it_b
        pd.font.name = "Arial"
        pd.font.size = Pt(12.5)
        pd.font.color.rgb = CHARCOAL
        pd.space_before = Pt(2)

    # ==========================================
    # SLIDE 17: [BIỂU ĐỒ 07] KHOẢNG TIN CẬY 95% (LAYOUT: LEFT HERO CHART)
    # ==========================================
    s17 = prs.slides.add_slide(blank_layout)
    fig7_path = os.path.join(FIG_DIR, "07_confidence_intervals_districts.png")
    create_left_chart_slide(
        s17,
        "Biểu Đồ 7: Khoảng Giá Trị An Toàn Của Từng Quận/Huyện",
        fig7_path,
        "KHOẢNG GIÁ AN TOÀN (BĐ 07)",
        [
            ("Tác Dụng & Mục Đích Biểu Đồ:",
             "Ước lượng dải biến thiên đơn giá thực tế của từng quận với độ tin cậy cao, xác định biên độ an toàn giữa mức giá sàn và mức giá trần."),
            ("Phương Pháp Ước Lượng Ổn Định:",
             "Kỹ thuật ước lượng không phụ thuộc giả định chuẩn hóa, bảo toàn độ chính xác ngay cả ở các khu vực có phân phối giá phân tán mạnh."),
            ("Minh Chứng Cặp Quận Tương Đồng:",
             "Thanh dải giá của Ba Đình, Cầu Giấy và Tây Hồ gối đè lên nhau, giải thích trực quan lý do tại sao 3 quận này có mức giá tương đương."),
            ("Ứng Dụng Quản Trị Rủi Ro Tín Dụng:",
             "Ngân hàng có thể sử dụng mức cận an toàn của dải giá làm cơ sở xác định hạn mức cho vay thế chấp bất động sản.")
        ]
    )

    # ==========================================
    # SLIDE 18: TÁC ĐỘNG CỦA CÁC YẾU TỐ & 3 NGUYÊN TẮC ĐẠO ĐỨC (LAYOUT: ASYMMETRIC SPLIT)
    # Loại bỏ beta, R^2 = 0.283, t = 66.31, p = 0.708, Ceteris Paribus
    # ==========================================
    s18 = prs.slides.add_slide(blank_layout)
    add_header(s18, "Tác Động Của Các Yếu Tố Đến Đơn Giá & 3 Nguyên Tắc Diễn Giải")

    tf_l18 = add_card(s18, Inches(0.8), Inches(1.35), Inches(4.30), Inches(5.65), "MỨC ĐỘ TÁC ĐỘNG ĐẾN ĐƠN GIÁ (MẪU NGHIÊN CỨU)", header_bg=NAVY, f_size=Pt(13.5))
    l18_items = [
        ("Vị trí nội đô:", "Cùng diện tích và số tầng, nhà nội đô gắn liền với mức giá cao hơn khoảng 33 triệu/m² so với ngoại thành."),
        ("Vị trí trong ngõ hẻm:", "Nhà trong ngõ hẻm gắn liền với mức giá thấp hơn khoảng 33 triệu/m² so với nhà mặt phố."),
        ("Chiều rộng mặt tiền:", "Mỗi mét mặt tiền mở rộng đi kèm với mức tăng thêm khoảng 2 triệu/m² đơn giá."),
        ("Chiều sâu thửa đất:", "Không cho thấy tác động rõ rệt đến đơn giá khi các yếu tố diện tích sàn và mặt tiền đã được xem xét.")
    ]
    for it_idx, (it_h, it_b) in enumerate(l18_items):
        pt = tf_l18.paragraphs[0] if it_idx == 0 else tf_l18.add_paragraph()
        pt.text = f"• {it_h}"
        pt.font.name = "Arial"
        pt.font.size = Pt(13.5)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(14)
        pd = tf_l18.add_paragraph()
        pd.text = it_b
        pd.font.name = "Arial"
        pd.font.size = Pt(13)
        pd.font.color.rgb = CHARCOAL
        pd.space_before = Pt(2)

    # 3 Thẻ Đạo Đức Dữ Liệu bên phải
    right_left_18 = Inches(0.8) + Inches(4.30) + Inches(0.35)
    right_w_18 = Inches(7.083)
    card_h_18 = Inches(1.72)
    gap_y_18 = Inches(0.24)

    ethics_cards = [
        ("1. NGUYÊN TẮC 1: KHÔNG KHẲNG ĐỊNH QUAN HỆ NHÂN QUẢ",
         "Bắt buộc dùng cụm từ 'gắn liền với / đi kèm với', không dùng từ 'gây ra'. Mô hình quan sát chỉ phản ánh mối liên hệ thống kê giữa các biến số, không chứng minh quan hệ nhân quả."),
        ("2. NGUYÊN TẮC 2: ĐIỀU KIỆN CỐ ĐỊNH CÁC YẾU TỐ KHÁC",
         "Mọi nhận định về mức tăng giảm giá chỉ có hiệu lực khi các đặc tính khác (diện tích, số tầng, vị trí) được giữ nguyên để cô lập tác động riêng lẻ của đặc tính đang xét."),
        ("3. NGUYÊN TẮC 3: GIỚI HẠN TRONG PHẠM VI DỮ LIỆU ĐÃ HỌC",
         "Kết quả phân tích chỉ có giá trị trong phạm vi dữ liệu quan sát (nhà đất phổ thông dưới 500 m² và dưới 500 tr/m²), tuyệt đối không suy diễn cho các dự án siêu biệt thự đặc thù.")
    ]
    for e_idx, (e_title, e_desc) in enumerate(ethics_cards):
        e_top = Inches(1.35) + e_idx * (card_h_18 + gap_y_18)
        tf_e = add_card(s18, right_left_18, e_top, right_w_18, card_h_18, e_title, header_bg=NAVY, f_size=Pt(13.5))
        p = tf_e.paragraphs[0]
        p.text = e_desc
        p.font.name = "Arial"
        p.font.size = Pt(13)
        p.font.color.rgb = CHARCOAL
        p.space_before = Pt(4)

    # ==========================================
    # SLIDE 19: [BIỂU ĐỒ 08] KIỂM ĐỊNH GIẢ ĐỊNH (LAYOUT: LEFT HERO CHART)
    # Loại bỏ LINE, Breusch-Pagan, Jarque-Bera rườm rà
    # ==========================================
    s19 = prs.slides.add_slide(blank_layout)
    fig8_path = os.path.join(FIG_DIR, "08_line_assumptions_diagnostics.png")
    create_left_chart_slide(
        s19,
        "Biểu Đồ 8: Kiểm Tra Tính Hợp Lệ Của Mô Hình Hồi Quy",
        fig8_path,
        "KIỂM ĐỊNH MÔ HÌNH (BĐ 08)",
        [
            ("Tác Dụng & Mục Đích Biểu Đồ:",
             "Kiểm tra xem mô hình dự báo ban đầu có đáp ứng đầy đủ các điều kiện khoa học (tính chuẩn hóa và tính ổn định của sai số) hay không."),
            ("Hiện Tượng Sai Số Phình To (Hình Phễu):",
             "Đồ thị sai số phình to rõ rệt ở phân khúc nhà giá cao: Nhà càng đắt tiền thì mức độ phân tán sai số dự báo càng lớn."),
            ("Ảnh Hưởng Của Nhóm Nhà Cao Cấp:",
             "Sự xuất hiện của các biệt thự giá trị lớn kéo dải phân phối uốn cong ở hai đầu đuôi, làm méo mó các ước lượng ban đầu."),
            ("Định Hướng Khắc Phục:",
             "Minh chứng lý do bắt buộc phải chuyển sang mô hình học máy phi tuyến (Gradient Boosting) hoặc áp dụng biến đổi thang đo Logarit.")
        ]
    )

    # ==========================================
    # SLIDE 20: ĐỘT PHÁ SAU BIẾN ĐỔI LOGARIT (LAYOUT: BEFORE VS AFTER CONTRAST)
    # Loại bỏ Skewness, Kurtosis, Breusch-Pagan, Jarque-Bera
    # ==========================================
    s20 = prs.slides.add_slide(blank_layout)
    add_header(s20, "So Sánh Hiệu Quả Trước & Sau Khi Biến Đổi Thang Đo Logarit")

    tf_l20 = add_card(s20, Inches(0.8), Inches(1.35), half_w, Inches(5.65), "TRƯỚC BIẾN ĐỔI LOGARIT (THANG ĐO GỐC)", header_bg=NAVY, f_size=Pt(14))
    l20_items = [
        ("Phân phối sai số bị kéo lệch:", "Sai số dự báo bị lệch nhiều về phía các căn nhà đắt tiền, phân phối không cân xứng."),
        ("Độ phân tán sai số không đồng đều:", "Nhà giá rẻ có sai số nhỏ, nhưng nhà giá cao có sai số tăng vọt (hiện tượng hình phễu)."),
        ("Sai số trung bình còn lớn:", "Sai số bình quân trên tập kiểm thử ở mức gần 30 triệu/m² do chịu ảnh hưởng của các ngoại lai giá cao."),
        ("Khả năng khái quát hóa hạn chế:", "Các giả định cơ bản của mô hình tuyến tính bị vi phạm, làm giảm độ tin cậy khi dự báo.")
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
        pd.font.size = Pt(13)
        pd.font.color.rgb = CHARCOAL
        pd.space_before = Pt(3)

    tf_r20 = add_card(s20, Inches(0.8) + half_w + gap_half, Inches(1.35), half_w, Inches(5.65), "SAU BIẾN ĐỔI LOGARIT (NẮN CHUẨN DỮ LIỆU)", header_bg=DARK_BLUE, bg_color=NAVY, f_size=Pt(14))
    r20_items = [
        ("Phân phối sai số đối xứng chuẩn mực:", "Sai số trở nên cân bằng hoàn hảo quanh mức 0, khắc phục triệt để hiện tượng lệch đuôi."),
        ("Độ phân tán sai số ổn định:", "Thu hẹp khoảng cách sai số giữa nhà bình dân và nhà cao cấp, triệt tiêu hiện tượng phình to."),
        ("Sai số trung bình giảm xuống 28.3 tr/m²:", "Giảm bớt trọng số phạt quá mức cho các căn nhà đắt tiền, tối ưu hóa độ chính xác."),
        ("Hệ số phản ánh mức thay đổi tương đối (%):", "Hỗ trợ diễn giải kinh tế mạch lạc: Nhà nội đô có mức đơn giá cao hơn khoảng 40% so với ngoại thành.")
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
        pd.font.size = Pt(13)
        pd.font.color.rgb = WHITE
        pd.space_before = Pt(3)

    # ==========================================
    # SLIDE 21: [BIỂU ĐỒ 09] REGULARIZATION (LAYOUT: LEFT HERO CHART)
    # Loại bỏ alpha = 0.3556, L1, L2 rườm rà
    # ==========================================
    s21 = prs.slides.add_slide(blank_layout)
    fig9_path = os.path.join(FIG_DIR, "09_regularization_lasso_vs_ridge.png")
    create_left_chart_slide(
        s21,
        "Biểu Đồ 9: Kiểm Soát Quá Khớp & Tự Động Chọn Lọc Đặc Trưng",
        fig9_path,
        "ĐIỀU CHUẨN MÔ HÌNH (BĐ 09)",
        [
            ("Tác Dụng & Mục Đích Biểu Đồ:",
             "So sánh cơ chế kiểm soát hiện tượng các đặc tính phụ thuộc lẫn nhau, giúp mô hình hoạt động ổn định và không bị quá khớp dữ liệu."),
            ("🎯 Cơ Chế Lasso - Tự Động Loại Bỏ Biến Dư Thừa:",
             "Lasso tự động triệt tiêu tác động của các biến dư thừa (như Diện tích đất thô và Chiều sâu) về bằng 0, chỉ giữ lại các yếu tố cốt lõi nhất."),
            ("🛡️ Cơ Chế Ridge - Ổn Định Trọng Số Các Biến:",
             "Ridge thu nhỏ đồng đều tác động của các biến có tương quan cao mà không loại bỏ biến, giúp mô hình ổn định trước biến động dữ liệu."),
            ("Ý Nghĩa Nghiệp Vụ Thực Tế:",
             "Khi mô hình đã có biến Tổng diện tích sàn và Mặt tiền, các biến diện tích thô trở nên dư thừa và được tự động gạt bỏ để tinh gọn phương trình.")
        ]
    )

    # ==========================================
    # SLIDE 22: 7 KẾT LUẬN THỰC TIỄN CHO DOANH NGHIỆP (LAYOUT: MA TRẬN 2x2)
    # ==========================================
    s22 = prs.slides.add_slide(blank_layout)
    add_header(s22, "Kết Luận Thực Tiễn Cho Doanh Nghiệp & Nhà Đầu Tư")

    action_pillars = [
        ("TRỤ CỘT 1: ĐỊNH GIÁ & GIAO DỊCH", [
            ("Mô hình Gradient Boosting tối ưu:", "Đạt sai số dự báo thấp nhất (26.1 triệu/m²), là công cụ định giá khách quan vượt trội."),
            ("Độ tin cậy được kiểm chứng:", "Mô hình ổn định trên 7.481 bản ghi kiểm thử, kiểm soát sai lệch giá hàng trăm triệu đồng."),
            ("Bảo vệ người mua nhà:", "Phát hiện ngay những tin rao khống giá hoặc lệch xa mặt bằng giao dịch thực tế của khu vực.")
        ]),
        ("TRỤ CỘT 2: ĐẦU TƯ & TỐI ƯU DANH MỤC", [
            ("Khai thác các cặp quận tương đương:", "Chuyển dịch dòng vốn sang quận lân cận có mặt bằng giá và tiềm năng tương đồng."),
            ("Nắm bắt cơ hội ven đô:", "Đón đầu các khu vực hưởng lợi từ quy hoạch đường vành đai và mạng lưới metro mở rộng."),
            ("Tối ưu giá trị thương mại:", "Ưu tiên lựa chọn bất động sản có mặt tiền từ 5m trở lên để tối đa hóa thanh khoản.")
        ]),
        ("TRỤ CỘT 3: QUẢN TRỊ TÍN DỤNG NGÂN HÀNG", [
            ("Xác lập ngưỡng cho vay an toàn:", "Sử dụng mức cận dưới của khoảng giá làm cơ sở phê duyệt hạn mức thế chấp an toàn."),
            ("Ngăn ngừa rủi ro nợ xấu:", "Nhận diện sớm các hiện tượng đầu cơ thổi giá cục bộ tại các khu vực đang sốt đất."),
            ("Tự động hóa luồng phê duyệt:", "Tích hợp công cụ định giá tự động vào quy trình thẩm định hồ sơ tín dụng.")
        ]),
        ("TRỤ CỘT 4: MINH BẠCH HÓA THỊ TRƯỜNG", [
            ("Dữ liệu được chuẩn hóa cao:", "Phễu sàng lọc 4 tầng loại bỏ triệt để tin rác, tin ảo và tin trùng lặp."),
            ("Tuân thủ chuẩn mực đạo đức AI:", "Minh bạch cách thức đưa ra mức giá, bảo vệ quyền riêng tư dữ liệu người dùng."),
            ("Sẵn sàng ứng dụng thực tế:", "Mô hình được đóng gói hoàn chỉnh, sẵn sàng tích hợp vào các hệ thống quản trị.")
        ])
    ]

    for idx, (a_title, a_items) in enumerate(action_pillars):
        row_i = idx // 2
        col_i = idx % 2
        a_left = Inches(0.8) + col_i * (m_w + m_gap_x)
        a_top = Inches(1.35) + row_i * (m_h + m_gap_y)

        tf_a = add_card(s22, a_left, a_top, m_w, m_h, a_title, header_bg=NAVY, f_size=Pt(13.5))
        for it_idx, (it_h, it_b) in enumerate(a_items):
            pt = tf_a.paragraphs[0] if it_idx == 0 else tf_a.add_paragraph()
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

    # ==========================================
    # SLIDE 23: LỘ TRÌNH CUỐI KỲ & Q&A (LAYOUT: SPLIT HERO)
    # ==========================================
    s23 = prs.slides.add_slide(blank_layout)
    add_header(s23, "Lộ Trình Hoàn Thiện Cuối Kỳ (Tuần 11 - 12) & Hỏi - Đáp")

    plan_w = Inches(6.20)
    qa_w = Inches(5.133)

    tf_l23 = add_card(s23, Inches(0.8), Inches(1.35), plan_w, Inches(5.65), "3 MỤC TIÊU HOÀN THIỆN ĐỒ ÁN (TUẦN 11 - 12)", header_bg=NAVY, f_size=Pt(14))
    plan_items = [
        ("1. Nâng cao năng lực mô hình học máy (Tuần 11):",
         "Thử nghiệm tối ưu hóa các thuật toán hiện đại (XGBoost, LightGBM) kết hợp kiểm định chéo K-Fold; Xây dựng mô hình phân loại tự động bất động sản vào 5 phân khúc giá."),
        ("2. Minh bạch hóa dự báo với công cụ giải thích SHAP (Tuần 12):",
         "Tích hợp công cụ giải thích mô hình (SHAP) để bóc tách rõ ràng lý do tại sao một căn nhà cụ thể được định giá tăng hay giảm dựa trên từng đặc tính riêng biệt."),
        ("3. Chuẩn hóa hồ sơ dữ liệu & Kiểm toán công bằng (Tuần 12):",
         "Xây dựng tài liệu hồ sơ dữ liệu và thẻ mô hình (Datasheet & Model Card) theo chuẩn mực quốc tế; Đảm bảo mô hình không bị định kiến sai lệch giữa các khu vực địa lý.")
    ]
    for it_idx, (it_h, it_b) in enumerate(plan_items):
        pt = tf_l23.paragraphs[0] if it_idx == 0 else tf_l23.add_paragraph()
        pt.text = it_h
        pt.font.name = "Arial"
        pt.font.size = Pt(14)
        pt.font.bold = True
        pt.font.color.rgb = GOLD
        if it_idx > 0:
            pt.space_before = Pt(18)
        pd = tf_l23.add_paragraph()
        pd.text = it_b
        pd.font.name = "Arial"
        pd.font.size = Pt(13)
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
    p_qa1.font.size = Pt(14.5)
    p_qa1.font.color.rgb = WHITE
    p_qa1.space_before = Pt(16)
    p_qa1.alignment = PP_ALIGN.CENTER

    prs.save(OUTPUT_PPTX)
    print(f"🎉 Đã xuất thành công tệp PowerPoint tại: {OUTPUT_PPTX}")


if __name__ == '__main__':
    create_deck()
