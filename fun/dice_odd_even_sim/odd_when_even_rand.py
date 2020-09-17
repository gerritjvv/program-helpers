#!/usr/bin/env python3
# For a dice with 6 equiprobable outcomes, what is the probability of odd when even
# we model Odd = False, Even = True
from random import choice


def random_numbers() -> int:
    with open('./vals.txt') as f:
        for line in f:
            yield int(line)


def experiment():
    even = 1
    odd = 0

    total = 0
    wins = 0
    numbers = random_numbers()

    while True:
        a = next(numbers, -1)
        b = next(numbers, -1)

        if a == -1 or b == -1:
            break

        total = total + 2

        if a % 2 == 0 and (not b % 2 == odd):
            wins += 1
    print(f"total: {total}")

    print(f"{wins}/{total} => {wins / total}")


if __name__ == '__main__':
    experiment()
