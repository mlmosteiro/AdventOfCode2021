def parseInputToDictionary():
    result = {}
    with open("input.txt", "r") as f:
        content = f.read()
        lines = content.split("\n")

        for line in lines:
            key, value = line.split(" ")
            if key in result.keys():
                result[key] += int(value)
            else:
                result[key] = int(value)

    return result


def main():
    listOfInstructions = parseInputToDictionary()

    firstNumber = listOfInstructions["down"] - listOfInstructions["up"]
    secondNumber = listOfInstructions["forward"]

    print(firstNumber * secondNumber)


main()
