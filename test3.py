<<<<<<< HEAD
arr = [[3, 3, 5, 3, 1],
       [2, 2, 4, 2, 6],
       [4, 9, 2, 3, 4],
       [1, 1, 1, 1, 1],
       [3, 3, 5, 9, 2]]

dy = [1,1,-1,-1]
dx = [-1,1,-1,1]   #왼오왼오

# y,x = map(int,input().split())

def getsum(y,x):
    sum = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<= ny < 5 and 0 <= nx < 5:
            sum = sum + arr[ny][nx]
    return  sum

result =[]
for i in range(4):
    for j in range(4):
        result.append(getsum(i,j))


# Max = 0
# for i in result:
#     if i > Max:
#         Max = i

for i in range(4):
    for j in range(4):
        if getsum(i,j) == 24:
            print(i,j)

# print(Max)
=======
pattern = [list(map(str, input())) for _ in range(2)]
print(pattern[0])
>>>>>>> c7f82a5702d3cf9fab3f6e67b4f589ad8587a5ab
