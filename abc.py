old_name = ""
new_name = ""

f = open(r"E:\PRASUN\KMCCS Website\Committee_Website\templates\index.html", "r")
f1 = open(r"E:\PRASUN\KMCCS Website\Committee_Website\templates\index2.html", "w")
# tags = ["src=\"", "href=\""]
tags = ["src=\""]
for line in f:
    edited = line
    for tag in tags:
        if tag in line:
            for word in line.split():
                if word.startswith(tag):
                    edited = line.replace(tag, tag + "{%static '")
                    edited = edited[:(line.index(tag) + len(tag))] + \
                        edited[(line.index(tag) + len(tag)):].replace("\"", "' %}\"")
    f1.write(edited)


