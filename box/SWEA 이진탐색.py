T=int(input())
for test_case in range(1,T+1):
    N,Atarget,Btarget = map(int,input().split()) #총 페이지 수
    data = list(range(N+1))

    def bin(target,data):
        cnt = 0
        left = 1
        right = len(data)-1

        while left <= right:
            mid = (left+right)//2
            cnt+=1

            if data[mid] == target:
                return cnt
            elif data[mid] < target:
                left = mid
            else:
                right = mid
        return False


    print(f'#{test_case}',end=' ')
    if bin(Atarget,data)<bin(Btarget,data):
        print('A')
    elif bin(Atarget,data)>bin(Btarget,data):
        print('B')
    else:
        print(0)

