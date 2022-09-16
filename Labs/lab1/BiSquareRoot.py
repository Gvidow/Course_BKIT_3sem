import sys
import math


class MismatchError(Exception):
    pass


class SquaredRoot:
    def __init__(self, a, b, c):
        if a == 0.0:
            raise MismatchError("Уравнение с такими коэффициентами \
            не является квадратным")
        self.a = a
        self.b = b
        self.c = c

    def calculate(self):
        descriminant = self.b * self.b - 4 * self.a * self.c
        if descriminant < 0.0:
            return []
        elif descriminant == 0.0:
            return [-self.b / (2 * self.a)]
        descriminant = math.sqrt(descriminant)
        return list(map(lambda x: (-self.b + x) / (2 * self.a),
                    (-descriminant, descriminant)))


class BiSquareRoot:
    def __init__(self, a, b, c):
        if a == 0.0:
            raise MismatchError("Уравнение с такими коэффициентами не \
                является биквадратным")
        self.a = a
        self.b = b
        self.c = c

    def calculate(self):
        try:
            equation = SquaredRoot(self.a, self.b, self.c)
        except MismatchError:
            raise MismatchError("Уравнение с такими коэффициентами не \
                является биквадратным")
        except Exception:
            return []
        roots = equation.calculate()
        res = []
        for i in list(filter(lambda x: x >= 0, roots)):
            if i == 0.0:
                res.append(0.0)
            else:
                res.extend((-i, i))
        return res


def parse_float(string):
    try:
        val = float(string)
    except ValueError:
        return
    except Exception:
        return
    return val


def read_factors():
    lst = []
    name_factors = ["a", "b", "c"]
    for i in sys.argv[1:]:
        lst.append(parse_float(i))
        if len(lst) == 3:
            return lst
    while len(lst) != 3:
        lst.append(parse_float(input(f"{name_factors[len(lst)]}: ")))
    return lst


def main():
    list_factors = read_factors()
    try:
        equation = BiSquareRoot(*list_factors)
        roots = equation.calculate()
        if len(roots) == 0:
            print("корней нет")
        else:
            print("корни уравнения: ", *roots)
    except MismatchError as err:
        print(err)
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
