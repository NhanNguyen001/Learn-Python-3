# from utility import multiply, divide
# from shopping.more_shopping import shopping_cart
#
# # Make sure that if this is the file that's being run
# # because a file can be either run or it can be imported if this is the file that
# # gets run it's the main file then do something
# if __name__ == '__main__':
#     print(multiply(2, 3))
#     print(divide(6, 2))
#     print(shopping_cart.buy('apple'))
#
#     print('please run this')



# from  random import shuffle
# print(random)
# help(random)
# print(dir(random.random))

# print(random.random())
# print(random.randint(1, 10))
# print(random.choice([1, 2, 3, 4, 5]))

# my_list = [1, 2, 3, 4, 5]
# shuffle(my_list)
# print(my_list)

# import sys

# first = sys.argv[1]
# last = sys.argv[2]
# print(f'hiii! {first} {last}')


# from random import randint
# import sys
# # Generator a number 1~10
# answer = randint(int(sys.argv[1]), int(sys.argv[2]))
#
# # get input from user
#
# # check that input is a number 1~10
# while True:
#     try:
#         print(answer)
#         guess = int(input('guess a number 1~10: '))
#
#         if 0 < guess < 11:
#             if guess == answer:
#                 print('you are a genious')
#                 break
#         else:
#             print('hey bozo, I said 1~10')
#     except ValueError:
#         print('Please enter a number')
#         continue

# check if number is the right guess. Otherwise
# ask again.


import pyjokes

print(pyjokes.get_joke('en', 'neutral'))