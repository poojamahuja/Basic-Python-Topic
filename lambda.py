def transform(n):
    return lambda x: x + n
f = transform(3)
print(f(4))