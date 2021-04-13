from searching import binary_search
from sorting import selection_sort
import random

array = list(range(56, 789, 9))
# print(binary_search(array, 317))

array = list(range(0, 301))
random.shuffle(array)
print(array)
print(selection_sort(array))

