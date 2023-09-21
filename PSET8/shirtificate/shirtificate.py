from fpdf import FPDF


class Shirtificate(FPDF):
    def header(self):
        self.image("shirtificate.png", 10, 70, 190)
        self.set_font("helvetica", "", 48)
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        self.ln(20)

    def create_pdf(self, name):
        self.add_page(orientation="portrait", format="A4")
        self.set_font("helvetica", size=24)
        self.set_text_color(255, 255, 255) # White text color
        self.cell(0, 213, f"{name} took CS50", align="C")
        self.output("shirtificate.pdf")


def main():
    shirtificate = Shirtificate()
    name = input("Name: ")
    shirtificate.create_pdf(name)


if __name__ == "__main__":
    main()