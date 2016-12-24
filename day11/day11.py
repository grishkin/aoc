import copy
import pprint
import functools
import queue
import math
import re
@functools.total_ordering
class State:
    def __init__(self,my_floors,curr_floor,g,h,prev,is_two = False):
        self.my_floors = my_floors
        self.curr_floor = curr_floor
        self.g = g
        self.h = h
        self.prev = prev
        self.is_two = False
    def __lt__(self,other):
        return self.g + self.h< other.g+ other.h
    def __le__(self,other):
        return self.g+ self.h <= other.g+other.h
    def __eq__(self,other):
        return self.g + self.h== other.g + other.h
    def __ne__(self,other):
        if other is None and self is None:
            return False 
        if other is None or self is None:
            return True
        return self.g + self.h != other.g + other.h
    def __gt__(self,other):
        return self.g  + self.h>= other.g + other.h
    def __ge__(self,other):
        return self.g + self.h >= other.g + other.h

def h(my_map):
    dist = 0
    # for floor in my_map:
    #     dist += num_loose(floor)

    if len(my_map[2]) == 1:  
        dist+=1
    else:
        dist+=math.ceil((len(my_map[2])/2))*(1)*5 

    if len(my_map[1]) == 1:  
        dist+=1
    else:
        dist+=math.ceil((len(my_map[1])/2))*(2)*5

    if len(my_map[0]) == 1:  
        dist+=1
    else:   
        dist+=math.ceil((len(my_map[0])/2))*(3)*5
    return dist

def a():
    # floors = []
    # floors.append(["t-g","t-m","p-g","s-g","e-g","e-m","d-g","d-m"])
    # floors.append(["p-m","s-m"])
    # floors.append(["pr-m","pr-g","r-g","r-m"])
    # floors.append([])

    floors = []
    floors.append(["t-g","t-m","p-g","s-g"])
    floors.append(["p-m","s-m"])
    floors.append(["pr-m","pr-g","r-g","r-m"])
    floors.append([])


    # floors = []
    # floors.append(["h-m","l-m"])
    # floors.append(["h-g"])
    # floors.append(["l-g"])
    # floors.append([])

    for floor in floors:
        print(is_valid_floor(floor))

    init_state = State(copy.deepcopy(floors),0,0,h(floors),None)
    #get_moves(init_state)
    q = queue.PriorityQueue()
    q.put(init_state)
    visited = []
    exp = 0
    while not q.empty():
        exp+=1
        curr_state = q.get()
        visited.append(curr_state)
        if is_goal(curr_state):
            print("huh?")
            print("expanded",exp)
            print(curr_state.g)
            print(curr_state.h)
            #pprint.pprint(curr_state.my_floors)
            path = []
            curr = curr_state

            while curr != None:
                #pprint.pprint (curr.my_floors)
                path.append(curr)
                curr = curr.prev
            path.reverse()
            for p in path:
                pprint.pprint(p.my_floors)
            break
        print(curr_state.g)
        print(curr_state.h)
        pprint.pprint(curr_state.my_floors)
        moves = get_moves(curr_state)
        for move in moves:
            if not is_dup(visited,move):
                q.put(move)    


def is_goal(state):
    if state.my_floors[0] == [] and state.my_floors[1] == [] and state.my_floors[2] == []:
        return True
    return False


def num_loose(floor):
    loose_count = 0
    for item in floor:
        is_loose = True
        e_type = element_type(item)
        i_type = item_type(item)
        for other in floor:
            if element_type(other) == e_type and item_type != i_type:
                is_loose = False
        if is_loose == True:
            loose_count+=1
    return loose_count


def is_dup(states,state):
    #return False
    dup = False
    for expanded in states:
        if state.my_floors == expanded.my_floors and state.curr_floor == expanded.curr_floor and state.g >= expanded.g:
            #print("duped")
            # print("my state")
            # pprint.pprint(state)
            # print("visited state")
            # pprint.pprint(expanded.my_floors)
            return True
    #return dup

    all_items = state.my_floors[0] + state.my_floors[1] + state.my_floors[2] + state.my_floors[3]
    
    for item in all_items:
        e = element_type(item)
        for other in all_items:
            if element_type(other) == e:
                continue
            temp_map = copy.deepcopy(state.my_floors)
            o = element_type(other)    
            for i in range(len(temp_map)):
                temp_map[i] = ['x-r' if x == e+"-r" else x for x in temp_map[i]]
                temp_map[i] = ['x-g' if x == e+"-g" else x for x in temp_map[i]]

            for i in range(len(temp_map)):
                temp_map[i] = [e+"-r" if x == o+"-r" else x for x in temp_map[i]]
                temp_map[i] = [e+"-g" if x == o+"-g" else x for x in temp_map[i]]

            for i in range(len(temp_map)):
                temp_map[i] = [o+"-r" if x == "x-r" else x for x in temp_map[i]]
                temp_map[i] = [o+"-g" if x == "x-g" else x for x in temp_map[i]]

            for floor in temp_map:
                floor.sort()
            for floor in state.my_floors:
                floor.sort()
            # print("replaced")    
            # pprint.pprint(temp_map)
            # print("original")
            # pprint.pprint(state)

            # if state.my_floors == temp_map and state.curr_floor == expanded.curr_floor and state.g >= expanded.g:
            #     #print ("yo")
            #     continue

            for expanded in states:
                if temp_map == expanded.my_floors and state.curr_floor == expanded.curr_floor and state.g >= expanded.g:
                    print("hey its a dup")
                    return True

                    # print("my state")
                    # pprint.pprint(temp_map)
                    # print("visited state")
                    # pprint.pprint(expanded.my_floors)
    return dup

def get_moves(state):
    up = -1
    down = -1
    if state.curr_floor != 3:
        up = state.curr_floor + 1
    if state.curr_floor != 0:
        down = state.curr_floor -1


    if len(state.my_floors[0]) == 1:
        up = -1

    if len(state.my_floors[1]) == 1 and state.curr_floor > 1 and len(state.my_floors[0]) == 0:
        up = -1


    if down == 0 and len(state.my_floors[0]) == 0:
        down = -1
    if down == 1 and len(state.my_floors[0]) == 0  and len(state.my_floors[1]) == 0:
        down = -1

    #if down == 1 and len(state.my_floors[0]) == 0 len(state.my_floors[1]) == 0:
    #    down = -1

    states = []
    my_map = copy.deepcopy(state.my_floors)

    pairs = set()
    for item in my_map[state.curr_floor]:
        for other in my_map[state.curr_floor]:
            if other == item:
                continue
            pairs.add(tuple(sorted([item,other])))

    if up != -1:
        for item in pairs:
            my_map[up].append(item[0])
            my_map[up].append(item[1])
            my_map[state.curr_floor] = [x for x in my_map[state.curr_floor] if x != item[0] and x!= item[1]]
            my_map[up].sort()
            my_map[state.curr_floor].sort()
            if is_valid_floor(my_map[state.curr_floor]) and is_valid_floor(my_map[up]):
                s = State(copy.deepcopy(my_map),up,state.g + 1,h(my_map),state)
                states.append(s)
            my_map = copy.deepcopy(state.my_floors)

        for item in my_map[state.curr_floor]:
            my_map[up].append(item)
            my_map[state.curr_floor] = [x for x in my_map[state.curr_floor] if x != item]

            my_map[up].sort()
            my_map[state.curr_floor].sort()

            if is_valid_floor(my_map[state.curr_floor]) and is_valid_floor(my_map[up]):
                s = State(copy.deepcopy(my_map),up,state.g + 1 ,h(my_map),state)
                states.append(s)
            my_map = copy.deepcopy(state.my_floors)


    if down != -1:
        for item in pairs:
            my_map[down].append(item[0])
            my_map[down].append(item[1])
            my_map[state.curr_floor] = [x for x in my_map[state.curr_floor] if x != item[0] and x!= item[1]]
            my_map[down].sort()
            my_map[state.curr_floor].sort()
            if is_valid_floor(my_map[state.curr_floor]) and is_valid_floor(my_map[down]):
                s = State(copy.deepcopy(my_map),down,state.g + 1,h(my_map),state)
                states.append(s)
            my_map = copy.deepcopy(state.my_floors)

        for item in my_map[state.curr_floor]:
            my_map[down].append(item)
            my_map[state.curr_floor] = [x for x in my_map[state.curr_floor] if x != item]

            my_map[down].sort()
            my_map[state.curr_floor].sort()

            if is_valid_floor(my_map[state.curr_floor]) and is_valid_floor(my_map[down]):
                s = State(copy.deepcopy(my_map),down,state.g + 1 ,h(my_map),state)
                states.append(s)
            my_map = copy.deepcopy(state.my_floors)
    return states

def item_type(string):
    return string.split('-')[1]

def element_type(string):
    return string.split('-')[0]

def is_valid_floor(floor):
    floor_gen = False
    for item in floor:
        if item_type(item) == 'g':
            floor_gen = True
            break
    rogue_chip = False
    for item in floor:
        if item_type(item) == 'm':
            has_gen = False
            for other in floor:
                if item_type(other) == 'g' and element_type(other) == element_type(item):
                    has_gen = True
            if has_gen == False:
                rogue_chip = True
                break

    if floor_gen and rogue_chip:
        return False
    else:
        return True

def finished():
    if len(floors[0]) == 0 and len(floors[1]) == 0 and len(floors[2]) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    a()
