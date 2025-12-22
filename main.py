from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_xy(10, 13)  
pdf.set_font("Times", "B", 13)
pdf.multi_cell(w=70, h=5, txt="O'zbekiston Respublikasi Prezididenti Administratsiyasi", align='C')

pdf.set_xy(10, 30)  
pdf.set_font("Times", "B", 13)
pdf.multi_cell(w=70, h=5, txt="O'zbekiston Respublikasi Prezididenti Administratsiyasi Arxivning Namangan viloyati bo'limi", align='C')

pdf.set_xy(135, 13)  
pdf.set_font("Times", "B", 13)
pdf.multi_cell(w=70, h=5, txt="O'zbekiston Respublikasi Prezididenti Administratsiyasi", align='C')

pdf.set_xy(135, 30)  
pdf.set_font("Times", "B", 13)
pdf.multi_cell(w=70, h=5, txt="O'zbekiston Respublikasi Prezididenti Administratsiyasi Arxivning Namangan viloyati bo'limi", align='C')

pdf.set_xy(26, 51)  
pdf.set_font("Times", "", 10)  
pdf.multi_cell(w=36, h=5, txt="160100 Namangan sh. Istiqlol ko'cha 57 Tel: 227-00-11", align='C')

pdf.set_xy(152, 51)  
pdf.set_font("Times", "", 10)  
pdf.multi_cell(w=36, h=5, txt="160100 Namangan sh. Istiqlol ko'cha 57 Tel: 227-00-11", align='C')

pdf.set_line_width(1)
pdf.line(10, 70, 200, 70)

pdf.set_xy(10, 73)  
pdf.set_font("Times", "B", 13)
pdf.multi_cell(w=70, h=5, txt="8 may 2025 yil", align='C')

pdf.set_xy(134, 73)  
pdf.set_font("Times", "B", 13)
pdf.multi_cell(w=70, h=5, txt="8 may 2025 yil", align='C')


pdf.set_xy(10, 80)  
pdf.set_font("Times", "", 13)
pdf.multi_cell(w=70, h=5, txt="2017 - yil maydagi", align='C')

pdf.set_xy(134, 80)  
pdf.set_font("Times", "", 13)
pdf.multi_cell(w=70, h=5, txt="No 546-sonli qarori", align='C')

pdf.image("doc_components/img/gerb.png", x=75, y=13, w=65, h=40)

pdf.output("rasmli_pdf.pdf")
