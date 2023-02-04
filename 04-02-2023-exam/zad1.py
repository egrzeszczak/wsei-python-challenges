# [x]: Zadanie 1

# [x]: Proszę utworzyć klasę LineSegment.
# [x]: Odcinek powinien zawierać informację o początku i o końcu.
# [x]: Klasa stworzona w zadaniu 1 powinna umożliwić zmierzenie długości odcinka.
# [x]: Klasa powinna zawierać gettery i settery umożliwiające pobranie informacji:
# [x]: o położeniu początki i końca odcinka
# [x]: oraz wyświetlenie informacji.

import math


class Point:
    _x: int
    _y: int

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def setX(self, _x: int):
        self._x = _x

    def setY(self, _y: int):
        self._y = _y

    def toString(self):
        return f"Point ({self._x}, {self._y})"

    def __init__(self, _x: int, _y: int):
        self._x = _x
        self._y = _y


class LineSegment:
    _a: Point
    _b: Point

    def setA(self, _point: Point):
        self._a = _point

    def setB(self, _point: Point):
        self._b = _point

    def getA(self):
        return self._a

    def getB(self):
        return self._b

    def toString(self):
        return f"LineSegment from ({self._a.getX()}, {self._a.getY()}) to ({self._b.getX()}, {self._b.getY()})"

    def distance(self):
        """https://pl.khanacademy.org/math/geometry/hs-geo-analytic-geometry/hs-geo-distance-and-midpoints/a/distance-formula"""
        return math.sqrt(
            (self._b.getX() - self._a.getX()) ** 2
            + (self._b.getY() - self._a.getY()) ** 2
        )

    def __init__(self, _a: Point, _b: Point):
        self._a = _a
        self._b = _b


a, b = Point(5, 0), Point(5, 10)
line = LineSegment(a, b)

print(b.toString())
print(a.toString())
print(line.toString())
print(f"Distance of {line} is", line.distance())
