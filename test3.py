arr = [list(map(int,input().split())) for _ in range(5)]

for i in range(5):
    summ = 0
    for j in range(5):
        summ += arr[j][i]
    print(summ)