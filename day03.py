input_text = open("inputs/input03.txt", "r").read()
sum_total = 0
enabled = True

for i in range(len(input_text)):
    if input_text[i:i + 4] == "do()":
        enabled = True
    elif input_text[i:i + 7] == "don't()":
        enabled = False
    if input_text[i:i + 4] == "mul(":
        pointer = i + 4
        for k in range(8):
            if pointer + k < len(input_text) and input_text[pointer + k] == ")":
                values = input_text[pointer:pointer + k].split(",")
                if enabled and len(values) == 2 and values[0].isdigit() and values[1].isdigit():
                    sum_total += int(values[0]) * int(values[1])
                break

print("Sum: " + str(sum_total))

