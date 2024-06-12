# pdf_splitter.py

import os
from PyPDF2 import PdfFileReader, PdfFileWriter
 
 
def pdf_splitter(path,strt,ed):
	fname = os.path.splitext(os.path.basename(path))[0]
	
	pdf = PdfFileReader(path)
	if pdf.isEncrypted:
		try:
			pdf.decrypt('')
		except:
			pdf.decrypt(input("Enter password for {}: ".format(fname)))
			
	pdf_writer = PdfFileWriter()
	for page in range(strt-1,ed):
		pdf_writer.addPage(pdf.getPage(page))
	
	output_filename = '{}.pdf'.format(fname)
 
	with open(output_filename, 'wb') as out:
		pdf_writer.write(out)
	
	print('Created: {}'.format(output_filename))	
	

basepath = os.path.dirname(os.path.abspath(__file__))

inp_path = os.path.join(basepath,'input')

srt=input("Start Page: ")
edd=input("End Page: ")

for inp in os.listdir(inp_path):
    file_path = os.path.join(inp_path, inp)
    pdf_splitter(file_path,int(srt),int(edd))

