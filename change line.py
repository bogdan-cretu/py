#Script that allows you to replace a certain line in all the files in your folder that have the same extension.
import glob

for file_name in glob.glob("*.txt"):
    file = open(file_name,"r" )
    file.close()
    line = "Insert line number here"
    text = "Insert new text here"
    myFile = open(file_name, "r")
    list_of_lines = myFile.readlines()
    list_of_lines[line] = text + "\n"
    myFile = open(file_name, "w")
    myFile.writelines(list_of_lines)
    file.close()
