from typing import List


def binarySearch(array, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binarySearch(array, target, low, mid - 1)
    else:
        return binarySearch(array, target, mid + 1, high)


def optStartAndEndTarget(array: List[int], target: int) -> List[int]:

    length = len(array)
    if length == 0:
        return [-1, -1]
    mid = binarySearch(array, target, 0, length - 1)
    if mid == -1:
        return [-1, -1]

    start_and_end = []
    temp_res, temp_mid = None, mid

    # Find start
    while temp_res != -1:
        temp_res = binarySearch(array, target, 0, temp_mid - 1)
        if temp_res == -1:
            start_and_end.append(temp_mid)
        else:
            temp_mid = temp_res

    temp_res, temp_mid = None, mid
    # Find end
    while temp_res != -1:
        temp_res = binarySearch(array, target, temp_mid + 1, length - 1)
        if temp_res == -1:
            start_and_end.append(temp_mid)
        else:
            temp_mid = temp_res

    return start_and_end


def startAndEndTarget(array, target):

    start_and_end = []
    start = binarySearch(array, target, 0, len(array) - 1)
    print(start)
    if start != -1:
        left, right = start, start
        while len(start_and_end) < 2:

            if left >= 0:
                if array[left] == target:
                    if left == 0:
                        start_and_end.append(left)
                    left -= 1
                elif len(start_and_end) == 0:
                    start_and_end.append(left + 1)

            if (right) < len(array):
                if array[right] == target:
                    if right == len(array) - 1:
                        start_and_end.append(right)
                    right += 1
                elif len(start_and_end) == 1:
                    start_and_end.append(right - 1)

        return start_and_end
    return [start, start]


if __name__ == '__main__':

    test_cases = [([1, 3, 5, 5, 5, 5, 5, 6, 7, 9], 5), ([3, 3, 3, 3, 3, 6, 7, 9, 12, 15, 67], 3), ([1, 3, 3, 5, 5, 5, 8, 9], 5),
                  ([1, 2, 3, 4, 5, 6], 4), ([1, 2, 3, 4, 5], 9), ([], 3)]

    for case in test_cases:
        print(optStartAndEndTarget(case[0], case[1]))
