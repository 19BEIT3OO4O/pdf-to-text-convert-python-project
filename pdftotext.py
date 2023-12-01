from PyPDF2 import PdfFileReader

file_path = 'googlecolab.pdf'

pdf = PdfFileReader(file_path)
with open('text.txt', 'w') as f:
    for page_num in range(pdf.numPages):
        pageObj = pdf.getPage(page_num)

        try:
            txt = pageObj.extractText()
            f.write('page {0}\n'.format(page_num + 1))
            f.write('-' * 15)
            f.write('\n')
            f.write(txt)
        except Exception as e:
            print('Error extracting text from page {0}: {1}'.format(page_num, e))

print('Text extraction completed.')
