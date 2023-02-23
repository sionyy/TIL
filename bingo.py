arr = [list(map(int,input().split()))for _ in range(5)]
TRY = [list(map(int,input().split()))for _ in range(5)]
lst=[]
for x in range(5):
    for y in range(5):
        lst.append(TRY[x][y])


for k in range(25):
    for i in range(5):
        garosum = -1
        serosum = -1
        for j in range(5):
            if arr[i][j] == lst[k]:
                arr[i][j] = 0