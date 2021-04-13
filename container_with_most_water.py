def container_with_most_water(sides):
	
	max_area = 0
	area = 0
	length = 0
	width = 0
	
	for i in range(len(sides)):
		l1 = sides[i]
		for j in range(i + 1, len(sides)):
			length = sides[i] if sides[i] <= sides[j] else sides[j]
			width = j - i
			area = length * width
			if area > max_area:
				max_area = area

	return max_area
	
def opt_container_with_most_water(sides):
	max_area = 0
	p1 = 0
	p2 = len(sides) - 1
	
	while p1 < p2:
		length = min(sides[p1], sides[p2])
		width = p2 - p1
		area = length * width
		
		if area > max_area:
			max_area = area
		
		if sides[p1] <= sides[p2]:
			p1+=1
		else:
			p2-=1
	
	return max_area

def rec_container_with_most_water(height, p1, p2, max_area):
	
	#base case 1
	if len(height) <= 1:
		return None
	
	if p1 >= p2:
		return max_area
	
	length = min(height[p1], height[p2])
	width = p2 - p1
	area = length * width
	if area > max_area:
		max_area = area
		
	if height[p1] <= height[p2]:
		return rec_container_with_most_water(height, p1 + 1, p2, max_area)
	else:
		return rec_container_with_most_water(height, p1, p2 - 1, max_area)

if __name__ == '__main__':
	
	sides = [6, 9, 3, 4, 5, 8]
	print(rec_container_with_most_water(sides, 0, len(sides) - 1, 0))
