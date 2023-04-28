# %% Creating empty lists of steps, stack symbols and levels
steps = []
stacks = []
levels = []

# Opening an input file
with open("05_input.txt", "r") as file:
    for line in file:
        # Filling the steps list with integers in sublists
        if line.startswith("move"):
            words = line.strip().split()[1::2]
            words = [int(word) for word in words]
            steps.append(words)
        # Filling the stacks list with integers corresponding to stack number
        elif line.strip().replace(" ", "").isnumeric():
            line = line.strip().replace(" ", "")
            for stack in line:
                stacks.append(int(stack))
        # Filling hte levels list witch supply symbols (with blanks)
        elif line != "\n":
            symbols = []
            for smb in line[1::4]:
                symbols.append(smb)
            levels.append(symbols)

# Creating an empty dictionary of stacks (k) and its supplies (v)
supplies = {stack: [] for stack in stacks}

# Converting list of levels to list of supplies in each stack and getting rid
# of blanks
for level in levels:
    index = 1
    for supp in level:
        if supp.isalpha():
            supplies[index].append(supp)
        index +=1
    index = 1

# Reversing supplies in each stacks (they were swapped before)
for k in supplies:
    supplies[k] = supplies[k][::-1]

# Applying steps
for step in steps:
    for i in range(step[0]):
        mv = supplies[step[1]].pop()
        supplies[step[2]].append(mv)

# Printing uppermost supply from each stack
for stack in supplies:
    print(supplies[stack][-1], end="")

# %%
