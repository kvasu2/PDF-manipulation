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
    import reorder
except ImportError as e:
    messagebox.showerror("Error", f"{e.name} module is missing. Please install the required modules by running \n{module_install_info(e.name)}")
    exit()


class PDFApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #---------------------------------------------------------------------------------------------------------
        # UI

        self.ordered_list=[]

        self.title("Tab Widget") 
        self.tabControl = ttk.Notebook(self) 

        self.tab1 = ttk.Frame(self.tabControl) 
        self.tab2 = ttk.Frame(self.tabControl) 

        self.tabControl.add(self.tab1, text ='MergePDF') 
        self.tabControl.add(self.tab2, text ='IMG2PDF') 
        self.tabControl.pack(expand = 1, fill ="both") 

        dir_path = os.path.dirname(os.path.realpath(__file__))
        input_path = os.path.join(dir_path, "input")

        # Tab 1
        self.input_label_1 = tk.Label(self.tab1, text="Input Folder:")
        self.input_label_1.pack(pady=10)

        self.input_entry_1 = tk.Entry(self.tab1, width=50)
        self.input_entry_1.insert(0, input_path)
        self.input_entry_1.pack(pady=5)

        self.input_button_1 = tk.Button(self.tab1, text="Select Input Folder", command=self.select_input_entry_1)
        self.input_button_1.pack(pady=5)

        self.get_order_button = tk.Button(self.tab1, text="Select and Order PDFs", command=self.get_pdf_order)
        self.get_order_button.pack(pady=5)

        self.choice = tk.IntVar()
        

        self.R1 = tk.Radiobutton(self.tab1, text="Merge PDFs in folder", variable=self.choice, value=1)
        self.R1.pack(anchor=tk.W)

        self.R2 = tk.Radiobutton(self.tab1, text="Select and order", variable=self.choice, value=2)
        self.R2.pack(anchor=tk.W)

        self.choice.set(1)

        self.output_label_1 = tk.Label(self.tab1, text="Output Folder:")
        self.output_label_1.pack(pady=10)

        self.output_entry_1 = tk.Entry(self.tab1, width=50)
        self.output_entry_1.insert(0, dir_path)
        self.output_entry_1.pack(pady=5)

        self.output_button_1 = tk.Button(self.tab1, text="Select Output Folder", command=self.select_output_entry_1)
        self.output_button_1.pack(pady=5)

        self.merged_file_label_1 = tk.Label(self.tab1, text="Merged File Name:")
        self.merged_file_label_1.pack(pady=10)

        self.merged_file_1 = tk.Entry(self.tab1, width=50)
        self.merged_file_1.insert(0, "merged")
        self.merged_file_1.pack(pady=5)

        self.merge_button_1 = tk.Button(self.tab1, text="Merge PDFs", command=self.run_mergepdf)
        self.merge_button_1.pack(pady=5)

        self.progress_1 = tk.Label(self.tab1, text="")
        self.progress_1.pack(pady=10)

        # Tab 2

        self.input_label_2 = tk.Label(self.tab2, text="Input Folder:")
        self.input_label_2.pack(pady=10)

        self.input_entry_2 = tk.Entry(self.tab2, width=50)
        self.input_entry_2.insert(0, input_path)
        self.input_entry_2.pack(pady=5)

        self.input_button_2 = tk.Button(self.tab2, text="Select Input Folder", command=self.select_input_entry_2)
        self.input_button_2.pack(pady=5)

        self.output_label_2 = tk.Label(self.tab2, text="Output Folder:")
        self.output_label_2.pack(pady=10)

        self.output_entry_2 = tk.Entry(self.tab2, width=50)
        self.output_entry_2.insert(0, dir_path)
        self.output_entry_2.pack(pady=5)

        self.output_button_2 = tk.Button(self.tab2, text="Select Output Folder", command=self.select_output_entry_2)
        self.output_button_2.pack(pady=5)

        self.merged_file_label_2 = tk.Label(self.tab2, text="Merged File Name:")
        self.merged_file_label_2.pack(pady=10)

        self.merged_file_2 = tk.Entry(self.tab2, width=50)
        self.merged_file_2.insert(0, "merged")
        self.merged_file_2.pack(pady=5)

        self.checkbox_var = tk.IntVar()
        self.checkbox = tk.Checkbutton(self.tab2, text="Enhance Images", variable=self.checkbox_var)
        self.checkbox.pack(pady=5)

        self.checkbox2_var = tk.IntVar()
        self.checkbox2 = tk.Checkbutton(self.tab2, text="Delete Processed Images", variable=self.checkbox2_var)
        self.checkbox2_var.set(1)
        self.checkbox2.pack(pady=5)

        self.checkbox3_var = tk.IntVar()
        self.checkbox3 = tk.Checkbutton(self.tab2, text="Delete Temp PDFs", variable=self.checkbox3_var)
        self.checkbox3_var.set(1)
        self.checkbox3.pack(pady=5)

        self.merge_button_2 = tk.Button(self.tab2, text="Convert to PDF", command=self.run_img2pdf)
        self.merge_button_2.pack(pady=5)

        self.progress_2 = tk.Label(self.tab2, text="")
        self.progress_2.pack(pady=10)

    #---------------------------------------------------------------------------------------------------------
    # Functions

    def select_input_entry_1(self):
        path = filedialog.askdirectory()
        if not path:
            return
        self.input_entry_1.delete(0, tk.END)
        self.input_entry_1.insert(0, path)

    def select_output_entry_1(self):
        path = filedialog.askdirectory()
        if not path:
            return
        self.output_entry_1.delete(0, tk.END)
        self.output_entry_1.insert(0, path)

    def select_input_entry_2(self):
        path = filedialog.askdirectory()
        if not path:
            return
        self.input_entry_2.delete(0, tk.END)
        self.input_entry_2.insert(0, path)

    def select_output_entry_2(self):
        path = filedialog.askdirectory()
        if not path:
            return
        self.output_entry_2.delete(0, tk.END)
        self.output_entry_2.insert(0, path)

    def run_mergepdf(self):
        self.progress_1.config(text="Merging PDFs. Please wait...")
        self.progress_1.update_idletasks()

        input_dir = self.input_entry_1.get()
        output_dir = self.output_entry_1.get()
        merged_filename = self.merged_file_1.get()

        if not input_dir and self.choice.get() == 1:
            messagebox.showerror("Error", "Please select Input folder.")
            return
        
        if not output_dir:
            messagebox.showerror("Error", "Please select an output folder.")
            return
        
        if not merged_filename:
            messagebox.showerror("Error", "Please enter an output filename.")
            return
        merged_filename = merged_filename+".pdf"

        if self.choice.get() == 1:
            
            try:
                pdf_manipulation.merge_pdfs(input_dir, output_dir,merged_filename)
            except Exception as e:
                self.progress_1.config(text="")
                messagebox.showerror("Error", f"{e}")
                return

            
        
        elif self.choice.get() == 2:
            try:
                pdf_manipulation.merge_pdfs_in_order(self.ordered_list,output_dir,merged_filename)
            except Exception as e:
                self.progress_1.config(text="")
                messagebox.showerror("Error", f"{e}")
                return

        self.progress_1.config(text="Merging PDFs successful.")

        messagebox.showinfo("Done", "Merging PDFs successful.")
        self.destroy()
        
    def get_pdf_order(self):
        self.progress_1.config(text="Select and order PDFs...")
        self.progress_1.update_idletasks()
        old_list = self.ordered_list.copy()
        self.ordered_list = []
        sbroot = tk.Toplevel(self)
        reorder.Application(sbroot,ordered_list=self.ordered_list,old_list=old_list)

        


        

    def run_img2pdf(self):
        self.progress_2.config(text="Converting images to PDF. Please wait...")
        self.progress_2.update_idletasks()
        input_dir = self.input_entry_2.get()
        output_dir = self.output_entry_2.get()
        merged_filename = self.merged_file_2.get()

        if self.checkbox_var.get() == 1:
            enhance = True
        else:
            enhance = False

        if self.checkbox2_var.get() == 1:
            delete_processed_images = True
        else:
            delete_processed_images = False
        
        if self.checkbox3_var.get() == 1:
            delete_temp_pdfs = True
        else:
            delete_temp_pdfs = False

        if not input_dir or not output_dir:
            messagebox.showerror("Error", "Please select both folder paths.")
            return
        
        if not merged_filename:
            messagebox.showerror("Error", "Please enter an output filename.")
            return
        merged_filename = merged_filename+".pdf"
        
        try:
            pdf_manipulation.convert2pdf(input_dir, output_dir,merged_filename, enhance, delete_processed_images, delete_temp_pdfs)
        except ImportError as e:
            self.progress_2.config(text="")
            messagebox.showerror("Error", f"{e.name} module is missing. Please install the required modules by running \n{module_install_info(e.name)}")
            exit()
        except Exception as e:
            self.progress_2.config(text="")
            messagebox.showerror("Error", f"{e}")
            return
            
        self.progress_2.config(text="Conversion to PDF successful.")
        messagebox.showinfo("Done", "Conversion to PDF successful.")
        self.destroy()

    #---------------------------------------------------------------------------------------------------------

def main():
    app = PDFApp()
    app.mainloop()  
    return 0
    
if __name__ == '__main__':
    main()