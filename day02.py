#Read Input File
file = open("input02.txt", "r")

def check_if_valid_digits(diff, increasing):
    # Check each criteria to not be safe, same value, more than 3 and not increasing/decreasing as required
    if diff == 0 or abs(diff) > 3 or (increasing and diff < 0) or (not increasing and diff > 0):
        return False
    else:
        return True

def check_if_valid_list(values):
    safe = True
    problem_count = 0
    # Check if increasing or decreasing
    increasing = int(values[1]) > int(values[0])
    for i in range(len(values)):
        if safe and i < len(values) - 1:
            diff = int(values[i + 1]) - int(values[i])
            if not check_if_valid_digits(diff, increasing):
                safe = False

    return safe

safe_count = 0

for line in file:
    values = line.split()
    #Check whole list
    if check_if_valid_list(values):
        safe_count += 1
    else:
        #If not safe, remove each value in turn and recheck the list
        for i in range(len(values)):
            new_values = values.copy()
            new_values.pop(i)
            if check_if_valid_list(new_values):
                #If any instance found to be true, increment the count and stop checking
                safe_count += 1
                break

print(safe_count)