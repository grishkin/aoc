import sys
def update_pos(dist,direction,my_pos,locs):
    if direction == 'E':
        for i in range(dist):
            visited = [my_pos[0]+i,my_pos[1]]
            if visited in locs:
                print (visited)
                sys.exit()
            locs.append(visited)
        my_pos[0]+=dist
    elif direction == 'W':
        for i in range(dist):
            visited = [my_pos[0]-i,my_pos[1]]
            if visited in locs:
                print (visited)
                sys.exit()
            locs.append(visited)
        my_pos[0]-=dist
    elif direction == 'S':
        for i in range(dist):
            visited = [my_pos[0],my_pos[1]-i]
            if visited in locs:
                print (visited)
                sys.exit()
            locs.append(visited)
        my_pos[1]-=dist
    elif direction == 'N':
        for i in range(dist):
            visited = [my_pos[0],my_pos[1]+i]
            if visited in locs:
                print (visited)
                sys.exit()
            locs.append(visited)
        my_pos[1]+=dist
    return my_pos


if __name__ == "__main__":
    steps = input().strip().split(', ')
    numsteps = len(steps)
    my_map = [[0 for x in range(numsteps)] for y in range(numsteps)]

    my_pos = [0,0]
    my_dir = 'N'

    right_turn = {}
    right_turn['N'] = 'E'
    right_turn['E'] = 'S'
    right_turn['S'] = 'W'
    right_turn['W'] = 'N'

    left_turn = {}
    left_turn['N'] = 'W'
    left_turn['W'] = 'S'
    left_turn['S'] = 'E'
    left_turn['E'] = 'N'

    locs = []

    for step in steps:
        old_pos = my_pos
        if step[0] == 'L':
            new_dir = left_turn[my_dir]
        elif step[0] == 'R':
            new_dir = right_turn[my_dir]
        my_pos = update_pos(int(step[1:]),new_dir,my_pos,locs)
        my_dir = new_dir

