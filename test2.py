T = int(input())
for tc in range(1,T+1):
    N=int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    dy = [-1,-1,-1,0,0,1,1,1]
    dx = [-1,0,1,-1,1,-1,0,1]
    def find(y,x):
        cnt=0
        for i in range(8):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny<0 or nx<0 or ny>N-1 or nx>N-1 : continue
            if arr[y][x] < arr[ny][nx]:
                cnt+=1
        return cnt

    def MAXMIN(y,x):
        MAX=0
        MIN = 999
        for i in range(8):
            ny = y+dy[i]
            nx = x+dx[i]
            if ny < 0 or nx < 0 or ny > N - 1 or nx > N - 1: continue
            if arr[ny][nx] > MAX:
                MAX = arr[ny][nx]
            MIN = arr[y][x]
        return MAX-MIN

    result=[]
    ans=0
    for i in range(N):
        for j in range(N):
            if find(i,j) == 8:
                ans+=1
                result.append(MAXMIN(i,j))
    print(result)
    MAX =0
    for i in range(len(result)):
        if MAX < result[i]:
            MAX = result[i]
    print(f'#{tc} {ans} {MAX}')