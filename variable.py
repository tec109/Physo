class Variable:
    def __init__(self, equation):
        self.equation = equation
        self.dataPoint = None

    def value(self):
        if self.dataPoint is None:
            if

class DataPoint:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

class Equation:
    def __init__(self, equation):
        self.equation = equation

    def solve(self):
