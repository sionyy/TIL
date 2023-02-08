# T = int(input())
# for test_case in range(1, T + 1):

K,N,M = map(int, input().split())
lst = list(map(int, input().split()))

result = K
count = 0
flag =0
count =0

for i in range(1, len(lst)):  # 조건1 : 최대 이동수를 넘었을 경우
    if lst[i] - lst[i - 1] > K:
        charge = 0
        flag = 1
        break

dummy = 0
while True:
    if flag == 1:
        break


    for i in range(len(lst) - 1, -1, -1):
        if result == lst[i]:
            result = result + K
            count += 1

    if result >= N:
        break
    dummy +=1
    if dummy ==20:
        result = result - 1


charge = count - 1
if flag == 1:
    charge = 0
print(charge)