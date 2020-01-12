letters = ['a', 'b', 'c', 'd']
matrix = [[0, 1], [2, 3]]
zeros = [0] * 100
combined = zeros + letters
# numbers = list(range(20))
# chars = list('Hello World')
# print(combined)
# print(numbers)
# print(chars)

# Accessing List
# print(letters[0:3])
# print(letters[:3])
# print(letters[0:])
# print(letters[1::2 ])
# print(numbers[::-1])


### List Unpacking
# numbers = [1, 2, 3, 4, 5, 96]
# first, second, third = numbers
# first, second, *other = numbers
# first, *other, last = numbers
# print(first)
# print(second)
# print(third)
# print(other)
# print(last)


### Looping over Lists
# for index, letter in enumerate(letters):
#     print(index, letter)


### Adding or Removing Items
letters = ['a', 'b', 'a', 'b', 'c']

### Add
# letters.append('d')
# letters.insert(0, '-')
# print(letters)

### Remove
# letters.pop()
# letters.pop(0)
# letters.remove('b')
# del letters[0:3]
# letters.clear()
# print(letters)


### Finding
# print(letters.count('a'))
# if 'd' in letters:
    # print(letters.index('d'))

### Sorting
numbers = [2, 51, 2, 8, 6]
# numbers.sort(reverse=True)
#newSotedList = sorted(numbers, reverse=True) # return a new list
# print(numbers)
# print(newSotedList)
items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12),
]

def sort_item(item):
    return item[1]

items.sort(key=lambda item:item[1], reverse=True)
# print(items)



### Map functions
items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12),
]

# The old implement
# prices = []
# for item in items:
#     prices.append(item[1])

prices = list(map(lambda item: item[1], items))
# for item in newItems:
#     print(item)

# print(prices)


### Filter functions
items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12),
]
filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered)



### List Comprehensions
items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12),
]

# [expression for item in items]
prices = [item[1] for item in items]
# print(prices)

filtered = [item for item in items if item[1] >= 10]
# print(filtered)




### Zip function
list1 = [ 1, 2, 3 ]
list2 = [10, 20, 30]

# [(1, 10), (2, 20), (3, 30)]
# print(list(zip('abc', list1, list2)))


list2 = []
if False:
    print('true')