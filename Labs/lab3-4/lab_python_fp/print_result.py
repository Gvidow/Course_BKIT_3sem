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
def return_dict():
    return {"one": 1, "two": 2}


@print_result
def return_list():
    return [1, 2, 3, 4, 5]


return_dict()
print("===========")
return_list()
