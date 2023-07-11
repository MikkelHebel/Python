# Convert hello to a list
print(list('Hello'))


name = 'Zophie'
print(name[1:5])


# Create new variable from name
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(newName)



import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42

print(spam)
print(cheese)