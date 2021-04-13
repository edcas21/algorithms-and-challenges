def binary_search(array, target):
	low = 0
	high = len(array) - 1
	
	while low <= high:
		mid = (low + high) // 2
		guess = array[mid]
		if guess == target:
			return mid
		elif guess < target:
			low = mid + 1
		else:
			high = mid - 1
	
	return -1

def rec_binary_search(array, target, low, high):
	# base case 1
	if low >= high:
		return -1
	mid = (low + high) // 2
	# base case 2
	if array[mid] == target:
		return mid
	# recursive case 1
	elif array[mid] < target:
		return rec_binary_search(array, target, mid + 1, high)
	# recursive case 2
	else:
		return rec_binary_search(array, target, low, mid - 1)
		

if __name__ == '__main__':
	
	array = list(range(2, 400, 7))
	print(array)
	print(rec_binary_search(array, 331, 0, len(array) - 1))
