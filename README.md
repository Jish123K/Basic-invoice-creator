# Basic-invoice-creator
This code uses the FPDF library in Python to create a PDF receipt.

The receipt contains a header with the company logo, customer information such as name, address, and email, and a table to list the purchased items along with their unit cost, quantity, total cost, and taxes. The receipt also includes a subtotal, tax, total, amount paid, and change.

The code starts by importing the necessary libraries such as FPDF and datetime. It then creates a PDF object using FPDF and sets up the font for the PDF. The code then adds the first page to the PDF object and adds the header to it.

Next, the code adds the customer data to the PDF object, including name, address, email, and other details. It also adds the current date and time to the receipt.

The code then creates a table for the purchased items and adds it to the PDF object. The table includes columns for the item, description, units, unit cost, total cost, and taxes.

Finally, the code calculates and adds the subtotal, tax, total, amount paid, and change to the PDF object, and saves the PDF file with the name "receipt.pdf".
