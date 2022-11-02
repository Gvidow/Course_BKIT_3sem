from cProfile import label
from field import field
import json
import sys
from print_result import print_result
from cm_timer import cm_timer_1
from gen_random import gen_random
from unique import Unique
from sorts import sort_not_use_lambda
# Сделаем другие необходимые импорты

path = "../data_light.json"

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path) as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return Unique(sort_not_use_lambda(arg))


@print_result
def f2(arg):
    return filter(lambda x: x[:11] == "программист", arg)


@print_result
def f3(arg):
    return map(lambda x: x + "с опытом Python ", arg)


@print_result
def f4(arg):
    return map(lambda x: f"{x[0]}, зарплата {x[1]} руб.",
               zip(field(data, "job-name"),
                   gen_random(len(data), 100000, 200000)))



if __name__ == '__main__':
    with cm_timer_1():
        print(*f2(f3(f4(data))), sep = "\n")
