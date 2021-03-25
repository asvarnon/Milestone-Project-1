from IPython.display import clear_output

gameList = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

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

placeMarker(gameList, player1, getPosition())
displayGame(gameList)

