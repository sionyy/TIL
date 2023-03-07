T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[input() for _ in range(N)]
    result=[]
    if N>=5:
        for i in range(N):
            for j in range(N):
                    if arr[i][j] =='o':
                        garo=0
                        sero=0
                        crossL =0
                        crossR =0
                        for k in range(5):
                            if arr[i][k] =='o':
                                garo+=1
                            if arr[k][i] =='o':
                                sero+=1
                            if arr[k][k] == 'o':
                                crossL +=1
                            if arr[k][5-k-1] == 'o':
                                crossR +=1
                        result.append(garo)
                        result.append(sero)
                        result.append(crossL)
                        result.append(crossR)
            # print(result)
        if 5 in result:
            ans = 'YES'
        else:
            ans = 'NO'
        print(f'#{tc} {ans}')