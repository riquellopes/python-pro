
def my_iterator(inter):
    return (i for i in inter)


for a in my_iterator(range(10)):
    print(a)


def iterathor(iteravel, start):
    """
        >>> iter = iterathor(range(10), 0)
        >>> next(iter)
        (0, 0)
        >>> next(iter)
        (1, 1)
    """
    # for value in iteravel:
    #     yield start, value
    #     start += 1
    yield from zip(infinito(start), iteravel)


def infinito(start):
    while True:
        yield start
        start += 1
