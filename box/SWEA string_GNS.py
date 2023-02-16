T=int(input())
for tc in range(1,T+1):
    du,mmy = map(str, input().split())
    lst = list(input().split())
    NUM = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']


    result =[]
    for i in range(len(NUM)):
        for j in range(len(lst)):
            if NUM[i] == lst[j]:
                result.append(lst[j])

    print(f'#{tc}',end=' ')
    print(*result)