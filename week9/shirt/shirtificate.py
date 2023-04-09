from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        header_y = 50.0
        header_x = self.epw
        header_font_size = 45
        self.set_font("helvetica", "", header_font_size)
        self.cell(header_x, header_y, "CS50 Shirtificate", align="C")


def main():
    pdf = PDF(orientation="P", unit="mm", format="A4")

    #Disable auto page break
    pdf.set_auto_page_break(False)

    #Create page
    pdf.add_page()

    #Set margin (mm)
    margin = 10
    pdf.set_margin(margin)

    #Display image
    image_x = margin
    image_y = 60.0
    pdf.image("shirtificate.png", x=image_x, y=image_y, w=pdf.epw)

    #Writing text onto shirt
    shirt_font_size = 20
    shirt_text = "Wangjinghong took CS50"
    shirt_text_y = 120
    pdf.set_font("helvetica", "", shirt_font_size)
    pdf.set_y(shirt_text_y)

    #Changing text color
    pdf.set_text_color(255,255,255)
    pdf.cell(pdf.epw, 0, shirt_text, align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    raise SystemExit(main())
