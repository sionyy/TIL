# N,K = map(int(input().split()))
N=5
K=3

arr = [[0,0,1,1,1],
       [1,1,1,1,0],
       [0,0,1,0,0],
       [0,1,1,1,1],
       [1,1,1,0,1]]

cnt=0
for i in range(N):
    for j in range(N-K+1):
        print(arr[i][j:j+3])