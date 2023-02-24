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
print(ans)