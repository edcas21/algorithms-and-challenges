def sum(array):
	if len(array) != 1:
		return array.pop() + sum_3(array)
	return array[0]

def gcd(num1, num2):
	if num2 != 0: # recursive case
		rem = num1 % num2
		return find_gcd(num2, rem)
	# base case is when num2 == 0
	return num1

if __name__ == '__main__':
	
