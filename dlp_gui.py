import tkinter
import re
import docx
import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *

window = tkinter.Tk()
window.title("GUI")
window.geometry("500x500")
sensitive_files  = []

def cfor_ssn(tmp_line):
    f=re.findall(r'(\d{3}-\d{2}-\d{4})',tmp_line)
    return f

def cfor_cc(tmp_line):
    f=re.findall(r'(\d{4}-\d{4}-\d{4}-\d{4})',tmp_line)
    return f

#folder = 'c:\\users\\tony'

def folder_select():
    global folder
    root = Tk()
    root.withdraw()
    folder = filedialog.askdirectory()
    if folder == "":
        tkinter.Label(window, text = "Please choose a folder").pack()
    else:
        tkinter.Label(window, text = folder).pack()

tkinter.Button(window, text = "Browse", command = folder_select, width = 10).pack()




# creating a function called say_hi()
def say_hi():
    for filename in os.listdir(folder):
        global sensitive_files
        absolute = folder + '\\' + filename
        if "docx" in filename:
            try:
                doc = docx.Document(absolute)
                for line in doc.paragraphs:
                    ssn_list=cfor_ssn(line.text)
                    cc_list=cfor_cc(line.text)

                    if len(ssn_list) != 0 or len(cc_list) != 0:
                        sensitive_files.append(absolute)
            except:
                print("Can't Read " + folder)

        elif "txt" in filename:
            absolute = folder + '\\' + filename
            try:
                with open(absolute,"r") as fh:
                    for line in fh.readlines():
                        ssn_list = cfor_ssn(line)
                        cc_list = cfor_cc(line)

                        if len(ssn_list) != 0 or len(cc_list) != 0:
                            sensitive_files.append(absolute)
            except:
                print(filename + " Could not be read")
    output = Text(window, width=50, height=10, background="light grey")
    for sensitive_file in sensitive_files:
        print(sensitive_file)
        output.insert(END, sensitive_file + "\n")
    output.pack()

tkinter.Button(window, text = "Click Me!", command = say_hi).pack() # 'command' is executed when you click the button
                                                                    # in this above case we're calling the function 'say_hi'.

window.mainloop()

