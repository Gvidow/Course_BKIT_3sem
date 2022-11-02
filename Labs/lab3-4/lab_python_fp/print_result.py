def print_result(func):
    def wrap(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__)
        if isinstance(res, list):
            print(*res, sep="\n")
        elif isinstance(res, dict):
            for key, val in res.items():
                print(f"{key} = {val}")

        return res

    return wrap


@print_result
def t():
    return {3:3, 4:4}


t()
