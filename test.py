N= int(input())
arr = [list(map(int, input().split()))for _ in range(N)]

# N = 5
# arr = [[2,5,4,3,6],
#        [7,1,5,1,8],
#        [4,2,6,2,5],
#        [1,9,5,8,3],
#        [5,3,7,6,8]]

dy = [-1,-1,-1,0,0,1,1,1]
dx = [-1,0,1,-1,1,-1,0,1]

def hole(y,x):
    sum = 0
    for i in range(8):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<N and 0<=nx<N:
            if arr[y][x] < arr[ny][nx]:
                sum +=1
    return sum


MAX = 0
sink = 0
box_MAX = []
for i in range(N):
    for j in range(N):
        if hole(i,j) == 8:
            sink+=1
            for k in range(8):
                if MAX < arr[i+dy[k]][j+dx[k]]:
                    MAX = arr[dy[k]][dx[k]]-arr[i][j]
                    box_MAX.append(MAX)

print(box_MAX)
MAXhole = 0
for i in range(len(box_MAX)):
    if MAXhole < box_MAX[i]:
        MAXhole = box_MAX[i]
print(sink, MAXhole)