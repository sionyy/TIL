<<<<<<< HEAD
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
=======
MAP = [[3,5,1],[3,8,1],[1,1,5]]

bittary = [list(map(int, input().split()))for _ in range(2)]


def happy(y,x):

    for i in range(2):
        for j in range(2):
            sum = sum + MAP[y+i][x+j]

#
# MAX = int(-21e8)
#
# for i in range(3):
#     for j in range(3):
#         if happy(i,j) > MAX:
#             MAX = happy(i,j)
#             if MAX == happy(i,j):
#                 MAXI = i
#                 MAXJ = j
# print(f'({MAXI},{MAXJ})')
>>>>>>> c7f82a5702d3cf9fab3f6e67b4f589ad8587a5ab
