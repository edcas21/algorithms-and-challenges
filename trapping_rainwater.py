def find_maxLR(array, index, L_or_R):
	max = 0
	last_index = index if L_or_R == 0 else len(array)
	start_index = 0 if L_or_R == 0 else (index + 1)
	for i in range(start_index, last_index):
		if array[i] > max:
			max = array[i]
	return max

def trapping_rainwater(array):
	total = 0
	maxL = 0
	maxR = 0
	for i in range(len(array)):
		maxL = find_maxLR(array, i, 0)
		maxR = find_maxLR(array, i, 1)
		current_water = min(maxL, maxR) - array[i]
		total += current_water if current_water > 0 else 0
	return total


if __name__ == '__main__':
	array = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
	array2 = []
	array3 = [3]
	array4 = [3, 4, 3]
	
	arrays = [array, array2, array3, array4]
	for i in range(len(arrays)):
		print(trapping_rainwater(arrays[i]))
