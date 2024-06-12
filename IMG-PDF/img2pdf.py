from PIL import Image
import os
import glob
from PyPDF2 import PdfFileWriter, PdfFileReader

dir_path = os.path.dirname(os.path.realpath(__file__))

if not os.path.exists(os.path.join(dir_path, "temp")):
    os.makedirs(os.path.join(dir_path, "temp"))

inp_path = os.path.join(dir_path,"input")
image_paths = sorted(os.listdir(inp_path))

# Create a new PDF file
pdf_prefix = os.path.join(dir_path,"temp","output_")

# Loop through each image
for image_path in image_paths:

    # Open the PDF file
    pdf = open(pdf_prefix+image_path+'.pdf', 'wb')

    # Open the image
    image = Image.open(os.path.join(inp_path,image_path))

    # Convert the image to RGB
    image = image.convert('RGB')

    # Save the image to the PDF
    image.save(pdf, 'PDF')

    # Close the PDF file
    pdf.close()



 
def merger(output_path, input_paths):
    pdf_writer = PdfFileWriter()
 
    for path in input_paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
 
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)

inp_path = os.path.join(dir_path,"temp")
inps = sorted(os.listdir(inp_path))
inp_files = []

for f in inps:
	inp_files.append(os.path.join(inp_path,f))

output_path = os.path.join(dir_path,"out.pdf")

merger(output_path, inp_files)