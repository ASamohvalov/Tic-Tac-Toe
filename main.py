import random

print('Tic Tac Toe')

class MainGame:
    field = [['.', ' ', '.', ' ', '.'],
             [' ', ' ', ' ', ' ', ' '],
             ['.', ' ', '.', ' ', '.'],
             [' ', ' ', ' ', ' ', ' '],
             ['.', ' ', '.', ' ', '.']]
    
    allMoves = []

    def printField():
        for i in MainGame.field:
            for j in i:
                print(j, end=' ')
            print()
    
    def putSymbol(coordinates : str, symbol : str):
        exchanger = []
        finalCoordinate = []
        for i in coordinates:
            if i.isdigit():
                exchanger.append(i)

                if i == '1':
                    finalCoordinate.append(0)
                elif i == '2':
                    finalCoordinate.append(2)
                elif i == '3':
                    finalCoordinate.append(4)
        
        MainGame.field[finalCoordinate[0]][finalCoordinate[1]] = symbol
        MainGame.allMoves.append(exchanger)

    def playersMove(player : str):
        print('Player', player)
        coordinates = input('coordinates - ')

        if not MainGame.isCoordinatesCorrect(coordinates):
            print('you entered something wrong, try again')
            MainGame.playersMove(player)
            return

        if MainGame.isMoveExsist(coordinates):
            print('this move already exists, try again')
            MainGame.playersMove(player)
            return

        MainGame.putSymbol(coordinates, player)

    def isCoordinatesCorrect(coordinates : str) -> bool:
        stack = ['1', '2', '3', '-', ' ']

        countDigits = 0
        for i in coordinates:
            if i not in stack:
                return False
            if i.isdigit():
                countDigits += 1
        
        if countDigits != 2:
            return False
        return True
    
    def isMoveExsist(coordinates : str) -> bool:
        exchanger = []
        for i in coordinates:
            if i.isdigit():
                exchanger.append(i)

        if exchanger in MainGame.allMoves:
            return True
        return False
    
    def isPlayerWon(player : str) -> bool:
        def isListContsinsList(list1, list2) -> bool:
            for i in list1:
                if i not in list2:
                    return False
            return True

        topCoordinate = [[0, 0], [0, 2], [0, 4]]
        midCoordinateH = [[2, 0], [2, 2], [2, 4]]
        bottomCoordinate = [[4, 0], [4, 2], [4, 4]]

        leftCoordinate = [[0, 0], [2, 0], [4, 0]]
        midCoordinateG = [[0, 2], [2, 2], [4, 2]]
        rightCoordinate = [[0, 4], [2, 4], [4, 4]]

        acrossDown = [[0, 0], [2, 2], [4, 4]]
        acrossUp = [[4, 0], [2, 2], [0, 4]]

        coordinates = []
        cntX = 0
        cntY = 0
        for i in MainGame.field:
            for j in i:
                if j == player:
                    coordinates.append([cntX, cntY])
                cntY += 1
            cntY = 0
            cntX += 1

        if isListContsinsList(topCoordinate, coordinates) or isListContsinsList(midCoordinateH, coordinates) or isListContsinsList(bottomCoordinate, coordinates):
            return True
        elif isListContsinsList(leftCoordinate, coordinates) or isListContsinsList(midCoordinateG, coordinates) or isListContsinsList(rightCoordinate, coordinates):
            return True
        elif isListContsinsList(acrossDown, coordinates) or isListContsinsList(acrossUp, coordinates):
            return True
        return False


class GameWithSPU(MainGame):
    def spuMove():
        moveX = random.randint(1, 3)
        moveY = random.randint(1, 3)

        coordinate = str(moveX) + str(moveY)
        if MainGame.isMoveExsist(coordinate):
            GameWithSPU.spuMove()
            return

        print('SPU :', moveX, '-', moveY)
        MainGame.putSymbol(coordinate, '0')


def start():
    print('1.game with a friend(2 player) 2.game with SPU (1 player)')
    choiseGame = input('your choise - ')

    if choiseGame == '1':
        game = MainGame
        withPlayer(game)
    elif choiseGame == '2':
        game = GameWithSPU
        withSPU(game)
    else:
        print('you entered something wrong, try again')
        start()

def withPlayer(game : MainGame):
    count = 4
    while True:
        game.printField()
        game.playersMove('X')
        if game.isPlayerWon('X'):
            game.printField()
            print('\n\t\tplayer X - wins!!!')
            break
        
        if count == 0:
            print('\n\t\tDRAW!!!')
            break

        game.printField()
        game.playersMove('0')
        if game.isPlayerWon('0'):
            game.printField()
            print('\n\t\tplayer 0 - wins!!!')
            break
        count -= 1 

def withSPU(game : GameWithSPU):
    count = 4
    while True:
        game.printField()
        game.playersMove('X')
        if game.isPlayerWon('X'):
            game.printField()
            print('\n\t\tplayer X - wins!!!')
            break

        if count == 0:
            print('\n\t\tDRAW!!!')
            break

        game.printField()
        game.spuMove()
        if game.isPlayerWon('0'):
            game.printField()
            print('\n\t\tSPU - wins:(')
            break
        count -= 1

start()