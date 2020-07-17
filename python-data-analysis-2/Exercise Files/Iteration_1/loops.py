import math
import collections

import numpy as np
import pandas as pd
import matplotlib.pyplot as pp

for i in range(0, 10):
    print(i)

for i in range(5):
    print(i)


# same as above, but now as a function that takes arbitrary total


def find_combinations(total):
    combinations_amounts = []

    for amount_100 in range(0, total + 1, 100):
        for amount_50 in range(0, total + 1, 50):
            for amount_25 in range(0, total + 1, 25):
                for amount_10 in range(0, total + 1, 10):
                    for amount_5 in range(0, total + 1, 5):
                        total_so_far = amount_100 + amount_50 + amount_25 + amount_10 + amount_5

                        if total_so_far <= total:
                            combinations_amounts.append([amount_100, amount_50, amount_25, amount_10, amount_5,
                                                         total - total_so_far])

    return combinations_amounts


totals = range(100, 100, 100)
lengths = [len(find_combinations(total)) for total in totals]

pp.plot(totals, lengths)

