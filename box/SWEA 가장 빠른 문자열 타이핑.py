T = int(input())
for test_case in range(1, T + 1):
    A,B = list(map(str, input().split()))

    cnt = 0
    for i in range(len(A)):
        if A[i:len(B)+i] == B:
            cnt+=1
    result = len(A)-(cnt*(len(B)-1))
    print(f'#{test_case} {result}')