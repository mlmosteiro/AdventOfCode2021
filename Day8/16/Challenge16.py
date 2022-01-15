from enum import Enum

FILE_NAME = "input.txt"

class Numbers():
    def __init__(self) :
        self.digits = [[] for i in range(10)]

    def setSegments(self, number, segments):
        segments.sort()
        self.digits[number].extend(segments)


class NumberSegments(Enum):
    ONE = 2
    FOUR = 4
    SEVEN = 3
    EIGHT = 7


def getLines():
    with open(FILE_NAME, "r") as f:
        content = f.read()
        return content.split("\n")

def parseSegmentsLine(line):
    numbersTxt = line.split("|")
    list_tmp = list(filter(None, numbersTxt[0].split(" ")))
    return [[char for char in segments] for segments in list_tmp]

def parseNumbersLine(line):
    numbersTxt = line.split("|")
    list_tmp = list(filter(None, numbersTxt[1].split(" ")))
    return [[char for char in segments] for segments in list_tmp]

def equal(list1, list2):
    list1.sort()
    list2.sort()
    return list1 == list2


def hasUniqueAmountOfSegments(number):
    for element in NumberSegments:
        if len(number) == element.value:
            return True
    return False

def parseNumber (displayDigits, element):
    number = ""
    for digit in element:
        digit.sort()
        number += displayDigits.digits.index(digit).__str__()

    return  int(number)

def fullfillOne(parsedNumbers, numbers):
    candidates = list(filter(lambda x: len(x) == NumberSegments.ONE.value, parsedNumbers))
    numbers.setSegments(1, candidates[0])


def fullfillFour(parsedNumbers, numbers):
    candidates = list(filter(lambda x: len(x) == NumberSegments.FOUR.value, parsedNumbers))
    numbers.setSegments(4, candidates[0])


def fullfillSeven(parsedNumbers, numbers):
    candidates = list(filter(lambda x: len(x) == NumberSegments.SEVEN.value, parsedNumbers))
    numbers.setSegments(7, candidates[0])


def fullfillEight(parsedNumbers, numbers):
    candidates = list(filter(lambda x: len(x) == NumberSegments.EIGHT.value, parsedNumbers))
    numbers.setSegments(8, candidates[0])


def fullfillThree(parsedNumbers, numbers):
    candidates = list(filter(lambda x: len(x) == 5, parsedNumbers))
    candidates = list(filter(lambda x: all(item in x for item in numbers.digits[1]), candidates))
    numbers.setSegments(3, candidates[0])


def fullfillSix(parsedNumbers, numbers):
    candidates = list(filter(lambda x: len(x) == 6, parsedNumbers))
    candidates = list(filter(lambda x: (numbers.digits[1][0] in x) ^ (numbers.digits[1][1] in x), candidates))
    numbers.setSegments(6, candidates[0])


def fullfillNine(parsedNumbers, numbers):
    candidates = list(filter(lambda x: len(x) == 6, parsedNumbers))
    candidates = list(filter(lambda x: all(item in x for item in numbers.digits[3]), candidates))
    numbers.setSegments(9, candidates[0])


def fullfillZero(parsedNumbers, numbers):
    candidates = list(filter(lambda x: len(x) == 6, parsedNumbers))
    candidates = list(filter(lambda x: not equal(x, numbers.digits[6]) and not equal(x,numbers.digits[9]), candidates))
    numbers.setSegments(0, candidates[0])


def fullfillFive(parsedNumbers, numbers):
    candidates = list(filter(lambda x: len(x) == 5, parsedNumbers))
    candidates = list(filter(lambda x: all(item in numbers.digits[6] for item in x) and  not equal(x, numbers.digits[3]), candidates))
    numbers.setSegments(5, candidates[0])


def fullfillTwo(parsedNumbers, numbers):
    candidates = list(filter(lambda x: len(x) == 5, parsedNumbers))
    candidates=list(filter(lambda x: not equal(x,numbers.digits[5]) and not equal(x,numbers.digits[3]), candidates))
    numbers.setSegments(2, candidates[0])


def decodeDisplay(segments):
    numbers = Numbers()
    fullfillOne(segments, numbers)
    fullfillFour(segments, numbers)
    fullfillSeven(segments, numbers)
    fullfillEight(segments, numbers)
    fullfillThree(segments, numbers)
    fullfillSix(segments, numbers)
    fullfillNine(segments, numbers)
    fullfillZero(segments, numbers)
    fullfillFive(segments, numbers)
    fullfillTwo(segments, numbers)

    return numbers

def main():
    lines = getLines()
    total = 0
    
    for line in lines:
        segments = parseSegmentsLine(line)
        goalNumbers = parseNumbersLine(line)
        display = decodeDisplay(segments)
        total += parseNumber(display, goalNumbers)

    print(total)

main()