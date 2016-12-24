import sys	
def make_numpad():
	numpad = [[1,2,3],[4,5,6],[7,8,9]]


def get_num(numpad,line,curr_pos):
	for char in line:
		#print (char)
		if char == 'U':
			if curr_pos[0] > 0:
				curr_pos[0]-=1 
		elif char == 'R':
			if curr_pos[1]<2:
				curr_pos[1]+=1
		elif char == 'D':
			if curr_pos[0] < 2:
				curr_pos[0]+=1
		elif char == 'L':
			if curr_pos[1]>0:
				curr_pos[1]-=1
	print(numpad[curr_pos[0]][curr_pos[1]])
	return curr_pos


if __name__ == "__main__":
	numpad = [[1,2,3],[4,5,6],[7,8,9]]
	curr_pos = [1,1]
	for line in sys.stdin:
		curr_pos = get_num(numpad,line,curr_pos)