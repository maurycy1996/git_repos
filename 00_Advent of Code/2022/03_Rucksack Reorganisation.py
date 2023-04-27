# %% Import modules

import string

# %% Creating priorities dictionary

letters = string.ascii_lowercase + string.ascii_uppercase

priors_rev = list(enumerate(letters, start=1))
priors = dict([(pair[1], pair[0]) for pair in priors_rev])

# %% Create set of items duplicating in rucksack compartments

itm = set()

with open("03_input.txt", "r") as file:
    for line in file:
        half = int((len(line)-1)/2)
        set1 = set(line[:half])
        set2 = set(line[half:])
        itm = itm.union(set1.intersection(set2))

# %% Summing up priorities of items

priors_sum = 0

for item in itm:
    priors_sum += priors[item]

print(f"The sum of item priorities is {priors_sum}")

# %%