def parseInputToMatrix():
    result = []
    with open("input.txt", "r") as f:
        content = f.read()
        lines = content.split("\n")

        for line in lines:
            result.append([int(char) for char in line])

    return result


def getMostCommonValueInColumn(matrix, col):
    column = []
    for row in range(len(matrix)):
        column.append(matrix[row][col])

    return 1 if column.count(1) >= column.count(0) else 0


def getLeastCommonValueInColumn(matrix, col):
    column = []
    for row in range(len(matrix)):
        column.append(matrix[row][col])

    return 0 if column.count(0) <= column.count(1) else 1


def filterRowsByValueInIndex(matrix, value, index):
    result = []
    for row in matrix:
        if row[index] == value:
            result.append(row)
    return result


def parseToDecimal(array):
    string_ints = [str(int) for int in array]
    return int("".join(string_ints), 2)


def getFilteredMatrixByMostCommonValueInColumn(matrix, column):
    if len(matrix) == 1:
        return matrix[0]

    commonValue = getMostCommonValueInColumn(matrix, column)
    newMatrix = filterRowsByValueInIndex(matrix, commonValue, column)
    return getFilteredMatrixByMostCommonValueInColumn(newMatrix, column + 1)


def getFilteredMatrixByLeastCommonValueInColumn(matrix, column):
    if len(matrix) == 1:
        return matrix[0]

    leastCommonValue = getLeastCommonValueInColumn(matrix, column)
    newMatrix = filterRowsByValueInIndex(matrix, leastCommonValue, column)
    return getFilteredMatrixByLeastCommonValueInColumn(newMatrix, column + 1)


def main():
    matrix = parseInputToMatrix()

    oxygenGeneratorRating = getFilteredMatrixByMostCommonValueInColumn(matrix, 0)
    co2ScrubberRating = getFilteredMatrixByLeastCommonValueInColumn(matrix, 0)

    gamma = parseToDecimal(oxygenGeneratorRating)
    epsilon = parseToDecimal(co2ScrubberRating)

    print(gamma * epsilon)


main()
