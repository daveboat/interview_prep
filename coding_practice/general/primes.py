import math


def sieve_of_eratosthenes(n):
    """
    The most basic sieve. Construct a sieve object which contains n True boolean values, then iterate from 2 to sqrt(n),
    rounded up, and turn all multiples of the sieve value to False.

    In this implementation if we do n=100, we sieve 2, 3, 5, and 7.
    """

    # construct our sieve list
    sieve = [True] * n

    # in our iterator, we iterate from 2 to sqrt(n). At each iteration, set all multiples of the value being sieved to
    # False
    for i in range(2, math.ceil(math.sqrt(n))):
        # only sieve if the number hasn't already been sieved (for example, if we've sieved 2, then don't sieve with 4)
        if sieve[i]:
            # set all multiples of i from i^2 to n to False
            sieve[i*i::i] = [False] * ((n - i*i - 1)//i + 1)

    return [i for i in range(2, n) if sieve[i]]


def sieve_of_eratosthenes_improved(n):
    """
    An improved version of the sieve of eratosthenes, where we begin don't sieve 2.

    So for n=100, we sieve 3, 5, and 7
    """

    sieve = [True] * n

    # for our iterator, we iterate from 3 to sqrt(n), in steps of 2
    for i in range(3, math.ceil(math.sqrt(n)), 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)  # here, replace i with 2i in the denominator

    # we have to add 2 to the return values, since we didn't sieve it
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def sieve_of_eratosthenes_improved_with_improved_memory(n):
    """
    A further improved version of the sieve of eratosthenes, where we only store half a sieve, since with
    sieve_of_eratosthenes_improved, we only used every other value of sieve anyways.

    This sieve theoretically has the same time complexity as sieve_of_eratosthenes_improved, but has theoretically half
    the space complexity
    """

    # initialize our sieve, but with only half the values, since we only need half of them. This way, the sieve
    # represents True/False values for 1, 3, 5, 7, and so on
    sieve = [True] * (n // 2)

    # To reuse the math we did before, we use the same iterator, but change how our indices work. Remember that the
    # index for the iterator is effectively twice the index of the sieve, so what was formerly i becomes i//2 and what
    # was formerly 2i becomes i. The number of False's stays the same, because we're still sieving the same number of
    # values for each sieved value 3 and larger
    for i in range(3, math.ceil(math.sqrt(n)), 2):
        if sieve[i//2]:
            sieve[i * i//2::i] = [False] * ((n - i*i - 1)//(2 * i) + 1)

    # for our return value, again we need to play with the indices
    return [2] + [2 * i + 1 for i in range(1, n//2) if sieve[i]]


print(sieve_of_eratosthenes_improved_with_improved_memory(100))


# print([2*i+1 for i in range(1,100//2)])
# print(len(sieve_of_eratosthenes(100)))
# print(primes1(100))
