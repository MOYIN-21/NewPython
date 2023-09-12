import re
import time


def enter():
    user = input("Enter Password: ")
    conditions(user)


def conditions(user=None):
    if len(user) < 8:
        print("Password is too short")
        enter()
        return False
    elif not re.search("[A-Z]", user):
        print("Password must start with uppercase letter")
        enter()
        return False

    elif not re.search("[a-z]", user):
        print("Password must contain lowercase letters")
        enter()
        return False

    if not re.search("[0-9]", user):
        print("Password must should contain digit")
        enter()
        return False

    if not re.search("[#?!@$%^&*-]", user):
        print("KIndly include special characters")
        enter()
        return False
    else:
        password_validation(user)
        print("valid")
        save()


def save():
    print("saving", end="")
    time.sleep(0.3)

    print("\nPassword save succefully")


def password_validation(user=None):
    userM = input("\nKindly enter password again")

    while user != userM:
        print("Password did not match,please try again")
        enter()
        password_validation()


if __name__ == "__main__":
    enter()
