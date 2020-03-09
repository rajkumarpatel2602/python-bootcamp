# TicToe Game related code goes here.

import pdb

checkList = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9],
             [3, 5, 7], [1, 4, 7], [2, 5, 8], [3, 6, 9]]
inputList = [' '] * 9
symList = ['x', 'o']
markedList = [None] * 9
totalInputs = 0

playerOneSym = 'a'
playerTwoSym = 'b'


def checkResult(playerSym):
    matchFlag = False
    for check in checkList:
        if matchFlag == True:
            return matchFlag
        for x in check:
            if(inputList[x-1] != playerSym):
                matchFlag = False
                break
            else:
                matchFlag = True
                continue
        else:
            break
    return matchFlag


def printTicToc():
    print '%s' % (inputList[0])+'|' + \
        '%s' % (inputList[1])+'|'+'%s' % (inputList[2])
    print '%s' % (inputList[3])+'|' + \
        '%s' % (inputList[4])+'|'+'%s' % (inputList[5])
    print '%s' % (inputList[6])+'|' + \
        '%s' % (inputList[7])+'|'+'%s' % (inputList[8])


def actualInput(userNum):
    global totalInputs, playerOneSym, playerTwoSym
    user = 0
    if totalInputs > 9:
        return False

    while True:
        if userNum == playerOneSym:
            print ('USER 1, your turn :\n')
        else:
            print ('USER 2, your turn :\n')
        user = int(raw_input())
        if user in [i for i in range(1, 10)]:
            if user in markedList:
                print 'this box is already marked!'
                continue
            else:
                totalInputs = totalInputs + 1
                markedList.append(user)
                break
        else:
            print ('wrong input!\n')
            continue

    inputList[user-1] = userNum
    return True


def userPress():

    print ('Attention : press 1-9 position always as an input : \n')
    markedList = [i for i in range(1, 10)]
    print markedList

    while True:
        if actualInput(playerOneSym) == False:
            print "Well played guys! It's a Tie!"
        printTicToc()
        if checkResult(playerOneSym) == True:
            print ('********************************************\n  player1 won! player2 betterluck next time\n********************************************\n')
            return True

        if actualInput(playerTwoSym) == False:
            print "Well played guys! It's a Tie!"
        printTicToc()
        if checkResult(playerTwoSym) == True:
            print ('********************************************\n  player2 won! player1 betterluck next time\n********************************************\n')
            return True

    return True


def userChoice():

    global playerTwoSym, playerOneSym
    print("let's us start the game now! ")
    while True:

        playerOneSym = raw_input('pick from x or o : ')
        print playerOneSym
        if playerOneSym != 'x' and playerOneSym != 'o':
            print 'Buddy don"t you read the note??? ;) '
            continue
        if playerOneSym in symList:
            print playerOneSym, symList
            symList.remove(playerOneSym)
            playerTwoSym = symList[0]
            print ('player1 choose ', playerOneSym)
            print ('player2 choose ', playerTwoSym)
            break
        else:
            print ('wrong value choosen')

    return True


def initGame():
    global inputList, symList, markedList, totalInputs, playerOneSym, playerTwoSym
    inputList = [' '] * 9
    symList = ['x', 'o']
    markedList = [None] * 9
    totalInputs = 0

    playerOneSym = 'a'
    playerTwoSym = 'b'


def main():

    while True:
        initGame()
        ready = raw_input(
            'Wanna Have TicToc fun? \nType "y" to continue or any key to quit : ')
        if ready != 'y':
            print "okay Chill honey! i'm going!"
            return
        if False == userChoice():
            continue
        userPress()


if __name__ == "__main__":
    main()
