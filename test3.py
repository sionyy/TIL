arr = [list(map(int,input().split())) for _ in range(100)]

garosum=0
serosum=0
LXsum=0
RXsum=0
result=[]
for i in range(100):
    garosum=0
    serosum=0
    for j in range(100):
        garosum+=arr[i][j]
        serosum+=arr[j][i]
    result.append(garosum)
    result.append(serosum)
    LXsum+=arr[i][i]
    RXsum+=arr[4-i][i]
    result.append(LXsum)
    result.append(RXsum)
ans =max(result)
print(ans)