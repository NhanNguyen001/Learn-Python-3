class Dog():

    def __init__(self, bread):  # self keywork tell this method refer to itself
        self.bread = bread  # It's a attribute


myDog = Dog(bread='Lab')
otherDog = Dog(bread='Huskie')
print(myDog.bread)
