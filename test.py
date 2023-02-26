#n개의 주사위를 던졌을 때 나올 수 있는 모든 경우를 출력해 주세요

n=int(input())
path=[0]*n
lst = [1,2,3,4,5,6]
def dice(level):
    if level == n:
        for i in range(n):
            print(path[i],end=' ')
        print()
        return
    else:
        for i in range(6):
            path[level] = lst[i]
            dice(level+1)

dice(0)