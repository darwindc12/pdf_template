from fpdf import FPDF
import pandas

pdf = FPDF(orientation="P", unit="mm", format="A4")
df = pandas.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    # Setting the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)
    pdf.line(10, 21, 200, 21)
    N = 31
    while N <= 241:
        pdf.line(10, N, 200, N)
        N += 10

    # Setting the footer
    pdf.ln(241)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="R", ln=1)

    for i in range(row['Pages'] - 1):
        pdf.add_page()
        # Setting up the page the number of succeeding pages
        pdf.ln(250)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row['Topic'], align="R", ln=1)

        N = 0
        while N <= 250:
            pdf.line(10, N, 200, N)
            N += 11

pdf.output("output.pdf")