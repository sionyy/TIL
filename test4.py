lst = list(input())
st = '78ATQP'

result = []
plus =''
for i in range(len(st)):
    for j in range(len(st)-1,-1,-1):
        plus+=st[j]
        result.append(plus)
print(result)