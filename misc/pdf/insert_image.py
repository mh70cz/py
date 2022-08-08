from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import io
from pathlib import Path

src_fld = Path("C:/git/py/misc/pdf")
dst_fld = Path("C:/git/py/misc/pdf")

in_pdf_file =  src_fld / "Prohlaseni-bezinfekcnost-gdpr-etc.pdf"  # 'multipage.pdf'
out_pdf_file = src_fld / 'out_with_img.pdf'
img_file_1 = src_fld / 'Martin_karta_poj_1.png'
img_file_2 = src_fld / 'Martin_karta_poj_2.png'

name = "Martin Houska"
address = "Lamačova 824/9, Praha 5, 152 00"
resp_m = "Irena Housková"
resp_f = "Miroslav Houska"

tel_m = "605 337 039"
tel_f = "731 126 295"

email_m = "houskova.irena@gmail.com"
email_f = "mh70@mh70.cz"


def add_image():
    packet = io.BytesIO()
    can = canvas.Canvas(packet)

    pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))

    can.setFont("Vera", 12)
    can.drawString(120, 766, name)
    
    can.drawString(120, 745, address)

    can.drawString(200, 725, resp_m)
    can.drawString(120, 705, tel_m )
    can.drawString(300, 705, email_m  )

    can.drawString(200, 685, resp_f)
    can.drawString(120, 662, tel_f )
    can.drawString(300, 662, email_f  )


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