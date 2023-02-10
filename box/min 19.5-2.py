lst = [list(map(int, input().split())) for _ in range(5)]


def check(y,x):
    sum=0
    for i in range(-1,2):
        for j in range(-1,2):
            if 0<=(y+i) < 5 and 0<=(x+j)<4:
                sum = sum+lst[y+i][x+j]
    return sum

result = 0
for i in range(5):
    for j in range(4):
        if lst[i][j] ==1:
            if check(i,j) >1:
                result = 1
                break

if result ==1:
    print('불안정된 상태')
elif result ==0:
    print('안정된 상태')