import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import pdf_manipulation

def select_folder_path():
    path = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, path)

def select_folder_path2():
    path = filedialog.askdirectory()
    folder_path_entry2.delete(0, tk.END)
    folder_path_entry2.insert(0, path)

def run_script():
    input_dir = folder_path_entry.get()
    output_dir = folder_path_entry2.get()
    checked = checkbox_var.get()
    if checked == 1:
        enhance = True
    else:
        enhance = False

    if checkbox2_var.get() == 1:
        delete_processed_images = True
    else:
        delete_processed_images = False
    
    if checkbox3_var.get() == 1:
        delete_temp_pdfs = True
    else:
        delete_temp_pdfs = False


    if not input_dir or not output_dir:
        messagebox.showerror("Error", "Please select both folder paths.")
        return

    # Replace the print statements with your script
    # script(folder_path1, folder_path2, checked)
    pdf_manipulation.convert2pdf(input_dir, output_dir, enhance, delete_processed_images, delete_temp_pdfs)

    messagebox.showinfo("Done", "Conversion to PDF successful.")
    root.destroy()

root = tk.Tk()
root.title("Folder Path Input")

folder_path_label = tk.Label(root, text="Input Folder:")
folder_path_label.pack()

dir_path = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(dir_path, "input")

folder_path_entry = tk.Entry(root, width=50)
folder_path_entry.insert(0, input_path)
folder_path_entry.pack()

folder_path_button = tk.Button(root, text="Browse", command=select_folder_path)
folder_path_button.pack()

folder_path_label2 = tk.Label(root, text="Output Folder:")
folder_path_label2.pack()

folder_path_entry2 = tk.Entry(root, width=50)
folder_path_entry2.insert(0, dir_path)
folder_path_entry2.pack()

folder_path_button2 = tk.Button(root, text="Browse", command=select_folder_path2)
folder_path_button2.pack()

checkbox_var = tk.IntVar()
checkbox = ttk.Checkbutton(root, text="Enhance images", variable=checkbox_var)
checkbox.pack()

checkbox2_var = tk.IntVar()
checkbox2 = ttk.Checkbutton(root, text="Delete Enhanced Images", variable=checkbox2_var)
checkbox2_var.set(1)
checkbox2.pack()

checkbox3_var = tk.IntVar()
checkbox3 = ttk.Checkbutton(root, text="Delete Temp PDFs", variable=checkbox3_var)
checkbox3_var.set(1)
checkbox3.pack()



run_button = tk.Button(root, text="Convert to pdf", command=run_script)
run_button.pack()

root.mainloop()