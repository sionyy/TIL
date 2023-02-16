# N = 배열판
# M = 글자수

# N,M= map(int, input().split())
# lst = [input() for _ in range(N)]

N = 20
M = 13

lst = [input() for _ in range(M)]

for i in range(N):
    for j in range(N-M+1):
        if lst[i][j:j+M]