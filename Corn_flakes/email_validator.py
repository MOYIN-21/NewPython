import re
import time


def email_validator():
    valid = []
    counter = 0

    while counter < 5:
        email = input("Enter your email: ")
        if email.startswith(".com") or email.endswith("@"):
            print("Wrong input")

        elif email.startswith(".it"):
            print("wrong input")

        elif email.startswith(".africa"):
            print("wrong input")

        elif re.match(r"[^@]+@[^@]+\.[^@]+", email):
            valid.append(email)
            counter += 1
            save()

        elif email.endswith(".com"):
            valid.append(email)
            counter += 1
            save()

        elif email.endswith(".it"):
            valid.append(email)
            counter += 1
            save()

        elif email.endswith(".africa"):
            valid.append(email)
            counter += 1
            save()

    return valid


def save():
    print("saving", end="")
    time.sleep(.5)

    print("\nPassword saved successfully")


if __name__ == "__main__":
    validate = email_validator()

print("validate E-mail : ", validate)
