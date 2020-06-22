# pdf_merger.py
 
import os
import glob
from PyPDF2 import PdfFileWriter, PdfFileReader
 
def merger(output_path, input_paths):
    pdf_writer = PdfFileWriter()
 
    for path in input_paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
 
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)

dir_path = os.path.dirname(os.path.realpath(__file__))
inp_path = os.path.join(dir_path,"input")
inps = sorted(os.listdir(inp_path))
inp_files = []

for f in inps:
	inp_files.append(os.path.join(inp_path,f))

output_path = os.path.join(dir_path,"out.pdf")

merger(output_path, inp_files)