import sys
def a():
	a,b,c,d = 0,0,1,0
	#print(a,b,c,d)
	instr = []
	for line in sys.stdin:
		instr.append(line.strip().split())
		#print(args)

	pc = 0 
	while pc < len(instr):
		curr = instr[pc]
		#print(curr)
		if curr[0] == "cpy":
			val1 = 0
			if curr[1] == 'a':
				val1 = a
			elif curr[1] == 'b':
				val1 = b
			elif curr[1] == 'c':
				val1 = c
			elif curr[1] == 'd':
				val1 = d
			else:
				val1 = int(curr[1])	

			if curr[2] == 'a':
				a = val1
			elif curr[2] == 'b':
				b = val1
			elif curr[2] == 'c':
				c = val1
			elif curr[2] == 'd':
				d = val1
			else:
				print("what the fuc")
		elif curr[0] == "inc":
			if curr[1] == 'a':
				a+=1
			elif curr[1] == 'b':
				b+=1
			elif curr[1] == 'c':
				c+=1
			elif curr[1] == 'd':
				d+=1
			else:
				print("what the fuck")
		elif curr[0] == "dec":
			if curr[1] == 'a':
				a-=1
			elif curr[1] == 'b':
				b-=1
			elif curr[1] == 'c':
				c-=1
			elif curr[1] == 'd':
				d-=1
			else:
				print("what the fuckl")
		elif curr[0] == "jnz":
			jump = False
			if curr[1] == 'a':
				if a != 0: jump = True
			elif curr[1] == 'b':
				#print(b)
				if b != 0: jump = True
			elif curr[1] == 'c':
				if c != 0: jump = True
			elif curr[1] == 'd':
				if d != 0: jump = True
			else:
				if int(curr[1]) != 0: jump  =True

			if jump== True:
				pc+=int(curr[2])
				continue
		else:
			print("what the fuck")
		pc+=1
	print(a)


#9227674

if __name__ == "__main__":
	a()