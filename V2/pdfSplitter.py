from PyPDF2 import PdfFileWriter, PdfFileReader
from tkinter import *
from tkinter import ttk, filedialog
import os,sys

path,file_folder,separator,file_name = '','','',''

def split_pdf():
    global path,file_folder,separator,file_name
    if path:
        inputpdf = PdfFileReader(open(path, "rb"))
        file_name = file_name.split('.')[0]
        newDirectory = file_folder + '/' + file_name
        if not os.path.exists(newDirectory):
            os.mkdir(newDirectory)
        for i in range(inputpdf.numPages):
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i))
            with open(newDirectory + "/%s-page%s.pdf" % (file_name,i), "wb") as outputStream:
                output.write(outputStream)

def select_file():
    global path,file_folder,separator,file_name
    path = filedialog.askopenfilename(title='Select file',filetypes = [('PDF files', '*.pdf')])
    file_folder,separator,file_name = path.rpartition('/')
    txtFile['text'] = file_name

root = Tk()
root.configure(bg = 'beige')
root.title('PDF Splitter by D.H')
root.columnconfigure(3, weight=1)
root.rowconfigure(3, weight=1)

btnSplit = ttk.Button(root, text='Split', command=split_pdf)
btnExit = ttk.Button(root, text='Exit', command=sys.exit)
btnSelect = ttk.Button(root, text='Select PDF', command=select_file)
txtFile = ttk.Label(root,text='--Select your PDF--')

btnSplit.grid(column=0,row=2, padx=15, pady=15)
btnExit.grid(column=1,row=2, padx=15, pady=15)
btnSelect.grid(column=0,row=0, padx=15, pady=15,columnspan=2)
txtFile.grid(column=0,row=1, padx=15, pady=15,columnspan=2)  

root.mainloop()




