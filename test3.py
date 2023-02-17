from collections import deque
arr=[[0,1,1,0],
     [0,0,1,1],
     [0,0,0,1],
     [0,0,0,0]]
name = ['A','B','C','D']
answer = []
used = [0]*4

def bfs(st):
    global answer
    q = deque()
    q.append(st)
    while q:
        now=q.popleft()
        answer.append(name[now])
        for i in range(4):
            if arr[now][]