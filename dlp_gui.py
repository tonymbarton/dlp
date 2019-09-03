import tkinter
import re
import docx
import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *

window = tkinter.Tk()
window.title("GUI")
window.geometry("700x700")
sensitive_files  = []

def cfor_ssn(tmp_line):
    f=re.findall(r'(\d{3}-\d{2}-\d{4})',tmp_line)
    return f

def cfor_cc(tmp_line):
    f=re.findall(r'(\d{4}\s\d{4}\s\d{4}\s\d{4})',tmp_line)
    return f

def cfor_password(tmp_line):
    f=re.findall('Password',tmp_line)
    return f

def cfor_email(tmp_line):
    f=re.findall(r'[\w\.-]+@[\w\.]+',tmp_line)
    return f

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




# creating a function called scan()
def scan():
    try:
        for root, dirs, files in os.walk(folder):
            for file in files:
                global sensitive_files
                absolute = os.path.join(root,file)
                print(absolute)
                if "docx" in file:
                    try:
                        doc = docx.Document(absolute)
                        for line in doc.paragraphs:
                            ssn_list=cfor_ssn(line.text)
                            ssn = ''.join(str(e) for e in ssn_list)
                            cc_list=cfor_cc(line.text)
                            cc = ''.join(str(e) for e in cc_list)
                            password_list=cfor_password(line.text)
                            password = ''.join(str(e) for e in password_list)
                            email_list=cfor_email(line.text)
                            email = ''.join(str(e) for e in email_list)

                            if len(ssn_list) != 0:
                                sensitive_files.append(absolute + " " + ssn)
                            elif len(cc_list) != 0:
                                sensitive_files.append(absolute + " " + cc)
                            elif len(password_list) != 0:
                                sensitive_files.append(absolute + " " + password)
                            elif len(email_list) != 0:
                                sensitive_files.append(absolute + " " + email)
                    except:
                        print(file + " Could not be read")

                elif "txt" in file:
                    absolute = os.path.join(root,file)
                    try:
                        with open(absolute,"r") as fh:
                            for line in fh.readlines():
                                ssn_list = cfor_ssn(line)
                                ssn = ''.join(str(e) for e in ssn_list)
                                cc_list = cfor_cc(line)
                                cc = ''.join(str(e) for e in cc_list)
                                password_list=cfor_password(line)
                                password = ''.join(str(e) for e in password_list)
                                email_list=cfor_email(line)
                                email = ''.join(str(e) for e in email_list)

                                if len(ssn_list) != 0:
                                    sensitive_files.append(absolute + " " + ssn)
                                elif len(cc_list) != 0:
                                    sensitive_files.append(absolute + " " + cc)
                                elif len(password_list) != 0:
                                    sensitive_files.append(absolute + " " + password)
                                elif len(email_list) != 0:
                                    sensitive_files.append(absolute + " " + email)
                    except:
                        print(file + " Could not be read")
        output = Text(window, width=80, height=10, background="light grey")
        for sensitive_file in sensitive_files:
            output.insert(END, sensitive_file + "\n")
        output.pack()
        if folder == "":
            messagebox.showerror("Error", "You must select a folder")
    except:
        messagebox.showerror("Error", "Something went wrong... Please try again!")

tkinter.Button(window, text = "Scan", command = scan).pack() # 'command' is executed when you click the button
                                                                    # in this above case we're calling the function 'say_hi'.

window.mainloop()

