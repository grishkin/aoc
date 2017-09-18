def a():
	curr = '10010000000110000'
	limit = 35651584
	while len(curr) < limit:
		curr = dragon(curr)
		if len(curr) > limit:
			curr = curr[:limit]
			break
	#print(curr)

	#curr = '110010110100'
	xsum = checksum(curr)
	while len(xsum)%2 == 0:
		xsum = checksum(xsum)
	print(xsum)


def checksum(num):
	i = 0 
	curr = list(num)
	xsum = ""
	while i < len(curr)-1:
		if curr[i] == curr[i+1]:
			xsum+='1'
		else:
			xsum+='0'
		i+=2
	return xsum



def dragon(init):
	init_bin = string_to_bin(init)
	a = init_bin
	b = list(a)[2:]
	b.reverse()
	b = "".join(b)
	flipped = ['1' if x == '0' else '0' for x in b]
	flipped = "".join(flipped)
	result = init + '0' + flipped
	return result

def string_to_bin(my_str):
	init_int = int(my_str,2)
	init_bin = bin(init_int)
	return init_bin

if __name__ == "__main__":
	a()

