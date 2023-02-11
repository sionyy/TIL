<<<<<<< HEAD
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
=======
arr = [3,7,1,2]
sum =0

def abc(level):
    global sum
    if level ==3:
        print(sum,end=' ')
        return
    for i in range(4):
        sum+=arr[i]
        abc(level+1)
        sum -= arr[i]

abc(0)
>>>>>>> c7f82a5702d3cf9fab3f6e67b4f589ad8587a5ab
