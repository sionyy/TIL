arr = [list(map(int, input().split())) for _ in range(100)]

totals = []
for i in range(100):
    total_r = 0
    for j in range(100):
        total_r += arr[i][j]
    totals.append(total_r)

for x in range(100):
    total_c = 0
    for y in range(100):
        total_c += arr[y][x]
    totals.append(total_c)

total_d1 = 0
for d1 in range(100):
    total_d1 += arr[d1][d1]
totals.append(total_d1)

total_d2 = 0
for d2 in range(100):
    total_d2 += arr[d2][99 - d2]
totals.append(total_d2)

max_val = totals[0]
for total in totals:
    if max_val < total:
        max_val = total