import equation


class Variable:
    def __init__(self, equations):
        self.equations = equations
        self.dataPoint = None

    def value(self):
        if self.dataPoint is None:
            for e in self.equations:
                trial = e.solve()
                if trial:
                    return trial
            return None
        else:
            return self.dataPoint


class DataPoint:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit


class Equation:
    def __init__(self, array):
        self.array = array
        self.checked = False

    def solve(self):
        if self.checked is True:
            self.checked = False
            return None

        simplified_array = []
        self.checked = True
        for e in self.array:
            if isinstance(e, Variable):
                val = e.value()
                if val is None:
                    return None
                else:
                    simplified_array.append(val)
                    self.checked = False
            else:
                simplified_array.append(e)
                self.checked = False

        return equation.compute(equation.parse(simplified_array))
