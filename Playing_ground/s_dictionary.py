def count_names_with_first_letter(names):
    if not names:
        return {}

    first_letter = names[0][0]
    names_starting_with_first_letter = [name for name in names if name[0] == first_letter]

    name_count = {}
    for name in names_starting_with_first_letter:
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1

    return name_count


# Example list of names
name_list = ["Segun", "Bob", "Anna", "Bella", "Alex", "Segun", "Abby", "Brad", "Seyi"]

result = count_names_with_first_letter(name_list)
