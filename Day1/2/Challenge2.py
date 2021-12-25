def parseInput():
    with open("input.txt", "r") as f:
        content = f.read()
    return content.split("\n")


def addThree(start, list):
    return list[start] + list[start + 1] + list[start + 2]


def main():
    list_numbers = parseInput()
    list_numbers = list(map(int, list_numbers))

    greaters = 0

    for i in range(len(list_numbers) - 3):
        j = i + 1
        firstSet = addThree(i, list_numbers)
        nextSet = addThree(j, list_numbers)

        if firstSet < nextSet:
            greaters += 1
    print(greaters)


main()
