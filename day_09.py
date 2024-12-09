import time
start_time = time.time()
def print_elapsed_time():
    elapsed_time = time.time() - start_time
    if elapsed_time < 0.1:
        print("%s ms" % float("%.3g" % (elapsed_time * 1000)))
    else:
        print("%s s" % float("%.3g" % elapsed_time))

input_text = open("inputs/input_test.txt", "r").read()
#input_text = open("inputs/input09.txt", "r").read()
disk = []
id = 0
#set the mode [0 - file, 1 - space]
mode = 0

for c in input_text:
    if mode == 0:
        for i in range(int(c)):
            disk.append(id)
        mode = 1
        id += 1
    else:
        for i in range(int(c)):
            disk.append("")
        mode = 0

flag_1 = True
flag_2 = True
end_pos = len(disk)
start_pos = 0
decompress_mode = 1
id -= 1

if decompress_mode == 0:
    while flag_1:
        end_pos -= 1
        flag_2 = True
        if start_pos >= end_pos:
            flag_1 = False
        elif disk[end_pos] != "":
            #Find next available space
            while flag_2:
                if disk[start_pos] == "":
                    disk[start_pos] = disk[end_pos]
                    disk[end_pos] = ""
                    flag_2 = False
                start_pos += 1
elif decompress_mode == 1:
    while id >= 0:
        #Get index of first and last instance of the id
        start_pos = disk.index(id)
        end_pos = len(disk) - 1 - disk[::-1].index(id)
        count = end_pos - start_pos + 1
        #Search from the left to find a place that will take it
        counter = 0
        space_start_pos = 0
        flag = False
        for i in range(start_pos):
            if disk[i] == "":
                if counter == 0:
                    space_start_pos = i
                counter += 1
                if counter >= count:
                    #Add the value in
                    for j in range(count):
                        disk[space_start_pos + j] = id
                        disk[start_pos + j] = ""
                    break
            else:
                counter = 0
        id -= 1

check_sum = 0
for i in range(len(disk)):
    if disk[i] == "":
        value = 0
    else:
        value = disk[i]
    check_sum += i * value

print(check_sum)

print_elapsed_time()