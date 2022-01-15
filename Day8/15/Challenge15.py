from enum import Enum

FILE_NAME = "input.txt"


class NumberSegments(Enum):
    ONE = 2
    FOUR = 4
    SEVEN = 3
    EIGHT = 7



def parseSegmentsFile():
    segments = []

    with open(FILE_NAME, "r") as f:
        content = f.read()
        lines = content.split("\n")
        for line in lines:
            numbersTxt = line.split("|")
            segments.extend (list(filter( None, numbersTxt[0].split(" "))))
        return segments

def parseNumbersFile():
    numbers = []

    with open(FILE_NAME, "r") as f:
        content = f.read()
        lines = content.split("\n")
        for line in lines:
            numbersTxt = line.split("|")
            numbers.extend (list(filter( None, numbersTxt[1].split(" "))))
        return numbers

def hasUniqueAmountOfSegments(number):
    for element in NumberSegments:
        if len(number) == element.value:
            return True
    return False


def main():
    numbers = parseNumbersFile()

    apparitions = 0
    for number in numbers:
        if hasUniqueAmountOfSegments(number):
            apparitions += 1
    
    print(apparitions)

main()
