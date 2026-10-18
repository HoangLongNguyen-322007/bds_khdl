"""
Xuất toàn bộ Báo cáo tiến độ Khoa học Dữ liệu (Tuần 1 - 10) sang định dạng Microsoft Word (.docx).
Thiết kế chuẩn học thuật: Trang bìa chuyên nghiệp, bảng biểu định dạng cao cấp (Borders, Zebra striping,
Header màu Navy #1F4E79), nhúng trực tiếp 9 biểu đồ độ phân giải cao và phân tích tường minh 4 phần:
1. Biểu đồ gì & Phân loại kỹ thuật
2. Có tác dụng gì trong quy trình KHDL
3. Đang biểu diễn thứ gì (Trục X, Trục Y, Màu sắc, Phân vị)
4. Mang lại ý nghĩa gì (Thống kê & Giá trị thực tiễn kinh tế BĐS)
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=160, right=160):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def style_table(table, col_widths=None):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="6" w:space="0" w:color="1F4E79"/>'
        f'  <w:bottom w:val="single" w:sz="8" w:space="0" w:color="1F4E79"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="D3D3D3"/>'
        f'  <w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

    # Header row formatting
    for idx, cell in enumerate(table.rows[0].cells):
        set_cell_background(cell, "1F4E79")
        set_cell_margins(cell, top=140, bottom=140, left=160, right=160)
        cell.vertical_anchor = WD_ALIGN_VERTICAL.CENTER
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
                r.font.size = Pt(10)

    # Data rows zebra striping
    for r_idx, row in enumerate(table.rows[1:], start=1):
        bg_color = "F9FAFB" if r_idx % 2 == 1 else "FFFFFF"
        for cell in row.cells:
            set_cell_background(cell, bg_color)
            set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
            cell.vertical_anchor = WD_ALIGN_VERTICAL.CENTER
            for p in cell.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(9.5)

    if col_widths:
        for row in table.rows:
            for idx, width in enumerate(col_widths):
                if idx < len(row.cells):
                    row.cells[idx].width = Inches(width)

def add_figure_4points(doc, img_path, caption, what_is, purpose, represents, meaning):
    if os.path.exists(img_path):
        doc.add_picture(img_path, width=Inches(5.7))
        p_cap = doc.add_paragraph(caption)
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].font.italic = True
        p_cap.runs[0].font.size = Pt(9.5)
        p_cap.paragraph_format.space_after = Pt(8)

    p_head = doc.add_paragraph()
    r_head = p_head.add_run("📌 Phân Tích Chuyên Sâu 4 Trọng Tâm:")
    r_head.font.bold = True
    r_head.font.color.rgb = RGBColor(31, 78, 121)

    points = [
        ("1. Biểu đồ gì & Phân loại kỹ thuật: ", what_is),
        ("2. Có tác dụng gì trong quy trình KHDL: ", purpose),
        ("3. Đang biểu diễn thứ gì (Trục X, Y, Màu sắc, Phân vị): ", represents),
        ("4. Mang lại ý nghĩa gì (Thống kê & Giá trị thực tiễn kinh tế BĐS): ", meaning)
    ]
    for title, desc in points:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.2)
        p.paragraph_format.space_after = Pt(4)
        r_title = p.add_run(title)
        r_title.font.bold = True
        r_title.font.color.rgb = RGBColor(180, 100, 20)
        r_desc = p.add_run(desc)
        r_desc.font.size = Pt(10.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

def build_docx_report():
    print("🚀 Bắt đầu tạo tệp Word báo cáo tiến độ toàn diện (BAO_CAO_TIEN_DO_KHDL.docx)...")
    doc = docx.Document()

    # Page setup - Margins 1 inch
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Styles setup
    style_normal = doc.styles['Normal']
    font_normal = style_normal.font
    font_normal.name = 'Times New Roman'
    font_normal.size = Pt(11)
    font_normal.color.rgb = RGBColor(30, 30, 30)

    figures_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'reports', 'figures')

    # ==========================================
    # TRANG BÌA (COVER PAGE)
    # ==========================================
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_inst = p_inst.add_run("ĐẠI HỌC QUỐC GIA HÀ NỘI — TRƯỜNG ĐẠI HỌC CÔNG NGHỆ\nVIỆN CÔNG NGHỆ THÔNG TIN & TRUYỀN THÔNG\n")
    r_inst.font.bold = True
    r_inst.font.size = Pt(12)
    r_inst.font.color.rgb = RGBColor(70, 70, 70)

    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(40)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_title.add_run("BÁO CÁO TIẾN ĐỘ ĐỒ ÁN KHOA HỌC DỮ LIỆU (INFO3020)\n")
    r_sub.font.bold = True
    r_sub.font.size = Pt(14)
    r_sub.font.color.rgb = RGBColor(31, 78, 121)

    r_main = p_title.add_run("PHÂN TÍCH KHÔNG GIAN VÀ DỰ ĐOÁN GIÁ BẤT ĐỘNG SẢN TẠI HÀ NỘI\n")
    r_main.font.bold = True
    r_main.font.size = Pt(20)
    r_main.font.color.rgb = RGBColor(16, 44, 87)

    r_desc = p_title.add_run("(Báo cáo triển khai thực tế từ Tuần 1 đến Tuần 10: Thu thập, Tiền xử lý, Kỹ nghệ đặc trưng, EDA, Thống kê suy luận & Chẩn đoán mô hình hồi quy)\n")
    r_desc.font.italic = True
    r_desc.font.size = Pt(11)
    r_desc.font.color.rgb = RGBColor(100, 100, 100)

    p_spacer2 = doc.add_paragraph()
    p_spacer2.paragraph_format.space_before = Pt(80)

    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_meta = p_meta.add_run(
        "Sinh viên thực hiện: Hoàng Long Nguyễn\n"
        "Mã nguồn dự án: HoangLongNguyen-322007/bds_khdl\n"
        "Học phần: Khoa học Dữ liệu (Data Science - INFO3020)\n"
        "Quy mô dữ liệu: 99.998 tin rao thực tế → 37.402 bản ghi chuẩn hóa sạch\n"
        "Thời gian thực hiện: Năm học 2025 - 2026\n"
        "Hà Nội, Tháng 10 Năm 2026"
    )
    r_meta.font.size = Pt(11.5)
    r_meta.font.color.rgb = RGBColor(50, 50, 50)

    doc.add_page_break()

    # ==========================================
    # PHẦN 1: TỔNG QUAN ĐỀ TÀI & 3 BÀI TOÁN KINH DOANH
    # ==========================================
    h1 = doc.add_heading("CHƯƠNG 1: TỔNG QUAN ĐỀ TÀI & BỐI CẢNH KINH DOANH (TUẦN 1 - 2)", level=1)
    h1.runs[0].font.color.rgb = RGBColor(31, 78, 121)

    doc.add_paragraph(
        "Thị trường bất động sản (BĐS) tại Thủ đô Hà Nội là một trong những môi trường kinh tế năng động và phức tạp bậc nhất cả nước. "
        "Tuy nhiên, giao dịch BĐS nhà ở riêng lẻ tại Hà Nội đang đối mặt với sự phân mảnh thông tin nghiêm trọng, hiện tượng đồn thổi giá đất "
        "và thiếu vắng các công cụ định lượng khoa học để hỗ trợ người dân cũng như các tổ chức tài chính."
    )

    doc.add_paragraph("Đồ án Khoa học Dữ liệu tập trung giải quyết 3 bài toán nghiệp vụ trọng tâm sau:")

    p1 = doc.add_paragraph()
    p1.paragraph_format.left_indent = Inches(0.2)
    r = p1.add_run("1. Minh bạch hóa thông tin thị trường (Transparency): ")
    r.font.bold = True
    p1.add_run("Xây dựng bức tranh phân bố giá khách quan theo không gian địa lý, loại bỏ định kiến cảm tính giữa người mua và môi giới.")

    p2 = doc.add_paragraph()
    p2.paragraph_format.left_indent = Inches(0.2)
    r = p2.add_run("2. Tự động hóa thẩm định giá sơ bộ (Automated Valuation Model - AVM): ")
    r.font.bold = True
    p2.add_run("Giúp ngân hàng và nhà đầu tư cá nhân ước tính giá trị tài sản chỉ trong vài giây, giảm thời gian thẩm định từ 3 ngày xuống dưới 1 giây.")

    p3 = doc.add_paragraph()
    p3.paragraph_format.left_indent = Inches(0.2)
    r = p3.add_run("3. Định lượng hóa giá trị kinh tế của từng đặc tính công trình: ")
    r.font.bold = True
    p3.add_run("Xác định chính xác bằng mô hình kinh tế lượng: Nhà mặt tiền tăng 1 mét thì giá trị tăng bao nhiêu? Nhà trong ngõ hẻm bị chiết khấu bao nhiêu phần trăm?")

    doc.add_page_break()

    # ==========================================
    # PHẦN 2: THU THẬP & SÀNG LỌC PHỄU DỮ LIỆU
    # ==========================================
    h2 = doc.add_heading("CHƯƠNG 2: THU THẬP & PHỄU SÀNG LỌC DỮ LIỆU (TUẦN 3 - 4)", level=1)
    h2.runs[0].font.color.rgb = RGBColor(31, 78, 121)

    doc.add_paragraph(
        "Dữ liệu được thu thập từ các nền tảng niêm yết BĐS lớn tại Việt Nam với tổng số 99.998 tin rao ban đầu. "
        "Để xây dựng một mô hình máy học đáng tin cậy, quy trình làm sạch dữ liệu được thiết kế theo cấu trúc PHỄU SÀNG LỌC 4 TẦNG nghiêm ngặt."
    )

    p = doc.add_paragraph()
    r = p.add_run("Bảng 1: Phễu sàng lọc dữ liệu chi tiết qua 4 giai đoạn kỹ thuật")
    r.font.bold = True

    t_funnel = doc.add_table(rows=5, cols=5)
    t_funnel.rows[0].cells[0].paragraphs[0].text = "Giai Đoạn Sàng Lọc"
    t_funnel.rows[0].cells[1].paragraphs[0].text = "Số Lượng Còn Lại"
    t_funnel.rows[0].cells[2].paragraphs[0].text = "Số Dòng Loại Bỏ"
    t_funnel.rows[0].cells[3].paragraphs[0].text = "Tỷ Lệ Giảm"
    t_funnel.rows[0].cells[4].paragraphs[0].text = "Nguyên Nhân Kỹ Thuật & Nghiệp Vụ"

    funnel_data = [
        ("1. Dữ liệu thô ban đầu", "99.998 dòng", "0 dòng", "0.0%", "Toàn bộ tin crawl từ các trang mạng, chứa tin lịch sử từ nhiều năm trước."),
        ("2. Lọc chu kỳ 18 tháng (2025-2026)", "38.505 dòng", "Loại 61.493 dòng", "Giảm 61.5%", "Loại bỏ tin cũ trước chu kỳ sốt đất 2024; giữ dữ liệu 18 tháng để phản ánh mặt bằng giá thực tế hiện hành."),
        ("3. Lọc Target rác & Missing", "37.630 dòng", "Loại 875 dòng", "Giảm 2.3%", "Loại bỏ các tin ghi 'Giá thỏa thuận', tin khuyết diện tích hoặc parser bị lỗi ra chuỗi vô cực 'inf'."),
        ("4. Lọc Outlier tri thức", "37.402 dòng", "Loại 228 dòng", "Giảm 0.6%", "Loại đơn giá ảo < 10 tr hoặc > 500 tr/m² (tin lừa đảo cọc hoặc gõ nhầm hàng chục số 0).")
    ]
    for idx, (b1, b2, b3, b4, b5) in enumerate(funnel_data, start=1):
        t_funnel.rows[idx].cells[0].paragraphs[0].text = b1
        t_funnel.rows[idx].cells[0].paragraphs[0].runs[0].font.bold = True
        t_funnel.rows[idx].cells[1].paragraphs[0].text = b2
        t_funnel.rows[idx].cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        t_funnel.rows[idx].cells[2].paragraphs[0].text = b3
        t_funnel.rows[idx].cells[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        t_funnel.rows[idx].cells[3].paragraphs[0].text = b4
        t_funnel.rows[idx].cells[3].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        t_funnel.rows[idx].cells[4].paragraphs[0].text = b5

    style_table(t_funnel, col_widths=[1.5, 1.0, 1.1, 0.9, 2.0])
    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # Bảng Missing Values
    p = doc.add_paragraph()
    r = p.add_run("Bảng 2: Kiểm kê chi tiết các lỗi Khuyết thiếu (Missing Values)")
    r.font.bold = True

    t_miss = doc.add_table(rows=6, cols=5)
    t_miss.rows[0].cells[0].paragraphs[0].text = "Thuộc Tính Khuyết"
    t_miss.rows[0].cells[1].paragraphs[0].text = "Số Lượng Lỗi"
    t_miss.rows[0].cells[2].paragraphs[0].text = "Tỷ Lệ Mẫu"
    t_miss.rows[0].cells[3].paragraphs[0].text = "Nguyên Nhân Gốc Rễ Phát Sinh Lỗi"
    t_miss.rows[0].cells[4].paragraphs[0].text = "Phương Pháp & Nguyên Lý Xử Lý"

    miss_data = [
        ("Biến mục tiêu (Giá/m2, Diện tích)", "875 dòng", "2.27%", "Người đăng cố tình ghi 'Giá thỏa thuận' để câu inbox, hoặc lỗi parser ra chuỗi vô cực 'inf'.", "Xóa bỏ hoàn toàn (MCAR Deletion); tuyệt đối không điền giá trị giả vào biến phụ thuộc."),
        ("Số tầng (Đất nền trống)", "2.140 dòng", "5.56%", "Bản chất vật lý: BĐS là đất nền trống chưa có công trình xây dựng, người bán để trống số tầng.", "Chuẩn hóa giá trị thực: Quét từ khóa đất -> Gán Số tầng = 0.0 phản ánh đúng hiện trạng."),
        ("Số tầng (Nhà ở thông thường)", "14.210 dòng", "36.91%", "Nhà ở có tầng nhưng người đăng lười nhập do biểu mẫu trang tin không bắt buộc điền.", "Tạo cờ chỉ báo: Điền median tập train kèm tạo cờ Thieu_So_Tang = 1 để mô hình học cơ chế thiếu."),
        ("Kích thước (Dài, Rộng mặt tiền)", "21.178 dòng", "55.00%", "Người bán chỉ nhớ tổng diện tích sổ đỏ, lười đo đạc kích thước chi tiết từng cạnh.", "Giữ nguyên dữ liệu tránh mất 55% mẫu; đưa vào Pipeline điền SimpleImputer(Median)."),
        ("Giấy tờ pháp lý", "13.476 dòng", "35.00%", "Tâm lý e ngại công khai pháp lý chưa hoàn chỉnh (nhà chờ cấp sổ, đất xen kẹt, đang cắm ngân hàng).", "Gán nhãn mặc định 'Chưa xác định' và mã hóa nhị phân co_so_do = 1 (nếu có sổ) / 0.")
    ]
    for idx, (m1, m2, m3, m4, m5) in enumerate(miss_data, start=1):
        t_miss.rows[idx].cells[0].paragraphs[0].text = m1
        t_miss.rows[idx].cells[0].paragraphs[0].runs[0].font.bold = True
        t_miss.rows[idx].cells[1].paragraphs[0].text = m2
        t_miss.rows[idx].cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        t_miss.rows[idx].cells[2].paragraphs[0].text = m3
        t_miss.rows[idx].cells[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        t_miss.rows[idx].cells[3].paragraphs[0].text = m4
        t_miss.rows[idx].cells[3].paragraphs[0].text = m5

    style_table(t_miss, col_widths=[1.5, 0.9, 0.8, 1.8, 1.5])
    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # Bảng Outlier & Nhiễu
    p = doc.add_paragraph()
    r = p.add_run("Bảng 3: Kiểm kê chi tiết các lỗi Ngoại lệ (Outliers) & Nhiễu nhập liệu")
    r.font.bold = True

    t_out = doc.add_table(rows=6, cols=4)
    t_out.rows[0].cells[0].paragraphs[0].text = "Dạng Lỗi / Nhiễu"
    t_out.rows[0].cells[1].paragraphs[0].text = "Số Dòng Tác Động"
    t_out.rows[0].cells[2].paragraphs[0].text = "Nguyên Nhân Gốc Rễ Phát Sinh"
    t_out.rows[0].cells[3].paragraphs[0].text = "Giải Pháp Khắc Phục Chuẩn Xác"

    out_data = [
        ("Outlier Đơn giá cực đoan (<10 tr hoặc >500 tr/m²)", "228 dòng", "Giá quá thấp (<10 tr) do tin lừa đảo cọc (rao 1-2 tr) hoặc đất rừng xa xôi; Giá quá cao (>500 tr) do người dùng gõ nhầm hàng chục số 0 (50 tỷ thành 5.000 tỷ).", "Bộ lọc miền tri thức: Thiết lập khung giá [10, 500] tr/m² và diện tích [10, 500] m² (loại bỏ bẫy cắt cụt 174M cũ từng làm nhô cột 175M)."),
        ("Lỗi Mặt tiền đơn vị milimet (1.000 <= val <= 35.000)", "1.420 dòng", "Người dùng quen nhập theo bản vẽ kỹ thuật bằng đơn vị mm thay vì mét (gõ 4500 mm thay vì 4.5 m).", "Quy đổi tự động: Nhận diện khoảng giá trị và tự động chia 1.000 đưa về mét chuẩn."),
        ("Outlier Mặt tiền dị biệt (Gõ nhầm 400.000 m)", "12 dòng", "Lỗi kẹt phím gõ nhầm mặt tiền lên tới 400.000m (kéo dãn trục hoành đồ thị scatter plot lên 400km).", "Chặn trần vật lý: Giới hạn kích thước mặt tiền tối đa là 30.0 mét."),
        ("Xung đột bảng mã Unicode (NFC vs NFD)", "38.505 dòng (100% text)", "Người đăng tin sử dụng các bộ gõ Unikey khác nhau sinh chuỗi tổ hợp (NFD) hoặc dựng sẵn (NFC).", "Chuẩn hóa Unicode NFC: Toàn bộ văn bản được chuẩn hóa về Unicode NFC dựng sẵn để join/group chuẩn xác."),
        ("Lỗi Trùng lặp (Duplicates)", "0 dòng", "Kiểm toán toàn bộ 12 trường thông tin không phát hiện bản ghi nào trùng khớp 100%.", "Bảo toàn nguyên vẹn tính duy nhất của từng tin đăng.")
    ]
    for idx, (o1, o2, o3, o4) in enumerate(out_data, start=1):
        t_out.rows[idx].cells[0].paragraphs[0].text = o1
        t_out.rows[idx].cells[0].paragraphs[0].runs[0].font.bold = True
        t_out.rows[idx].cells[1].paragraphs[0].text = o2
        t_out.rows[idx].cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        t_out.rows[idx].cells[2].paragraphs[0].text = o3
        t_out.rows[idx].cells[3].paragraphs[0].text = o4

    style_table(t_out, col_widths=[1.8, 1.0, 1.8, 1.9])
    doc.add_page_break()

    # ==========================================
    # PHẦN 3: KỸ NGHỆ ĐẶC TRƯNG & THIẾT KẾ PIPELINE
    # ==========================================
    h3 = doc.add_heading("CHƯƠNG 3: KỸ NGHỆ ĐẶC TRƯNG & THIẾT KẾ SCIKIT-LEARN PIPELINE (TUẦN 5)", level=1)
    h3.runs[0].font.color.rgb = RGBColor(31, 78, 121)

    doc.add_paragraph(
        "Từ 12 trường thuộc tính thô ban đầu, dự án tiến hành phân tích sâu và kỹ nghệ thành 38 biến phái sinh bao quát toàn diện các khía cạnh định giá."
    )

    p = doc.add_paragraph()
    r = p.add_run("Bảng 4: 6 Nhóm biến phái sinh tiêu biểu được kỹ nghệ chuyên sâu")
    r.font.bold = True

    t_feat = doc.add_table(rows=7, cols=3)
    t_feat.rows[0].cells[0].paragraphs[0].text = "Nhóm Đặc Trưng"
    t_feat.rows[0].cells[1].paragraphs[0].text = "Biến Số Phái Sinh Tiêu Biểu"
    t_feat.rows[0].cells[2].paragraphs[0].text = "Ý Nghĩa Nghiệp Vụ Kinh Doanh"

    feat_data = [
        ("1. Quy mô tài sản", "Tong_Gia_ty (Tỷ VNĐ)", "Đơn giá * Diện tích / 1000 -> Đánh giá phân khúc tổng giá trị tài sản."),
        ("2. Hình thái đất", "ty_le_dai_rong & hinh_dang_dat", "Tỷ lệ Sâu / Mặt tiền: Mặt tiền lớn (<1.0), Vuông vắn (1.0-2.5), Nhà ống hẹp (>2.5)."),
        ("3. Công năng sàn", "tong_dien_tich_san_m2", "Diện tích đất * Số tầng -> Phản ánh không gian ở thực tế của gia đình."),
        ("4. Tiện nghi phòng", "dien_tich_moi_phong_ngu_m2", "Diện tích đất / Số phòng ngủ -> Đo lường mức độ thông thoáng, tiện nghi."),
        ("5. Vị trí lõi", "khu_vuc_noi_do (0/1)", "Cờ nhị phân 7 quận trung tâm (Ba Đình, Hoàn Kiếm, Đống Đa, Cầu Giấy, Hai Bà Trưng, Tây Hồ, Thanh Xuân)."),
        ("6. Loại hình nhà", "loai_nha_ngo_hem & loai_nha_mat_pho", "Bóc tách cờ nhị phân nhận diện nhà trong ngõ hẹp vs nhà mặt phố kinh doanh.")
    ]
    for idx, (f1, f2, f3) in enumerate(feat_data, start=1):
        t_feat.rows[idx].cells[0].paragraphs[0].text = f1
        t_feat.rows[idx].cells[0].paragraphs[0].runs[0].font.bold = True
        t_feat.rows[idx].cells[1].paragraphs[0].text = f2
        t_feat.rows[idx].cells[2].paragraphs[0].text = f3

    style_table(t_feat, col_widths=[1.5, 2.0, 3.0])
    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    doc.add_paragraph(
        "Thiết kế Scikit-Learn Pipeline chống Rò rỉ Dữ liệu (Data Leakage):\n"
        "Toàn bộ quy trình tiền xử lý được tích hợp trong ColumnTransformer của Scikit-Learn:\n"
        "• Nhánh Biến Định Lượng: SimpleImputer(strategy='median') kết hợp RobustScaler (dựa trên IQR để triệt tiêu ảnh hưởng của các căn biệt thự triệu đô).\n"
        "• Nhánh Biến Định Danh: SimpleImputer(strategy='most_frequent') kết hợp OneHotEncoder(drop='first', handle_unknown='ignore') triệt tiêu bẫy biến giả.\n"
        "• Quy tắc Chống Rò rỉ Tuyệt đối: Dữ liệu được chia Train/Test 80/20 ngay từ bước đầu. Mọi tham số (Median, Q25, Q75, Tần suất) CHỈ ĐƯỢC HỌC (fit) trên tập Train (80%), sau đó mới áp dụng (transform) sang tập Test (20%)."
    )

    doc.add_page_break()

    # ==========================================
    # PHẦN 4: THỐNG KÊ MÔ TẢ 4 HỌ (TUẦN 6)
    # ==========================================
    h4 = doc.add_heading("CHƯƠNG 4: THỐNG KÊ MÔ TẢ 4 HỌ & BẢN CHẤT LỆCH PHẢI LOG-NORMAL (TUẦN 6)", level=1)
    h4.runs[0].font.color.rgb = RGBColor(31, 78, 121)

    p = doc.add_paragraph()
    r = p.add_run("Bảng 5: Bộ 4 họ đại lượng thống kê mô tả (Tập sạch n = 37.402)")
    r.font.bold = True

    t_stat = doc.add_table(rows=12, cols=3)
    t_stat.rows[0].cells[0].paragraphs[0].text = "Họ Thống Kê / Chỉ Số Đo Lường"
    t_stat.rows[0].cells[1].paragraphs[0].text = "Đơn Giá (Triệu VNĐ/m²)"
    t_stat.rows[0].cells[2].paragraphs[0].text = "Tổng Giá Trị Tài Sản (Tỷ VNĐ)"

    stat_data = [
        ("1. LOCATION (Độ tập trung)", "", ""),
        ("   - Giá trị nhỏ nhất (Min)", "10.00 triệu/m²", "0.25 Tỷ VNĐ"),
        ("   - Phân vị Q1 (25%)", "72.67 triệu/m²", "2.75 Tỷ VNĐ"),
        ("   - TRUNG VỊ (Median - Chuẩn)", "90.00 triệu/m²", "3.60 Tỷ VNĐ"),
        ("   - TRUNG BÌNH (Mean)", "102.18 triệu/m²", "5.10 Tỷ VNĐ"),
        ("   - Phân vị Q3 (75%)", "112.50 triệu/m²", "5.30 Tỷ VNĐ"),
        ("   - Giá trị lớn nhất (Max)", "500.00 triệu/m²", "237.00 Tỷ VNĐ"),
        ("2. SPREAD (Độ tán sắc)", "", ""),
        ("   - Khoảng liên phân vị (IQR)", "39.83 triệu/m²", "2.55 Tỷ VNĐ"),
        ("   - Độ lệch chuẩn (Std)", "54.78 triệu/m²", "5.76 Tỷ VNĐ"),
        ("3. SHAPE (Hình dạng phân phối)", "+2.75 (Lệch phải mạnh)", "+8.80 (Lệch phải cực lớn)")
    ]
    for idx, (s1, s2, s3) in enumerate(stat_data, start=1):
        t_stat.rows[idx].cells[0].paragraphs[0].text = s1
        if "LOCATION" in s1 or "SPREAD" in s1 or "SHAPE" in s1:
            t_stat.rows[idx].cells[0].paragraphs[0].runs[0].font.bold = True
        t_stat.rows[idx].cells[1].paragraphs[0].text = s2
        t_stat.rows[idx].cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
        t_stat.rows[idx].cells[2].paragraphs[0].text = s3
        t_stat.rows[idx].cells[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT

    style_table(t_stat, col_widths=[2.5, 2.0, 2.0])
    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    doc.add_paragraph(
        "Hiện tượng Mean (102.18 tr) cao hơn Median (90.00 tr) tới 13.5%: Do sự xuất hiện của các bất động sản mặt phố cổ và biệt thự hạng sang (150 - 450 tr/m²), giá trị trung bình bị kéo cao. Trong thẩm định giá BĐS, Trung vị (90.00 triệu/m²) là chỉ số đại diện chuẩn xác và tin cậy nhất cho mức chi trả thực tế của 50% người dân Thủ đô."
    )

    doc.add_page_break()

    # ==========================================
    # PHẦN 5: TRỰC QUAN HÓA CHUYÊN SÂU 4 BIỂU ĐỒ (TUẦN 7)
    # ==========================================
    h5 = doc.add_heading("CHƯƠNG 5: PHÂN TÍCH CHI TIẾT 4 BIỂU ĐỒ TRỰC QUAN HÓA EDA (TUẦN 7)", level=1)
    h5.runs[0].font.color.rgb = RGBColor(31, 78, 121)

    # HÌNH 1: CORRELATION HEATMAP
    add_figure_4points(
        doc,
        os.path.join(figures_dir, '01_correlation_heatmap.png'),
        "Hình 1: Ma trận tương quan đa biến Pearson giữa các thuộc tính định lượng",
        "Ma trận tương quan đa biến (Correlation Heatmap Matrix) hiển thị hệ số tương quan tuyến tính Pearson (r thuộc [-1.0, +1.0]) giữa tất cả các cặp biến số định lượng và biến nhị phân.",
        "Quét đồng thời toàn bộ mối quan hệ giữa biến mục tiêu (Đơn giá tr/m², Tổng giá tỷ) với các biến độc lập; nhận diện sớm nguy cơ đa cộng tuyến (Multicollinearity) giữa các biến kích thước thửa đất; định hướng kỹ nghệ đặc trưng.",
        "Hai trục X và Y liệt kê 10 đặc trưng cốt lõi (Đơn giá, Tổng giá, Diện tích, Mặt tiền, Chiều sâu, Số tầng, Số phòng ngủ, Cờ nội đô, Cờ ngõ hẻm, Cờ mặt phố). Thang màu chuyển từ xanh lam đậm (r = -1.0) qua trắng (r = 0) đến đỏ cam đậm (r = +1.0). Mỗi ô vuông hiển thị con số chính xác hệ số Pearson r.",
        "• Vị trí và loại hình là nhân tố tối cao: Cờ nội đô tương quan dương mạnh nhất với đơn giá (r = +0.283), cờ ngõ hẻm tương quan âm mạnh nhất (r = -0.279). Nhà ngõ hẻm luôn chịu mức chiết khấu giá rất sâu.\n"
        "• Đặc trưng công năng vật lý gia tăng giá trị: Số phòng ngủ (r = +0.242) và Số tầng (r = +0.225) đồng biến mạnh với đơn giá đất vì chi phí xây dựng hoàn thiện được cộng gộp vào giá chào bán.\n"
        "• Thặng dư thương mại mặt tiền: Sau khi sửa triệt để lỗi milimet, mặt tiền có tương quan dương (r = +0.161) – mặt tiền càng rộng thì đơn giá đất càng cao nhờ khả năng kinh doanh buôn bán.\n"
        "• Cảnh báo đa cộng tuyến: Diện tích đất và Tổng diện tích sàn tương quan với nhau rất cao (r = 0.88), cảnh báo mô hình tuyến tính sẽ bị bất ổn định nếu không dùng Regularization."
    )

    # HÌNH 2: PRICE DISTRIBUTION
    add_figure_4points(
        doc,
        os.path.join(figures_dir, '02_price_distribution.png'),
        "Hình 2: Phân phối tần suất Đơn giá (triệu VNĐ/m²) và Tổng giá trị (Tỷ VNĐ)",
        "Biểu đồ phân phối tần suất kép (Dual Distribution Plot) gồm Histogram dạng cột ghép đôi kết hợp đường cong ước lượng mật độ hạt nhân trơn (Kernel Density Estimation - KDE).",
        "Kiểm tra trực quan hình thái phân phối thực tế của biến mục tiêu; đo lường mức độ bất đối xứng (Skewness) và độ nhọn (Kurtosis); xác định xem dữ liệu có tuân theo phân phối chuẩn Gaussian hay không; nhận diện phân khúc thanh khoản sôi động nhất.",
        "Đồ thị bên trái biểu diễn Đơn giá (triệu VNĐ/m², từ 10 đến 500 tr/m²); đồ thị bên phải biểu diễn Tổng giá bán (Tỷ VNĐ, từ 0.25 đến 50 Tỷ VNĐ). Trục tung Y là Mật độ xác suất (Density). Cột histogram xanh lam biểu diễn tần suất phân tổ; đường cam KDE biểu diễn hàm mật độ liên tục; đỉnh sóng KDE là điểm mốt tập trung giao dịch đông nhất (Mode).",
        "• Bản chất phân phối Lệch phải tự nhiên (Right-Skewed / Log-Normal): Đuôi phải kéo dài sang các bất động sản giá siêu đắt (300 - 500 tr/m² và 20 - 50 tỷ VNĐ). Skewness đơn giá là +2.75 và Tổng giá là +8.80.\n"
        "• Tâm chấn thanh khoản thị trường: Đỉnh mật độ đơn giá tập trung ở 75 - 90 tr/m²; tổng giá tập trung ở 2.5 - 5.0 tỷ VNĐ. Hơn 75% toàn bộ thị trường nằm dưới ngưỡng 5.30 Tỷ VNĐ.\n"
        "• Quyết định kỹ thuật sống còn: Bắt buộc phải áp dụng phép biến đổi log(y) khi hồi quy tuyến tính để không vi phạm giả định phần dư chuẩn."
    )

    # HÌNH 3: SCATTER FACADE & AREA
    add_figure_4points(
        doc,
        os.path.join(figures_dir, '03_price_vs_area_scatter.png'),
        "Hình 3: Tương quan phân tán Diện tích vs Tổng giá & Mặt tiền vs Đơn giá",
        "Biểu đồ phân tán đám mây điểm 2 chiều (Bivariate Scatter Plot) kết hợp đường xu hướng hồi quy tuyến tính OLS màu đỏ.",
        "Khảo sát mối quan hệ giữa các biến hình học vật lý cốt lõi (Diện tích đất, Chiều rộng mặt tiền) với giá cả; phát hiện hiện tượng phương sai sai số thay đổi (Heteroscedasticity) trực quan qua hình thái đám mây điểm; kiểm chứng thặng dư thương mại của mặt tiền.",
        "Đồ thị bên trái biểu diễn Diện tích (m², từ 20 đến 300 m²) theo Tổng giá bán (Tỷ VNĐ, từ 1 đến 50 Tỷ). Đồ thị bên phải biểu diễn Mặt tiền (mét, từ 1.5m đến 16m sau chuẩn hóa) theo Đơn giá (triệu VNĐ/m², từ 10 đến 500 tr/m²). Điểm dữ liệu tập trung thành các dải sọc đứng ứng với quy chuẩn phân lô: 3m, 3.5m, 4m, 4.5m, 5m, 6m.",
        "• Hiện tượng phương sai hình phễu (Funnel Shape): Ở diện tích nhỏ (< 50m²), các điểm tập trung rất sát đường hồi quy (sai số thấp). Khi diện tích tăng (> 120m²), các điểm xòe rộng thành hình phễu từ 8 tỷ (ven đô) đến 35 tỷ (nhà phố trung tâm).\n"
        "• Thặng dư thương mại mặt tiền: Đường hồi quy mặt tiền dốc lên rõ rệt từ mức ~88 tr/m² (mặt tiền 2m) lên mức ~170 tr/m² (mặt tiền 16m).\n"
        "• Ngưỡng bùng nổ thương mại: Tại mốc Mặt tiền = 4.0m, đơn giá có bước nhảy vọt. Nhà có mặt tiền >= 4.0m cho phép mở cửa hàng, kinh doanh tầng 1 hoặc cho thuê văn phòng, tạo ra dòng tiền đều đặn."
    )

    # HÌNH 4: DISTRICT BOXPLOT
    add_figure_4points(
        doc,
        os.path.join(figures_dir, '04_price_by_district_boxplot.png'),
        "Hình 4: Phân bố đơn giá 12 quận/huyện trọng điểm sắp xếp theo Trung vị",
        "Biểu đồ hộp và râu đa nhóm (Multi-Group Box-and-Whisker Plot), được sắp xếp thứ tự giảm dần theo giá trị Trung vị (Median-Ordered Boxplot).",
        "So sánh trực quan đồng thời phân phối đơn giá của 12 quận/huyện trọng điểm tại Hà Nội mà không bị đánh lừa bởi giá trị ngoại lai; phân tích 5 số tóm tắt và độ phân tán IQR từng địa bàn; phân tầng địa kinh tế Thủ đô.",
        "Trục hoành X là 12 quận/huyện sắp xếp theo trung vị từ trái sang phải (Cầu Giấy, Ba Đình, Tây Hồ, Đống Đa, Thanh Xuân, Hai Bà Trưng, Nam Từ Liêm, Bắc Từ Liêm, Hoàng Mai, Long Biên, Hà Đông, Thanh Trì). Trục tung Y là Đơn giá (triệu VNĐ/m²). Thân hộp màu là 50% dữ liệu ở giữa (IQR = Q3 - Q1); vạch ngang bên trong hộp là Trung vị; râu kéo dài đến 1.5 * IQR; các chấm ngoài râu là ngoại lai (Outliers).",
        "• Phân định 3 tầng thứ bậc rõ nét:\n"
        "  + Tầng 1 - Lõi di sản & phát triển (Trung vị >= 100 tr/m²): Cầu Giấy (105 tr), Ba Đình (104 tr), Tây Hồ (101.9 tr), Đống Đa (100 tr). Hộp IQR rất cao và râu dài, thể hiện biên độ phân hóa lớn giữa nhà ngõ và mặt phố lớn.\n"
        "  + Tầng 2 - Đô thị phát triển năng động (Trung vị 85 - 93 tr/m²): Thanh Xuân (92.5 tr), Hai Bà Trưng (89.7 tr), Nam Từ Liêm (85.7 tr). Thân hộp ngắn, giá cả đồng đều.\n"
        "  + Tầng 3 - Vành đai & Ven đô (Trung vị 60 - 80 tr/m²): Bắc Từ Liêm (80 tr), Hoàng Mai (78.8 tr), Long Biên (77.5 tr), Hà Đông (74.4 tr), Thanh Trì (60.9 tr/m²). Mặt bằng giá mềm, phù hợp với gia đình trẻ.\n"
        "• Giá trị thực tiễn: Giúp người mua nhà định hình ngay ngân sách: Nếu chỉ có dưới 80 triệu/m², lựa chọn tối ưu là hướng sang Tầng 3 (Hà Đông, Hoàng Mai, Long Biên)."
    )

    doc.add_page_break()

    # ==========================================
    # PHẦN 6: THỬ NGHIỆM MÔ HÌNH HÓA (HỒI QUY & ENSEMBLES)
    # ==========================================
    h6 = doc.add_heading("CHƯƠNG 6: THỬ NGHIỆM MÔ HÌNH HÓA & ĐÁNH GIÁ THỰC NGHIỆM (TUẦN 10 - 11)", level=1)
    h6.runs[0].font.color.rgb = RGBColor(31, 78, 121)

    p = doc.add_paragraph()
    r = p.add_run("Bảng 6: So sánh hiệu năng 4 mô hình học máy trên tập kiểm thử (n = 7.481)")
    r.font.bold = True

    t_mod = doc.add_table(rows=5, cols=5)
    t_mod.rows[0].cells[0].paragraphs[0].text = "Thuật Toán Học Máy"
    t_mod.rows[0].cells[1].paragraphs[0].text = "MAE (tr/m²)"
    t_mod.rows[0].cells[2].paragraphs[0].text = "RMSE (tr/m²)"
    t_mod.rows[0].cells[3].paragraphs[0].text = "Hệ Số R²"
    t_mod.rows[0].cells[4].paragraphs[0].text = "Đánh Giá Kỹ Thuật"

    mod_data = [
        ("Linear Regression", "28.47", "44.13", "0.3644", "Baseline cơ sở, chưa bắt được tương tác phi tuyến giữa các đặc tính."),
        ("Ridge Regression (L2)", "28.47", "44.21", "0.3621", "Kiểm soát đa cộng tuyến, hiệu năng tương đương Linear Regression."),
        ("Random Forest (50 cây)", "26.17", "41.85", "0.4284", "Cải thiện vượt bậc; giảm mạnh sai số MAE tới 8.1%."),
        ("Gradient Boosting (GBDT)", "26.07", "41.46", "0.4390", "QUÁN QUÂN HIỆU NĂNG: MAE thấp nhất, R² cao nhất toàn diện.")
    ]
    for idx, (m1, m2, m3, m4, m5) in enumerate(mod_data, start=1):
        t_mod.rows[idx].cells[0].paragraphs[0].text = m1
        t_mod.rows[idx].cells[0].paragraphs[0].runs[0].font.bold = True
        t_mod.rows[idx].cells[1].paragraphs[0].text = m2
        t_mod.rows[idx].cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        t_mod.rows[idx].cells[2].paragraphs[0].text = m3
        t_mod.rows[idx].cells[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        t_mod.rows[idx].cells[3].paragraphs[0].text = m4
        t_mod.rows[idx].cells[3].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        t_mod.rows[idx].cells[4].paragraphs[0].text = m5

    style_table(t_mod, col_widths=[1.6, 1.0, 1.1, 0.9, 2.0])
    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # HÌNH 5: MODEL COMPARISON
    add_figure_4points(
        doc,
        os.path.join(figures_dir, '05_model_comparison.png'),
        "Hình 5: So sánh hiệu năng đối đầu MAE, RMSE, R² giữa 4 mô hình học máy",
        "Biểu đồ cột nhóm ghép đôi (Dual-Metric Grouped Bar Chart) so sánh song song sai số tuyệt đối trung bình (MAE) và hệ số xác định (R² Score) trên tập kiểm thử độc lập (Test Set: 7.481 bản ghi).",
        "Đánh giá khách quan năng lực học tập và khái quát hóa giữa 4 trường phái thuật toán (OLS, Ridge L2, Random Forest, Gradient Boosting), tìm ra Champion Model có sai số dự báo nhỏ nhất.",
        "Trục hoành X là 4 thuật toán học máy. Cột đỏ cam biểu thị Sai số MAE (triệu/m² - Càng thấp càng tốt). Cột xanh lam biểu thị Hệ số R² (Càng cao càng tốt). Số liệu gắn trên đầu cột: Linear (MAE 28.47 tr, R² 0.364) -> Ridge (MAE 28.47 tr, R² 0.362) -> Random Forest (MAE 26.17 tr, R² 0.428) -> Gradient Boosting (MAE 26.07 tr, R² 0.439).",
        "• Chiến thắng áp đảo của mô hình Cây (Tree-based Ensemble): GBDT giảm sai số MAE tới 8.4% và tăng R² thêm +20.5% so với Linear Regression.\n"
        "• Bản chất phi tuyến của thị trường BĐS: Bất động sản có sự tương tác phi tuyến cực mạnh (mặt tiền 6m ở quận trung tâm có giá trị thương mại gấp nhiều lần mặt tiền 6m ở huyện ngoại thành). Mô hình cây tự động phân tách các vùng không gian đa chiều để khớp chính xác các mối quan hệ này.\n"
        "• Ứng dụng thực tiễn: Giúp ngân hàng thẩm định giảm thiểu rủi ro định giá sai lệch hàng trăm triệu đồng cho mỗi hợp đồng tín dụng."
    )

    # HÌNH 6: FEATURE IMPORTANCE
    add_figure_4points(
        doc,
        os.path.join(figures_dir, '06_feature_importance.png'),
        "Hình 6: Xếp hạng tầm quan trọng của các yếu tố định giá (Feature Importance)",
        "Biểu đồ thanh ngang xếp hạng tầm quan trọng đặc trưng (Horizontal Feature Importance Bar Chart) trích xuất từ mô hình quán quân Gradient Boosting dựa trên độ giảm độ vẩn đục Gini (Mức tăng thông tin).",
        "Mở chiếc 'hộp đen' (Black-box) của thuật toán học máy, minh bạch hóa các yếu tố cốt lõi nào đang dẫn dắt và định đoạt giá bán nhà tại Hà Nội.",
        "Trục tung Y là Top 10 đặc trưng có lực chi phối mạnh nhất xếp từ cao xuống thấp. Trục hoành X là Tỷ lệ phần trăm đóng góp tầm quan trọng (%) vào quyết định phân nhánh của các cây quyết định.",
        "• Bộ đôi Vị trí & Loại hình chi phối trên 36% toàn bộ giá trị: loai_nha_ngo_hem chiếm 20.01% (yếu tố tiếp giáp ngõ hẻm làm giảm giá trị nhiều nhất), tiếp theo là khu_vuc_noi_do chiếm 16.14% (thuộc 7 quận lõi quyết định mức sàn giá).\n"
        "• Minh chứng sức mạnh của Kỹ nghệ đặc trưng: Biến phái sinh tong_dien_tich_san_m2 (8.26%) và dien_tich_moi_phong_ngu_m2 (7.07%) xuất sắc lọt Top 5, vượt trội hoàn toàn so với biến diện tích đất thô.\n"
        "• Ứng dụng thực tiễn: Thẩm định viên chỉ cần tập trung kiểm chứng 5 yếu tố hàng đầu này là đã làm chủ trên 60% cơ sở định giá của một tài sản."
    )

    doc.add_paragraph(
        "Đóng gói Pipeline Suy Diễn & Khả Năng Tái Lập (Inference Pipeline & Reproducibility):\n"
        "Toàn bộ luồng tiền xử lý (One-Hot, Imputation) và mô hình học máy quán quân Gradient Boosting được đóng gói thành một Pipeline duy nhất (`pipeline.pkl`). Hàm `pipeline.predict()` cho phép đưa trực tiếp một bản ghi dữ liệu thô (ví dụ: nhà 50m², Quận Cầu Giấy, 3 tầng, 3 phòng ngủ, nhà ngõ, có sổ đỏ) vào quy trình và nhận về giá trị dự báo 90.3 triệu/m² (tương đương 4.51 Tỷ VNĐ) với thời gian trễ dưới 0.05 giây, đảm bảo tính tái lập (Reproducibility) và sẵn sàng tích hợp hệ thống sản xuất."
    )

    doc.add_page_break()

    # ==========================================
    # PHẦN 7: THỐNG KÊ SUY LUẬN (TUẦN 9)
    # ==========================================
    h7 = doc.add_heading("CHƯƠNG 7: THỐNG KÊ SUY LUẬN & KIỂM ĐỊNH GIẢ THUYẾT (TUẦN 9)", level=1)
    h7.runs[0].font.color.rgb = RGBColor(31, 78, 121)

    doc.add_paragraph(
        "Chuyển từ Thống kê mô tả (chỉ tóm tắt tập mẫu quan sát được) sang Thống kê suy luận (khẳng định bản chất của toàn bộ thị trường hàng triệu căn nhà Hà Nội với mức rủi ro xác định)."
    )

    p = doc.add_paragraph()
    r = p.add_run("1. Kiểm định Welch's Two-Sample t-test & Mann-Whitney U: Nội đô vs Ngoại thành")
    r.font.bold = True

    t_ttest = doc.add_table(rows=4, cols=4)
    t_ttest.rows[0].cells[0].paragraphs[0].text = "Phép Kiểm Định"
    t_ttest.rows[0].cells[1].paragraphs[0].text = "Đại Lượng Thống Kê"
    t_ttest.rows[0].cells[2].paragraphs[0].text = "Giá Trị p-value"
    t_ttest.rows[0].cells[3].paragraphs[0].text = "Kết Luận Thống Kê"

    ttest_data = [
        ("Welch's t-test (Tham số)", "t = 64.18", "< 10^-16 (0.0000)", "Bác bỏ H0 đanh thép: Đơn giá Nội đô (114.2 tr) cao hơn Ngoại thành (82.2 tr) 32.04 tr/m² (+39.0%)."),
        ("Mann-Whitney U (Phi tham số)", "U = 2.35 * 10^8", "< 10^-16 (0.0000)", "Khẳng định tuyệt đối: Không phụ thuộc vào giả định phân phối chuẩn."),
        ("Cohen's d (Effect Size)", "d = 0.610", "—", "Mức tác động từ Trung bình đến Lớn: Khoảng cách giá mang ý nghĩa kinh tế thực tế lớn.")
    ]
    for idx, (t1, t2, t3, t4) in enumerate(ttest_data, start=1):
        t_ttest.rows[idx].cells[0].paragraphs[0].text = t1
        t_ttest.rows[idx].cells[0].paragraphs[0].runs[0].font.bold = True
        t_ttest.rows[idx].cells[1].paragraphs[0].text = t2
        t_ttest.rows[idx].cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        t_ttest.rows[idx].cells[2].paragraphs[0].text = t3
        t_ttest.rows[idx].cells[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        t_ttest.rows[idx].cells[3].paragraphs[0].text = t4

    style_table(t_ttest, col_widths=[1.8, 1.2, 1.2, 2.4])
    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # ANOVA & Tukey HSD
    p = doc.add_paragraph()
    r = p.add_run("2. One-Way ANOVA & 9 Cặp quận 'Song sinh về giá' từ Tukey's HSD:")
    r.font.bold = True
    doc.add_paragraph(
        "Kiểm định ANOVA (F = 368.11, p < 0.0001) khẳng định giữa 12 quận có sự phân hóa sâu sắc. Phép kiểm định hậu nghiệm Tukey's HSD (so sánh 66 cặp đối đầu và kiểm soát sai số họ) phát hiện 9 cặp quận không có sự khác biệt có ý nghĩa thống kê (p > 0.05):\n"
        "• Tam giác vàng đỉnh cao: Ba Đình (128.6 tr) vs Cầu Giấy (125.3 tr) (p = 0.4769) và Ba Đình vs Tây Hồ (123.7 tr) (p = 0.1795) -> Có mặt bằng giá tương đương nhau!\n"
        "• Cặp đôi đô thị phát triển: Hai Bà Trưng (102.6 tr) vs Thanh Xuân (102.7 tr) chênh lệch chỉ 0.11 tr/m² (p = 1.0000) -> Giá gần như là một!\n"
        "• Nhóm vành đai ven đô: Hoàng Mai vs Bắc Từ Liêm (p = 1.0000), Hoàng Mai vs Hà Đông (p = 0.2171), Bắc Từ Liêm vs Long Biên (p = 0.9999)."
    )

    # HÌNH 7: CONFIDENCE INTERVALS
    add_figure_4points(
        doc,
        os.path.join(figures_dir, '07_confidence_intervals_districts.png'),
        "Hình 7: Khoảng tin cậy 95% (95% CI) cho đơn giá trung bình 12 quận/huyện Hà Nội",
        "Biểu đồ khoảng tin cậy dạng thanh sai số (95% Confidence Interval Forest / Error Bar Plot), tính toán từ sai số chuẩn (SE = s / sqrt(n)) dựa trên phân phối t-Student (CI 95% = x_bar +- t * SE).",
        "Chuyển từ thống kê mô tả trên mẫu (Sample) sang suy luận tổng thể (Population Inference): Tuyên bố với độ tin cậy 95% mức giá thật của từng quận ngoài thực tế nằm trong khoảng nào; kiểm tra hiện tượng chồng lấn dải tin cậy; đánh giá độ tin cậy theo quy mô mẫu (n).",
        "Trục hoành X là 12 quận/huyện sắp xếp theo đơn giá trung bình mẫu giảm dần từ trái sang phải. Trục tung Y là Đơn giá trung bình (triệu VNĐ/m²). Điểm tròn trung tâm là Giá trị trung bình mẫu. Thanh dọc có hai đầu mút (Error Bar) biểu diễn khoảng tin cậy 95% [Lower, Upper]. Dải nền bóng mờ biểu thị vùng chồng lấn giữa các quận lân cận.",
        "• Độ tin cậy khoa học vững chắc: Ta tự tin 95% rằng đơn giá trung bình thực sự của toàn bộ thị trường quận Ba Đình nằm trong khoảng [125.55 - 131.57] tr/m², Cầu Giấy trong khoảng [123.04 - 127.50] tr/m².\n"
        "• Minh chứng thị giác cho 9 cặp quận 'song sinh giá' (Tukey's HSD): Thanh CI của Ba Đình, Cầu Giấy và Tây Hồ gối đè lên nhau gần như hoàn toàn -> Giải thích tại sao kiểm định ANOVA/Tukey khẳng định 3 quận này không có sự khác biệt có ý nghĩa thống kê về mặt bằng giá.\n"
        "• Cỡ mẫu lớn mang lại độ chuẩn xác cao: Quận Hoàng Mai có tới 4.880 tin rao nên thanh CI cực hẹp (+-0.89 tr/m²), chứng minh kết quả ước lượng đạt độ tin cậy thực tế tuyệt đối."
    )

    p = doc.add_paragraph()
    r = p.add_run("Bảng 7: Khoảng tin cậy 95% (95% CI) chi tiết cho 12 Quận/Huyện")
    r.font.bold = True

    t_ci = doc.add_table(rows=13, cols=6)
    t_ci.rows[0].cells[0].paragraphs[0].text = "Quận / Huyện"
    t_ci.rows[0].cells[1].paragraphs[0].text = "Cỡ Mẫu (n)"
    t_ci.rows[0].cells[2].paragraphs[0].text = "Trung Bình"
    t_ci.rows[0].cells[3].paragraphs[0].text = "Trung Vị"
    t_ci.rows[0].cells[4].paragraphs[0].text = "CI 95% Giới Hạn"
    t_ci.rows[0].cells[5].paragraphs[0].text = "Biên Độ (±)"

    ci_data = [
        ("Quận Ba Đình", "2.223", "128.56", "104.00", "[125.55 - 131.57]", "± 3.01"),
        ("Quận Cầu Giấy", "2.990", "125.27", "105.00", "[123.04 - 127.50]", "± 2.23"),
        ("Quận Tây Hồ", "1.450", "123.73", "101.92", "[120.04 - 127.42]", "± 3.69"),
        ("Quận Đống Đa", "6.495", "117.96", "100.00", "[116.45 - 119.46]", "± 1.51"),
        ("Quận Thanh Xuân", "5.474", "102.70", "92.50", "[101.54 - 103.86]", "± 1.16"),
        ("Quận Hai Bà Trưng", "4.479", "102.59", "89.74", "[101.03 - 104.15]", "± 1.56"),
        ("Quận Nam Từ Liêm", "1.513", "94.08", "85.71", "[92.02 - 96.15]", "± 2.06"),
        ("Quận Long Biên", "2.028", "85.53", "77.50", "[83.77 - 87.29]", "± 1.76"),
        ("Quận Bắc Từ Liêm", "774", "83.93", "80.00", "[81.22 - 86.64]", "± 2.71"),
        ("Quận Hoàng Mai", "4.880", "83.82", "78.82", "[82.93 - 84.71]", "± 0.89"),
        ("Quận Hà Đông", "3.728", "80.80", "74.44", "[79.65 - 81.95]", "± 1.15"),
        ("Huyện Thanh Trì", "574", "62.88", "60.94", "[60.81 - 64.95]", "± 2.07")
    ]
    for idx, (c1, c2, c3, c4, c5, c6) in enumerate(ci_data, start=1):
        t_ci.rows[idx].cells[0].paragraphs[0].text = c1
        t_ci.rows[idx].cells[0].paragraphs[0].runs[0].font.bold = True
        t_ci.rows[idx].cells[1].paragraphs[0].text = c2
        t_ci.rows[idx].cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        t_ci.rows[idx].cells[2].paragraphs[0].text = c3
        t_ci.rows[idx].cells[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
        t_ci.rows[idx].cells[3].paragraphs[0].text = c4
        t_ci.rows[idx].cells[3].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
        t_ci.rows[idx].cells[4].paragraphs[0].text = c5
        t_ci.rows[idx].cells[4].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        t_ci.rows[idx].cells[5].paragraphs[0].text = c6
        t_ci.rows[idx].cells[5].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

    style_table(t_ci, col_widths=[1.5, 0.8, 0.9, 0.9, 1.5, 0.8])
    doc.add_page_break()

    # ==========================================
    # PHẦN 8: CHẨN ĐOÁN HỒI QUY LINE (TUẦN 10)
    # ==========================================
    h8 = doc.add_heading("CHƯƠNG 8: CHẨN ĐOÁN HỒI QUY TUYẾN TÍNH & 4 GIẢ ĐỊNH LINE (TUẦN 10)", level=1)
    h8.runs[0].font.color.rgb = RGBColor(31, 78, 121)

    p = doc.add_paragraph()
    r = p.add_run("Bảng 8: Bảng hồi quy OLS đa biến & 3 Nghĩa vụ đạo đức diễn giải hệ số Beta")
    r.font.bold = True

    t_ols = doc.add_table(rows=8, cols=4)
    t_ols.rows[0].cells[0].paragraphs[0].text = "Thuộc Tính (X)"
    t_ols.rows[0].cells[1].paragraphs[0].text = "Hệ Số Beta"
    t_ols.rows[0].cells[2].paragraphs[0].text = "Giá Trị p-value"
    t_ols.rows[0].cells[3].paragraphs[0].text = "Diễn Giải Nghiệp Vụ Chuẩn Mực (Ceteris Paribus)"

    ols_data = [
        ("khu_vuc_noi_do", "+33.13", "< 0.0001", "Cùng diện tích & số tầng, nhà nội đô gắn liền với mức giá cao hơn 33.13 tr/m² so với ngoại thành."),
        ("loai_nha_ngo_hem", "-33.46", "< 0.0001", "Nhà trong ngõ hẻm gắn liền với mức chiết khấu giảm 33.46 tr/m² so với nhà mặt phố."),
        ("loai_nha_mat_pho", "+14.77", "< 0.0001", "Nhà mặt phố gắn liền với thặng dư thương mại tăng 14.77 tr/m²."),
        ("mat_tien_m", "+1.94", "< 0.0001", "Mỗi mét mặt tiền mở rộng thêm gắn liền với mức tăng 1.94 tr/m² đơn giá."),
        ("Số phòng ngủ", "+5.86", "< 0.0001", "Mỗi phòng ngủ thiết kế thêm gắn liền với mức tăng 5.86 tr/m² đơn giá."),
        ("Số tầng", "+2.45", "< 0.0001", "Mỗi tầng xây dựng thêm gắn liền với mức tăng 2.45 tr/m² đơn giá."),
        ("chieu_sau_m", "-0.04", "0.7080", "Không có ý nghĩa thống kê (p > 0.05), biến dư thừa gây nhiễu.")
    ]
    for idx, (l1, l2, l3, l4) in enumerate(ols_data, start=1):
        t_ols.rows[idx].cells[0].paragraphs[0].text = l1
        t_ols.rows[idx].cells[0].paragraphs[0].runs[0].font.bold = True
        t_ols.rows[idx].cells[1].paragraphs[0].text = l2
        t_ols.rows[idx].cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        t_ols.rows[idx].cells[2].paragraphs[0].text = l3
        t_ols.rows[idx].cells[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        t_ols.rows[idx].cells[3].paragraphs[0].text = l4

    style_table(t_ols, col_widths=[1.5, 1.0, 1.0, 3.0])
    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # HÌNH 8: LINE DIAGNOSTICS
    add_figure_4points(
        doc,
        os.path.join(figures_dir, '08_line_assumptions_diagnostics.png'),
        "Hình 8: Bộ chẩn đoán 4 giả định LINE và hiệu quả nắn chuẩn của biến đổi Logarit",
        "Tổ hợp ma trận 4 biểu đồ chẩn đoán vi phạm hồi quy kinh tế lượng (4-in-1 LINE Regression Diagnostic Matrix): Residuals vs Fitted, Q-Q Plot gốc, Q-Q Plot sau Log, Phân phối phần dư trước/sau Log.",
        "Kiểm tra 4 điều kiện cốt tử để mô hình hồi quy OLS có hiệu lực học thuật (LINE: Linearity, Independence, Normality, Equal Variance); phát hiện phương sai thay đổi hình phễu (Heteroscedasticity) và đuôi dày ngoại lai (Heavy Tails); minh chứng sự vượt trội của biến đổi Logarit.",
        "Góc trên trái: Trục X là Giá trị dự báo; Trục Y là Phần dư e = y - y_hat; đường chấm ngang y=0 và đường Lowess đỏ. Góc trên phải: Q-Q Plot mô hình gốc uốn cong vểnh lên trời. Góc dưới trái: Q-Q Plot sau Log với các điểm xanh bám khít 100% vào đường thẳng đỏ 45 độ. Góc dưới phải: Đường cong mật độ phần dư đỏ (gốc) so với xanh (sau Log).",
        "• Vạch trần sai phạm của mô hình OLS gốc: Kiểm định Breusch-Pagan cho BP = 4417.73 (p < 0.0001), khẳng định mô hình gốc vi phạm nghiêm trọng giả định Homoscedasticity (nhà rẻ tiền sai số +-15 triệu, nhưng nhà đắt tiền sai số vọt lên +-200 triệu).\n"
        "• Sự kỳ diệu của Logarit: Nắn Skewness phần dư từ +2.18 về -0.29 (đối xứng lý tưởng); giảm Kurtosis từ 10.79 về 3.72 (sát mức chuẩn 3.0); giảm MAE từ 29.90 xuống 28.35 tr/m².\n"
        "• Ý nghĩa pháp lý: Bảo vệ tính hợp lệ của các kiểm định t và F, đảm bảo kết quả định giá có căn cứ khoa học vững chắc."
    )

    # HÌNH 9: REGULARIZATION LASSO VS RIDGE
    add_figure_4points(
        doc,
        os.path.join(figures_dir, '09_regularization_lasso_vs_ridge.png'),
        "Hình 9: Kỹ thuật điều chuẩn: So sánh cơ chế co hệ số giữa OLS, Ridge và Lasso",
        "Biểu đồ cột nhóm so sánh trọng số hồi quy chuẩn hóa (Multi-Model Regularization Coefficient Comparison Bar Chart) giữa 3 phương pháp: OLS cổ điển, Hồi quy sườn Ridge (L2) và Hồi quy dây thòng lọng Lasso (L1).",
        "Khắc phục triệt để vấn đề Đa cộng tuyến (Multicollinearity) giữa các biến hình học thửa đất (Diện tích đất vs Tổng diện tích sàn r = 0.88); minh chứng tính năng thưa hóa (Sparsity) và chọn lọc biến số tự động (Automatic Feature Selection) của hình học hàm phạt L1.",
        "Trục hoành X là 8 đặc trưng cốt lõi (khu_vuc_noi_do, loai_nha_ngo_hem, loai_nha_mat_pho, tong_dien_tich_san_m2, mat_tien_m, Số phòng ngủ, Dien_tich_m2, chieu_sau_m). Trục tung Y là Độ lớn hệ số hồi quy chuẩn hóa (Beta). 3 cột màu sắc tại mỗi đặc trưng: Cột xám (OLS), Cột xanh lam (Ridge L2 với alpha = 4.2813), Cột đỏ cam (Lasso L1 với alpha = 0.3556).",
        "• Bản chất của Ridge (L2): Phạt bình phương tổng hệ số (alpha * sum(beta^2)). Ridge co đều tất cả các hệ số nhỏ lại để giảm phương sai, nhưng KHÔNG CÓ biến nào bị loại bỏ hoàn toàn (không có hệ số nào bằng 0).\n"
        "• Đột phá của Lasso (L1): Phạt trị tuyệt đối tổng hệ số (alpha * sum(|beta|)). Nhờ cấu trúc hình học có các góc nhọn tiếp xúc với trục tọa độ, Lasso đã tự động triệt tiêu hệ số của 2 biến Dien_tich_m2 (0.000) và chieu_sau_m (0.000) về đúng số 0!\n"
        "• Giải thích kinh tế: Khi mô hình đã sở hữu biến tong_dien_tich_san_m2 (phản ánh toàn bộ công năng sàn ở thực) và biến mat_tien_m (phản ánh giá trị tiếp giáp thương mại), thì biến Dien_tich_m2 và chieu_sau_m trở nên thừa thãi. Lasso đã thông minh 'gạt bỏ' hai biến này khỏi phương trình định giá, giúp mô hình gọn gàng hơn mà độ chính xác không hề suy giảm."
    )

    doc.add_page_break()

    # ==========================================
    # PHẦN 9: TỔNG KẾT & LỘ TRÌNH (TUẦN 11 - 12)
    # ==========================================
    h9 = doc.add_heading("CHƯƠNG 9: TỔNG KẾT TIẾN ĐỘ & LỘ TRÌNH TRIỂN KHAI CUỐI KỲ (TUẦN 11 - 12)", level=1)
    h9.runs[0].font.color.rgb = RGBColor(31, 78, 121)

    p = doc.add_paragraph()
    r = p.add_run("7 Kết luận thực tiễn then chốt rút ra từ dữ liệu:")
    r.font.bold = True
    doc.add_paragraph(
        "1. Vị trí nội đô chi phối mạnh nhất: Đóng góp hơn 36% giá trị định giá, đẩy đơn giá cao hơn 32.04 triệu/m² (+39.0%) so với ngoại thành.\n"
        "2. 'Tam giác vàng' Cầu Giấy (125 tr), Ba Đình (128 tr), Tây Hồ (123 tr) đồng nhất về giá: Kiểm định ANOVA và Tukey's HSD khẳng định không có sự khác biệt có ý nghĩa thống kê giữa 3 quận này.\n"
        "3. Phân phối lệch phải là bản chất tự nhiên: Bộ lọc miền tri thức [10, 500] tr/m² bảo toàn trọn vẹn nhóm nhà cao cấp mà không làm méo mó phân phối.\n"
        "4. Mặt tiền rộng mang lại thặng dư kinh tế thật sự: Mỗi mét mặt tiền mở rộng gia tăng thêm trung bình ~1.94 triệu/m² đơn giá.\n"
        "5. Mô hình OLS tuyến tính vi phạm phương sai đồng nhất: Cần cẩn trọng với hiện tượng hình phễu ở phân khúc cao cấp.\n"
        "6. Biến đổi Logarit là chìa khóa vàng nắn chuẩn: Giúp Q-Q plot bám khít đường 45 độ và giảm MAE xuống 28.35 tr/m².\n"
        "7. Gradient Boosting là động cơ định giá tối ưu nhất: Đạt MAE = 26.07 triệu/m² và R² = 0.4390 nhờ khả năng bắt tương tác phi tuyến."
    )

    p = doc.add_paragraph()
    r = p.add_run("Lộ trình bứt phá Tuần 11 & Tuần 12:")
    r.font.bold = True
    doc.add_paragraph(
        "• Tuần 11: Huấn luyện XGBoost / LightGBM kết hợp K-Fold Cross-Validation; Tích hợp công cụ SHAP (Shapley Additive exPlanations) bóc tách hộp đen AI; Phân loại 5 phân khúc giá.\n"
        "• Tuần 12: Xây dựng tài liệu chuẩn mực quốc tế Datasheets for Datasets và Model Card; Kiểm toán định kiến vùng miền (Fairness Audit); Hoàn thiện báo cáo và đóng gói nghiệm thu."
    )

    # Save document
    output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'BAO_CAO_TIEN_DO_KHDL.docx')
    doc.save(output_path)
    print(f"🎉 Đã xuất thành công tệp Word tại: {output_path}")

if __name__ == '__main__':
    build_docx_report()
