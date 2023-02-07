arr = [
    [65000, 35, 42, 70],
    [70, 35, 65000, 1300],
    [65000, 30000, 38, 42]
]

Max = int(-21e8)
for i in range(3):
    for j in range(4):
        if arr[i][j]>Max:
            Max = arr[i][j] # 65000

bucket = [0]*(Max+1)

for i in range(3):
    for j in range(4):
        bucket[arr[i][j]]+=1

bucketMax = int(-21e8)
for i in range(len(bucket)):
    if bucket[i] > bucketMax:
        bucketMax = bucket[i]

for i in range(len(bucket)): #버킷의 최대값인 3
    if bucketMax == bucket[i]:
        print(i)

