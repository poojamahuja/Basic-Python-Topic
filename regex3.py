import re

str = "Sat, hat, mat, pat, cat"
allstr = re.findall("[Shmpc]at", str)
for i in allstr:
	print(i)