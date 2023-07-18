print('Hello there!\nHow are you?\nI\'m doing fine.')

print(r'That is Carol\'s cat.')

# Multiline strings with triple quotes
print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')



# isalpha() - letters only
# isalnum() - letters and numbers only
# isdecimal() - numbers only
# isspace() - whitespace only
# istitle() - titlecase only

print('hello'.isalpha())
print('hello123'.isalnum())
print('123'.isdecimal())
print('   '.isspace())
print('Hello World'.isspace())
print('Hello World'[5].isspace())
# All words have to start with a capital letter for istitle to be true
print('This Is Title Case'.istitle())



# startswith() and endswith()
print('Hello world'.startswith('Hello'))
print('Hello world'.endswith('Hello'))
print('Hello world'.endswith('world'))



# join() and split()
# Join will join a list of strings together
print(', '.join(['cats', 'rats', 'bats']))
# Split will split a string into a list of strings
print('My name is Simon'.split())
print('MyABCnameABCisABCSimon'.split('ABC'))
print('My name is Simon'.split('m'))



# rjust(), ljust(), and center()
# rjust() and ljust() will add spaces to the left or right of a string
# center() will add spaces to the left and right of a string
print('Hello'.rjust(10))
print('Hello'.rjust(20))
print('Hello World'.rjust(20))
print('Hello'.ljust(10))
print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))
print('Hello'.center(20))
print('Hello'.center(20, '='))



# strip(), rstrip(), and lstrip()
# strip() will remove whitespace from the left and right of a string
# rstrip() will remove whitespace from the right of a string
# lstrip() will remove whitespace from the left of a string
spam = '    Hello World     '
# Remove whitespace
print(spam.strip())
# Remove whitespace on the left
print(spam.lstrip())
# Remove whitespace on the right
print(spam.rstrip())



# Remove all instances of a character
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))



# Replace all instances of a character
spam = 'Hello there!'
print(spam.replace('e', 'XYZ'))



# Combine multiple strings
variable = 'cats' + 'dogs'
print(variable)


# Invitation
name = 'Alice'
place = 'Main Street'
time = '6 pm'
food = 'turnips'
print('Hello ' + name + ', you are invited to a party at ' + place + ' at ' + time + '. Please bring ' + food + '.')
print('Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (name, place, time, food))