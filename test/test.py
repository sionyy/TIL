import sys
input = sys.stdin.readline

N=int(input())
lst=[]
lst2=[]
for i in range(N):
    lst.append(int(input()))

lst2=lst[:]
lst2.sort()
#lst=[10,1,5,2,3]
#lst=[1,2,3,5,10]

ans=1
for i in range(len(lst)-1,0,-1):
    if lst==lst2:
        break
    ans+=1
    for j in range(i):
        if lst[i] == lst2[i]:
            break
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(ans)