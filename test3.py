N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def check(y, x):
    sum = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny<0 or nx<0 or ny>N-1 or nx>N-1:continue
        sum += abs(arr[y][x] - arr[ny][nx])
    return sum

print(check(0,0))
ans=0
for i in range(N):
    for j in range(N):
     ans+=check(i,j)

print(ans)