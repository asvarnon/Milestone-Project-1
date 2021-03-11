# gameList = [0,1,2]
# gameOn: True

#displays list
def displayGame(gameList):
    print("Here is the current List:")
    print(gameList)

#gets user Choice
def positionChoice():
    choice = ''
    while choice not in ['0','1','2']:
        choice = input('Pick a position between (0-2): ')
        if choice not in ['0','1','2']:
            print("Sorry, invalid choice")
    return int(choice)

#replacement choice
def replacementChoice(gameList,position):
    userPlacement = input('Type string to place at position: ')
    gameList[position] = userPlacement

#replayability
def gameOnChoice():
    choice = 'wrong'
    while choice not in ['Y', 'N', 'y', 'n']:
        choice = input('Continue playing? Y/N: \n')
        if choice not in ['Y', 'N', 'y', 'n']:
            print('Sorry, invalid choice!')
    if choice == 'Y' or choice == 'y':
        return True
    else:
        return False


def startGame():
    gameList = [0,1,2]
    gameOn = True
    while gameOn:
        displayGame(gameList)
        position = positionChoice()
        gameList = replacementChoice(gameList, position)
        displayGame(gameList)
        gameOn = gameOnChoice()

startGame()



# displayGame(gameList)
# replacementChoice(gameList, positionChoice())
# displayGame(gameList)