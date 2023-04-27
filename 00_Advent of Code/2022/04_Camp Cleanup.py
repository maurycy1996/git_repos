# %% Creating counter of cases
counter = 0

# Opening file

with open("04_input.txt", "r") as file:
    
# Clearing txt data
    for pair in file:
        pair_res = pair.strip().split(",")
        pair_list = []
        for elf in pair_res:
            elf_limits = elf.split("-")
            elf_set = set(range(int(elf_limits[0]), int(elf_limits[1]) + 1))
            pair_list.append(elf_set)
        
# Condition if sets ar subsets or supersets        
        
        if pair_list[0].issubset(pair_list[1]) or pair_list[0].issuperset(pair_list[1]):
            counter +=1

print(f"One of elves' duties are contained in other elf's duties in {counter} pairs.")

# %%