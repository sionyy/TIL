T = int(input())
for test_case in range(1, T + 1):
    #N = 당근 수확 (5~1000)
    #C - 당근의 크기 (1~10)

    N = int(input())
    lst = list(map(int,input().split()))
    ans = 1
    cnt = 1

    lst.append(0)

    for i in range(N):
        if lst[i]<lst[i+1]:
            cnt+=1
            ans = cnt
        else:
            if ans<=cnt:
                ans = cnt
            cnt =1

    print(f'#{test_case} {ans}')