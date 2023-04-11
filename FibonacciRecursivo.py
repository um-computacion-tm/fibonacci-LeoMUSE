def fibonacciRecursivo(number):
    if number <= 1:
        return number
    return fibonacciRecursivo(number - 1) + fibonacciRecursivo(number - 2)

if __name__ == '__main__':
    pass