import re

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

# Check if the message contains a phone number by checking for reguler expressions containing 3 digits, a dash, 3 digits, a dash, and 4 digits
# \d\d\d-\d\d\d-\d\d\d\d
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)

print(mo.group())
print(phoneNumRegex.findall(message))