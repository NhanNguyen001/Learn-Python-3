# import pyjokes
#
# joke = pyjokes.get_joke('en', 'neutral')
# print(joke)

# my_file = open('test.log')

# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())

# print(my_file.readlines())
#
# my_file.close()

# with open('test.log', mode='w') as my_file:
#     text = my_file.write(':)')
#     print(text)
    # print(my_file.readlines())

with open('test1.log', mode='r+') as my_file:
    text = my_file.write(':))')
    print(text)
    # print(my_file.readlines())
