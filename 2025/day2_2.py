import textwrap
from itertools import groupby


def all_equal(iterable):
    if len(iterable) <= 1:
        return False
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


lines = open("2025/input.txt").read().split(",")

result = 0

for i in lines:
    low, high = i.split("-")
    for j in range(int(low), int(high) + 1):
        for k in range(1, len(str(j)) + 1):
            if all_equal(textwrap.wrap(str(j), k)):
                result += int(j)
                break

print(result)
