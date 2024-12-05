file = open("input04.txt", "r")

#Create a list to store the grid, access with grid_list[row][col]
grid_list = []
for line in file:
    new_row = []
    line = line.rstrip()
    for c in line:
        new_row.append(c)
    grid_list.append(new_row)

rows = len(grid_list)
cols = len(grid_list[0])
word_count = 0
word_count_2 = 0
search_word = ["X","M","A","S"]

for r in range(rows):
    for c in range(cols):
        if grid_list[r][c] == "A":
            if r > 0 and r < rows - 1 and c > 0 and c < rows - 1:
                flag = True
                diagonal_1 = grid_list[r - 1][c - 1] + "A" + grid_list[r + 1][c + 1]
                diagonal_2 = grid_list[r - 1][c + 1] + "A" + grid_list[r + 1][c - 1]
                if (diagonal_1 == "MAS" or diagonal_1 == "SAM") and (diagonal_2 == "MAS" or diagonal_2 == "SAM"):
                    word_count_2 += 1

        if grid_list[r][c] == "X":
            #Forward
            flag = True
            for a in range(1, 4):
                new_row = r
                new_col = c + a
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or grid_list[new_row][new_col] != search_word[a]:
                    flag = False
                    break
            if flag:
                word_count += 1

            #Backward
            flag = True
            for a in range(1, 4):
                new_row = r
                new_col = c - a
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or grid_list[new_row][new_col] != \
                        search_word[a]:
                    flag = False
                    break
            if flag:
                word_count += 1

            #Up
            flag = True
            for a in range(1, 4):
                new_row = r + a
                new_col = c
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or grid_list[new_row][new_col] != \
                        search_word[a]:
                    flag = False
                    break
            if flag:
                word_count += 1

            #Down
            flag = True
            for a in range(1, 4):
                new_row = r - a
                new_col = c
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or grid_list[new_row][new_col] != \
                        search_word[a]:
                    flag = False
                    break
            if flag:
                word_count += 1

            #Diagonal Up Right
            flag = True
            for a in range(1, 4):
                new_row = r + a
                new_col = c + a
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or grid_list[new_row][new_col] != \
                        search_word[a]:
                    flag = False
                    break
            if flag:
                word_count += 1

            # Diagonal Up Left
            flag = True
            for a in range(1, 4):
                new_row = r + a
                new_col = c - a
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or grid_list[new_row][new_col] != \
                        search_word[a]:
                    flag = False
                    break
            if flag:
                word_count += 1

            # Diagonal Down Right
            flag = True
            for a in range(1, 4):
                new_row = r - a
                new_col = c + a
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or grid_list[new_row][new_col] != \
                        search_word[a]:
                    flag = False
                    break
            if flag:
                word_count += 1

            # Diagonal Down Left
            flag = True
            for a in range(1, 4):
                new_row = r - a
                new_col = c - a
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or grid_list[new_row][new_col] != \
                        search_word[a]:
                    flag = False
                    break
            if flag:
                word_count += 1
print(word_count)
print(word_count_2)