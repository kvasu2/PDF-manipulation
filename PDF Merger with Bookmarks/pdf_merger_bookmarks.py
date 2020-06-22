# pdf_merger.py
 
import os
import glob
from PyPDF2 import PdfFileWriter, PdfFileReader

# method that mergers the input_paths into out_paths. It will add bookmarks for each input file with a corresponding name from bookmark_names 
def merger(output_path, input_paths, bookmark_names):
    pdf_writer = PdfFileWriter()
    page_no=0
    count = 0
    for path in input_paths:
        pdf_reader = PdfFileReader(path)
        page_no_temp=pdf_reader.getNumPages()
        for page in range(page_no_temp):
            pdf_writer.addPage(pdf_reader.getPage(page))
        pdf_writer.addBookmark(bookmark_names[count],page_no)
        count = count + 1
        page_no = page_no + page_no_temp
 
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)

# this section gets the paths of the files to be mergerd
dir_path = os.path.dirname(os.path.realpath(__file__))
inp_path = os.path.join(dir_path,"input")
bookmark_names_path = os.path.join(dir_path,"bookmarks","bookmark_names.txt")
inps = sorted(os.listdir(inp_path))
inp_files = []
inp_file_names = []

#this section get the bookmarks file
file= open(bookmark_names_path,"r")
bookmark_names = file.readlines()

for f in inps:
    inp_files.append(os.path.join(inp_path,f))
    #inp_file_names.append(f[0:-4])

output_path = os.path.join(dir_path,"out.pdf")

merger(output_path, inp_files, bookmark_names)