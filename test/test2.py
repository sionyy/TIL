<<<<<<< HEAD
N=int(input())
lst=list(map(int,input().split()))

time=0
pl=1
mi=1
box=[]
while True:
    if len(lst)==1:
        box.append(1)
        break
    if lst[time] <= lst[time+1]:
        pl+=1
    elif lst[time]>lst[time+1]:
        box.append(pl)
        pl=1

    if lst[time] >= lst[time+1]:
        mi+=1
    elif lst[time]<lst[time+1]:
        box.append(mi)
        mi=1


    time+=1
    if time==N-1:
        box.append(pl)
        box.append(mi)
        break
print(max(box))
=======
mul=int(input()) #곱할 수

lst=[]
full=[]
eastlst=[]
westlst=[]
southlst=[]
northlst=[]
for i in range(6):
    di,num=map(int,input().split())
    if di == 1:
        lst.append(di)
        eastlst.append(num)
        full.append(num)
    elif di == 2:
        lst.append(di)
        westlst.append(num)
        full.append(num)
    elif di == 3:
        lst.append(di)
        southlst.append(num)
        full.append(num)
    elif di==4:
        lst.append(di)
        northlst.append(num)
        full.append(num)


def check():
    temp=[]
    for i in range(len(lst)):
        if lst[i] in temp:
            return i #num값,몇번째
        temp.append(lst[i])



MAX=sum(eastlst)*sum(northlst)
MIN=full[check()]*full[check()-1]
print((MAX-MIN)*mul)
>>>>>>> 2f308afbf96d6e859c02affaf8e7fa16231095ed
