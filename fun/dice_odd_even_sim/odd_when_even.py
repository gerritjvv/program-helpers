#!/usr/bin/env python3
# For a dice with 6 equiprobable outcomes, what is the probability of odd when even
# we model Odd = False, Even = True
from random import choice


def roll() -> bool:
    return choice([True, False])


def experiment():
    even = True
    odd = False

    total = 100000
    wins = 0

    for _ in range(total):
        a = roll()
        b = roll()
        if a == even and b == odd:
            wins += 1

    print(f"{wins}/{total} => {wins/total}")


if __name__ == '__main__':
    for _ in range(10):
        experiment()
