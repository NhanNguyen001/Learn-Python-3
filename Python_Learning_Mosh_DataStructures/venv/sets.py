# collection no duplicate
# set is un-oder list
numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
second = {1, 2, 1}
second.add(5)
second.remove(5)
# print(len(second))
# print(uniques)
# print(second)

first = set(numbers)
second = {1, 5}
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)
