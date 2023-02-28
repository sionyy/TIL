# N행 M열
"""
6 14
WWWWWWWWWWWWWW
WWRRWWBBBBBBWW
WRRRWWWBWWWWRB
WWBWBWWWBWRRRR
WBWBBWWWBBWRRW
WWWWWWWWWWWWWW
W W W W W W W W W W W W W W
W W R R W W B B B B B B W W
W R R R W W W B W W W W R B
W W B W B W W W B W R R R R
W B W B B W W W B B W R R W
W W W W W W W W W W W W W W
"""

N,M = map(int,input().split())
flag = [list(input()) for _ in range(N)]

resultW=[]
resultB=[]
resultR=[]
for i in range(N):
    resultW.append(M-flag[i].count('W')) #각 줄 아닌알파벳 숫자 세기
    resultB.append(M-flag[i].count('B'))
    resultR.append(M-flag[i].count('R'))
print(resultW)
print(resultB)
print(resultR)
