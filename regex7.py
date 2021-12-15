import re

randstr = "1234560000"

print("Matches:", len(re.findall("\d",randstr)))


num = "123 1234 12345 123456 1234567"

print("Matches:", len(re.findall("\d{5,7}", num)))