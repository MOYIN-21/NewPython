def intersection_num(list1, list2):
    # intersection = []

    # for element in list1:
    #     for elements in list2:
    #         if elements == element:
    #             intersection += [element]
    element = {elements for elements in list1 if elements in list2}

    return tuple(element)


if __name__ == "__main__":

    list1 = [30, 20, 30, 60, 65, 100, 10, 75, 100]
    list2 = [42, 30, 80, 65, 75, 88, 95, 10, 100]
    print(intersection_num(list1, list2))




