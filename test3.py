N = int(input())
arr = [list(input())+['.']*4 for _ in range(N)]
result = []
if N >= 5:
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                garo = 0
                sero = 0
                for k in range(5):
                    if arr[i][k] == 'o':
                        garo += 1
                    if arr[k][i] == 'o':
                        sero += 1
                result.append(garo)
                result.append(sero)

                crossL = 0
                crossR = 0
                for k in range(5):
                    try:
                        if arr[i+k][j+k] == 'o':
                            crossL += 1
                    except IndexError:
                        pass
                    try:
                        if arr[i+k][j-k]=='o':
                            crossR += 1
                    except IndexError:
                        pass
                result.append(crossL)
                result.append(crossR)
print(set(result))
print(result)