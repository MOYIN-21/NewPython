number = int(input("Enter five digit: "))
num1 = number // 10000
num2 = (number % 10000) // 1000
num3 = (number % 1000) // 100
num4 = (number % 100) // 10

num4 = number % 10
print(num1, num2, num3, num4)
palindrome = (num1 == num4) and (num2 == num3)

if palindrome:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")