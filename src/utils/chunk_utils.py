import itertools


def chunks(iterable, size):
    """Yield successive n-sized chunks from iterable."""
    iterator = iter(iterable)
    for first in iterator:
        yield itertools.chain([first], itertools.islice(iterator, size - 1))
