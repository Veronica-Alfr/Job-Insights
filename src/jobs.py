from functools import lru_cache
from csv import DictReader


@lru_cache
def read(path):
    with open(path) as file:
        data = DictReader(file, delimiter=",")
        return list(data)
