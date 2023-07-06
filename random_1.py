import random
import pyperclip
# random.randint(1, 10)

def hello():
    print('Hello this program will generate a random number and copy it to your clipboard.')

def myFunction(range1, range2):
    range1 = int(input('Enter the first number: '))
    range2 = int(input('Enter the second number: '))

    result = random.randint(range1, range2)
    print(result)
    pyperclip.copy(result)

hello()
myFunction(1, 10)