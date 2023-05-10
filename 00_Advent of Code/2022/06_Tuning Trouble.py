code_list = []

with open("06_input.txt", "r") as file:
    for line in file:
        for letter in line:
            code_list.append(letter)

counter = 0
code = []

for letter in code_list:
    counter += 1
    if len(code) < 4:
        code.append(letter)
    else:
        code.append(letter)
        code.remove(code[0])
    if len(set(code)) == 4:
        print(counter)
        print(code)
        break