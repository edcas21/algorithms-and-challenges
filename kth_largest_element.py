def qsort(array):
    if len(array) <= 1:
        return array
    pivot = array[-1]
    less = [num for num in array[:-1] if num <= pivot]
    greater = [num for num in array[:-1] if num > pivot]
    return qsort(less) + [pivot] + qsort(greater)

def kth_largest_element(array, k):
    return qsort(array)[-k]

if __name__ == '__main__':
    test_cases = [
        [5, 3, 1, 6, 4, 2, 2],
        [2, 3, 1, 2, 4, 2, 4]
    ]
    
    for test_case in test_cases:
        print(kth_largest_element(test_case[:-1], test_case[-1]))