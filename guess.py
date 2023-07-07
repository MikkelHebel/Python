import random
print('Hello. This is a guessing game.')
print('Choose a difficulty: easy, medium, or hard.')
print('easy: 10 tries, medium: 5 tries, hard: 3 tries')
difficulty = input()
tries = 0
i = 0
guess = 0
number = random.randint(1, 100)


if difficulty == 'easy':
    tries = 10
elif difficulty == 'medium':
    tries = 5
elif difficulty == 'hard':
    tries = 3
else:
    print('Error: You did not enter a valid difficulty.')

print('Guess a number between 1 and 100.')
for i in range(tries):
    guess = int(input())

    if guess < number:
        print('Your guess is too low. You have ' + str(tries - i - 1) + ' tries left.')
    elif guess > number:
        print('Your guess is too high. You have ' + str(tries - i - 1) + ' tries left.')
    else:
        break

if guess == number:
    print('You guessed the number in ' + str(i + 1) + ' tries.')
else:
    print('The number was ' + str(number) + '.')