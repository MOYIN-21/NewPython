def is_palindrome(string):
    if string == string[:: -1]:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")


is_palindrome("mmm")



