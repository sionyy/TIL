lst = ['A','B','C']
path = [0]*2
def abc(level):
    if level == 2:
        for i in range(2):
            print(path[i],end='')
        print()
        return
    for i in range(3):
        path[level] = lst[i]
        abc(level+1)
abc(0)

# 북 남 서 동 : 1/2/3/4
# 사각형을 생각하라
#
# 현재 = abs[위좌표 - 아래좌표]
# 반대 = abs[위좌표 - 아래좌표] + 현재 + 세로
# 옆 =