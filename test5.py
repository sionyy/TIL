K,N,M = map(int, input().split())
lst = list(map(int, input().split()))

result = K
count = 0
flag =0
for i in range(1, len(lst)):  # 조건1 : 최대 이동수를 넘었을 경우
    if lst[i] - lst[i - 1] > K:
        charge = 0
        flag =1
        break