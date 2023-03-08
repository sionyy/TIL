# 세로 R
# 가로 C
result=[]
def check(y1,x1,y2,x2,y3,x3,y4,x4):
    for i in range(y2-y1+1):
        for j in range(x1,x2+1):
            arr[i][j]+=1
    for i in range(y4-y3+1):
        for j in range(x3,x4+1):
            arr[i][j]+=1

    for i in range(MAXX):
        for j in range(MAXX):
            if arr[i][j]==2:
                if arr[i+2][j+2] ==2 or arr[i+2][j-2]==2 or arr[i-2][j+2] ==2 or arr[i-2][j-2] ==2:
                    return result.append('a')
                if arr[i+1][j] ==2 or arr[i-1][j]==2 or arr[i][j+1]==2 or arr[i][j-1] == 2:
                    return result.append('b')
                if arr[i+1][j+1] ==2 or arr[i+1][j-1]==2 or arr[i-1][j+1] ==2 or arr[i-1][j-1] ==2:
                    return result.append('c')
    return result.append('d')

for repeat in range(4):
    y1,x1,y2,x2,y3,x3,y4,x4=map(int,input().split())
    MAXX = max(y1,x1,y2,x2,y3,x3,y4,x4)+1

    arr=[[0]*MAXX for _ in range(MAXX)]
    check(y1,x1,y2,x2,y3,x3,y4,x4)

print(result)

