import re

str = "we need to inform him with information"

for i in re.finditer('inform',str):
	loctup = i.span()
	print(loctup)

