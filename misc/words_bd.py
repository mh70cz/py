with open(r"c:\temp\Czech.3-2-5.dic_utf8.txt  ", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines[:]:
    if "j" in line and "i" in line and "h" in line and len(line) < 8:
        print(line)


#      c:\temp\Czech.3-2-5.dic_utf8.txt  