arr = [list(input()) for _ in range(4)]

"""
[
[A_C]
[_K_]
[T__]
[___]
]
"""
for repeat in range(4):
    for j in range(3):
        for i in range(3,0,-1):
            if arr[i-1][j] !='_' and arr[i][j] !='_': continue
            if arr[i-1][j]!='_':
                arr[i][j] = arr[i-1][j]
                arr[i - 1][j] ='_'

for i in range(4):
    print(''.join(arr[i]))