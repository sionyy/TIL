T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split()))for _ in range(N)]

    for i in range(N):
        arr[i] = arr[i]+[0]
    arr = arr + [[0]*(N+1)]

    # 가로탐색
    # N만큼의 배열 / K 까지탐색 /
    # K까지의 합이 K and x+1,K+1의합이 K!=라면 cnt+=1

    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt+=1
            if arr[i][j] ==0:
                cnt =0
            if cnt > K:
                cnt =0
            if cnt ==K and arr[i][j+1]==0:
                cnt =0
                result+=1

    Hresult = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt+=1
            if arr[j][i] ==0:
                cnt = 0
            if cnt > K:
                cnt = 0
            if cnt ==K and arr[j+1][i]==0:
                cnt =0
                Hresult+=1
    print(f'#{tc} {result+Hresult}')
