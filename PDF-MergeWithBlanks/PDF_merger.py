
import PyPDF2
import os


# List all files in a directory using os.listdir
basepath = os.path.dirname(os.path.abspath(__file__))

files_path = os.path.join(basepath,'files')

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
        #files.append(open(file_path, 'rb'))
        
        pdf_merger.append(file_path)
        
        # creating a pdf File object of original pdf
        pdfReader = PyPDF2.PdfFileReader(file_path)
        
        if pdfReader.numPages%2 ==1:
            
            pdf_merger.append(blank_path)
        


newFile = open(output_path, 'wb')

pdf_merger.write(newFile)

pdf_merger.close()




# creating a pdf file object
#pdfFileObj = open('example.pdf', 'rb')
 
# creating a pdf reader object
#pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
# printing number of pages in pdf file
#print(pdfReader.numPages)
 
# creating a page object
#pageObj = pdfReader.getPage(0)
 
# extracting text from page
#print(pageObj.extractText())
 
# closing the pdf file object
#pdfFileObj.close()