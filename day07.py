import time
start_time = time.time()

file = open("inputs/input07.txt", "r")

#List of operations to
operations_list = []
#List of possible operations
operators = ["*", "+", "||"]
#Dictionary to store all possible combination of operators
operator_combinations = {}
success_sum = 0

for line in file:
    #Add each operation to a line in the operations_list in the form [value, [inputs]]
    operations_list.append([int(line.split(":")[0]), [int(elem) for elem in line.split(":")[1].split()]])

def list_all_operators(count, operators):
    all_operators = []
    operator_count = len(operators)
    #Get the list of all combinations of operators
    for i in range(pow(operator_count, count)):
        operator_list = []
        for j in range(count):
            power = pow(operator_count, count - j - 1)
            operator_list.append(operators[(i // power) % operator_count])
        all_operators.append(operator_list)
    return all_operators

#Loop through each set of operations
for i in range(len(operations_list)):
    final_value = operations_list[i][0]
    inputs = operations_list[i][1]

    #Get a list of all possible combinations of the operators, store it in a dictionary for future access
    if len(inputs) in operator_combinations:
        required_operators = operator_combinations[len(inputs)]
    else:
        required_operators = list_all_operators(len(inputs) - 1, operators)
        operator_combinations[len(inputs)] = required_operators

    #Apply the operators in order
    for j in range(len(required_operators)):
        calc_value = inputs[0]
        for k in range(len(required_operators[j])):
            if required_operators[j][k] == "*":
                calc_value = calc_value * inputs[k + 1]
            elif required_operators[j][k] == "+":
                calc_value = calc_value + inputs[k + 1]
            elif required_operators[j][k] == "||":
                calc_value = int(str(calc_value) + str(inputs[k + 1]))
        if calc_value == final_value:
            success_sum += final_value
            break

print(success_sum)
print("%s seconds" % (time.time() - start_time))