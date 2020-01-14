class Point:
    # Class Object attribute
    default_color = 'red'

    # Instance method
    def __init__(self, x, y):
        # Instance attribute
        self.x = x
        self.y = y

    # Instance method
    def draw(self):
        print(f'Point ({self.x}, {self.y})')

    @classmethod
    def zero(cls):
        return cls(0, 0)

# Point.default_color = 'yellow'

# point = Point(1, 2)
# print(point.default_color)
# print(Point.default_color)
# point.draw()
#
# another = Point(3, 4)
# print(another.default_color)
# another.draw()

point = Point.zero()
point.draw()