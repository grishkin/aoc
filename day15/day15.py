import sys,re, copy
def a():
	discs = {}
	for line in sys.stdin:
		m = re.search(r'Disc #(.*) has (.*) positions; at time=0, it is at position (.*)\.',line)
		no,num_positions,pos = int(m.group(1)),int(m.group(2)),int(m.group(3))
		discs[no] = [num_positions,pos,0]

	while True:
		discs_copy = copy.deepcopy(discs)
		if can_pass(discs_copy):
			print("wew lad")
			print(discs[1][2])
			sys.exit()
		else:
			discs = inc_pos(discs)

	
def inc_pos(discs):
	for key in discs:
		disc = discs[key]
		#add wraparound
		if disc[1] + 1 == disc[0]:
			disc[1] = 0
			disc[2]+=1
		else:
			disc[1]+=1
			disc[2]+=1
	return discs

def can_pass(discs):
	#print(discs)
	curr_disc = 1
	discs = inc_pos(discs)
	disc_pos = discs[curr_disc][1]
	while curr_disc < 7:
		curr_disc+=1
		discs = inc_pos(discs)
		new_disc_pos = discs[curr_disc][1]
		if new_disc_pos != disc_pos:
			return False
		else:
			disc_pos = new_disc_pos
	return True

if __name__ == "__main__":
	a()