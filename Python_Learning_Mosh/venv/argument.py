### Positional argument
# def greet(first_name, last_name):
#     print(f'Hi {first_name} {last_name}')
#     print('Welcome aboard')
#
# greet('Mosh', 'Hamedani')


### Keywords Arguments
# def increment(number, by):
#     return number + by
#
# result = increment(2, by=1)
# print(result)


### Default Arguments
# def increment(number, by=5):
# #     return number + by
# #
# # result = increment(2)
# # print(result)



### *args
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total
#
# print(multiply(2, 3, 4, 5))

### **args
# def save_user(**user):
#     print(user)
# 
# save_user(id=1, name="John", age=22)
