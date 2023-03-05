N,M=map(int,input().split())
ylst=[]
xlst=[]
ysum=0
xsum=0
for i in range(M):
    y,x = map(int,input().split())
    ylst.append(y)
    xlst.append(x)
    ysum+=y
    xsum+=x

ymok=ysum//M
xmok=xsum//M

yans=0
xans=0
for i in range(M):
    yans+=abs(ymok-ylst[i])
    xans+=abs(xmok-xlst[i])
print(yans+xans)