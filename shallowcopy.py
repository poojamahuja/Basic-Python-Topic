import copy

l1 = [1,3,[9,4],6,8]
l2 = copy.copy(l1) #Making a shallow copy

print('List 1 = ', l1)
print('List 2 = ', l2)

print('Performing change in list 2')
l2[2][0] = 5

print('List 1 = ',l1)
print('List 2 = ',l2)
