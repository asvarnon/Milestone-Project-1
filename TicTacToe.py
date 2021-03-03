
boardRow1 = [' ', ' ', ' ']
boardRow2 = [' ', ' ', ' ']
boardRow3 = [' ', ' ', ' ']

def gameBoard(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

def getPosition():
    userRowInput = int(input("Choose a row: "))
    userIndexInput = int(input("Choose an index position: "))
    return userRowInput, userIndexInput

