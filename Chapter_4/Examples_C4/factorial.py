def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    num1 = 5
    print(f'{num1}! = {factorial(num1)}')
    num2 = 0
    print(f'{num2}! = {factorial(num2)}')