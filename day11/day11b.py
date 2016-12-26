#use sets, use combination, all
from itertools import combinations
from heapq import heappush,heappop
from pprint import pprint
import copy

def is_valid(floor):
	gen = any([x > 0 for x in floor])
	if not gen: return True

	return all([-chip in floor for chip in floor if chip <  0])

def get_moves(curr_state):
	curr_g = curr_state[3]
	curr_floor,no = curr_state[1][curr_state[2]],curr_state[2]
	items_to_move = [[item] for item in curr_floor] + [list(item) for item in combinations(list(curr_floor),2)]
	#print(items_to_move)
	directions = (1,-1)
	#print(new_floors)
	new_states = []
	for direction in directions:
		for item in items_to_move:
			new_floors = list(copy.deepcopy(curr_state[1]))
			new_floors[no] = tuple(sorted([x for x in new_floors[no] if x not in item]))
			if 0 <= no + direction <=3:
				#print(no+direction)
				#pprint(new_floors)
				new_floors[no+direction] = tuple(sorted(list(new_floors[no+direction]) + item))
				priority = curr_g - len(new_floors[3])*10
				if is_valid(new_floors[no]) and is_valid(new_floors[no+direction]):
					new_states.append((priority,new_floors,no + direction,curr_g+1))
	return new_states


def is_goal(state):
	floors = state[1]
	if floors[0] == () and floors[1] == () and floors[2] == ():
		return True
	return False



def a():
	th,pl,st,pr,ru,x,z = 1,2,3,4,5,6,7
	#the negative implies its a microchip
	# start_floors = ( 
	# (1,-1,2,3),        
	# (-2,-3),
	# (4,-4,5,-5),
	# ()		   
	# )
	start_floors = ( 
	(th,-th,pl,st,x,-x,z,-z),        
	(-pl,-st),
	(pr,-pr,ru,-ru),
	()		   
	)

	visited = []
	queue = []
	g,h = 0,0
	priority = g + h
	initial = (priority,start_floors,0,g)
	heappush(queue,initial)
	exp = 0
	while len(queue) != 0:
		exp+=1
		curr_state = heappop(queue)
		visited.append((curr_state[1],curr_state[2],curr_state[3]))
		#print(curr_state[1])
		if is_goal(curr_state):
			print("got it")
			print("number of steps",curr_state[3])
			print("expanded",exp)
			break
		moves = get_moves(curr_state)
		#print("states")
		for move in moves:
			move_state = (move[1],move[2],move[3])
			if move_state not in visited:
				heappush(queue,move)
			#pprint(move[1]) 


if __name__ == "__main__":
	a()