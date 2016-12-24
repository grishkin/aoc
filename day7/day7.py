import sys
import re
def a():
	count = 0
	for line in sys.stdin:
		inbrack = re.sub(r'^[a-z]*\[',"|",line)
		inbrack = re.sub(r'\][^[]*\[',"|",inbrack)
		inbrack = re.sub(r'\].*$',"|",inbrack)
		contains = False
		for i in range(0,len(inbrack)):
			if (i+3) == len(inbrack):
				break
			if (inbrack[i] == inbrack[i+3]) and (inbrack[i+1] == inbrack[i+2]) and inbrack[i] != inbrack[i+1]:
				contains = True 
				break
		if contains == True:
			continue

		oldline = line
		line = re.sub(r'\[[^]]*\]',"|",line)
		contains = False
		for i in range(0,len(line)):
			if (i+3) == len(line):
				break
			if (line[i] == line[i+3]) and (line[i+1] == line[i+2]) and line[i] != line[i+1]:
				contains = True 
				break
		if contains == True:
			count+=1
	print(count)


def b():
	count = 0
	for line in sys.stdin:
		inbrack = re.sub(r'^[a-z]*\[',"|",line)
		inbrack = re.sub(r'\][^[]*\[',"|",inbrack)
		inbrack = re.sub(r'\].*$',"|",inbrack)
		babs = []
		for i in range(0,len(inbrack)):
			if (i+2) == len(inbrack):
				break
			if (inbrack[i] == inbrack[i+2]) and inbrack[i] != inbrack[i+1]:
				babs.append(inbrack[i]+inbrack[i+1]+inbrack[i+2])

		oldline = line
		line = re.sub(r'\[[^]]*\]',"|",line)
		for i in range(0,len(line)):
			if (i+3) == len(line):
				break
			if (line[i] == line[i+2]) and line[i] != line[i+1]:
				contains = True 
				invert = line[i+1] + line[i]+ line[i+1]
				if invert in babs:
					count+=1
					break
	print(count)

if __name__ == "__main__":
	b()