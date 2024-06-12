import pdf_manipulation
import os

dir = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(dir, "input")

pdf_manipulation.merge_pdfs(input_path, dir, dir)
