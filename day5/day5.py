import hashlib

my_input = "wtnhxymk"
def a():
	i = 0
	pw = ""
	while True:
		door_string = my_input+str(i)
		#find the MD5 has of this
		m = hashlib.md5()
		m.update(door_string.encode())
		digest = m.hexdigest()
		#print(digest)
		#print(str(digest))
		#break
		if digest[:5] == "00000":
			next_char = digest[5]
			pw += next_char
			print("door string "+door_string,"digest" + digest[:5] + next_char, "pw "+pw)
			if len(pw) == 8:
				break
		i+=1
	print(pw)

def b():
	i = 0
	pw = [" "," "," "," "," "," "," "," "]
	print (pw)
	while True:
		door_string = my_input+str(i)
		#find the MD5 has of this
		m = hashlib.md5()
		m.update(door_string.encode())
		digest = m.hexdigest()
		#print(digest)
		if digest[:5] == "00000":
			print("door string "+door_string,"digest" + digest[:7])
			pos_of_digest = digest[5]
			if pos_of_digest.isdecimal() == False:
				i+=1
				continue
			else:
				pos_of_digest = int(digest[5])
			next_char = digest[6]
			if pos_of_digest <= 7 and pw[pos_of_digest] == " ":
				pw[int(pos_of_digest)] = next_char
				print(pw)
			else:
				i+=1
				continue
		else:
			i+=1
			continue
		fin = True
		for char in pw:
			if char == " ":
				fin = False
		if fin == True:
			break
		i+=1
	print(pw)




if __name__ == "__main__":
	b()


#76301cc0