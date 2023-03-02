# 횟수
# x,y,너비,높이
N=int(input())
arr = [[0]*1001 for _ in range(1001)]
for k in range(N): #y,x가 일반적이지만 반대여서 i,j위치 바꿈
    x, y, m, n = map(int, input().split())
    for j in range(m):
        for i in range(n):
            arr[y+i][x+j]=k+1 #더하는게 아니라 =으로 할당해야함


result=[]
for k in range(1,N+1):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
         #count 1부터 N까지를 출력하기
            if arr[i][j]==k:
                cnt+=1
    print(cnt)

