T= int(input())
for tc in range(1,T+1):

    N= int(input())
    lst = list(map(int, input().split()))
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]


    result = []
    start =0
    end =-1
    while True:
        result.append(lst[end])
        result.append(lst[start])
        end = end-1
        start = start + 1
        if start == 5 and end == -6:
            break
    print(f'#{tc}',end = ' ')
    print(*result)