# defining a generator
def generator():
    x = 0
    while x <= 5:
        yield x
        x += 1

# yielding values directly into a list
mylist = list(generator())

# use for loop to print mylist items
for x in mylist:
    print(x)