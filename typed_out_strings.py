def remove_chars(string):
	has_hash = True
	string_chars = list(string)
	while has_hash:
		try:
			hash_index = string_chars.index('#')
			string_chars.pop(hash_index)
			if hash_index > 0:
				string_chars.pop(hash_index - 1)
		except:
			has_hash = False
	return string_chars.join('')
	
def better_remove_chars(string):
	string_chars = []
	for char in string:
		if char == '#':
			string_chars.pop()
		else:
			string_chars.append(char)
	return ''.join([char for char in string_chars])

def typed_out_string(string1, string2):
	return better_remove_chars(string1) == better_remove_chars(string2)

def opt_typed_out_string(string1, string2):
	p1, p2 = len(string1) - 1, len(string2) - 1
	while p1 >= 0 or p2 >= 0:
		if string1[p1] == '#' or string2[p2] == '#':
			if string1[p1] == '#':
				back_count = 2
				while back_count > 0:
					p1-=1
					back_count-=1
					if string1[p1] == '#':
						back_count+=2
			if string2[p2] == '#':
				back_count = 2
				while back_count > 0:
					p2-=1
					back_count-=1
					if string2[p2] == '#':
						back_count+=2
		else:
			if string1[p1] != string2[p2]:
				return False
			else:
				p1-=1
				p2-=2
	return True

if __name__ == '__main__':
	string1 = "y#fo##f"
	string2 = "y#fx#o##f"
	res = print(opt_typed_out_string(string1, string2))
