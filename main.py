import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os

def module_install_info(module_name):
    if module_name == "PIL":
        return "pip install pillow"
    elif module_name == "cv2":
        return "pip install opencv-python"
    elif module_name == "numpy":
        return "pip install numpy"
    elif module_name == "PyPDF2":
        return "pip install PyPDF2"
    else:
        return "pip install " + module_name


try:
    import pdf_manipulation
except ImportError as e:
    messagebox.showerror("Error", f"{e.name} module is missing. Please install the required modules by running \n {module_install_info(e.name)}")
    exit()


    
def select_folder_path():
    path = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, path)

def select_folder_path2():
    path = filedialog.askdirectory()
    folder_path_entry2.delete(0, tk.END)
    folder_path_entry2.insert(0, path)

def select_folder_path_merge():
    path = filedialog.askdirectory()
    input_entry.delete(0, tk.END)
    input_entry.insert(0, path)

def select_folder_path_merge2():
    path = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, path)

def run_img2pdf():
    input_dir = folder_path_entry.get()
    output_dir = folder_path_entry2.get()
    merged_filename=merged_file2.get()+".pdf"

    if checkbox_var.get() == 1:
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
    
    try:
        pdf_manipulation.convert2pdf(input_dir, output_dir,merged_filename, enhance, delete_processed_images, delete_temp_pdfs)
    except ImportError as e:
        messagebox.showerror("Error", f"{e.name} module is missing. Please install the required modules by running \n{module_install_info(e.name)}")
        exit()

    except:
        messagebox.showerror("Error", "Error converting images to PDFs. Make sure the input folder contains images.")
        return
        
    
    messagebox.showinfo("Done", "Conversion to PDF successful.")
    root.destroy()

def run_mergepdf():
    input_dir = input_entry.get()
    output_dir = output_entry.get()
    merged_filename = merged_file1.get()+".pdf"


    if not input_dir or not output_dir:
        messagebox.showerror("Error", "Please select both folder paths.")
        return
    
    try:
        pdf_manipulation.merge_pdfs(input_dir, output_dir,merged_filename)
    except:
        messagebox.showerror("Error", "Error merging PDFs.")
        return


    messagebox.showinfo("Done", "Merging PDFs successful.")
    root.destroy()

def run_splitpdf():
    input_dir = input_entry2.get()
    output_dir = output_entry2.get()

    if not input_dir or not output_dir:
        messagebox.showerror("Error", "Please select both paths.")
        return
    try:
        start = int(start_entry.get())
        end = int(end_entry.get())
    except:
        messagebox.showerror("Error", "Please enter valid page numbers.")
        return
    if end < start:
        messagebox.showerror("Error", "End page must be greater than start page.")
        return


    try:
        status = pdf_manipulation.pdf_splitter(input_dir, output_dir,start,end)
    except IndexError:
        messagebox.showerror("Error", "Page numbers out of range. Please enter valid page numbers.")
        return
    except pdf_manipulation.DecryptionError:
        messagebox.showerror("Error", "Document is encrypted. Please correct password.")
        return

    if status ==0:
        messagebox.showinfo("Done", "Splitting PDFs successful.")
        root.destroy()
    else:
        messagebox.showerror("Error", "Error splitting PDFs. Make sure the start and end pages are valid.")



root = tk.Tk() 
root.title("Tab Widget") 
tabControl = ttk.Notebook(root) 

tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 
tab3 = ttk.Frame(tabControl)


tabControl.add(tab1, text ='MergePDF') 
tabControl.add(tab2, text ='IMG2PDF') 
tabControl.add(tab3, text="Split PDFs")
tabControl.pack(expand = 1, fill ="both") 

dir_path = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(dir_path, "input")

# Tab 1
input_label = tk.Label(tab1, text="Input Folder:")
input_label.pack(pady=10)

input_entry = tk.Entry(tab1, width=50)
input_entry.insert(0, input_path)
input_entry.pack(pady=5)

input_button = tk.Button(tab1, text="Select Input Folder", command=select_folder_path_merge)
input_button.pack(pady=5)

output_label = tk.Label(tab1, text="Output Folder:")
output_label.pack(pady=10)

output_entry = tk.Entry(tab1, width=50)
output_entry.insert(0, dir_path)
output_entry.pack(pady=5)

output_button = tk.Button(tab1, text="Select Output Folder", command=select_folder_path_merge2)
output_button.pack(pady=5)

merged_file_label = tk.Label(tab1, text="Merged File Name:")
merged_file_label.pack(pady=10)

merged_file1 = tk.Entry(tab1, width=50)
merged_file1.insert(0, "merged")
merged_file1.pack(pady=5)

merge_button = tk.Button(tab1, text="Merge PDFs", command=run_mergepdf)
merge_button.pack(pady=5)








# Tab 2

folder_path_label = ttk.Label(tab2, text="Input Folder:")
folder_path_label.pack(pady=10)



folder_path_entry = ttk.Entry(tab2, width=50)
folder_path_entry.insert(0, input_path)
folder_path_entry.pack(pady=5)

select_folder_button = ttk.Button(tab2, text="Select Folder", command=select_folder_path)
select_folder_button.pack(pady=5)

folder_path_label2 = ttk.Label(tab2, text="Output Folder:")
folder_path_label2.pack(pady=10)

folder_path_entry2 = ttk.Entry(tab2, width=50)
folder_path_entry2.insert(0, dir_path)
folder_path_entry2.pack(pady=5)

select_folder_button2 = ttk.Button(tab2, text="Select Folder", command=select_folder_path2)
select_folder_button2.pack(pady=5)

merged_file_label2 = tk.Label(tab2, text="Merged File Name:")
merged_file_label2.pack(pady=10)

merged_file2 = tk.Entry(tab2, width=50)
merged_file2.insert(0, "merged")
merged_file2.pack(pady=5)


checkbox_var = tk.IntVar()
checkbox = ttk.Checkbutton(tab2, text="Enhance images", variable=checkbox_var)
checkbox.pack(pady=5)

checkbox2_var = tk.IntVar()
checkbox2 = ttk.Checkbutton(tab2, text="Delete processed images", variable=checkbox2_var)
checkbox2_var.set(1)
checkbox2.pack(pady=5)

checkbox3_var = tk.IntVar()
checkbox3 = ttk.Checkbutton(tab2, text="Delete temporary PDFs", variable=checkbox3_var)
checkbox3_var.set(1)
checkbox3.pack(pady=5)

run_button = ttk.Button(tab2, text="Convert Images to PDF", command=run_img2pdf)
run_button.pack(pady=5)



# Tab 3: Merge PDFs with Bookmarks


input_label2 = tk.Label(tab3, text="Input File:")
input_label2.pack(pady=10)

input_entry2 = tk.Entry(tab3, width=50)
input_entry2.pack(pady=5)

input_button2 = tk.Button(tab3, text="Select Input File", command=lambda: select_input_file(input_entry2))
input_button2.pack(pady=5)

output_label2 = tk.Label(tab3, text="Output Folder:")
output_label2.pack(pady=10)

output_entry2 = tk.Entry(tab3, width=50)
output_entry2.insert(0, dir_path)
output_entry2.pack(pady=5)

output_button2 = tk.Button(tab3, text="Select Output Folder", command=lambda: select_output_folder(output_entry2))
output_button2.pack(pady=5)

start_label = tk.Label(tab3, text="Start Page:")
start_label.pack(pady=10)

start_entry = tk.Entry(tab3, width=50)
start_entry.pack(pady=5)

end_label = tk.Label(tab3, text="End Page:")
end_label.pack(pady=10)

end_entry = tk.Entry(tab3, width=50)
end_entry.pack(pady=5)

merge_button2 = tk.Button(tab3, text="Split PDF", command=run_splitpdf)
merge_button2.pack(pady=5)


def select_input_file(entry):
    input_file = filedialog.askopenfilename(title="Select Input File")
    if input_file:
        entry.delete(0, tk.END)
        entry.insert(0, input_file)

def select_output_folder(entry):
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if output_folder:
        entry.delete(0, tk.END)
        entry.insert(0, output_folder)







root.mainloop() 
