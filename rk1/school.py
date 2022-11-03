from operator import itemgetter
from collections import Counter
from prettytable import PrettyTable


class Schoolboy:
    """Школьник"""
    def __init__(self, id, fio, old, class_id):
        self.id = id
        self.fio = fio
        self.old = old
        self.class_id = class_id


class SchoolClass:
    """Класс"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class SchoolboyClass:
    """
    'Школьники' для реализации
    связи многие-ко-многим
    """
    def __init__(self, schoolboy_id, class_id):
        self.schoolboy_id = schoolboy_id
        self.class_id = class_id


# Классы
list_class = [
    SchoolClass(1, "A"),
    SchoolClass(2, "B"),
    SchoolClass(3, "C"),
    SchoolClass(4, "D"),
    SchoolClass(5, "E")
]

# Школьники
schoolboys = [
    Schoolboy(1, "Ivan", 7, 3),
    Schoolboy(2, "Vadim", 1, 1),
    Schoolboy(3, "Andrey", 10, 3),
    Schoolboy(4, "Boris", 12, 2),
    Schoolboy(5, "Egor", 8, 2),
    Schoolboy(6, "Petr", 7, 1),
    Schoolboy(7, "Timur", 17, 5),
    Schoolboy(8, "Fedor", 12, 3),
    Schoolboy(9, "Dmitry", 11, 3),
    Schoolboy(10, "Oleg", 15, 3)
]

schoolboy_class = [
    SchoolboyClass(5, 3),
    SchoolboyClass(5, 4),
    SchoolboyClass(8, 5),
    SchoolboyClass(7, 3),
    SchoolboyClass(2, 1),
    SchoolboyClass(2, 2),
    SchoolboyClass(3, 4),
    SchoolboyClass(7, 1),
    SchoolboyClass(4, 5),
    SchoolboyClass(5, 1)
]


def draw(name_of_fields, data):
    table = PrettyTable(name_of_fields)
    table.align = "l"
    table.add_rows(data)
    print(table)


def main():
    print("Задание Б1")
    list_schoolboy_class = [(scb.fio, scb.old, cls.name, cls.id)
                            for scb in schoolboys
                            for cls in list_class
                            if scb.class_id == cls.id]
    res1 = sorted(map(lambda x: x[:-1], list_schoolboy_class),
                  key=itemgetter(0))
    draw(("ФИО", "Возраст", "Название класса"), res1)

    print("\nЗадание Б2")
    schoolboy_in_class = Counter((class_id, class_name)
                                 for _, _, class_name, class_id
                                 in list_schoolboy_class)
    res2 = sorted([(cls[1], cou_scb)
                   for cls, cou_scb in schoolboy_in_class.items()],
                  key=itemgetter(1))
    draw(("Название класса", "Количество учеников"), res2)

    print("\nЗадание Б3")
    res3 = {}
    for scb in schoolboys:
        if scb.fio[-1] == "r":
            list_class_for_scb = [cls.name for mm in schoolboy_class
                                  for cls in list_class
                                  if (cls.id == mm.class_id and
                                      scb.id == mm.schoolboy_id)]
            if len(list_class_for_scb) > 0:
                res3[scb.fio] = list_class_for_scb
    draw(("ФИО", "Названия классов"),
         [(scb, ", ".join(lst)) for scb, lst in res3.items()])


main()
