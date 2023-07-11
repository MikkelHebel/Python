myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])

spam = {12345: 'Luggage Combination', 42: 'The Answer'}
print(spam[42])


eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'name': 'Zophie', 'age': '8'}

print('Eggs keys:')
print(list(eggs.keys()))
print('Eggs values:')
print(list(eggs.values()))

if 'cat' in eggs.values():
    print('Cat found in eggs!!1')


picnicItems = {'apples': 5, 'cups': 2, 'plates': 3, 'cookies': 8000}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
print('I am bringing ' + str(picnicItems.get('cookies', 0)) + ' cookies :3')