numbers = [1, 2, 3]
print(*numbers)

values = list(range(5))
values = [*range(5), *'Hello']
print(values)

first = [1, 2]
second = [3]
valuesNew = [*first, 'a', *second, *'Hello']
print(valuesNew)

firstDic = {'x': 1}
secondDic = {'x': 10, 'y': 2}
combined = {**firstDic, **secondDic, 'z': 1}
print(combined)