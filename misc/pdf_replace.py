import pdf_redactor
import re
import PyPDF2

ENCRYPTED_FILE_PATH = './Martin_Houska.pdf'
HESLO = "1411281014"
DECRYPTED_FILE_PATH = "./MH.pdf"
REDACTED_FILE_PATH =  "./MH_redacted.pdf"
REPLACED_FILE_PATH =  "./MH_replaced.pdf"

with open(ENCRYPTED_FILE_PATH, mode='rb') as fr:        
    reader = PyPDF2.PdfFileReader(fr)
    if reader.isEncrypted:
        reader.decrypt(HESLO)
        #  print(f"Number of page: {reader.getNumPages()}")

    pageObj = reader.getPage(0)  # staci 1. strana  
    # txt = pageObj.extractText()
    # print(pageObj)    

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(pageObj)
    with open(DECRYPTED_FILE_PATH , mode='wb') as fw:
        writer.write(fw)


# nahrady (content_filters) nad danym pdf nefunguji
# pravdepodobne z duvodu formatu .pdf
# ale jako side effect se vystup ulozi do formatu, 
# kde lze pouzit replace v binary modu - viz nize
options = pdf_redactor.RedactorOptions()
options.input_stream = DECRYPTED_FILE_PATH
options.output_stream = REDACTED_FILE_PATH  
options.content_filters = [	
	(
		re.compile(u"regex_for_orig_text"),
		lambda m : "replacement"
	)
]

pdf_redactor.redactor(options)

# replace v binary modu
with open(REDACTED_FILE_PATH, mode='rb') as fr:
    s = fr.read()

s = s.replace(b"15.07",b"22.07")
s = s.replace(b"17.07",b"24.07")

with open(REPLACED_FILE_PATH, mode='wb') as fw:
    fw.write(s)