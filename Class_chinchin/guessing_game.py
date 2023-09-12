# numb = 5


def num(you):
    # num = int(input("Enter any number: "))
# for num in range (1,10):
    if you == 5:
        print("):...You have won!!!")
    elif you > 0 and you < 5:
        print("Too low,try again")
        num()
    else :
        # you > 5 and you <= 10:
        print("Too high, try again")
        num()

num(8)


