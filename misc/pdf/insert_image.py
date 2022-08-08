from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
import io
from pathlib import Path

src_fld = Path("C:/git/py/misc/pdf")
dst_fld = Path("C:/git/py/misc/pdf")

in_pdf_file =  src_fld / "Prohlaseni-bezinfekcnost-gdpr-etc.pdf"  # 'multipage.pdf'
out_pdf_file = src_fld / 'out_with_img.pdf'
img_file_1 = src_fld / 'Martin_karta_poj_1.png'
img_file_2 = src_fld / 'Martin_karta_poj_2.png'

def add_image():
    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    #can.drawString(10, 100, "Hello world")
    x_start_1 = 90
    y_start_1 = -20
    x_start_2 = 310
    y_start_2 = -22
    can.drawImage(img_file_1, x_start_1, y_start_1, width=190, preserveAspectRatio=True, mask='auto')
    can.drawImage(img_file_2, x_start_2, y_start_2, width=190, preserveAspectRatio=True, mask='auto')
    can.showPage()
    can.showPage()
    can.showPage()   
    can.showPage()
    can.save()
 
    #move to the beginning of the StringIO buffer
    packet.seek(0)
 
    new_pdf = PdfFileReader(packet)
 
    # read the existing PDF
    existing_pdf = PdfFileReader(open(in_pdf_file, "rb"))
    output = PdfFileWriter()
 
    for i in range(len(existing_pdf.pages)):
        page = existing_pdf.getPage(i)
        page.mergePage(new_pdf.getPage(i))
        output.addPage(page)
 
    outputStream = open(out_pdf_file, "wb")
    output.write(outputStream)
    outputStream.close()

add_image()    