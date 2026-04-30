"""
TOOL: EXCEL TO PDF CONVERTER
BUILDER: AHMED HAMDI
PURPOSE: تحويل قوائم البيانات والفواتير إلى ملفات PDF احترافية
"""

import pandas as pd
from fpdf import FPDF

def create_pdf(csv_file, output_pdf):
    # قراءة البيانات
    try:
        df = pd.read_csv(csv_file)
    except:
        print("خطأ: يرجى التأكد من وجود ملف data.csv")
        return

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # عنوان التقرير
    pdf.cell(200, 10, txt="Business Data Report", ln=True, align='C')
    pdf.ln(10)

    # إضافة البيانات
    for index, row in df.iterrows():
        line = " - ".join([str(val) for val in row.values])
        pdf.cell(0, 10, txt=line, ln=True)
    
    pdf.output(output_pdf)
    print(f"تم بنجاح إنشاء الملف: {output_pdf}")

if __name__ == "__main__":
    # مثال للتشغيل
    create_pdf("data.csv", "Business_Report.pdf")
