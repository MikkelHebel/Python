import pprint

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}

theBoard['mid-M'] = 'X'
theBoard['top-L'] = 'O'
theBoard['top-R'] = 'O'
theBoard['top-M'] = 'X'

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])

printBoard(theBoard)

# Data types
print(type(theBoard))
print(type('String'))
print(type(42))
print(type(theBoard['top-M']))