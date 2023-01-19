fruits=input().split(',')
result=[]
for i in fruits:
    i = i.lower()
    i = i.replace('rotten', '')
    result.append(i)
    
print(result)