from words import WORDS

def gen_primes(size):
	primes = []
	pos_prime = 2
	while len(primes) < size:
		isPrime = True
		for num in range(2, pos_prime):
			if pos_prime % num == 0:
				isPrime = False
				break
		
		if isPrime:
			primes.append(pos_prime)
		
		pos_prime += 1
	
	return primes

def gen_pairs(array1, array2):
	pairs = {}
	for i in range(len(array1)):
		pairs[array1[i]] = array2[i]
	return pairs

def gen_index(pairs, word, size):
	sum = 0
	for char in word:
		sum += pairs[char]
	return sum % size
	

if __name__ == '__main__':
	
	hash_size = 1000
	alphabet = [chr(x + 97) for x in range(0, 26)]
	primes = gen_primes(26)
	pairs = gen_pairs(alphabet, primes)
	
	collisions = {}
	
	for word in WORDS:
		index = gen_index(pairs, word, hash_size)
		if index in collisions:
			collisions[index] += 1
		else:
			collisions[index] = 1
	
	for key, value in collisions.items():
		print(key, ':', value)
		
