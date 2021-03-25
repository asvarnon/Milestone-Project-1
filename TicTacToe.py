from IPython.display import clear_output

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
# player1 = playerSides()[0]
# player2 = playerSides()[1]

# print(player1)
# print(player2)


def displayGame(gameList):
    clear_output()
    print("Here is the current board:")
    print(gameList[6]+' | '+gameList[7]+' | '+gameList[8])
    print('----------')
    print(gameList[3]+' | '+gameList[4]+' | '+gameList[5])
    print('----------')
    print(gameList[0]+' | '+gameList[1]+' | '+gameList[2])
    

displayGame(gameList)


