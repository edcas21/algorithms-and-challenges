import random

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if (j + 1) < len(array) and array[j + 1] < array[j]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


# SelectionSort implementations

def selection_sort_1(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp
	

def find_smallest(array):
	smallest = array[0]
	smallest_index = 0
	for i in range(1, len(array)):
		if array[i] < smallest:
			smallest = array[i]
			smallest_index = i
	return smallest_index

def selection_sort_2(array):
	sorted = []
	for i in range(len(array)):
		sorted.append(array.pop(find_smallest(array)))
	return sorted


# InsertionSort implementation
def insertion_sort(array):
    for i in range(len(array)):
        cur_val = array[i]
        j = i - 1
        while array[j] > cur_val and j >= 0:
            array[j + 1] = array[j]
            array[j] = cur_val
            j-=1


# Various QuickSort implementations

# using list comprehension
def qsort_simple(array):
    if len(array) <= 1:
        return array
    pivot = array[-1]
    less = [num for num in array[:-1] if num <= pivot]
    greater = [num for num in array[:-1] if num > pivot]
    return qsort_simple(less) + [pivot] + qsort_simple(greater)


# using filter
def qsort_simple_no_lc(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) - 1]
    less = list(filter(lambda x: x <= pivot, array[:-1]))
    greater = list(filter(lambda x: x > pivot, array[:-1]))
    return qsort_simple_no_lc(less) + [pivot] + qsort_simple_no_lc(greater)

# -------------------------
# without filter or list comprehensions
def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def partition(array, left, right):
    pivot = array[right]
    partition_index = left
    for j in range(left, right):
        if array[j] < pivot:
            swap(array, partition_index, j)
            partition_index += 1
    swap(array, partition_index, right)
    return partition_index


def qsort(array, left, right):
    if left < right:
        partition_index = partition(array, left, right)
        qsort(array, left, partition_index - 1)
        qsort(array, partition_index + 1, right)
# -------------------------


if __name__ == '__main__':
	
	array = list(range(0, 10000))
	random.shuffle(array)
	print(array)
	
	array = qsort(array)
	print()
	print(array)
