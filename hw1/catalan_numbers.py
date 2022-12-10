from inspect import isgeneratorfunction

def catalan_numbers_gen():
    num, prev = 1, 1
    while True:
        yield prev
        prev = 2 * (2*num - 1) * prev // (num + 1)
        num += 1
