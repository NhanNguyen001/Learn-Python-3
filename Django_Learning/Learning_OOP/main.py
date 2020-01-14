# class Dog():
#     # Class object attribute
#     species = 'mammal'

#     def __init__(self, bread, name):  # self keywork tell this method refer to itself
#         self.bread = bread  # It's a attribute
#         self.name = name


# myDog = Dog(bread='Lab', name='Sammy')
# otherDog = Dog(bread='Huskie', name='Dean')
# print(myDog.bread)
# print(myDog.name)
# print(myDog.species)
# print(otherDog.species)


class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        # pi is an object level attribute
        return self.radius*self.radius*Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r


myc = Circle(3)
myc.set_radius(100)
print(myc.area())
