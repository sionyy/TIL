# K 가능 정류장 수
# N 종점
# M 정류장개수
K, N, M = map(int, input().split())
lst = list(map(int, input().split()))

result = 0
count = 0  # 정류장을 거친 횟수
flag = 0
while True:
    for i in range(1, len(lst)):  # 조건 1 : 최대 이동수를 넘었을 경우
        if lst[i] - lst[i - 1] > K:
            charge = 0
            flag = 1
            break

    for i in range(len(lst) - 1, -1, -1):
        if flag == 1:  # 조건 1을 위반했을 때
            break

        if len(lst) ==1:
            count +=1
            result = result + K
            break

        if lst[i] <= result + K:  # 최대이동수보다 같거나 많을때
            result = lst[i]
            lst = lst[i+1:]  # 위치를 i로 이동하고 charge+1
            count += 1
            if lst == []:
                result = result + K
                break


    if result >= N or flag == 1:  # 탈출조건
        break
print(count)