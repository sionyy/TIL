for tc in range(1,11):
    testcase = int(input())
    arr = [[0] + list(map(int, input().split()))+[0] for _ in range(100)]

    x=0
    for j in range(101):
        if arr[99][j] ==2:
            x = j

    y=99
    while y>0:
        if arr[y][x-1] ==0 and arr[y][x+1] ==0:
            arr[y][x] = 0
            y-=1
        elif arr[y][x-1] ==1 and arr[y][x+1] ==0:
            arr[y][x] = 0
            x-=1
        elif arr[y][x+1] ==1 and arr[y][x-1]==0:
            arr[y][x] = 0
            x+=1
    print(f'#{testcase} {x-1}')