import random
x = 1000000
dict = {}

limit = int(input("What is the max number?: "))
for i in range(1,limit+1):
    dict[i] = 0

for _ in range(0, x):
    rollA = random.randint(1, limit)
    rollB = random.randint(1, limit)
    if rollA < rollB:
        if rollB in dict:
            dict[rollB] += 1

    elif rollA > rollB:
        if rollA in dict:
            dict[rollA] += 1
    else:
        if rollA in dict:
            dict[rollA] += 1

for i in range(1,limit+1):
    perc = dict[i]/x

    print(f"{i} | Times Rolled: {dict[i]} | Percentage: {perc:.5f} ")
             
    

