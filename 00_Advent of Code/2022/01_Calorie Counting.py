# %%
cal = []

with open("00_Advent of Code/2022/01_calories.txt", "r") as file:
    for i in file:
        i = i[:-1]
        cal.append(i)

# %%

total_cal = []
per_elf = 0

for j in cal:
    if j:
        j = int(j)
        per_elf += j
    else:
        total_cal.append(per_elf)
        per_elf = 0
total_cal.append(per_elf)
  
print(f"The calory-richest elf has a total of {max(total_cal)} calories on the"\
      " expedition.")
        
# %%
