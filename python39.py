import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore randomtext\nAnd some more")

with open("mydata.txt", encoding="utf-8") as myFile:

    print(myFile.read())

# print(myFile.closed)
# print(myFile.name)
# print(myFile.mode)
# os.rename("mydata.txt", "mydata2.txt")

print("Current directory : ", os.getcwd())
