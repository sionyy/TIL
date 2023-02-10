lst = list(map(int, input().split()))

numlst=[[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10,11,12],
        [13,14,15,16]]
zerolst = [[0]*4 for _ in range(4)]

for k in range(len(lst)):
    for i in range(4):
        for j in range(4):
            if numlst[i][j] == lst[k]:
                zerolst[i][j] = k+1

for i in range(4):
    for j in range(4):
        print(zerolst[i][j],end=' ')
    print()


