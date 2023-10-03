def sum(lists, value):
    for index, val in enumerate(lists):
        for index2, val2 in enumerate(lists):
            if index == index2:
                continue
            print(f'Value from outer loop = {val}, Index from outer loop = {index}' )
            print(f'Value from Inner loop = {val2}, Index from inner loop = {index2}' )
            print(f'Sum of outer loop + inner loop = {val + val2}')
            if val + val2 == value:
                print(f"{index} {index2}")
                return [index,index2]


if __name__ == "__main__":
    l1 = [5, 4, 9, 7, 2, 0]
    sum(l1, 12)
