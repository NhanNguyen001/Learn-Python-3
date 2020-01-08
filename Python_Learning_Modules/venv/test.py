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



from  random import shuffle
# print(random)
# help(random)
# print(dir(random.random))

# print(random.random())
# print(random.randint(1, 10))
# print(random.choice([1, 2, 3, 4, 5]))

my_list = [1, 2, 3, 4, 5]
shuffle(my_list)
print(my_list)