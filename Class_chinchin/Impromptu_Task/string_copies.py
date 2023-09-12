
def integer():
    user = input("Enter a word")
    user2 = int(input("Enter a number"))
    print(user * user2)
    if user < '2':
        print(user * 10)


if __name__=="__main__":
    integer()