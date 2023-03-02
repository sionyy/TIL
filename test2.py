from collections import deque
n=int(input())
arr=[[0]*n for _ in range(n)]
y,x=map(int,input().split())

arr[y][x]=1

q=deque()
q.append([y,x])

directy=[-1,1,0,0]
directx=[0,0,-1,1]
answer=0
while q:
    now =q.popleft()
    y,x=now[0],now[1]
    for i in range(4):
        dy=y+directy[i]
        dx=x+directx[i]
        if 0<=dy<n and 0<= dx<n:
            if arr[dy][dx]==0:
                arr[dy][dx]=arr[y][x]+1
                answer=arr[dy][dx]
                q.append([dy,dx])

print(answer)