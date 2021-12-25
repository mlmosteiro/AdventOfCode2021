FILE_NAME = "input.txt"
TOTAL_OF_DAYS = 80

class Fish:
    RESET_CICLO_DAY = 6
    NEW_CICLO_DAY = 8

    def __init__(self, day=NEW_CICLO_DAY):
        self.day = day

    def hasFinishCiclo(self) -> bool:
        return self.day == 0

    def __eq__(self, __o: object) -> bool:
        return self.day == __o.day

    def __hash__(self) -> int:
        return hash(self.day)

    def __repr__(self) -> str:
        return f"Day {self.day}"

class Fishes:
    def __init__(self):
        self.list = {}

    def add(self, fish: Fish, value = 1):
        if fish not in self.list.keys():
            self.list[fish] = value
        else:
            self.list[fish] += value

    def get(self, fish: Fish) -> int:
        if fish in self.list.keys():
            return self.list[fish]
        return 1
    
    def __iter__(self):
        for fish in self.list.keys():
            yield fish

def parseFile():
    fishes = Fishes()

    with open(FILE_NAME, "r") as f:
        content = f.read()
        numbers = content.split(",")

        for numberText in numbers:
            fish = Fish(int(numberText))
            fishes.add(fish)

    return fishes


def countFishes(fishes: dict) -> int:
    fishesCount = 0
    for fish in fishes:
        fishesCount += fishes.get(fish)

    return fishesCount


def main():
    fishes = parseFile()

    for day in range(0, TOTAL_OF_DAYS):

        nextDayFishes = Fishes()
        for fish in fishes:
            if fish.hasFinishCiclo():
                nextDayFishes.add(Fish(), fishes.get(fish))
                nextDayFishes.add(Fish(Fish.RESET_CICLO_DAY), fishes.get(fish))

            else:
                nextDayFishes.add(Fish(fish.day-1), fishes.get(fish))

        fishes = nextDayFishes

    print(countFishes(fishes))


main()
