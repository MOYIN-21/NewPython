price = 0
vat = 0


def vat():
    global price
    global vat
    while True:
        try:
            price_of_item = eval(input("Enter the price of an item"))
            if not price_of_item.isdigit():
                print("Enter amount in digit")
                continue
            elif price_of_item < 0:
                print("Amount less than 0 is not allowed")
                continue

            var = float(input("Enter value added tax"))
            if not price_of_item.isdigit():
                print("not a digit")
                continue
            elif var <= 0:
                print("Amount less than 0 is not allowed ")
                continue
            else:
                price = float(price_of_item)
                vat = float(var)
                your_vat()
        except SyntaxError:
            print("Invalid decimal literal")
        except NameError:
            print("input is not defined")


def your_vat():
    global price
    global vat
    price_calulation = price / 100 * vat
    total = vat + price_calulation
    return price(total)


if __name__ == "__main__":
    vat()
