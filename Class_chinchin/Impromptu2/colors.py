def color(color_list_1, color_list_2):
    element = {elements for elements in color_list_1 if elements not in color_list_2}
    return tuple(element)


if __name__ == "__main__":
    color_list_1 = (["White", "Black", "Red"])
    color_list_2 = (["Red", "Green"])
    print(color(color_list_1, color_list_2))
