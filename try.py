lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
 
    lst.append(ele) # adding the element
     
print(lst)

squaring_iterator = map(lambda n: n ** 2, lst)
squared_numbers = list(squaring_iterator)

print(squared_numbers)
