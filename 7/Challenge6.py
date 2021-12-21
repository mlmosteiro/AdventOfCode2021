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
        lines.pop(0)  ## quitamos la primera línea de números
        lines.pop(0)  ## quitamos el salto de línea

        board = {}
        for line in lines:
            if line == "":
                boards.append(board)
                board = {}
                continue

            boardLine = line.split(" ")
            for number in boardLine:
                if number != "":
                    board[int(number)] = False

        boards.append(board)
    return boards


def markNumberInBoards(boards, number):
    for board in boards:
        if number in board:
            board[number] = True


def checkHoizontalBingo(board):
    columns = int(math.sqrt(len(board)))
    row = []
    index = 0
    rowNumber = 1

    while len(row) < columns and rowNumber < columns:
        number = list(board.keys())[index]
        if index < columns and board[number]:
            row.append(number)
            index += 1
        else:
            row = []
            index = rowNumber * columns
            rowNumber += 1

    return len(row) == columns


def checkVerticalBingo(board):
    columns = int(math.sqrt(len(board)))
    rows = columns

    column = []
    index = 0
    columnNumber = 1
    while len(column) < rows and columnNumber < columns and index < len(board):

        number = list(board.keys())[index]
        if board[number]:
            column.append(number)
            index += columns
        else:
            column = []
            index = columnNumber
            columnNumber += 1

    return len(column) == rows


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
            hasBingo = checkHoizontalBingo(board)
            if hasBingo:
                print(getBoardPoints(board, number))
                return
            hasBingo = checkVerticalBingo(board)
            if hasBingo:
                print(getBoardPoints(board, number))
                return


main()
