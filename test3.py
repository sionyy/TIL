n = 3
card = ['A', 'B', 'C', 'D']
path = [0] * n


def abc(level):
    if level == n:
        for i in range(n):
            print(path[i], end=' ')
        print()
        return

    for i in range(4):
        if level>0 and path[level-1] >= card[i] : continue
        path[level] = card[i]
        abc(level + 1)
        path[level] = ''

abc(0)
