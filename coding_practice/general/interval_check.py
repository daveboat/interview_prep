from typing import List


def check_interval(interval_list: List[tuple], interval_to_check: tuple) -> bool:
    # sort interval list by start
    interval_list = sorted(interval_list, key=lambda x: x[0])

    # iterate through interval list, creating a list of superintervals
    superinterval_list = []
    for interval in interval_list:
        # if the superinterval list is empty, add the first interval
        if len(superinterval_list) == 0:
            superinterval_list.append(interval)
        # otherwise, do our checks to see if we should add a new superinterval or extend the current one, or do nothing
        else:
            # for convenience, get the latest superinterval
            current_superinterval = superinterval_list[-1]
            # if the interval's start is greater than the current superinterval's end, then start a new superinterval
            if interval[0] > current_superinterval[1]:
                superinterval_list.append(interval)
            # else if the interval's start is less than the current superinterval's end, extend the current
            # superinterval if the interval's end is greater than the current superinterval's end
            else:
                if interval[1] > current_superinterval[1]:
                    superinterval_list[-1] = (current_superinterval[0], interval[1])
                # else do nothing

    # now, interate through the superinterval list. if the interval to check lies inside a superinterval, return true.
    # else, if we've gone through the whole list, return false
    for superinterval in superinterval_list:
        if interval_to_check[0] >= superinterval[0] and interval_to_check[1] <= superinterval[1]:
            return True
    return False


if __name__ == '__main__':
    ilist = [(4, 6), (1, 2), (1.5, 2.5), (3, 9), (8, 14)]

    print(check_interval(ilist, (2.7, 6)))
    print(check_interval(ilist, (4, 6)))