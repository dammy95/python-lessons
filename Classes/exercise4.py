

class Numbers:
    MULTIPLIER = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, x, y):
        return self.x + self.y

    @classmethod
    def multiply(cls, a):
        return a * cls.MULTIPLIER

    @staticmethod
    def subtract(b, c):
        return b - c

    @property
    def value(self):
        return (self.x, self.y)

    @value.setter
    def value(self, value):
        x, y = value
        self.x = x
        self.y

    @value.deletter
    def value(self):
        del x
        del y

