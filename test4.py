N = 9
lst = [7, 4, 2, 0, 0, 6, 0, 7, 0]
# lst = list(map(int, input().split()))

count =0
for i in range(N):
    for j in range(i+1,N):
        if