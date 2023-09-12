def divisor(num1, num2):
    if num1 & num2 % 2 == 0:
        print("The greatest common divisor is", 2)
    if num1 & num2 % 3 == 0:
        print("The greatest common divisor is", 2)
    if num1 & num2 % 5 == 0:
        print("The greatest common divisor is", 5)
    if num1 & num2 % 2 & 3 & 5 == 0:
        print("The greatest common divisor is", 2)
    else:
        print("):")


if __name__ == "__main__":
    print(divisor(4, 10))
