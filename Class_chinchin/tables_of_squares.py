print("{:^10s}{:^10s}{:^10s}".format("Number", "Square", "Cube"))
for num in range(6):
    square = num ** 2
    cube = num ** 3
    print("{:^10d}{:^10d}{:^10d}".format(num, square, cube))
