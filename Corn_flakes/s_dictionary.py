def check(word_list, letter):
    word_counts = {}

    for words in word_list:
        if words.casefold().startswith(letter):
            word = words.casefold()
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1

    return word_counts


if __name__ == "__main__":
    names = ["joe", "Daniel", "Seyi", "Kelvin", "Huhammed", "Hakimi", "Muhammed", "Hakimi", "Segun", "Ashly", "Seyi"]
    word_to_check = "s"
    result = check(names, word_to_check)
    print(result)
