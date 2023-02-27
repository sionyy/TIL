"""
A 10
B 7
C 5

AAAAAAAAAA
BBBBBBBCCC
CC
"""

full=''
N=int(input())
for i in range(N):
    alpha,num = map(str,input().split())
    full+=alpha*int(num)

for i in range(len(full)):
    print(full[i],end='')
