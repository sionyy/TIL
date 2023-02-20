arr = [list(map(int, input().split())) for _ in range(100)]
x = 0

for j in range(100):
    if arr[99][j] == 2:
        x = j
