import sys
import PyPDF2

template = PyPDF2.PdfFileReader(open(sys.argv[1], 'rb'))
watermark = PyPDF2.PdfFileReader(open(sys.argv[2], 'rb'))
output =  PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

file = open('new_pdf.pdf', 'wb')
output.write(file)

print('All done')