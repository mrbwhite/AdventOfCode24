file = open("input05.txt", "r")

rules = []
updates = []
mode = 1
sum_total = 0
new_sum_total = 0

#Create a list of rules and updates
for line in file:
    line = line.rstrip()
    if line == "":
        mode = 2
    elif mode == 1:
        rules.append([int(x) for x in line.split("|")])
    elif mode == 2:
        updates.append([int(x) for x in line.split(",")])

def checkValidUpdate(update):
    for i in range(len(update)):
        value = update[i]
        j = 0
        while j < len(rules):
        #for j in range(len(rules)):
            if rules[j][0] == value or rules[j][1] == value:
                #Return false if any rules are violated
                try:
                    if update.index(rules[j][0]) > update.index(rules[j][1]):
                        return False
                except:
                    pass
            j += 1
    #Return true if none of this previous rules have been violate
    return True

def correctInvalidUpdate(update):
    invalid_rules = []
    #for i in range(len(update)):
    i = 0
    while i < len(update):
        value = update[i]
        i += 1
        j = 0
        while j < len(rules):
        #for j in range(len(rules)):
            try:
                # Set values
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
                        i = 0
                        break
                        #invalid_rules.append(rules[j])
            except:
                pass
            j += 1

    return update

#Loop through all of the updates, adding valid updates to a new list
for i in range(len(updates)):
    if checkValidUpdate(updates[i]):
        sum_total += updates[i][len(updates[i]) // 2]
    else:
        new_update = correctInvalidUpdate(updates[i])
        new_sum_total += new_update[len(new_update) // 2]

print(sum_total)
print(new_sum_total)