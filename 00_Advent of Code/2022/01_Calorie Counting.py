# %% 1
cal = []

with open("01_calories.txt", "r") as file:
    for i in file:
        i = i[:-1]
        cal.append(i)

# %% 2

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
  
print(f"The calory-richest elf has a total of {max(total_cal)} calories on the"\
      " expedition.")
        
# %%
