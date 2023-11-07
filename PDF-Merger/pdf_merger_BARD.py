import tkinter as tk
from tkinter import filedialog
import os
import PyPDF2

def select_input_folder():
    input_folder = filedialog.askdirectory(title="Select Input Folder")
    if input_folder:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, input_folder)

def select_output_folder():
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if output_folder:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, output_folder)

def merge_pdfs():
    input_folder = input_entry.get()
    select_output_folder()
    output_folder = output_entry.get()
    if input_folder and output_folder:
        pdf_files = []
        for filename in os.listdir(input_folder):
            if filename.endswith('.pdf'):
                pdf_files.append(os.path.join(input_folder, filename))

        merger = PyPDF2.PdfMerger()
        for pdf_file in pdf_files:
            with open(pdf_file, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                merger.append(reader)

        with open(os.path.join(output_folder, 'merged.pdf'), 'wb') as f:
            merger.write(f)

        output_label['text'] = "PDFs Merged Successfully!"

root = tk.Tk()
root.title("PDF Merger")

input_label = tk.Label(root, text="Input Folder:")
input_label.pack(pady=10)

input_entry = tk.Entry(root, width=50)
input_entry.pack(pady=5)

input_button = tk.Button(root, text="Select Input Folder", command=select_input_folder)
input_button.pack(pady=5)

output_label = tk.Label(root, text="Output Folder:")
output_label.pack(pady=10)

output_entry = tk.Entry(root, width=50)
output_entry.pack(pady=5)

output_button = tk.Button(root, text="Select Output Folder", command=merge_pdfs)
output_button.pack(pady=5)



root.mainloop()
