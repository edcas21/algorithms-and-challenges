def find_maxLR(array, index, L_or_R):
	max = 0
	last_index = index if L_or_R == 0 else len(array)
	start_index = 0 if L_or_R == 0 else (index + 1)
	for i in range(start_index, last_index):
		if array[i] > max:
			max = array[i]
	return max

def opt_find_maxR(array, index):
	max, ind = 0, 0
	for i in range(index + 1, len(array)):
		if array[i] > max:
			max = array[i]
			ind = i
	return [max, ind]

def trapping_rainwater(array):
	total, maxL, maxR = 0, 0, 0
	for i in range(len(array)):
		maxL = find_maxLR(array, i, 0)
		maxR = find_maxLR(array, i, 1)
		current_water = min(maxL, maxR) - array[i]
		total += current_water if current_water > 0 else 0
	return total

def opt_trapping_rainwater(array):
	total, maxL, maxR = 0, 0, 0
	for i in range(len(array)):
		# Search for new max right if the current index is the index of the current max
		if i == maxR[1]:
			maxR = opt_find_maxR(array, i)
		current_water = min(maxL, maxR[0]) - array[i]
		# Keep track of the largest maxL and replace only if the current value is greater
		if array[i] > maxL:
			maxL = array[i]
		total += current_water if current_water > 0 else 0
	return total

def opt2_trapping_rainwater(array):
	left, right = 0, len(array) - 1
	total, maxL, maxR = 0, 0, 0
	while left < right:
		if array[left] <= array[right]:
			if array[left] >= maxL:
				maxL = array[left]
			else:
				total += maxL - array[left]
			left+=1
		# value at pR is less than one at pL
		else:
			if array[right] > maxR:
				maxR = array[right]
			else:
				total += maxR - array[right]
			right-=1
	return total


if __name__ == '__main__':
	array = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
	array2 = []
	array3 = [3]
	array4 = [3, 4, 3]
	
	arrays = [array, array2, array3, array4]
	for i in range(len(arrays)):
		print(opt2_trapping_rainwater(arrays[i]))
