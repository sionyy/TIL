arr = [3,7,1,2]
sum =0

def abc(level):
    global sum
    if level ==3:
        print(sum,end=' ')
        return
    for i in range(4):
        sum+=arr[i]
        abc(level+1)
        sum -= arr[i]

abc(0)