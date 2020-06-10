import os
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 350, bg = 'gray90', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Type Package:', bg = 'gray90')
label1.config(font=('helvetica', 14))
canvas1.create_window(150, 80, window=label1)

entry1 = tk.Entry (root, width=27)
canvas1.create_window(150, 120, window=entry1)

def installPackage ():
    global installPythonPackage
    installPythonPackage = 'pip install ' + entry1.get()
    
    os.system('start cmd /k ' + installPythonPackage)


def uninstallPackage ():
    global uninstallPythonPackage
    uninstallPythonPackage = 'pip uninstall ' + entry1.get()
    
    os.system('start cmd /k ' + uninstallPythonPackage)

    
button1 = tk.Button(text='      Install Package    ', command=installPackage, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=button1)


button2 = tk.Button(text='   Uninstall Package  ', command=uninstallPackage, bg='coral3', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=button2)

root.mainloop()