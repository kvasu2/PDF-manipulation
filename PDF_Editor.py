import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pdf_manipulation

root = tk.Tk()
root.title("PDF Merger and Bookmark Adder")

tabControl = ttk.Notebook(root)

# Tab 1: Merge PDFs
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Merge PDFs")

input_label = tk.Label(tab1, text="Input Folder:")
input_label.pack(pady=10)

input_entry = tk.Entry(tab1, width=50)
input_entry.pack(pady=5)

input_button = tk.Button(tab1, text="Select Input Folder", command=lambda: select_input_folder(input_entry))
input_button.pack(pady=5)

output_label = tk.Label(tab1, text="Output Folder:")
output_label.pack(pady=10)

output_entry = tk.Entry(tab1, width=50)
output_entry.pack(pady=5)

output_button = tk.Button(tab1, text="Select Output Folder", command=lambda: select_output_folder(output_entry))
output_button.pack(pady=5)

merge_button = tk.Button(tab1, text="Merge PDFs", command=lambda: pdf_manipulation.merge_pdfs(input_entry.get(), output_entry.get()))
merge_button.pack(pady=5)

# Tab 2: Merge PDFs with Bookmarks
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Merge PDFs with Bookmarks")

input_label2 = tk.Label(tab2, text="Input Folder:")
input_label2.pack(pady=10)

input_entry2 = tk.Entry(tab2, width=50)
input_entry2.pack(pady=5)

input_button2 = tk.Button(tab2, text="Select Input Folder", command=lambda: select_input_folder(input_entry2))
input_button2.pack(pady=5)

csv_label = tk.Label(tab2, text="CSV Path:")
csv_label.pack(pady=10)

csv_entry = tk.Entry(tab2, width=50)
csv_entry.pack(pady=5)

csv_button = tk.Button(tab2, text="Select CSV File", command=lambda: select_csv_file(csv_entry))
csv_button.pack(pady=5)

output_label2 = tk.Label(tab2, text="Output Folder:")
output_label2.pack(pady=10)

output_entry2 = tk.Entry(tab2, width=50)
output_entry2.pack(pady=5)

output_button2 = tk.Button(tab2, text="Select Output Folder", command=lambda: select_output_folder(output_entry2))
output_button2.pack(pady=5)

merge_button2 = tk.Button(tab2, text="Merge PDFs with Bookmarks", command=lambda: pdf_manipulation.merge_pdfs_with_bookmarks(input_entry2.get(), csv_entry.get(), output_entry2.get()))
merge_button2.pack(pady=5)

tab3 = tk.ttk.Frame(tabControl)
tabControl.add(tab3, text="Info")

info_label = tk.Label(tab3, text="This application provides two functions:\n1. Merge PDFs\n2. Merge PDFs with Bookmarks\n\nFor each function, select the input folder containing the PDFs to merge and the output folder where the merged PDF will be saved.\n\nFor the 'Merge PDFs with Bookmarks' function, also select the CSV file that specifies the order and optional bookmarks for the merged PDF.\nThe CSV file should have two columns: 'filename' and 'bookmark_title'.", justify=tk.LEFT, font=('Arial', 10))
info_label.pack(pady=10)

tabControl.pack(expand=1, fill="both")

def select_input_folder(entry):
    input_folder = filedialog.askdirectory(title="Select Input Folder")
    if input_folder:
        entry.delete(0, tk.END)
        entry.insert(0, input_folder)

def select_output_folder(entry):
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if output_folder:
        entry.delete(0, tk.END)
        entry.insert(0, output_folder)

def select_csv_file(entry):
    csv_path = filedialog.askopenfilename(title="Select CSV File")
    if csv_path:
        entry.delete(0, tk.END)
        entry.insert(0, csv_path)

root.mainloop()
