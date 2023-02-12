# 풀이 설계
# 모든 BLUE와 RED의 좌표를 각각 하나의 배열에 할당한다.
# 2개의 배열로 PURPLE좌표를 구한다.
# 각각의 색을 MAP에 1을 더한 후 값이 2라면 겹친영역
T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    MAP = [[0] * 10 for _ in range(10)]

    # 각각의 좌표 하나의 배열에 할당
    ALLBLUE = [0] * 5
    ALLRED = [0] * 5
    for i in range(N):
        if lst[i][4] == 1:
            for k in range(4):
                ALLBLUE[k] = ALLBLUE[k] + lst[i][k]
        elif lst[i][4] == 2:
            for k in range(4):
                ALLRED[k] = ALLRED[k] + lst[i][k]
    ALLBLUE[4] = 1
    ALLRED[4] = 1
    # 각각 (x1,y1,x2,y2,color) 할당 완료

    count = 0
    for i in range(10):
        for j in range(10):
            if ALLBLUE[0] <= i <= ALLBLUE[2] and ALLBLUE[1] <= j <= ALLBLUE[3]:
                MAP[i][j] += 1
            if ALLRED[0] <= i <= ALLRED[2] and ALLRED[1] <= j <= ALLRED[3]:
                MAP[i][j] += 1
            if MAP[i][j] > 1:
                count += 1
    print(f'#{test_case} {count}')