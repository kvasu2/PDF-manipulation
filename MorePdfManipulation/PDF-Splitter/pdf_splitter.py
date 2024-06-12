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
			pdf.decrypt(input("Enter password: "))
			
	pdf_writer = PdfFileWriter()
	for page in range(strt-1,ed):
		pdf_writer.addPage(pdf.getPage(page))
	
	output_filename = '{}_pages_{}-{}.pdf'.format(fname, strt,ed)
 
	with open(output_filename, 'wb') as out:
		pdf_writer.write(out)
	
	print('Created: {}'.format(output_filename))	
	
inp_path = os.path.join("","input")
inp = os.path.join(inp_path,os.listdir(inp_path)[0])

srt=input("Start Page: ")
edd=input("End Page: ")
pdf_splitter(inp,int(srt),int(edd))

