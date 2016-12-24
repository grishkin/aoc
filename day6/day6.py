import sys
def a():
	#[ for i in ]
	cols = {}
	for line in sys.stdin:
		line = line.strip()
		chars = list(line)
		#print (chars)
		for i in range(0,len(chars)):
			if str(i) in cols:
				cols[str(i)].append(chars[i])
			else:
				cols[str(i)] = [chars[i]]
	#print(cols)
	for i in range(0,len(cols)):
		curr_col = cols[str(i)]
		curr_freq = {}
		for char in curr_col:
			if char in curr_freq:
				curr_freq[char]+=1
			else:
				curr_freq[char] = 1
		tups = [(key,curr_freq[key]) for key in sorted(curr_freq,key=curr_freq.get,reverse = True)]
		print(i, tups[-1][0])

if __name__ == "__main__":
	a()