lst = [['_', '_', '_', '_', '_'],
       ['_', '_', '_', '_', '_'],
       ['_', '_', '_', '_', '_'],
       ['_', '_', '_', '_', '_']]


y,x = map(int, input().split())
y1,x1 = map(int, input().split())
dy = [1,1,1,0,0,-1,-1,-1]
dx = [-1,0,1,-1,1,-1,0,1] #왼중오 / 왼 오 / 왼중오


def boom(y,x):
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<= ny < 4 and 0<=nx < 5:
            lst[ny][nx] = '#'
    return lst

boom(y,x)
boom(y1,x1)

for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j], end = ' ')
    print()