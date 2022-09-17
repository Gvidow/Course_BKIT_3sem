import sys
import math


class MismatchError(Exception):
    pass


class SquaredRoot:
    def __init__(self, a, b, c):
        if a == 0.0:
            raise MismatchError("Уравнение с такими коэффициентами " +
                                "не является квадратным")
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
            raise MismatchError("Уравнение с такими коэффициентами не " +
                                "является биквадратным")
        self.a = a
        self.b = b
        self.c = c

    def calculate(self):
        equation = SquaredRoot(self.a, self.b, self.c)
        roots = equation.calculate()
        res = []
        for i in list(filter(lambda x: x >= 0, roots)):
            if i == 0.0:
                res.append(0.0)
            else:
                root = math.sqrt(i)
                res.extend((-root, root))
        return res


def update_list_factors(lst, val):
    try:
        lst.append(float(val))
    except ValueError:
        return lst
    except Exception:
        return lst
    return lst


def read_factors():
    lst = []
    name_factors = ["a", "b", "c"]
    for i in sys.argv[1:]:
        lst = update_list_factors(lst, i)
        if len(lst) == 3:
            return lst
    while len(lst) != 3:
        lst = update_list_factors(
            lst,
            input(f"введите коэффициент {name_factors[len(lst)]}: ")
                    )
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
