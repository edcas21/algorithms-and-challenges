def length(array):
	if array:
		array.pop()
		return length(array) + 1
	return 0

def max(array, n):
	if len(array) != 1:
		return max(array[n - 1], max(array, n - 1))
	return array[0]
	
def sum_1(array, currSum = 0):
	if len(array) != 0:
		currSum += array.pop()
		return sum_1(array, currSum)
	return currSum
	
def sum_2(array):
	if len(array) > 1:
		sum = array[0] + array[1]
		array.pop(1)
		array[0] = sum
		return sum_2(array)
	return array[0]
	
def sum_3(array):
	if len(array) != 1:
		return array.pop() + sum_3(array)
	return array[0]

def find_gcd(num1, num2):
	if num2 != 0: # recursive case
		rem = num1 % num2
		return find_gcd(num2, rem)
	# base case is when num2 == 0
	return num1
			
def countdown_1(top):
	print(top)
	if top > 0:
		countdown(top - 1)

def countdown_2(top):
	print(top)
	# Base case - what stops the recursion
	if top <= 0:
		return
	else:
	# Recursive case
		countdown_2(top - 1)

def iter_countdown(top):
	count = []
	while top >= 0:
		count.append(top)
		if top <= 0: break
		top -= 1
	
	print(count)
	print(top)

def greet2(name):
	print('how are you,', name + '?') # print gets pushed on top of greet2()
	# print gets executed and then popped off the stack
	
def bye():
	print('ok bye!')

def greet(name): # When greet() is called, it gets pushed onto the stack
	print('Hello,', name + '!') # print gets pushed on top of greet()
	# After printing print gets popped off the stack
	greet2(name) # greet2() gets pushed onto the stack
	# greet2() gets executed and then popped off the stack
	print('Getting ready to say bye...') # print gets pushed onto the stack
	# print gets popped off the stack
	bye() # bye gets pushed onto the stack
	# bye get popped off the stack
		
# greet('Edgar') # pushed onto the stack
# Done executing so it gets popped off 

# print(length([3, 2, 1, 6, 6, 24]))
