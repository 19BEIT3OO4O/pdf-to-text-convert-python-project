import PyPDF2


def extract_text_from_pdf(pdf_file='DBMS_Notes.pdf', output_file ='text.txt'):
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        with open('text.txt', 'w', encoding='utf-8') as output:
            for page in pdf_reader.pages:
                text = page.extract_text()
                output.write(text)

# Specify the input PDF file and output text file paths
pdf_file = 'DBMS_Notes.pdf'
text_file = 'text.txt'

# Call the function to extract text from the PDF and write it to the text file
extract_text_from_pdf(pdf_file, text_file)


