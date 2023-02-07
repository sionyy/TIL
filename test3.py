arr = [
    [65000, 35, 42, 70],
    [70, 35, 65000, 1300],
    [65000, 30000, 38, 42]
]

Max = -int(21e8)  # arr Max값 구하기
for y in range(len(arr)):
    for x in range(len(arr[y])):
        if arr[y][x] > Max:
            Max = arr[y][x]

cnt = [0] * (Max + 1)  # bucket 값 등록 (MAX+1)
for y in range(3):
    for x in range(4):
        cnt[arr[y][x]] += 1


Max = -int(21e8)    #가장 많이 등록된 값 찾기
for i in range(len(cnt)):
    if cnt[i] > Max:
        Max = cnt[i]


lst = []
for i in range(len(cnt)):
    if cnt[i] == Max:
        lst.append(i)

print(*lst)
