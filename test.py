<<<<<<< HEAD
MAP =[[3,5,1],
      [3,8,1],
      [1,1,5]]

bit = [list(map(int, input().split()))for _ in range(2)]
allbit = bit[0]+bit[1]

dy = [0,0,1,1]
dx = [0,1,0,1]

def masking(y,x):
    sum = 0
=======
lst = [list(map(int, input().split())) for _ in range(5)]
>>>>>>> c7f82a5702d3cf9fab3f6e67b4f589ad8587a5ab

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if allbit[i] == True:
            if 0<=ny<3 and 0<=nx<3:
                sum = sum+MAP[ny][nx]
    return sum

<<<<<<< HEAD
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
=======
def check(y,x):
    sum=0
    for i in range(-1,2):
        for j in range(-1,2):
            if 0<=(y+i) < 5 and 0<=(x+j)<4:
                sum = sum+lst[y+i][x+j]
    return sum

result = 0
for i in range(5):
    for j in range(4):
        if lst[i][j] ==1:
            if check(i,j) >1:
                result = 1
                break

if result ==1:
    print('불안정된 상태')
elif result ==0:
    print('안정된 상태')
>>>>>>> c7f82a5702d3cf9fab3f6e67b4f589ad8587a5ab
