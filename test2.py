lst = [65000, 35, 42, 70,70, 35, 65000, 1300,65000, 30000, 38, 42]

bucket = [0] * 65001

for i in range(len(lst)):
    bucket[lst[i]] += 1

