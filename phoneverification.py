import re

phn = "412-555-1212"

if re.search("\d{3}-\d{3}-\d{4}", phn):
	print("it is a valid phone number")
else:
	print("not a valid phone number")