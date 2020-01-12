# Genertor object is an iterable we can iterate
# over them and in each iteration they spit out a new value
from sys import getsizeof

values = (x * 2 for x in range(1000000))
print('gen:', getsizeof(values))

values2 = [x * 2 for x in range(1000000)]
print('gen:', getsizeof(values2))
# print(values)
# for x in values:
#     print(x)



