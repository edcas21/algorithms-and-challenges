import re

def is_palindrome_converge(s):
	s = re.sub(r'[^A-Za-z0-9]', '', s)
	left, right = 0, len(s) - 1
	while left <= right:
		if s[left].lower() != s[right].lower():
			return False
		left+=1
		right-=1
	return True

def is_palindrome_diverge(s, alphabet = 'abcdefghiklmnopqrstuvwxyz'):
	s = "".join([char.lower() for char in s if char.lower() in alphabet])
	mid = (len(s) - 1) // 2
	left = mid
	right = mid + 1 if len(s) % 2 == 0 else mid
	while left >= 0 and right < len(s):
		if s[left] != s[right]:
			return False
		left-=1
		right+=1
	return True

def is_palindrome_reverse(s, alphabet = 'abcdefghiklmnopqrstuvwxyz'):
	s = "".join([char.lower() for char in s if char.lower() in alphabet])
	t = s[::-1]
	return s == t


if __name__ == '__main__':
	strings = ['aabaa', 'aabbaa', 'abc', 'a', '', 'A man, a plan, a canal: Panama']
	for s in strings:
		print(is_palindrome_converge(s))
