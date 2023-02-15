A=input()
alpha=input()
# 65~122
bucket = [0]*130

for i in range (len(alpha)):
    bucket[ord(alpha[i])]+=1

for i in range (len(bucket)):
    print(i,bucket[i],end=' ')
    print()

change=[]
for i in range(len(A)):
    change.append(ord(A[i]))
# [69, 79, 71, 71, 88, 89, 80, 86, 83, 89]

result = []
for i in change:
    result.append(bucket[i])

MAX = -1
for i in range(len(result)):
    if result[i]>MAX:
        MAX = result[i]
print(MAX)