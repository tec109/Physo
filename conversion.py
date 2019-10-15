from fractions import Fraction

units = {}


class Unit:
    def __init__(self, unit_type, standard):
        self.unit_type = unit_type
        self.standard = standard
        self.variations = {}

    def add_variation(self, variation, conversion):
        self.variations[variation] = conversion

    def get_conversion(self, variation):
        return self.variations[variation]

    def check_valid(self, unit_type, variation):
        if unit_type == self.unit_type and (variation in self.variations or self.standard == variation):
            return True
        else:
            return False

    def get_unit_type(self):
        return self.unit_type

    def get_standard(self):
        return self.standard


def setup_conversion():
    time = Unit('time', 'seconds')
    time.add_variation('minutes', Fraction(1, 60))
    time.add_variation('hours', Fraction(1, 3600))
    time.add_variation('days', Fraction(1, 86400))
    units['time'] = time

    distance = Unit('distance', 'meters')
    distance.add_variation('feet', Fraction(1, 0.3048))
    distance.add_variation('miles', Fraction(1, 1609.344))
    distance.add_variation('kilometer', Fraction(1, 1000))
    units['distance'] = distance


def check_valid_unit(unit_type, variation):
    if units[unit_type].check_valid(unit_type, variation):
        return True
    else:
        return False


def convert(unit_type, value, current_unit, end_unit):
    result = value
    if check_valid_unit(unit_type, current_unit) and check_valid_unit(unit_type, end_unit):
        working_unit = units[unit_type]

        if current_unit != working_unit.get_standard():
            result = result / working_unit.get_conversion(current_unit)

        return result * working_unit.get_conversion(end_unit)
    else:
        print("Units are not valid")
        return 0
