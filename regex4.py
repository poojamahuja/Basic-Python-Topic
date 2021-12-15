import re

str = "Sat, hat, mat, pat, cat"
allstr = re.findall("[^h-m]at", str)
for i in allstr:
	print(i)