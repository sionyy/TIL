N=int(input())

lst=[]
abslst=[]
for i in range(N):
    lst.append(int(input()))
    abslst.append(abs(lst[-1]))
    if len(lst)==0:
        print(0)
    elif lst[-1]==0:
        for i in range(len(abslst)):
            if min(abslst)==abslst[i]:
                print(lst[i])
                del lst[i]
                del abslst[i]