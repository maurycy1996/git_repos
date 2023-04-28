# %% Part 1
cal = []

with open("01_input.txt", "r") as file:
    for line in file:
        line = line.strip()
        cal.append(line)

total_cal = []
per_elf = 0

for i in cal:
    if i:
        i = int(i)
        per_elf += i
    else:
        total_cal.append(per_elf)
        per_elf = 0
total_cal.append(per_elf)
  
print(max(total_cal))

# %% Part 2

print(sum(sorted(total_cal, reverse=True)[:3]))

# %%
