import math

FILE_NAME = "input.txt"


def parseBingoNumbers():
    result = []
    with open(FILE_NAME, "r") as f:
        content = f.read()
        numbers = content.split("\n")[0].split(",")

        return [int(number) for number in numbers]


def parseBingoBoards():
    boards = []
    with open(FILE_NAME, "r") as f:
        content = f.read()
        lines = content.split("\n")
        lines.pop(0)  # quitamos la primera línea de números

        board = {}
        for line in lines:
            if line != "":
                boardLine = line.split(" ")
                for number in boardLine:
                    if number != "":
                        board[int(number)] = False
            elif board != {}:
                boards.append(board)
                board = {}
        boards.append(board)
    return boards


def markNumberInBoards(boards, number):
    for board in boards:
        if number in board:
            board[number] = True


def getNumberByIndex(board, index):
    return list(board.keys())[index]


def checkHoizontalBingo(board):
    matrixOrder = int(math.sqrt(len(board)))
    winningRow = []
    index = 0
    checkedRow = 0

    while len(winningRow) < matrixOrder and checkedRow < matrixOrder:
        number = getNumberByIndex(board, index)
        if len(winningRow) < matrixOrder and board[number]:
            winningRow.append(number)
            index += 1
        else:
            winningRow = []
            checkedRow += 1
            index = checkedRow * matrixOrder

    return len(winningRow) == matrixOrder


def checkVerticalBingo(board):
    matrixOrder = int(math.sqrt(len(board)))

    winningColumn = []
    index = 0
    checkedColumn = 0

    while len(winningColumn) < matrixOrder and checkedColumn < matrixOrder and index < len(board):
        number = getNumberByIndex(board, index)
        if board[number]:
            winningColumn.append(number)
            index += matrixOrder
        else:
            winningColumn = []
            checkedColumn += 1
            index = checkedColumn

    return len(winningColumn) == matrixOrder


def getBoardPoints(board, lastCalledNumber):
    sumOfNotMarkedNumbers = 0
    for number in board:
        if board[number] == False:
            sumOfNotMarkedNumbers += number

    return sumOfNotMarkedNumbers * lastCalledNumber


def main():
    bingoNumers = parseBingoNumbers()
    boards = parseBingoBoards()

    for number in bingoNumers:
        markNumberInBoards(boards, number)

        for board in boards:
            if checkHoizontalBingo(board) or checkVerticalBingo(board):
                print(getBoardPoints(board, number))
                return


main()
