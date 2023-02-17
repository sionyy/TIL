#싱크홀의 개수와 높이차이를 하나의 함수로 표현하려고 하니 안돼서
#싱크홀을 구하고 싱크홀 주변값을 탐색해보았습니다.

def hole(y, x):  # 주변보다 높은 수의 갯수를 구하기
    check = 0
    for i in range(8):  # len(dy)
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if arr[y][x] < arr[ny][nx]:
                check += 1
    return check

T=int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    dy = [-1,-1,-1,0,0,1,1,1]
    dx = [-1,0,1,-1,1,-1,0,1]

    MAX=int(-21e8)
    result = []
    sink =0 # 싱크홀의 갯수

    for i in range(N):
        for j in range(N):
            if hole(i,j) ==8: #주변보다 높은 수의 갯수가 8이라면
                sink+=1 #싱크홀이다
                for k in range(8): #싱크홀일때 탐색
                    if MAX < arr[i+dy[k]][j+dx[k]]:
                        MAX = arr[i+dy[k]][j+dx[k]]
                        result.append(MAX-arr[i][j]) #중심부보다 크다면 MAX값-중심부로 list에 담는다

    MAX_sink =int(-21e8)
    for i in range(len(result)):
        if MAX_sink < result[i]:
            MAX_sink = result[i]


    print(f'#{tc} {sink} {MAX_sink}')