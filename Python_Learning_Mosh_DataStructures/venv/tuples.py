# Is a read only list
# point = (1, 2) + (3, 4)
# point = (1, 2) * 3
# point = tuple([1, 2])
# point = tuple('Hello World')
point = (1, 2, 3)
point2 = (1, 2, 3)
print(id(point))
print(id(point2))
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
print(id(list1))
print(id(list2))
# print(point == point2)
# print(point[0:2])
# z, y, z = point
# if 10 in point:
#     print('exists')

# print(point)
# point[0] = 10
