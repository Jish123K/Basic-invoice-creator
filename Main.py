from fpdf import FPDF

from datetime import datetime

# Example data

data = ['John', 'Doe', '111111111', '310310310', '5555 W Nice Street', 'Nashville, Tennesse, USA', 'myemail@email.com']

# Create PDF object

pdf = FPDF(orientation='P', unit='pt', format='A4')

# Set up fonts

pdf.add_font('Times-Roman', '', 'times.ttf', uni=True)

pdf.set_font('Times-Roman', '', 12)

# Add first page

pdf.add_page()

# Header

pdf.cell(0, 20, "¡Hola! Este es tu recibo en el cual puedes ver el detalle de tu venta:", ln=1)

pdf.line(20, 40, 575, 40)

pdf.line(20, 45, 575, 45)

pdf.image("C:/image/Company-logo.png", x=20, y=50, w=100, h=80)

pdf.rect(20, 200, 320, 80)

pdf.rect(400, 215, 160, 60)

# Customer data

pdf.set_font('Times-Roman', '', 9)

pdf.cell(50, 20, "Name:")

pdf.cell(130, 20, data[0])

pdf.ln()

pdf.cell(50, 20, "Last Name:")

pdf.cell(130, 20, data[1])

pdf.ln()

pdf.cell(50, 20, "ID number:")

pdf.cell(130, 20, data[2])

pdf.ln()

pdf.cell(50, 20, "Telephone:")

pdf.cell(130, 20, data[3])

pdf.ln()

pdf.cell(50, 20, "Address:")

pdf.cell(130, 20, data[4])

pdf.ln()

pdf.cell(50, 20, "City/State:")

pdf.cell(130, 20, data[5])

pdf.ln()

pdf.cell(50, 20, "Email:")

pdf.cell(130, 20, data[6])

pdf.ln()

pdf.cell(200, 20, "Date & Hour:")

pdf.cell(130, 20, datetime.now().isoformat())

pdf.ln()

pdf.cell(200, 20, "Receipt No.:")

pdf.cell(130, 20, "XXX")

pdf.ln()

pdf.line(20, 280, 575, 280)

pdf.line(20, 285, 575, 285)

# Item's table

pdf.cell(35, 20, "Ítem")

pdf.cell(115, 20, "Description")

pdf.cell(70, 20, "Units")

pdf.cell(60, 20, "Unit Cost")

pdf.cell(60, 20, "Total Cost")

pdf.cell(60, 20, "Taxes")

pdf.ln()

pdf.line(20, 295, 575, 295)

# Grid for data product

yitem = list(range(1, 16))

ygrid = list(range(315, 565, 20))

xgrid = list(range(375, 575, 3))

for p in yitem:

    pdf.cell(35, 20, str(p))

    pdf.cell(115, 20, "")

    pdf.cell(70, 20, "")

    pdf.cell(60, 20, "")

    pdf.cell(60, 20, "")

    pdf.cell(60, 20, "")

    pdf.ln()
#Total

pdf.line(20, 565, 575, 565)

pdf.line(20, 570, 575, 570)

pdf.cell(335, 20, "")

pdf.cell(60, 20, "Subtotal")

pdf.cell(60, 20, "$XX.XX")

pdf.ln()

pdf.cell(335, 20, "")

pdf.cell(60, 20, "Tax")

pdf.cell(60, 20, "$XX.XX")

pdf.ln()

pdf.cell(335, 20, "")

pdf.cell(60, 20, "Total")

pdf.cell(60, 20, "$XX.XX")

pdf.ln()

pdf.cell(335, 20, "")

pdf.cell(60, 20, "Amount Paid")

pdf.cell(60, 20, "$XX.XX")

pdf.ln()

pdf.cell(335, 20, "")

pdf.cell(60, 20, "Change")

pdf.cell(60, 20, "$XX.XX")

Save PDF

pdf.output("receipt.pdf")
#
