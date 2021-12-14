import numbers


class Rectangle:
    def __init__(self, length, width):
        if not isinstance(length, numbers.Number):
            raise TypeError
        if not isinstance(width, numbers.Number):
            raise TypeError
        if length <= 0:
            raise ValueError
        if width <= 0:
            raise ValueError
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side


if __name__ == '__main__':
    sq = Square(2)
    print(sq.area())
