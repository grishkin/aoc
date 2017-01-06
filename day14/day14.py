import hashlib
import re
import sys
def a():
	salt_letters = "cuanljph"
	i = 0
	key_count = 0
	keys = []
	hashes = []
	while True:
		my_hash = hashlib.md5(bytearray(salt_letters+str(i),"utf-8")).hexdigest()
		for j in range(0,2016):
			my_hash = hashlib.md5(bytearray(my_hash,"utf-8")).hexdigest()

		seqs = get_seqs(my_hash)
		hashes.append(seqs)
		for seq in seqs:
			if seq[0] == 5:		
				if i < 1000:
					start = 0
				else:
					start = i-1000
				for n in range(start,i):
					for m in range(0,len(hashes[n])):
						if hashes[n][m][0] == 3 and hashes[n][m][1] == seq[1]:
							print(hashes[n],hashes[i])
							key_count+=1

							exists = False
							for key in keys:
								if key[0] == n:
									exists = True
									break
							if exists == False:
								keys.append((n,i))
							if len(keys) == 64:
								print(sorted(keys))
								print(n)
								sys.exit()
							break
		if key_count > 63:
			print("done")
			print(sorted(keys))
			sys.exit()

		i+=1


def get_seqs(line):
	prev_char = ''
	tripcount = 0 
	trip_found = False
	seqs = []
	for char in line:
		if prev_char == '': 
			prev_char = char
			continue
		if prev_char == char:
			tripcount+=1
		else:
			tripcount = 0

		if tripcount == 2 and trip_found == False:
			seqs.append((3,prev_char))
			trip_found = True
		if tripcount == 4:
			seqs.append((5,prev_char))

		prev_char = char
	return seqs


if __name__ == "__main__":
	#l = [1,2,3,4]
	#print(l[0:3+1])
	a()
	# for i in range(0,5):
	# 	print(i)