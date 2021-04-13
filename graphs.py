from collections import deque

def person_is_seller(name):
	return name[-1] == 'm'

def bfs(graph, name):
	search_queue = deque()
	search_queue += graph[name]
	searched = []
	while search_queue:
		person = search_queue.popleft()
		if person not in searched:
			if person_is_seller(person):
				print(person + ' is a mango seller!')
				return True
			else:
				search_queue += graph[person]
				search_queue.append(person)
	return False

# Using array as queue
def sec_bfs(graph, name):
	queue = []
	queue += graph[name]
	searched = []
	
	while len(queue):
		person = queue.pop(0)
		if person not in searched:
			if person_is_seller(person):
				print(person + ' is a mango seller!')
				return True
			else:
				searched.append(person)
				queue += graph[person]
	
	return False

if __name__ == '__main__':
	graph = {}
	graph['you'] = ['alice', 'bob', 'claire']
	graph['bob'] = ['anuj', 'peggy']
	graph['alice'] = ['peggy']
	graph['claire'] = ['thom', 'jonny'] 
	graph['anuj'] = []
	graph['peggy'] = []
	graph['thom'] = []
	graph['jonny'] = []
	
	# print(graph) 
	sec_bfs(graph, 'you')
