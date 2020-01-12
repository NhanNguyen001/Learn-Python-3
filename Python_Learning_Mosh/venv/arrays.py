# take less memory than list and perform a little bit faster
from array import array

numbers = array("i", [1, 2, 3])
# numbers.append(4.4)
print(numbers[0])