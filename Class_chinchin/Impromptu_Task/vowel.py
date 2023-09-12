import re


def letter():
    user = str(input("Any letter"))
    if re.search('[aeiou]', user):
        print(user, "is a vowel")
    else:
        print(user, "user is a consonant")


if __name__ == "__main":
    print(letter())
