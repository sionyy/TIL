T = int(input())
for test_case in range(1, T + 1):

    MAP = [[0]*10 for _ in range(10)]

    def boom(y1, x1, y2, x2, col):
        for i in range(y2-y1+1):
            for j in range(x2-x1+1):
                if col == 1:
                    MAP[i+y1][j+x1] += 1
                if col == 2:
                    MAP[i+y1][j+x1] += 2
        return

    N = int(input())
    check = [list(map(int,input().split())) for _ in range(N)]

    for i in range(N):
        boom(check[i][0],check[i][1],check[i][2],check[i][3],check[i][4])


    cnt =0
    for i in range(10):
        for j in range(10):
            if MAP[i][j] == 3:
                cnt+=1

    print(f'#{test_case} {cnt}')