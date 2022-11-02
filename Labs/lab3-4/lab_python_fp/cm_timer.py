import time
from contextlib import contextmanager


class cm_timer_1:
    def __init__(self):
        self.start = 0

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        print(time.time() - self.start)


@contextmanager
def cm_timer_2():
    start = 0
    try:
        start = time.time()
        yield None
    finally:
        print(time.time() - start)


with cm_timer_1():
    time.sleep(2)
    print("exit cm_timer_1")
print("==================")
with cm_timer_2():
    time.sleep(1)
    print("exit cm_timer_2")
