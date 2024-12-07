file = open("inputs/input06.txt", "r")

#Create a list to store the grid, access with grid_list[row][col]
grid_list = []
#[row, col, dir]
guard_pos = []
row = 0
col = 0

for line in file:
    new_row = []
    line = line.rstrip()
    col = 0
    for c in line:
        if c == "^":
            new_row.append("X")
            guard_pos = [row, col, "up"]
        else:
            new_row.append(c)
        col += 1
    grid_list.append(new_row)
    row += 1

max_row = row - 1
max_col = col - 1

def copy_grid_list(grid_list):
    new_grid_list = []
    for i in range(len(grid_list)):
        new_grid_list.append(grid_list[i].copy())
    return new_grid_list

original_guard_pos = guard_pos.copy()
original_grid_list = copy_grid_list(grid_list)

def run_patrol(grid_list, guard_pos):
    flag = False
    loop = False
    visited_list = []
    j = 0
    while not flag:
        grid_list[guard_pos[0]][guard_pos[1]] = "X"
        if j > 10000:
            loop = True
            flag = True
        elif guard_pos[2] == "up":
            new_row = guard_pos[0] - 1
            new_col = guard_pos[1]
            if new_row < 0 or new_row > max_row or new_col < 0 or new_col > max_col:
                flag = True
            else:
                val = grid_list[new_row][new_col]
                if val == "#":
                    #Turn right
                    guard_pos[2] = "right"
                else:
                    #Move forward (up)
                    guard_pos = [new_row, new_col, guard_pos[2]]
        elif guard_pos[2] == "right":
            new_row = guard_pos[0]
            new_col = guard_pos[1] + 1
            if new_row < 0 or new_row > max_row or new_col < 0 or new_col > max_col:
                flag = True
            else:
                val = grid_list[new_row][new_col]
                if val == "#":
                    #Turn right
                    guard_pos[2] = "down"
                else:
                    #Move forward
                    grid_list[guard_pos[0]][guard_pos[1]] = "X"
                    guard_pos = [new_row, new_col, guard_pos[2]]
        elif guard_pos[2] == "down":
            new_row = guard_pos[0] + 1
            new_col = guard_pos[1]
            if new_row < 0 or new_row > max_row or new_col < 0 or new_col > max_col:
                flag = True
            else:
                val = grid_list[new_row][new_col]
                if val == "#":
                    #Turn right
                    guard_pos[2] = "left"
                else:
                    #Move forward
                    grid_list[guard_pos[0]][guard_pos[1]] = "X"
                    guard_pos = [new_row, new_col, guard_pos[2]]
        elif guard_pos[2] == "left":
            new_row = guard_pos[0]
            new_col = guard_pos[1] - 1
            if new_row < 0 or new_row > max_row or new_col < 0 or new_col > max_col:
                flag = True
            else:
                val = grid_list[new_row][new_col]
                if val == "#":
                    #Turn right
                    guard_pos[2] = "up"
                else:
                    #Move forward
                    grid_list[guard_pos[0]][guard_pos[1]] = "X"
                    guard_pos = [new_row, new_col, guard_pos[2]]
        j += 1
    print(j)
    return loop

run_patrol(grid_list, guard_pos)
visited_count = 0
for i in range(len(grid_list)):
    for j in range(len(grid_list[i])):
        print(grid_list[i])
        if grid_list[i][j] == "X":
            visited_count += 1

'''obstructions_count = 0

for i in range(len(grid_list)):
    for j in range(len(grid_list[i])):
        if i == 6 and j == 3:
            test = "test"
        #print(str(i) + "-" + str(j))
        new_grid_list = copy_grid_list(original_grid_list)
        new_guard_pos = original_guard_pos.copy()
        value = new_grid_list[i][j]
        if value == "." or value == "X":
            new_grid_list[i][j] = "#"
            if run_patrol(new_grid_list, new_guard_pos):
                obstructions_count += 1

print(obstructions_count)'''
