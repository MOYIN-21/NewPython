# try:
#     num1, num2 = eval(input("Enter two number seperated by a comma: "))
#     result = num1 * num2
#     print(result)
# except SyntaxError:
#     print("Enter a comma seperated numbers")
# except ZeroDivisionError:
#     print("numbers can not be multiplied by Zero")
# else:
#     print("Successful")
# finally:
#     print("Trust MOYINOLUWA Calculator")
#
#
# def number(num1, num2):
#     try:
#         # num1, num2 = eval(input("Enter two number seperated by a comma: "))
#         result = num1 + num2
#         print(result)
#     except SyntaxError:
#         print("Enter a comma seperated numbers")
#     except ZeroDivisionError:
#         print("You can not divide by Zero")
#     else:
#         print("Successful")
#     finally:
#         print("In God we trust")
#
#
# number(32, 2)

while True:
    try:
        num1, num2 = eval(input("Enter two number seperated by a comma: "))
        result = num1 / num2
        print(result)
    except SyntaxError:
        print("Enter a comma seperated numbers")
    except ZeroDivisionError:
        print("You can not be divided by Zero, try again")
    except TypeError:
        print("Enter two numbers seperated by comma ")
    except NameError:
        print("IDIOT!!! Enter two correct input")
    # except NameError:
        print("name" + " " + num1 + " " + num2 + " " + "is not defined")
    else:
        print("Successful")
        break
    finally:
        print("We love you")

    # from Class_chinchin import Dictionary
    # Dictionary.accounts()
