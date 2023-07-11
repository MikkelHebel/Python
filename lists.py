animals = ['cat', 'rat', 'bat', 'elephant', 'horse']
print(animals[0:3])


lists = ['cat', 'dog'], [10, 20, 30, 40, 50, 100]
print(lists[0][1])
# Print 50
print(lists[1][4])

# Setting new value in list
lists[1][4] = 500
# Print 500
print(lists[1][4])


# Get last line in list 2
print(lists[1][-1])



# Grab all the values from the beginning to value 10
numberList = [10, 20, 30, 40, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
print(numberList[:10])


# Check for word in list
if 'heyas' in ['hello', 'test', 'world', 'heyas']:
    print('Found it!')


# List of suppliesg
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])