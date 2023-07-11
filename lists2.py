list = ['hello', 'hi', 'howdy', 'heyas']

# Returns index of value 'hello'
print(list.index('hello'))

# Returns index of value 'howdy'
print(list.index('howdy'))



# Add value 'hej' to list
list.append('hej')
print(list.index('hej'))



# Insert value 'hello there' at index 1
list.insert(1, 'hello there')
print(list)



# Remove value 'howdy' from list
list.remove('howdy')
print(list)



# Sorting a list with numbers
numbers = [2, 5, 3.14, 1, -7]
print('Before sorting:')
print(numbers)

numbers.sort()
print('After sorting:')
print(numbers)

numbers.sort(reverse=True)
print('After reverse sorting:')
print(numbers)



# Sorting a list with strings
list = ['ants', 'cats', 'dogs', 'Alice', 'elephants', 'Bob', 'badgers']
print('Before sorting:')
print(list)

list.sort()
print('After sorting:')
print(list)

list.sort(key=str.lower)
print('After sorting with lower case:')
print(list)