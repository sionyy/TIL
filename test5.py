arr=[0]*200

def findboss(member):
    if arr[ord(member)]==0:
        return member
    result = findboss(arr[ord(member)])
    return result

def setunion(x, y):
    fa,fb= findboss(x), findboss(y)
    if fa==fb:
        return
    arr[ord(fb)]=fa

cnt=0
N=int(input())
for i in range(N):
    a,b = input().split()
    if findboss(a)!=findboss(b):
        setunion(a,b)
        cnt+=1

print(cnt)