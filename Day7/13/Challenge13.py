from numpy import median

FILE_NAME = "input.txt"

def parseFile():
    crabs = []

    with open(FILE_NAME, "r") as f:
        content = f.read()
        numbers = content.split(",")
        crabs = [int(number) for number in numbers]          

    return crabs

def getBestPossition(crabs):
    return int(median(crabs))

def getConsumedFuel(crab, newPosition):
    return abs(crab - newPosition)

def main():
    crabs = parseFile()

    commonPosition = getBestPossition(crabs)

    print("The common position is: {}".format(commonPosition))

    totalFuel = 0
    for crab in crabs:
        totalFuel += getConsumedFuel(crab, commonPosition)

    print("The total fuel is: {}".format(totalFuel))


main()
