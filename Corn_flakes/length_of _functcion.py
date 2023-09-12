def calculate_size(collection):
    size = 0
    for item in collection:
        size += 1
    return size


def main():
    my_list = [1, 2, 3, 4, 5]
    size = calculate_size(my_list)
    print("Size of the collection:", size)


if __name__ == "__main__":
    main()
