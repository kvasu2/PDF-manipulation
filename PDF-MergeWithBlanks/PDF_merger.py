
import PyPDF2
import os



basepath = os.path.dirname(os.path.abspath(__file__))

files_path = os.path.join(basepath,'input')

blank_path = os.path.join(basepath,'blank.pdf')

if not os.path.isfile(blank_path):

    blankPDF = PyPDF2.PdfFileWriter()
    blankPDF.addBlankPage(width=612, height=792)
    blankPDF.write(open(blank_path,'wb'))

output_path = os.path.join(basepath,'output.pdf')


pdf_merger = PyPDF2.PdfFileMerger()


for entry in os.listdir(files_path):
    file_path = os.path.join(files_path, entry)
    if os.path.isfile(file_path):
        
        pdf_merger.append(file_path)
        
        pdfReader = PyPDF2.PdfFileReader(file_path)
        
        if pdfReader.numPages%2 ==1:
            
            pdf_merger.append(blank_path)
        


newFile = open(output_path, 'wb')

pdf_merger.write(newFile)

pdf_merger.close()

if os.path.exists(blank_path):
  os.remove(blank_path)