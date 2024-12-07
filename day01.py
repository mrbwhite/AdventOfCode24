#Read Input File
file = open("inputs/input01.txt", "r")

difference = 0
similarity_score = 0
left_list = []
right_list = []

#Create arrays
for line in file:
    values = line.split()
    if len(values) >= 2:
        left_list.append(int(values[0]))
        right_list.append(int(values[1]))

left_list.sort()
right_list.sort()

#Iterate through left list and calculate values
for i in range(len(left_list)):
    difference += abs(right_list[i] - left_list[i])
    left_val = left_list[i]
    count = 0
    #Check count in right list
    for j in range(len(right_list)):
        if left_val == right_list[j]:
            count += 1
    similarity_score += left_val * count
    count = 0

print("Difference: " + str(difference))
print("Similarity: " + str(similarity_score))