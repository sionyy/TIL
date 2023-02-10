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
