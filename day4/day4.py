import sys
import re
#name, sector ID and checksum
def a():
	room_sum = 0
	for line in sys.stdin:
		line = line.strip()
		(room,checksum) = line.split("[")
		checksum = checksum[:-1]
		elems = room.split("-")
		room_id = int(elems[-1])
		room_name = "".join(elems[:-1])
		if is_valid(room_name,checksum):
			room_sum+=room_id
	print(room_sum)

def is_valid(name,checksum):
	freq = {}
	for char in name:
		if char in freq:
			freq[char]+=1
		else:
			freq[char] = 1

	freq_reverse = {}
	for key in freq:
		letter = key
		num_times = str(freq[key])
		if str(freq[key]) in freq_reverse:
			freq_reverse[num_times].append(letter)
		else:
			freq_reverse[str(freq[key])] = [key]

	
	thing = [(k, sorted(freq_reverse[k])) for k in sorted(freq_reverse, reverse=True)]
	#print(thing)
	my_checksum = []
	total = []
	for i in thing:
		total += i[1]
	my_checksum = "".join(total)
	my_checksum = my_checksum[:5]
	if checksum == my_checksum:
		return True
	else:
		return False



def b():
	for line in sys.stdin:
		line = line.strip()
		(room,checksum) = line.split("[")
		checksum = checksum[:-1]
		elems = room.split("-")
		room_id = int(elems[-1])
		room_name = "".join(elems[:-1])
		if is_valid(room_name,checksum):
			#find the name
			actual_name = ""
			for letter in room_name:
				value = ord(letter)
				value = value%97
				value += room_id
				value %= 26
				value += 97
				shifted = chr(value)
				actual_name += shifted
			#print(actual_name)
			if re.search(r'north',actual_name) is not None:
				print (actual_name,room_id)



if __name__ == "__main__":
	#a()
	b()