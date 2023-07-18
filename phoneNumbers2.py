import re

# Check for phone number in a message
phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
phoneNumRegex.search('My number is 415-555-4242.')

mo = phoneNumRegex.search('My number is (415) 555-4242.')

print(mo.group())



# Check for patterns of text
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))