import conversion

variables = {}


class Variable:
    def __init__(self, equation, input_variables):
        self.units_needed = units_needed

    def __init__(self, unit_type):
        self.is_base_variable = True
        


class DataPoint:
    def __init__(self, units):
        self.value = 0.0
        self.units = units

    def update_value(self, value):
        self.value = value

    def update_units(self, units):
        self.units = units


def add_variables():
    # work here, figure out how to best do complex units
    variables['acceleration'] = Data(['distance', 'time'])
    variables['time'] = Data(['time'])
    variables['distance'] = Data(['distance'])
    variables['velocity_initial'] = Data(['distance', 'time'])
    variables['velocity_final'] = Data(['distance', 'time'])


def main():
    conversion.setup_conversion()
    add_variables()

    print("Hello, welcome to Physo!/n")
    cont = True
    while cont:
        print("Please select an option:")
        print("a: add variable")
        print("q: quit Physo")
        user = input("/n")
        if user == "a":
            variable = input("What variable of the physics problem is this?/n")
            # check to see if variable is in system

            value = input("What is its value?/n")

        elif user == "q":
            exit()
        else:
            print("Please try again!/n")


if __name__ == '__main__':
    main()
