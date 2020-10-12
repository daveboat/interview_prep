"""
LC509 - Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is
the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.

Given N, calculate F(N).

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
"""


from math import sqrt


def fib(n: int) -> int:
    return int((((1+sqrt(5))/2)**n - ((1-sqrt(5))/2)**n)/sqrt(5))


def fib_(n: int) -> int:
    f_0 = 0
    f_1 = 1

    if n == 0:
        return f_0
    elif n == 1:
        return f_1
    else:
        for i in range(1, n):
            temp = f_1
            f_1 = temp + f_0
            f_0 = temp

    return f_1


if __name__ == '__main__':
    for i in range(10):
        print(fib(i))

    print('')

    for i in range(10):
        print(fib_(i))