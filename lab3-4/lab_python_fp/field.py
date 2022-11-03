from collections.abc import Generator


def field(lst, *args):
    # assert len(lst) > 0
    if len(args) == 0:
        return
    if len(args) == 1:
        key = args[0]
        for dct in lst:
            if key in args:
                yield dct[key]
    else:
        for dct in lst:
            res = {}
            for key in args:
                if key in dct:
                    res[key] = dct[key]
            yield res


if __name__ == "__main__":
    # Пример:
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    a = field(goods, 'title')
    print(isinstance(a, Generator))
    print(list(a))  # должен выдавать 'Ковер', 'Диван для отдыха'
    print(list(a))
    print("=============")

    b = field(goods, 'title', 'price')
    print(isinstance(a, Generator))
    print(list(b))
    # должен выдавать {'title': 'Ковер', 'price': 2000},
    # {'title': 'Диван для отдыха', 'price': 5300}
    print(list(b))
    print("=============")

    c = field(goods)
    print(isinstance(a, Generator))
    print(list(c))
