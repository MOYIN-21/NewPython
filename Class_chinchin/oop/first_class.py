# defining a class
class Point:

    # To define a constractor in a class
    def __init__(self, a, b):
        self.a = a
        self.b = b

        # draw is a instance method

    def draw(self):
        print("drawing...")
        return f"({self.a}, {self.b})"

    # To String
    def __str__(self):
        return f"({self.a}, {self.b})"

    #  instantiation of a class


p1 = Point(1, 5)
p2 = Point(5, 6)
print(p1.draw())
print(p1)
print(p2)
