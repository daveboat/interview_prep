"""
From a number, remove k digits to make the number as small as possible
"""


def remove_one_digit(num):
    # when removing one digit, we always remove the largest value as long as values are increasing monotonically,
    # counting from the start of the number
    found = False
    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            found = True
            break

    if not found:
        i += 1

    return num[:i] + num[i + 1:]


def removeKdigits(num, k):
    # trivial case
    if k == len(num):
        return '0'

    # for removing k digits, we just want to do the removing 1 digit algorithm k times. We can improve this by finding
    # sequences of monotonic digits, etc, for speedups
    for i in range(k):
        num = remove_one_digit(num).lstrip('0')

    if num == '':
        return '0'
    else:
        return num


if __name__ == '__main__':
    print(removeKdigits("1432219", 3))
    print(removeKdigits("112", 1))