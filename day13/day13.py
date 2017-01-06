from heapq import heappush, heappop
from pprint import pprint
import math
curr_map = {}
goal = (31,39)


def a():
	curr_pos = (1,1)
	init_state = (goal[0]+goal[1],curr_pos,0)
	queue = []
	visited = []
	heappush(queue,init_state)
	while len(queue) != 0:
		curr_state = heappop(queue)
		visited.append((curr_state[1],curr_state[2]))
		# if curr_state[1] == goal:
		# 	print("hey")
		# 	print("moves", curr_state[2])
		# 	break
		moves = get_moves(curr_state)
		for move in moves:
			if (move[1],move[2]) not in visited:
				heappush(queue,move)
	print("done")
	positions = [x[0] for x in visited]
	print(len(set(positions)))
	print(set(positions))
def print_map():
	for x in curr_map:
		for y in curr_map[x]:
			print(curr_map[x][y],end='')
		print()

def get_moves(state):
	moves = []
	curr_pos = state[1]
	x,y = curr_pos[0],curr_pos[1]
	positions = [(x,y+1),(x,y-1),(x-1,y),(x+1,y)]
	for pos in positions:
		if pos[0] < 0 or pos[1] < 0:
			continue

		if pos[0] not in curr_map: 
			curr_map[pos[0]] = {}
		if pos[1] not in curr_map[pos[0]]:
			a = pos[0]**2 + 3*pos[0] + 2*pos[0]*pos[1] + pos[1] + pos[1]**2 + 1350
			a = list(bin(a))

			ones = [x for x in a if x == '1']
			if len(ones)%2 == 0 :
				curr_map[pos[0]][pos[1]] = '.'
			else:
				curr_map[pos[0]][pos[1]] = '#'

		if curr_map[pos[0]][pos[1]] == '.' and state[2] <50:
			man_dist = abs(pos[1]-goal[1]) + abs(pos[0]-goal[0])
			man_dist*=2
			moves.append((state[2]+1 + man_dist,pos,state[2]+1))		
	return moves

if __name__ == "__main__":
	a()

#92