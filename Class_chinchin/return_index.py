def sum(lists, value):
    for index, val in enumerate(lists):
        for index2, val2 in enumerate(lists):
            print(val, index)
            print(val2, index2)


if __name__ == "__main__":
    l1 = [5, 4, 9, 7, 2, 0]
    sum(l1, 12)
