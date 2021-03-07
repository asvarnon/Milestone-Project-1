
boardRow1 = [' ', ' ', ' ']
boardRow2 = [' ', ' ', ' ']
boardRow3 = [' ', ' ', ' ']


#Makes Gameboard
def gameBoard(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


#Gets position
def getPosition():
    userRowInput = int(input("Choose a row: "))
    userIndexInput = int(input("Choose an index position: "))
    return userRowInput, userIndexInput

userRowInput, userIndexInput = getPosition()
print(userRowInput)
print(userIndexInput)



