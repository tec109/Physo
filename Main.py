variables = {}
unit_types = {}


class Data:
    def __init__(self, units):
        self.value = 0
        self.units = units

    def update_value(self, value):
        self.value = value

    def update_units(self, units):
        self.units = units


class Equation:
    pass


def add_units():
    unit_types['time'] = ['seconds', 'minutes', 'hours', 'days']
    unit_types['distance'] = ['feet', 'meters', 'miles']


def add_variables():
    variables['acceleration'] = Data(['distance', 'time'])
    variables['time'] = Data('time')
    variables['velocity_initial'] = Data(['distance', 'time'])
    variables['velocity_final'] = Data(['distance', 'time'])


def add_equations():
    pass


def main():
    add_units()
    add_variables()
    add_equations()
    dataType = input("What variable of the physics problem is this? ")
    dataValue = input("What is its value? ")


if __name__ == '__main__':
    main()
