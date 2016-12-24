import sys

screen = [[0 for i in range(50)] for i in range(6)]

def a():
	for line in sys.stdin:
		line = line.strip()
		args = line.split(" ")
		cmd = args[0]
		if cmd == "rect":
			axb = args[1].split('x')
			a = int(axb[0])
			b = int(axb[1])
			rect(a,b)
		elif cmd == "rotate":
			axis = args[1]
			y = args[2].split('=') 
			a = int(y[1])
			b = int(args[4])
			if axis == "row":
				rotate_row(a,b)
			elif axis == "column":
				rotate_col(a,b)
	count_screen()
	print_screen()

def rect(a,b):
	for i in range(b):
		for j in range(a):
			screen[i][j] = 1

def rotate_row(a,b):
	row_size = len(screen[a])
	carry = 0
	for j in range(b):
		for i in range(row_size): 
			if i == 0:
				carry = screen[a][i]
				screen[a][i] = 0
			elif i == row_size -1:
				curr = screen[a][i]
				screen[a][i] = carry 
				if curr == 1:
					screen[a][0] = 1
			else:
				curr = screen[a][i]
				screen[a][i] = carry 
				carry = curr

def rotate_col(a,b):
	col_size = len(screen)
	carry = 0
	for j in range(b):
		for i in range(col_size):
			if i == 0:
				carry = screen[i][a]
				screen[i][a] = 0
			elif i == col_size -1:
				curr = screen[i][a]
				screen[i][a] = carry 
				if curr == 1:
					screen[0][a] = 1
			else:
				curr = screen[i][a]
				screen[i][a] = carry 
				carry = curr



def print_screen():
	for i in range(len(screen)):
		for j in range(len(screen[i])):
			#print(screen[i][j],end="")
			if screen[i][j] == 0:
				print(" ",end='')
			else:
				print("#",end='')
		print()

def count_screen():
	count = 0
	for i in range(len(screen)):
		for j in range(len(screen[i])):
			if(screen[i][j] == 1):
				count+=1	
	print(count)

if __name__ == "__main__":
	a()