def parseInput():
    with open("input.txt", "r") as f:
        content = f.read()
    return content.split("\n")


def main():
    list_numbers = parseInput()
    list_numbers = list(map(int, list_numbers))

    greaters = 0

    for i in range(len(list_numbers) - 1):
        j = i + 1
        if list_numbers[i] < list_numbers[j]:
            greaters += 1
    print(greaters)


main()
