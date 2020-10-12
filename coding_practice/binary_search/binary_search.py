
def binary_search(arr, n):
    # binary search arr for n, return index if found, otherwise return -1
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == n:
            return mid

        if n > arr[mid]:
            left = mid + 1
        elif n < arr[mid]:
            right = mid - 1

    return -1


def find_a_number(n):
    start = 0
    end = 1000

    while start <= end:
        mid = (end + start) // 2
        print(start, mid, end)
        if mid == n:
            print('found number at ' + str(mid))
            return
        elif n > mid:
            start = mid + 1
        else:
            end = mid - 1

    print('didn\'t find the number')


if __name__ == '__main__':
    # find_a_number(786)
    # find_a_number(501.5)

    a = [1, 2]

    print(binary_search(a, 2))
