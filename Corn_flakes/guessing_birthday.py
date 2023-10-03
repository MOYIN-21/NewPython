# def set1():
set1 = ("""
            1 3 5 7
            9 11 13 15
            17 19 21 23
            25 27 29 31 """)

def set2():
    print("Is your birthday in set1?\n")
    print(""" 
                    2 3 6 7
                    10 11 14 15
                    16 19 22 23
                    18 26 27 30 31""")

def set3():
    print("Is your birthday in set1?\n")

    print("""4 5 6 7
            12 13 14 15
            20 21 22 23
            28 29 30 31 """)


def set4():
    input(""" 8 9 10 11
            12 13 14 15
            24 25 26 27
            28 29 30 31""")


def set5():
    print("""16 17 18 19
            20 21 22 23
            24 25 26 27
            28 29 30 31 """)
    day = 0

    input = eval(input("Is your number in set1?\n"))
    print(set1())
    print("\nEnter 0 for No and 1 for yes: ")
    ans = input
    if ans == 1:
        day += 1

    input = eval(input("Is your number in set1?\n"))
    set1()
    print("\nEnter 0 for No and 1 for yes: ")
    ans = input
    if ans == 1:
        day += 1

    input = eval(input("Is your number in set1?\n"))
    set1()
    print("\nEnter 0 for No and 1 for yes: ")
    ans = input
    if ans == 1:
        day += 1

    input = eval(input("Is your number in set1?\n"))
    set1()
    print("\nEnter 0 for No and 1 for yes: ")
    ans = input
    if ans == 1:
        day += 1


def response():
    print("\nEnter 0 for No and 1 for yes: ")

print(set1())