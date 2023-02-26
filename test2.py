<<<<<<< HEAD
T = 10
for tc in range(1, T + 1):
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

    ans=0
    for i in range(N):
        for j in range(N):
         ans+=check(i,j)
    print(f'#{tc} {ans}')
=======
#n개의 주사위를 던졌을 때 나올 수 있는 모든 경우를 출력해 주세요

n=int(input())
path=[0]*n
lst = [1,2,3,4,5,6]
def dice(level):
    if level == n:
        for i in range(n):
            print(path[i],end=' ')
        print()
        return
    for i in range(6):
        path[level] = lst[i]
        dice(level+1)

dice(0)
>>>>>>> 2ad82a1233bb3a66b5f1f43c907ca66d3e5207f9
