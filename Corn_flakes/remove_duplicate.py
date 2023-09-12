def check_duplicate(word):
    dup = [i for i in word if word.count(i) > 1]
    return dup[0]


print(check_duplicate(["james", "paul", "moyin", "moyin", "precious", "Dorcas"]))
