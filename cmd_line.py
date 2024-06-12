import pdf_manipulation
import os

dir = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(dir, "input")

pdf_manipulation.merge_pdfs(input_path, dir)

# pdf_manipulation.convert2pdf(input_path, dir, enhance_img=False, delete_processed_images=False, delete_temp_pdfs=False)

# strt=1
# ed=3
# pdf_manipulation.pdf_splitter(input_path,dir,strt,ed)