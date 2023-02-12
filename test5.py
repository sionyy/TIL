# 풀이 설계
# 각각의 범위에 대해 1을 할당
# 할당된값이 1을 넘을 경우 경우당 범위 1로 계산.
T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    lst = [list(map(int, input().split()))for _ in range(N)]
    MAP = [[0]*10 for _ in range(10)]

    # 각각 (x1,y1,x2,y2,color) 할당 완료

    cnt=0
    for k in range(N):
        for i in range(10):
            for j in range(10):
                if lst[k][1]<=i<=lst[k][3] and lst[k][0]<=j<=lst[k][2]:
                    if lst[k][4] == 1:
                        MAP[i][j] += 1
                    if lst[k][4] == 2:
                        MAP[i][j] += 2

    for i in range(10):
        for j in range(10):
            if MAP[i][j] ==3:
                    cnt+=1
    print(f'#{test_case} {cnt}')