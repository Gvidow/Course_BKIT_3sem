import unittest
from school import task1, task2, task3, Schoolboy, SchoolClass, SchoolboyClass


class TestSchool(unittest.TestCase):
    def setUp(self):
        self.list_class = [
                            SchoolClass(1, "A"),
                            SchoolClass(2, "B"),
                            SchoolClass(3, "C"),
                            SchoolClass(4, "D"),
                            SchoolClass(5, "E")
                        ]

        self.schoolboys = [
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

        self.schoolboy_class = [
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

    def test_task1(self):
        res = task1(self.schoolboys, self.list_class)
        self.assertListEqual(res, [
                                    ('Andrey', 10, 'C'), 
                                    ('Boris', 12, 'B'), 
                                    ('Dmitry', 11, 'C'),
                                    ('Egor', 8, 'B'),
                                    ('Fedor', 12, 'C'),
                                    ('Ivan', 7, 'C'),
                                    ('Oleg', 15, 'C'),
                                    ('Petr', 7, 'A'),
                                    ('Timur', 17, 'E'),
                                    ('Vadim', 1, 'A')])

    def test_task2(self):
        res = task2(self.schoolboys, self.list_class)
        self.assertListEqual(res, [('E', 1), ('A', 2), ('B', 2), ('C', 5)])

    def test_task3(self):
        res = task3(self.schoolboys, self.schoolboy_class, self.list_class)
        self.assertListEqual(res, [
                                    ('Egor', 'C, D, A'),
                                    ('Timur', 'C, A'),
                                    ('Fedor', 'E')])


if __name__ == "__main__":
    unittest.main()
