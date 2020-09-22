#!/usr/bin/env python3
# We roll two dice (all 36 outcomes are equiprobable).
# What is the conditional probability to have 1 on the first dice under the condition that the sum of two numbers is 6?
# is => 1/30
from random import choice


def roll1() -> bool:
    return choice([1, 2, 3, 4, 5, 6])

def roll2() -> bool:
    return choice([1, 2, 3, 4, 5, 6])


def experiment():
    total = 100000
    wins = 0

    for _ in range(total):
        a = roll1()
        b = roll2()
        if a == 1 and a + b == 6:
            wins += 1

    print(f"{wins}/{total} => {wins / total}")


if __name__ == '__main__':
    for _ in range(10):
        experiment()
