
myFile = open('example.txt','r+')
myFile.seek(5)
print(myFile.read())


myFile.tell()