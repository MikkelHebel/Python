print('How many cats do you have?')
numcats = input()
try:
    if int(numcats) >= 4:
        print('That is a lot of cats.')
    elif int(numcats) < 0:
        print('You cannot have negative cats.')
    else:
        print('That is not that many cats.')    
except ValueError:
    print('You did not enter a number.')