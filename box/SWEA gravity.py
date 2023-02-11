T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))



    MAX = int(-21e8)
    ans=[]
    for i in range(len(lst)):
        count = 0
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                count+=1
        ans.append(count)

    MAXANS = int(-21e8)
    for i in range(len(ans)):
        if MAXANS < ans[i]:
            MAXANS = ans[i]


    print(f'#{test_case} {MAXANS}')