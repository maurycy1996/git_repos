# %% Creating list of rounds from txt file

match = []

with open("02_input.txt", "r") as file:
    for line in file:
        round = []
        for i in line:
            if i.isalpha():
                round.append(i)
        match.append(round)

match
    
# %%

def pts(x, y):
    
    wins = [["X", "C"], ["Y", "A"], ["Z", "B"]]
    draws = [["X", "A"], ["Y", "B"], ["Z", "C"]]
    
    shp = 0
    res = 0
    
    if y == "X":
        shp = 1
    elif y == "Y":
        shp = 2
    elif y == "Z":
        shp = 3
    
    if [y, x] in draws:
        res = 3
    elif [y, x] in wins:
        res = 6
    else:
        res = 0 

    return shp + res
    
# %%

for round in match:
    points = pts(round[0], round[1])
    print(points)


# %%
