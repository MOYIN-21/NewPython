# Input three different floating-point numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

minimum = min(num1, num2, num3)
maximum = max(num1, num2, num3)
middle = num1 + num2 + num3 - minimum - maximum

print("Numbers in increasing order:", minimum, middle, maximum)
