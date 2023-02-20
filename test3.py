T = 10
for test_case in range(1, T + 1):
    nnnnnn = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    x = 0

    for j in range(100):
        if arr[99][j] == 2:
            x = j

    y = 99
    while True:
        if x == 99:
            while True:
                if arr[y][x - 1] == 0:
                    arr[y][x] = 0
                    y -= 1
                    if y == 0:
                        break
                else:
                    arr[y][x] = 0
                    x -= 1
                    break
        if x == 0:
            while True:
                if arr[y][x + 1] == 0:
                    arr[y][x] = 0
                    y -= 1
                    if y == 0:
                        break
                else:
                    arr[y][x] = 0
                    x += 1
                    break

        while True:
            if y == 0:
                break
            if arr[y][x - 1] == 0 and arr[y][x + 1] == 0:
                arr[y][x] = 0
                y -= 1

            elif (arr[y][x - 1] == 1 and arr[y][x] == 1) or (arr[y][x + 1] == 1 and arr[y][x] == 1):
                break

        if y == 0:
            break

        if x < 100 and arr[y][x + 1] == 1:
            while True:
                if x < 99 and arr[y][x + 1] == 1:
                    arr[y][x] = 0
                    x += 1
                else:
                    arr[y][x] = 0
                    y -= 1
                    break

        if x > -1 and arr[y][x - 1] == 1:
            while True:
                if x > 0 and arr[y][x - 1] == 1:
                    arr[y][x] = 0
                    x -= 1
                else:
                    arr[y][x] = 0
                    y -= 1
                    break
        if y == 0:
            break
    print(f'#{test_case} {x}')