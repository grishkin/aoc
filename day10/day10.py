import sys
import re

instr = {}
bots = {}
outputs = {}
def a():
	lines = []
	for line in sys.stdin:
		lines.append(line)

	for line in lines:
		m = re.search(r'bot (.*) gives low to (.*) and high to (.*)',line)
		if m is not None:
			bot = m.group(1)

			low = m.group(2)
			high = m.group(3)
			instr[bot+"low"] = low
			instr[bot+"high"] = high

	for line in lines:
		m = re.search(r'value (.*) goes to bot (.*)',line)
		if m is not None:
			#print(m.group(1),m.group(2))
			value = m.group(1)
			to_bot = m.group(2)

			add_to_bot(to_bot,value)

			if len(bots[to_bot]) == 2:
				#this triggers a reaction
				overflowed = []
				overflowed.append(to_bot)
				while len(overflowed) != 0:
					to_clear = overflowed.pop()
					print(to_clear)
					bots[to_clear].sort()
					low = bots[to_clear][0] 
					high = bots[to_clear][1] 

					# if low == 17 and high == 61:
					# 	print ("the answer bot is",to_clear)
					# 	sys.exit()

					send_low_to = instr[to_clear+"low"]
					send_high_to = instr[to_clear+"high"]

					if re.search(r'output',send_low_to) is not None:
						send_low_to = send_low_to.split()[1]
						outputs[send_low_to] = low

					else:
						send_low_to = send_low_to.split()[1]
						add_to_bot(send_low_to,low)
						if len(bots[send_low_to]) == 2:
							overflowed.append(send_low_to)
					
					if re.search(r'output',send_high_to) is not None:
						outputs[send_high_to] = high
					else:
						send_high_to = send_high_to.split()[1]
						add_to_bot(send_high_to,high)
						if len(bots[send_high_to]) == 2:
							overflowed.append(send_high_to)

	print(bots)

	o0 = int(outputs['0'])
	o1 = int(outputs['1'])
	o2 = int(outputs['2'])
	print(o0*o1*o2)

def add_to_bot(bot,value):
	if bot not in bots:
		bots[bot] = []
	bots[bot].append(int(value))				

if __name__ == "__main__":
	a()