import PyPDF2
import io
from PIL import Image

# Open the PDF file in binary mode
pdf_file = open('googlecolab.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Loop through each page in the PDF file
for page_num in range(pdf_reader.numPages):
    # Get the current page object
    page = pdf_reader.getPage(page_num)
    
    # Extract the text from the page
    text = page.extractText()
    print(f'Page {page_num+1} text:\n{text}')
    
    # Extract the images from the page
    xObject = page['/Resources']['/XObject'].getObject()
    for obj in xObject:
        # Check if the object is an image
        if xObject[obj]['/Subtype'] == '/Image':
            # Get the image data and metadata
            img_data = xObject[obj]._data
            img_size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
            
            # Create a PIL image object from the image data
            img = Image.open(io.BytesIO(img_data))
            
            # Display the image and save it to a file
            img.show()
            img.save(f'page{page_num+1}_image{obj}.jpg', 'JPEG')