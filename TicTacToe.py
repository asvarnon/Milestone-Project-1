

gameList = ['1','2','3','4','5','6','7','8','9']

def playerSides():
    player1 = ''
    player2 = ''
    choices = ['X', 'O']
    while player1 not in choices:
        player1 = input("P1, Choose a side X or O: \n")
        if player1 not in choices:
            print('Invalid Answer')
        else:
            print(f'Player 1 is: {player1}')
            choices.remove(player1)
            print(f'This is getting removed {choices}')
            player2 = choices[0]
            return player1, player2
    
# print(playerSides())
player1 = playerSides()[0]
player2 = playerSides()[1]

# print(player1)
# print(player2)


def displayGame(gameList):
    print("Here is the current List:")
    print(gameList)

def playGame():
    return null


