import re

randstr = '''
Janice is 22 and Theon is 33
Gabriel is 44 and Joey is 21
'''

print(randstr)

regex = re.compile("\n")

randstr = regex.sub(" ",randstr)

print(randstr)
