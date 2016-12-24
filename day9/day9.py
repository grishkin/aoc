import sys
import re
def get_len(line,start,end):
	#for all children in this subset, call function recursively, and increment to next marker
	#print(line,start,end)
	print("this is my line",line[start:end])
	if re.search(r'\(',line[start:end]) is None:
		print("base is",end-start)
		return end - start

	i = start
	length = 0
	while(i < end):
		#(line[i])
		if line[i] == '(':
			#we have a marker
			j = i+1
			marker = ""
			while line[j] != ')':
				marker+=line[j]
				j+=1
			#print(marker)
			(a,b) = marker.split('x')

			new_start = len(marker) + i + 2
			new_end = new_start + int(a)
			print("recursing on",line[new_start:new_end],new_start,new_end)
			#print(int(b),"x",get_len(line,new_start,new_end))
			sub_len = get_len(line,new_start,new_end)
			print(sub_len,"x",int(b))
			length+= int(b) * sub_len
			i = new_end
			continue
		else:
			#we have a single character
			length+=1
		i+=1
	print("length of",line[start:end],"is",length)
	return length



if __name__ == "__main__":
	line = input()
	start = 0
	end = len(line)
	length = get_len(line,start,end)
	print(length)
