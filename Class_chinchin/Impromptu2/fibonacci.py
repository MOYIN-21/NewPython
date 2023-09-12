def fibonacci(number):
    start = 0
    stop = 1
    for m in range(number):
        print(start, end=", ")
        count = stop + start
        stop = start
        start = count


if __name__ == "__main__":
    fibonacci(11)
