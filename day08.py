import time
start_time = time.time()

#file = open("inputs/input_test.txt", "r")
file = open("inputs/input08.txt", "r")

#Dictionary to store the locations of the antennas
antennas = {}
antinodes = []

rows = 0
cols = 0
for line in file:
    line = line.rstrip()
    col = 0
    for c in line:
        if c != ".":
            if c in antennas:
                antennas[c].append([rows, col])
            else:
                antennas[c] = [[rows, col]]
        col += 1
    rows += 1
    cols = len(line)

def locate_antinodes(antenna_1, antenna_2):
    #Find the difference vector between the antinodes
    diff = [antenna_2[0] - antenna_1[0], antenna_2[1] - antenna_1[1]]
    #Subtract difference from antinode 1
    antinode_1 = [antenna_1[0] - diff[0], antenna_1[1] - diff[1]]
    #Add difference to antinode 2
    antinode_2 = [antenna_2[0] + diff[0], antenna_2[1] + diff[1]]
    return [antinode_1, antinode_2]

def new_locate_antinodes(antenna_1, antenna_2):
    #Find the difference vector between the antinodes
    diff = [antenna_2[0] - antenna_1[0], antenna_2[1] - antenna_1[1]]
    local_antinodes = [antenna_1.copy(), antenna_2.copy()]
    flag = True
    subtract_mode = True
    new_antinode = antenna_1.copy()
    while flag:
        # Add/subtract difference from current antinode
        new_antinode[0] = new_antinode[0] - (diff[0] if subtract_mode else -1 * diff[0])
        new_antinode[1] = new_antinode[1] - (diff[1] if subtract_mode else -1 * diff[1])

        if new_antinode[0] < 0 or new_antinode[0] >= rows or new_antinode[1] < 0 or new_antinode[1] >= rows:
            if subtract_mode:
                new_antinode = antenna_2.copy()
                subtract_mode = False
            else:
                flag = False
        else:
            local_antinodes.append(new_antinode.copy())

    return local_antinodes

def add_antinode(antinode):
    #Check if valid
    if not (antinode[0] < 0 or antinode[0] >= rows or antinode[1] < 0 or antinode[1] >= rows):
        #Add to list if not already there
        if not antinode in antinodes:
            antinodes.append(antinode)
    return

for char in antennas:
    for i in range(len(antennas[char])):
        antenna_1 = antennas[char][i]
        for j in range(i + 1, len(antennas[char])):
            antenna_2 = antennas[char][j]
            #local_antinodes = locate_antinodes(antenna_1, antenna_2)
            local_antinodes = new_locate_antinodes(antenna_1, antenna_2)
            for k in range(len(local_antinodes)):
                add_antinode(local_antinodes[k])

print(len(antinodes))

print("%s seconds" % (time.time() - start_time))