from IPython.display import clear_output

gameList = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
testList = ['X',' ',' ',' ','X',' ',' ',' ','X']

'''
OUTPUT = (Player 1, Player 2)
'''
def playerSides():
    player1 = ''
    player2 = ''
    choices = ['X', 'O']
    while player1 not in choices:
        player1 = input("P1, Choose a side X or O: \n").upper()
        if player1 == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')
    

player1, player2 = playerSides()
print(player1)
print(player2)


def displayGame(gameList):
    clear_output()
    print("Here is the current board:")
    print(gameList[6]+' | '+gameList[7]+' | '+gameList[8])
    print('----------')
    print(gameList[3]+' | '+gameList[4]+' | '+gameList[5])
    print('----------')
    print(gameList[0]+' | '+gameList[1]+' | '+gameList[2])
    
def getPosition():
    position = ''
    while position not in range(1,10):
        position = int(input('Choose a number between 1-9 to place your marker.\n'))
    return position

def placeMarker(board, marker, position):
    gameList[position - 1] = marker

# placeMarker(gameList, player1, getPosition())
# displayGame(gameList)

def winCheck(board, mark):
    # check all rows, and columns with 2 diagonals match. 
    # (board[1] == mark and board[2] == mark and board[3] == mark)
    return((board[0] == board[1] == board[2] == mark) or #bottom row
    (board[3] == board[4] == board[5] == mark) or #middle Row
    (board[6] == board[7] == board[8] == mark) or #top row
    (board[0] == board[3] == board[6] == mark) or #left column
    (board[1] == board[4] == board[7] == mark) or #middle column
    (board[2] == board[5] == board[8] == mark) or #right column
    (board[6] == board[4] == board[2] == mark) or #top left to bottom right diagonal
    (board[0] == board[4] == board[8] == mark)) #bottom left to top right diagonal
    
displayGame(testList)
print(winCheck(testList, 'X'))

