MAP =[[3,5,1],
      [3,8,1],
      [1,1,5]]

bit = [list(map(int, input().split()))for _ in range(2)]
allbit = bit[0]+bit[1]

dy = [0,0,1,1]
dx = [0,1,0,1]

def masking(y,x):
    sum = 0

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if allbit[i] == True:
            if 0<=ny<3 and 0<=nx<3:
                sum = sum+MAP[ny][nx]
    return sum

MAX = int(-21e8)
MAXI = int(-21e8)
MAXJ = int(-21e8)
for i in range(3):
    for j in range(3):
        if masking(i,j)> MAX:
            MAX = masking(i,j)
            MAXI = i
            MAXJ = j

print(f'({MAXI},{MAXJ})')