import re

food = "hat rat mat pat cat sat"

regex = re.compile("[r]at")

food = regex.sub('food',food)

print(food)