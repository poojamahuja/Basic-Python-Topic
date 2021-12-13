# Reading & writing text file

with open("example.txt") as f:
    for line in f:
    # will print all the lines one by one
         print (line)


myFile = open("example.txt","w+")

content = "Hello, World. I am learning Python"
fileline = myFile.write(content)

