def filename():
    user = input("Enter filename")
    if user.endswith(".java"):
        print("java")
    else:
        print(filename())


if __name__ == "__main__":
    filename()
