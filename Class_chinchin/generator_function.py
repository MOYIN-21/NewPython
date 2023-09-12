
def big_list(num: int):
    double = []
    for i in range(num):
        double.append(i * 2)
    return double


print(big_list(5))


#
#   def generator_func(100):
#       for c in g:
#       pass
#
#
#
def generator_func(n):
    for i in range(n):
        yield i


print(generator_func(10))
#
x = [i for i in range(10) if i % 2 == 0]
print(x)


print()

