import sys
def a():
	i = 0
	for line in sys.stdin:
		line = line.strip()
		sides = list(map(int,line.split()))
		if sides[0] + sides[1] <= sides[2]:
			continue
		if sides[1] + sides[2] <= sides[0]:
			continue
		if sides[0] + sides[2] <= sides[1]:
			continue
		i+=1
	print(i)

def b():
	cols = [[],[],[]]
	for line in sys.stdin:
		line = line.strip()
		nums = list(map(int,line.split()))
		cols[0].append(nums[0])
		cols[1].append(nums[1])
		cols[2].append(nums[2])
	tripcount = 0
	sides = []
	validcount = 0
	print(cols[1])
	for i in range(0,len(cols)):
		for j in cols[i]:
			sides.append(j)
			tripcount+=1
			if tripcount == 3:
				if sides[0] + sides[1] <= sides[2]:
					pass
				elif sides[1] + sides[2] <= sides[0]:
					pass
				elif sides[0] + sides[2] <= sides[1]:
					pass
				else:
					validcount+=1
				tripcount = 0
				sides = []

	print(validcount)


if __name__ == "__main__":
	b()