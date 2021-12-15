import re

email = '''
pooja@gmail.com
pooja.com
pooja.in.co
poo@gmail.com
'''

print(email)

print("Email matches:", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email)))
