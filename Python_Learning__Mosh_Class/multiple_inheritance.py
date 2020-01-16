class Employee:
    def great(self):
        print('Employee Greet')


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class Person:
    def greet(self):
        print('Person Greet')


class FlyingFish(Flyer, Swimmer):
    pass

# Employee first


class Manager(Employee, Person):
    pass


m = Manager()
m.great()
