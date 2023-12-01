from PyPDF2 import PdfReader

reader = PdfReader("googlecolab.pdf")

page = reader.pages[2]
count = 0

for image_file_object in page.images:
    with open(str(count) + image_file_object.name, "wb") as fp:
        fp.write(image_file_object.data)
        count += 1