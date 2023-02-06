lst = [['F','E','W'],['D','C','A']]

st = input()


def findCh(T):
    flag = 0
    for i in range(2):
        for j in range(3):
            if lst[i][j] == T:
                flag = flag+1
                result = '발견'
            else:
                result = '미발견'
        if flag==1:
            break
    return result

print(findCh(st))