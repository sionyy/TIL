# N : 배열범위
# M : 세기
N,M = map(int,input().split())
arr = [[1, 3, 3, 6, 7],
       [8, 13,9, 12,8],
       [4, 16,11,12,6],
       [2, 4, 1, 23,2],
       [9, 13,4, 7, 3]]

def killer(y,x):
    sum = 0
    for m in range(1,M+1):
        for i in range(4):
            directy = [-m,m,0,0]
            directx = [0,0,-m,m]
            if 0 <= directy[i]+y < N and 0 <= directx[i]+x < N:
                sum+=arr[directy[i]+y][directx[i]+x]
    return sum

def Xkiller(y,x):
    sum2 = 0
    for m in range(1,M+1):
        for i in range(4):
            Xdirecty = [-m,m,-m,m]
            Xdirectx = [-m,-m,m,m]
            if 0<=Xdirecty[i]+y<N and 0<=Xdirectx[i]+x<N:
                sum2 +=arr[Xdirecty[i]+y][Xdirectx[i]+x]
    return sum2

print(Xkiller(2,2))