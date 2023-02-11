T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))



    MAX = int(-21e8)
    for i in range(len(lst)):
        if MAX < lst[i]:
            MAX = lst[i]

    result = []
    for i in range(len(lst)):
        if MAX == lst[i]:
            result = lst[i:]
            break

    count = 0
    for i in range(len(result)):
        if result[i] != MAX:
            count+=1
    # print(f'#{test_case} {count}')