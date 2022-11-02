from gen_random import gen_random


class Unique:
    def __init__(self, items, **kwargs):
        self.it = iter(items)
        self.ignore_case = kwargs["ignore_case"] if "ignore_case" in kwargs\
            else False
        self.prev = None
        self.is_first = True

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            current = next(self.it)
            if self.is_first or current != self.prev and not self.ignore_case\
                or (self.ignore_case and isinstance(current, str)
                    and isinstance(self.prev, str)
                    and current.lower() != self.prev.lower()):
                break
        self.prev = current
        self.is_first = False
        return current


data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
print(list(Unique(data)))

data = gen_random(10, 1, 3)
print(list(Unique(data)))

data = ["a", "A", "b", "B", "a", "A", "b", "B"]
print(list(Unique(data)))

print(list(Unique(data, ignore_case=True)))
