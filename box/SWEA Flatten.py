T = 10
for test_case in range(1, T + 1):

    N = int(input())  # 리스트 원소 개수
    lst = list(map(int, input().split()))

    for i in range(N):
        MAXX = int(-21e8)
        MAXi = 0
        MINN = int(21e8)
        MINi = 0
        for j in range(len(lst)):
            if lst[j] > MAXX:
                MAXX = lst[j]
                MAXi = j
        for k in range(len(lst)):
            if lst[k] < MINN:
                MINN = lst[k]
                MINi = k
        lst[MAXi] = lst[MAXi] - 1
        lst[MINi] = lst[MINi] + 1


    resultMAX=-99999999
    resultMIN= 99999999

    for i in range(len(lst)):
        if lst[i]>resultMAX:
            resultMAX=lst[i]
        if lst[i]<resultMIN:
            resultMIN = lst[i]

    result = resultMAX-resultMIN

    print(f'#{test_case} {result}')
