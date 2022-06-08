import cProfile


def add():
    total = 0
    for i in range(1, 10000001):
        total += i


cProfile.run("add()")
