
boardRow1 = [' ', ' ', ' ']
boardRow2 = [' ', ' ', ' ']
boardRow3 = [' ', ' ', ' ']


#Makes Gameboard
def gameBoard(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


#Gets positions

def getRow():
    #initial
    userRowInput = ""
    acceptableValues = range(1,4)
    withinRange = False

    #Two Conditons to check, isDigit & within Range
    while userRowInput.isdigit() == False or withinRange == False:
        userRowInput = input("Choose a row (1-3): ")
        #Digit Check
        if not userRowInput.isdigit():
            print("Sorry, that is not a digit.")
        #Range Check
        if userRowInput.isdigit():
            if int(userRowInput) in acceptableValues:
                withinRange = True
            else:
                print("Not in Acceptable Range")
                pass
    return int(userRowInput)
        

def getIndex():
    #initial
    userIndexInput = ""
    acceptableValues = range(1,4)
    withinRange = False

    #Two Conditons to check, isDigit & within Range
    while userIndexInput.isdigit() == False or withinRange == False:
        userIndexInput = input("Choose a row (1-3): ")
        #Digit Check
        if not userIndexInput.isdigit():
            print("Sorry, that is not a digit.")
        #Range Check
        if userIndexInput.isdigit():
            if int(userIndexInput) in acceptableValues:
                withinRange = True
            else:
                print("Not in Acceptable Range")
                pass
    return int(userIndexInput)

userRowInput = getRow()
userIndexInput = getIndex()
print(userRowInput)
print(userIndexInput)


