equations = {}
variables = {}


class Variable:
    def __init__(self, unit_type):
        self.unit_type = unit_type
        self.value = None

    def add_value(self, value):
        self.value = value


class Equation:
    def __init__(self, solves):
        self.solves = solves

    def solve(self):
        for s in self.solves:
            result = s()
            if result is not None:
                print(result)


def add_variables():
    variables['time'] = Variable('time')
    variables['distance'] = Variable('distance')

    variables['acceleration'] = Variable('complex')


def add_equations():
    # acceleration

    def acceleration():
        d = variables['distance'].value
        t = variables['time'].value
        if d is not None and t is not None:
            return d / (t ** 2)

    equations['acceleration'] = Equation([variables['time'], variables['distance']])
    variables['velocity_initial'] = Data(['distance', 'time'])
    variables['velocity_final'] = Data(['distance', 'time'])
