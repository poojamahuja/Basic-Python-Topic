import re

name = "Ahuja Pooja"

if re.search("\w{2,20}\s\w{2,20}", name):
	print("it is a valid name")
else:
	print("not a valid name")