# Introduction to Strings
mystring = "This is not my first string"
print (mystring)

# accessing string characters
# 0 to start from front
print (mystring[0]);

# -1 to strart from end
print (mystring[-1]);

# 4th character from start 0..1..2..3(this is the 4th)
print (mystring[5]);

# 4th character from end -1..-2..-3..-4(this is the 4th)
print (mystring[-4]);


# String Slicing
str = "TCSion Python Test"
print (str[1:18:2])

# You can use String slicing to accomplish
# amazing tasks. You just have to be a little clever

# we can even provide only the start and end
newStr = "Studytonight"
print (newStr[5:12])