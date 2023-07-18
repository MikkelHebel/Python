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