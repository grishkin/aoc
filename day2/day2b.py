import sys	
def make_numpad():
	numpad = [[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,'A','B','C',0],[0,0,'D',0,0]]
	return numpad

def get_num(numpad,line,curr_pos):
	for char in line:
		#print (char)
		if char == 'U':
			if curr_pos[0] > 0:
				new_pos = [curr_pos[0]-1,curr_pos[1]]
				if can_move(numpad,new_pos): 
					 curr_pos[0]-=1
		elif char == 'R':
			if curr_pos[1]<4:
				new_pos = [curr_pos[0],curr_pos[1]+1]
				if can_move(numpad,new_pos): 
					 curr_pos[1]+=1
		elif char == 'D':
			if curr_pos[0] < 4:
				new_pos = [curr_pos[0]+1,curr_pos[1]]
				if can_move(numpad,new_pos): 
					 curr_pos[0]+=1
		elif char == 'L':
			if curr_pos[1]>0:
				new_pos = [curr_pos[0],curr_pos[1]-1]
				if can_move(numpad,new_pos): 
					 curr_pos[1]-=1
	print (curr_pos[0], curr_pos[1])
	print(numpad[curr_pos[0]][curr_pos[1]])
	return curr_pos


def can_move(numpad, pos):
	if pos[0] == 0 and pos[1] != 2:
		return False
	if pos[0] == 1 and (pos[1] == 0 or pos[1] == 4):
		return False
	if pos[0] == 3 and (pos[1] == 0 or pos[1] == 4):
		return False
	if pos[0] == 4 and pos[1] != 2:
		return False
	return True

if __name__ == "__main__":
	numpad = make_numpad()
	curr_pos = [1,1]
	for line in sys.stdin:
		curr_pos = get_num(numpad,line,curr_pos)