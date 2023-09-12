def number():
    user = int(input("Enter any number: "))
    if user % 2 == 0:
        print("You are GREAT!!!")
    else:
        print("You are AWESOME")


if __name__ == "__main__":
    print(number())
