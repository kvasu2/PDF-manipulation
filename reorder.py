import tkinter as Tkinter
from tkinter import filedialog
from tkinter import messagebox

class DragDropListbox(Tkinter.Listbox):
    """ A Tkinter listbox with drag'n'drop reordering of entries and file upload. """
    def __init__(self, master, **kw):
        kw['selectmode'] = Tkinter.SINGLE
        Tkinter.Listbox.__init__(self, master, kw)
        self.bind('<Button-1>', self.setCurrent)
        self.bind('<B1-Motion>', self.shiftSelection)
        self.curIndex = None
        self.config(width=80)

    def setCurrent(self, event):
        self.curIndex = self.nearest(event.y)

    def shiftSelection(self, event):
        i = self.nearest(event.y)
        if i < self.curIndex:
            x = self.get(i)
            self.delete(i)
            self.insert(i+1, x)
            self.curIndex = i
        elif i > self.curIndex:
            x = self.get(i)
            self.delete(i)
            self.insert(i-1, x)
            self.curIndex = i

    def upload_files(self):
        """ Opens a file dialog to upload files. """
        files = filedialog.askopenfilenames()
        for file in files:
            self.insert(Tkinter.END, file)

class Application(Tkinter.Frame):
    def __init__(self, master,ordered_list=None,old_list=None):
        super().__init__(master)
        self.master = master
        master.title('Drag and Drop Listbox')
        self.pack()
        self.ordered_list=ordered_list
        self.old_list=old_list
        self.create_widgets()
        
        

    def create_widgets(self):
        self.listbox = DragDropListbox(self)
        self.listbox.pack(fill='both', expand=True, padx=10, pady=10)

        for file in self.old_list:
            self.listbox.insert(Tkinter.END, file)

        self.upload_button = Tkinter.Button(self, text='Upload Files', command=self.listbox.upload_files)
        self.upload_button.pack()

        self.clear_button = Tkinter.Button(self, text='Clear List', command=self.clear_list)
        self.clear_button.pack()

        self.process_button = Tkinter.Button(self, text='Process Files', command=self.process_files)
        self.process_button.pack()

        self.quit = Tkinter.Button(self, text="Quit", command=self.quit_listbox)
        self.quit.pack()
    
    def clear_list(self):
        """ Clear the listbox. """
        self.listbox.delete(0, Tkinter.END)
        self.listbox.curIndex = None

    
    def process_files(self):
        """ Process files in the listbox. """
        current_order = self.listbox.get(0, Tkinter.END)
        self.ordered_list.extend([l for l in current_order])
        self.master.destroy()

    def quit_listbox(self):
        """ Quit the listbox. """
        self.ordered_list.extend([l for l in self.old_list])
        self.master.destroy()
