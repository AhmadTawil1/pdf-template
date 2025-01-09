from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P',unit='mm',format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")
for index, row in df.iterrows():
    for i in range (df['Pages'][index]):
        # Set the header
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(100,100,100)
        pdf.cell(w=0, h=12, txt=df['Topic'][index], ln=1, align="L")
        pdf.line(x1=10,y1=20, x2=200,y2=20)

        # Set the footer
        pdf.ln(265)

        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


pdf.output("output.pdf")