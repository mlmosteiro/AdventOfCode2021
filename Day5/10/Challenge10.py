FILE_NAME = "input.txt"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def isGreaterThan(self, otherPoint):
        if self.x == otherPoint.x:
            return self.y > otherPoint.y

        if self.y == otherPoint.y:
            return self.x > otherPoint.x

        return self.x > otherPoint.x

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Point):
            return self.x == __o.x and self.y == __o.y
        return False

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return "({}, {})".format(self.x, self.y)


class Line:
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.slope = self.getSlope()
        self.yIntercept = self.startPoint.y - self.slope * self.startPoint.x

    def __repr__(self) -> str:
        return "({}, {}) - ({}, {})".format(self.startPoint, self.endPoint)

    def getSlope(self):
        a = self.endPoint.y - self.startPoint.y
        b = self.endPoint.x - self.startPoint.x
        return a / b if b != 0 else 0

    def getAllPoints(self):
        if self.isVertical():
            return [
                Point(self.startPoint.x, y)
                for y in range(self.startPoint.y, self.endPoint.y + 1)
            ]

        elif self.isHorizontal():
            return [
                Point(x, self.startPoint.y)
                for x in range(self.startPoint.x, self.endPoint.x + 1)
            ]

        return [
            Point(x, self.getPointGivenX(x))
            for x in range(self.startPoint.x, self.endPoint.x + 1)
        ]

    def isVertical(self):
        return self.startPoint.x == self.endPoint.x

    def isHorizontal(self):
        return self.startPoint.y == self.endPoint.y

    def getPointGivenX(self, x):
        return int((self.slope * x) + self.yIntercept)


def parseLines():
    lines = []
    with open(FILE_NAME, "r") as f:
        content = f.read()
        textLines = content.split("\n")

        for textLine in textLines:
            textPoints = textLine.strip().split("->")

            startPoint = Point(
                int(textPoints[0].split(",")[0]), int(textPoints[0].split(",")[1])
            )
            endPoint = Point(
                int(textPoints[1].split(",")[0]), int(textPoints[1].split(",")[1])
            )

            if startPoint.isGreaterThan(endPoint):
                startPoint, endPoint = endPoint, startPoint

            lines.append(Line(startPoint, endPoint))
    return lines


def main():
    lines = parseLines()
    lines.sort(key=lambda line: line.startPoint.x)

    markedPoints = {}

    for line in lines:
        points = line.getAllPoints()
        for point in points:
            if point in markedPoints:
                markedPoints[point] += 1
            else:
                markedPoints[point] = 1

    pointsWithIntersections = [
        point for point in markedPoints if markedPoints[point] > 1
    ]

    print(len(pointsWithIntersections))


main()
