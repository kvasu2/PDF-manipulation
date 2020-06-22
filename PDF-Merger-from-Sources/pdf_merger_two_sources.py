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
inp_path1 = os.path.join(dir_path,"input1")
inps1 = sorted(os.listdir(inp_path1))
inp_files1 = []

inp_path2 = os.path.join(dir_path,"input2")
inps2 = sorted(os.listdir(inp_path2))
inp_files2 = []

count =0

for f in inps1:
    inp_temp=[]
    inp_temp.append(os.path.join(inp_path1,inps1[count]))
    inp_temp.append(os.path.join(inp_path2,inps2[count]))
    out_temp = os.path.join(dir_path,"out",inps1[count])
    merger(out_temp,inp_temp)
    count = count+1
