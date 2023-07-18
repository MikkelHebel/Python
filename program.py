# Windows:
#! python3

# OS X:
#! /usr/bin/env python3

# Linux:
#! /usr/bin/python3


# Import modules
import os
import sys
import time
import pyperclip

# Set variables
name = 'Alice'
place = 'Main Street'
time = '6 pm'
food = 'turnips'

# Print invitation
print('Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (name, place, time, food))