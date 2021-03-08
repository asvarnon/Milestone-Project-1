
boardRow1 = [' ', ' ', ' ']
boardRow2 = [' ', ' ', ' ']
boardRow3 = [' ', ' ', ' ']


#Makes Gameboard
def gameBoard(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


#Gets position
def getRow():
    userRowInput = input("Choose a row (1-3): ")
    while userRowInput.isdigit() == False:
        userRowInput = input("Choose a row (1-3): ")
        if not userRowInput.isdigit():
            print("Sorry, that is not a digit.")
    return int(userRowInput)
        

def getIndex():
    userIndexInput = input("Choose an index position (1-3): ")
    while userIndexInput.isdigit() == False:
        userIndexInput = input("Choose a row (1-3): ")
        if not userIndexInput.isdigit():
            print("Sorry, that is not a digit.")
    return int(userIndexInput)

userRowInput = getRow()
userIndexInput = getIndex()
print(userRowInput)
print(userIndexInput)


