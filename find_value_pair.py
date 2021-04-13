# 1
def find_value_pair(array, target):
	for i in range(len(array)):
		for j in range(i + 1, len(array)):
			if (array[i] + array[j]) == target:
				return (i, j)	
	return None

def opt_find_value_pair(array, target):
	map = {}
	for i in range(len(array)):
		
		if array[i] in map:
			return (map[array[i]], i)
		
		num_to_find = target - array[i]
		map[num_to_find] = i
	
	return None
		
def rec_find_value_pair(array, target, index):
	if index <= 0:
		return None
	num_to_find = abs(target - array[index])
	if num_to_find in array:
		return (array.index(num_to_find), index)
	return rec_find_value_pair(array, target, index - 1)
	
def run_find_value_pair(version, target, array = [1, 3, 7, 9, 2]):
	
	if version == 1:
		value_pair = opt_find_value_pair(array, target)
	elif version == 2:
		value_pair = find_value_pair(array, target)
	elif version == 3:
		value_pair = rec_find_value_pair(array, target, len(array) - 1)
	else:
		print('Pick 1 for iterative, 2 for recursive')
	
	if value_pair:
		print(value_pair)
		print(array[value_pair[0]] + array[value_pair[1]])
	else: 
		print('No pair in the array adds up to the target value.')


if __name__ == '__main__':
	
	select = 1
	
	if select == 1:
		run_find_value_pair(1, 1, [0, 1])
		run_find_value_pair(2, 1, [0, 1])

		
