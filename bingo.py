N=10
lst =[1,2,3,8,0,9,9,0,8,4]

result=[]


for i in range(len(lst)-1):
    result.append(lst[i])
    if result[-1] == lst[i+1]:
        result.append(lst[i+1])
        del(result[-2])
        del (result[-1])
print(result)

