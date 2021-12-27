import sys

FILE_NAME = "input.txt"


def parseFile():
    crabs = []

    with open(FILE_NAME, "r") as f:
        content = f.read()
        numbers = content.split(",")
        crabs = [int(number) for number in numbers]

    return crabs


def getConsumedFuel(crab, newPosition):
    fuel = 0
    cost = 0
    if crab < newPosition:
        start = crab
        end = newPosition
    else:
        start = newPosition
        end = crab

    for position in range(start, end):
        cost += 1
        fuel += cost

    return fuel


def main():
    crabs = parseFile().sort()
    leastFuel = sys.maxsize
    bestPosition = 0

    ## we ignore the first and last third of the list, it's improbable that those positions will be the best
    for position in range(int(len(crabs) / 3), int(len(crabs) / 3 * 2)):
        totalFuel = 0
        for crab in crabs:
            totalFuel += getConsumedFuel(crab, position)
            if totalFuel > leastFuel:
                continue

        if leastFuel is None or totalFuel < leastFuel:
            leastFuel = totalFuel
            bestPosition = position

    print("The total fuel is: {}".format(leastFuel))
    print("The position of the best is: {}".format(bestPosition))


main()
