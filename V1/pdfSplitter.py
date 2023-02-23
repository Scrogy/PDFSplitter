from PyPDF2 import PdfFileWriter, PdfFileReader

from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
import os,sys

files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.pdf')]
print(files)

def selection_changed(event):
    print("Nuevo elemento seleccionado:", combo.get())

def split_pdf():
    global files
    if combo.get():
        inputpdf = PdfFileReader(open(str(combo.get()), "rb"))

        for i in range(inputpdf.numPages):
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i))
            with open("document-page%s.pdf" % i, "wb") as outputStream:
                output.write(outputStream)

        files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.pdf')]
        combo["values"] = files


raiz = Tk()


raiz.configure(bg = 'beige')

raiz.title('PDF Splitter by D.H')

raiz.columnconfigure(3, weight=1)
raiz.rowconfigure(3, weight=1)

btnSplit = ttk.Button(raiz, text='Split', command=split_pdf)
btnExit = ttk.Button(raiz, text='Salir', command=sys.exit)

btnSplit.grid(column=0,row=1, padx=25, pady=25)
btnExit.grid(column=1,row=1, padx=25, pady=25)


combo = ttk.Combobox()
combo.grid(column=0,row=0, padx=25, pady=25,columnspan= 2)
combo["values"] = files
combo.bind("<<ComboboxSelected>>", selection_changed)
        
    

raiz.mainloop()




