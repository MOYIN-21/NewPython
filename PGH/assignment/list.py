def alternate_elements(input_list):
    result_list = input_list[::2]
    return result_list


input_list = ['a', 'b', 'c', 'd', 'e']
output = alternate_elements(input_list)
print(output)

# 1. Write a Python function that takes a list as input and returns a new list containing alternate elements using slicing.
# print(alternate_elements([1, 2, 3, 4, 5, 6]))      # Output: [1, 3, 5]
# print(alternate_elements(['a', 'b', 'c', 'd', 'e']))  # Output: ['a', 'c', 'e']

# 2. Write a Python function that takes a list and an integer k as input and performs a circular right shift of the list by k positions using slicing.
# print(circular_shift([1, 2, 3, 4, 5], 2))    # Output: [4, 5, 1, 2, 3]
# print(circular_shift(['a', 'b', 'c', 'd'], 1))  # Output: ['d', 'a', 'b', 'c']
