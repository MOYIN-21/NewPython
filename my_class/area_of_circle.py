import math


# def area(radius):
#     user = float(radius)
#     circle = 3.1428 * (user ** 2)
#     return circle


def area(radius):
    if type(radius) != int:
        raise TypeError("Type Value")
    if radius < 0:
        raise ValueError("Value Error")
    else:
        return math.pi * (radius ** 2)


print(area(4))
#
# if __name__ == "__main__":
#     print(area(20))
