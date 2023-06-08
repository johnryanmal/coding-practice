# Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

import random
import itertools

def chance(frac):
    return random.random() < frac

def choice_iter(iterator):
    try:
        chosen = next(iterator)
    except StopIteration:
        raise StopIteration('Cannot choose from empty sequence') from None

    for order, item in zip(itertools.count(2), iterator):
        if chance(1/order):
            chosen = item
    return chosen


print(choice_iter(iter(range(3)))) #equivalent to random.choice(list(range(3)))