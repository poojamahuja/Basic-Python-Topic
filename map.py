def square(n):
    return n ** 2
squares = map(square, range(1, 10, 2))  
squares
# returns map object
print(list(squares))