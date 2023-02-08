lst = [7, 4, 2, 0, 0, 6, 0, 7, 0]

Max = 0
for i in range(len(lst)):  # 버켓생성을 위한  최대값 구하기
    if lst[i] > Max:
        Max = lst[i]

bucket = [0] * (Max + 1)

for i in range(len(lst)):  # 버켓에 데이터 담기
    bucket[lst[i]] += 1

