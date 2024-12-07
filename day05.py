import time
start_time = time.time()

file = open("inputs/input05.txt", "r")

rules = []
updates = []
mode = 1
valid_sum_total = 0
invalid_sum_total = 0

#Create a list of rules and updates
for line in file:
    line = line.rstrip()
    if line == "":
        mode = 2
    elif mode == 1:
        rules.append([int(x) for x in line.split("|")])
    elif mode == 2:
        updates.append([int(x) for x in line.split(",")])

def check_valid_update(update):
    for i in range(len(update)):
        value = update[i]
        for j in range(len(rules)):
            if rules[j][0] == value or rules[j][1] == value:
                #If there is a relevant rule check if it's followed
                try:
                    if update.index(rules[j][0]) > update.index(rules[j][1]):
                        return False
                except:
                    pass
    #Return true if none of this previous rules have been violated
    return True

def correct_invalid_update(update):
    i = 0
    while i < len(update):
        value = update[i]
        i += 1
        for j in range(len(rules)):
            try:
                # For each rule check if it's followed, if a violated rule is found then switch the positions and recheck from the start
                value_1 = rules[j][0]
                value_2 = rules[j][1]
                if value_1 == value or value_2 == value:
                    # Set postions
                    pos_1 = update.index(value_1)
                    pos_2 = update.index(value_2)
                    if pos_1 > pos_2:
                        #Switch positions
                        update[pos_1] = value_2
                        update[pos_2] = value_1
                        #Force restart
                        i = 0
                        break
            except:
                pass

    return update

#Loop through the updates, adding valid updates to a new list
for i in range(len(updates)):
    if check_valid_update(updates[i]):
        valid_sum_total += updates[i][len(updates[i]) // 2]
    else:
        new_update = correct_invalid_update(updates[i])
        invalid_sum_total += new_update[len(new_update) // 2]

print(valid_sum_total)
print(invalid_sum_total)
print("%s seconds" % (time.time() - start_time))