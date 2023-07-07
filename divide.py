def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Error: Invalid argument.')



print(divide(1, 10))
print(divide(3, 0))
print(divide(5, 32))
print(divide(1, 1234))