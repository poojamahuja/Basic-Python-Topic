# try block
try:
    a = 10
    b = 2
    print("Result of Division: " + str(a/b))

# except block 
except(ZeroDivisionError):
    print("You have divided a number by zero, which is not allowed.")

# finally block
finally:
    print("Finally block is called!")
    