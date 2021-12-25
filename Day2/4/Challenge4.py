def parseInputToList():
    result = []
    with open("input.txt", "r") as f:
        content = f.read()
        lines = content.split("\n")

        for line in lines:
            instruction = {}
            key, value = line.split(" ")
            instruction[key] = int(value)
            result.append(instruction)

    return result


def main():
    listOfInstructions = parseInputToList()

    aim = 0
    horizontal = 0
    depth = 0

    for instruction in listOfInstructions:
        key = list(instruction.keys())[0]

        if key == "down":
            aim += instruction[key]
        elif key == "up":
            aim -= instruction[key]
        elif key == "forward":
            horizontal += instruction[key]
            depth += aim * instruction[key]

    print(horizontal * depth)


main()
