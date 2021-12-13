file1 = open("example.txt", "r")
file2 = open("duplicate.txt", "w")
l = file1.readline()
while l:
	file2.write(l)
	l = file1.readline()
file1.close()
file2.close()