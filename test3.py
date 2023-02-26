<<<<<<< HEAD
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def check(y, x):
    sum = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny<0 or nx<0 or ny>N-1 or nx>N-1:continue
        sum += abs(arr[y][x] - arr[ny][nx])
    return sum

print(check(0,0))
ans=0
for i in range(N):
    for j in range(N):
     ans+=check(i,j)

=======
lst = [110,70,10]

Q = int(input()) #총돈

result =[]
for i in range(3):
    if Q%lst[i] ==0:
        result.append(lst[i])

print(result)
ans=0
for i in range(3):
    if Q % result[0] == 0:
        ans = int(Q/result[0])
    else:
        if Q < 70:
            ans = Q//10
        elif Q < 110:
            ans = (Q-70)//10 +1
        else:
            a = Q//110
            b = (Q-110*a)//70
            c = (Q-110*a-70*b)//10
            ans = a+b+c
>>>>>>> 2ad82a1233bb3a66b5f1f43c907ca66d3e5207f9
print(ans)