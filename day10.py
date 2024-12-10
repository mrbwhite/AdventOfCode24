import time
start_time = time.time()
def print_elapsed_time():
    elapsed_time = time.time() - start_time
    if elapsed_time < 0.1:
        print("%s ms" % float("%.3g" % (elapsed_time * 1000)))
    else:
        print("%s s" % float("%.3g" % elapsed_time))

#file = open("inputs/input_test.txt", "r")
file = open("inputs/input10.txt", "r")

#Create a list to store the grid, access with grid_list[row][col]
grid_list = []
for line in file:
    new_row = []
    line = line.rstrip()
    for c in line:
        new_row.append(int(c))
    grid_list.append(new_row)

reachable_nines = []
def add_reachable_nine(row, col):
    #Only add if the nine has not already been reached
    if not [row, col] in reachable_nines:
        reachable_nines.append([row, col])

def search_for_valid_next_step (row, col, value, running_total):
    #Up
    if row - 1 >= 0 and grid_list[row - 1][col] == value + 1:
        if value + 1 < 9:
            running_total = search_for_valid_next_step(row - 1, col, value + 1, running_total)
        else:
            add_reachable_nine(row - 1, col)
            running_total += 1
    # Right
    if col + 1 < len(grid_list[row]) and grid_list[row][col + 1] == value + 1:
        if value + 1 < 9:
            running_total = search_for_valid_next_step(row, col + 1, value + 1, running_total)
        else:
            add_reachable_nine(row, col + 1)
            running_total += 1

    # Down
    if row + 1 < len(grid_list) and grid_list[row + 1][col] == value + 1:
        if value + 1 < 9:
            running_total = search_for_valid_next_step(row + 1, col, value + 1, running_total)
        else:
            add_reachable_nine(row + 1, col)
            running_total += 1

    # Left
    if col - 1 >= 0 and grid_list[row][col - 1] == value + 1:
        if value + 1 < 9:
            running_total = search_for_valid_next_step(row, col - 1, value + 1, running_total)
        else:
            add_reachable_nine(row, col - 1)
            running_total += 1

    return running_total

def find_trailhead_scores(row, col):
    reachable_nines.clear()
    rating = search_for_valid_next_step(row, col, 0, 0)
    return [len(reachable_nines), rating]


score_sum = 0
rating_sum = 0
#Loop through each value and find starting values
for row in range(len(grid_list)):
    for col in range(len(grid_list[row])):
        if grid_list[row][col] == 0:
            return_list = find_trailhead_scores(row, col)
            score_sum += return_list[0]
            rating_sum += return_list[1]

print(score_sum)
print(rating_sum)

print_elapsed_time()