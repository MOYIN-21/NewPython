import datetime
import re

storeName = "SEMICOLON STORES"

Branch = "MAIN BRANCH"
Address: "312, HERBERT MACAULAY WAY, SABO YABA, LAGOS STATE."
contact = "03293828343"
DateTime = datetime.datetime.now()
cashierName = " "
customerName = " "
product = []
quantityPurchase = []
price = []
total = []
discount = 0
AmountPaid = 0
bill_total = 0
vat = 0
balance = 0
subTotal = 0


def name():
    global customerName
    user = input("What is the customers name: ")
    if re.search("^(?!$)\D+$", user):
        customerName = user
        userBuy()
    else:
        print("invalid input")
        name()


def userBuy():
    global product
    keyboard = input("What did the user buy?: ")
    if re.search("^(?!$)\D+$", keyboard):
        product.append()
        pieces()
    else:
        print("invalid input")
        userBuy()


def pieces():
    global quantityPurchase
    num = int(input("How many pieces?: "))
    if num.isdigit():
        quantityPurchase.append()
        unit()
    else:
        input("invalid input")
        pieces()


def unit():
    global price
    amount = float(input("How much per unit?: "))
    if amount.isdigit():
        price.append()
        item()
    else:
        print("invalid input: ")
        unit()


def item():
    global discount
    response = float(input("\nAdd more items?" + "\nYes or No?"))
    if re.search("^(?!$)\D+$", response):
        if response.casefold() == "yes":
            userBuy()
        if response.casefold() == "no":
            cashierNameEntry()
        else:
            print("\ninvalid input")
            item()


def cashierNameEntry():
    global cashierName
    person = input("What is your name? ")
    if re.search("^(?!$)\D+$", person):
        cashierName = person
        discountInput()
    else:
        print("Invalid input")
        cashierNameEntry()


def discountInput():
    global discount
    pricecut = float(input("How much discount will he get?: "))
    if pricecut.isdigit() and int(pricecut) <= 10:
        discount = int(pricecut)
        storeInfo()
    else:
        print("Discount maximum is 10% ")
        discountInput()


def storeInfo():
    global cashierName
    global customerName

    print(
        f"\n{storeName}\n{Branch}\nLocation : {Address}\nTel : {contact}\nDate : {datetime}\nCashier : {cashierName}\nCustomer Name : {customerName}")
    storeReceipt()


def storeReceipt():
    global discount
    global total

    print(f"""\n{"=" * 50}\n\tITEM\tQTY\t\tPRICE\t\tTOTAL(NGN)\n{"-" * 50}""")

    num = 0
    subtotal = 0.0

    for index in range(len(product)):
        num = quantityPurchase[index] * price[index]
        total.append(num)

    subtotal += num
    for index in range(len(product)):
        print(f"""
        {product[index]:<10}{quantityPurchase[index]:<10}{price[index]:<14.2f}{total[index]:<14.2f}
        """)
        discount_t = subtotal * (discountInput / 100)
        discount = discount_t
        vaty = subtotal * 0.175
        vat = vaty
        billy = subtotal + vat - discount_t
        billTotal = billy
        balanced = AmountPaid - billTotal
        balance = balanced


# print("""
#     "-" * 60,"\n\t\t\t\tSub Total:",total,"\n\n\t\t\t\t Discount:",discount,"\n\n\t\t\t\t VAT @17.50:" vat,"\n",
#     ""=" * 60"\n\t\t\t\t Bill Total:", {bill_total:.2f}\n\n\t\t\t\tAmount Paid: { AmountPaid:.2f}\n\n\t\t\t\tBalance:{
#     balance:.2f}\n"=" * 60\n THANK YOU FOR YOUR PATRONAGE\n{"=" * 60}
#      """)
# print(bill_total)
# print(discount)
# print(vat)
# print(balance)
# # print("=" * 60)


if __name__ == "__main__":
    print(name())
