# try block
try:
    a = 10
    b = 0
    print("Result of Division: " + str(a/b))
    print("No! This line will not be executed.")
except:
    print("You have divided a number by zero, which is not allowed.")

# outside the try-except blocks
print("Yo! This line will be executed.")
