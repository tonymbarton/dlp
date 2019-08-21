import re
import docx
import os

def cfor_ssn(tmp_line):
    f=re.findall(r'(\d{3}-\d{2}-\d{4})',tmp_line)
    return f

def cfor_cc(tmp_line):
    f=re.findall(r'(\d{4}-\d{4}-\d{4}-\d{4})',tmp_line)
    return f

folder = input("Folder: ")

for filename in os.listdir(folder):
    absolute = folder + '\\' + filename
    if "docx" in filename:
        try:
            doc = docx.Document(absolute)
            for line in doc.paragraphs:
                ssn_list=cfor_ssn(line.text)
                cc_list=cfor_cc(line.text)

                if len(ssn_list) != 0 or len(cc_list) != 0:
                    print(absolute)
                    print(cc_list)
                    print(ssn_list)
        except:
            print("Can't Read " + absolute)

    elif "txt" in filename:
        absolute = folder + '\\' + filename
        try:
            with open(absolute,"r") as fh:
                for line in fh.readlines():
                    ssn_list = cfor_ssn(line)
                    cc_list = cfor_cc(line)

                    if len(ssn_list) != 0:
                            print("----Filename----")
                            print(filename)
                            print("----Line Found In----")
                            print(line)
                            print("----Data Found----")
                            print(ssn_list)
                            print("\n")
                    elif len(cc_list) != 0:
                            print(filename)
                            print(cc_list)
                            print("\n")
        except:
            print(filename + " Could not be read")

#file = input("File: ")
