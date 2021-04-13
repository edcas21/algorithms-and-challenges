import random

def find_smallest(array):
	smallest = array[0]
	smallest_index = 0
	for i in range(1, len(array)):
		if array[i] < smallest:
			smallest = array[i]
			smallest_index = i
	return smallest_index

def selection_sort(array):
	sorted = []
	for i in range(len(array)):
		sorted.append(array.pop(find_smallest(array)))
	return sorted

def qsort(array):
	
	if len(array) <= 1:
		return array
	else:
		pivot = array[0]
		less = [i for i in array[1:] if i <= pivot]
		greater = [i for i in array[1:] if i > pivot]
		
		return qsort(less) + [pivot] + qsort(greater)


if __name__ == '__main__':
	
	array = list(range(0, 10000))
	random.shuffle(array)
	print(array)
	
	array = qsort(array)
	print()
	print(array)
