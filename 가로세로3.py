N = 5
K = 3
arr = [[0,0,1,1,1],
       [1,1,1,1,0],
       [0,0,1,0,0],
       [0,1,1,1,1],
       [1,1,1,0,1]]


for i in range(N):
    arr[i] = arr[i]+[0]
arr = arr + [[0]*(N+1)]

# 가로탐색
# N만큼의 배열 / K 까지탐색 /
# K까지의 합이 K and x+1,K+1의합이 K!=라면 cnt+=1

# for i in range(N):
#     for j in range(N-K+1):
#         for s in range(K):
#             # if arr[i][j]