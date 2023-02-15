# N 수열의 길이
T = int(input())
for test_case in range(1,T+1):

    N = int(input())
    lst = list(map(int, input()))

    lst.append(0)
    result = []
    cnt = 1

    for i in range(N):
        if lst[i] and lst[i + 1] == 1:
            cnt += 1
            if lst[i] and lst[i + 2] != 1:
                result.append(cnt)
                cnt = 1


    result.append(1)

    MAX = 0
    for i in range(len(result)):
        if result[i] > MAX:
            MAX = result[i]

    print(f'#{test_case} {MAX}')