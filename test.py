T=int(input())
for tc in range(1,T+1):
    A = input()
    B = input()

    result = 0
    if (A in B) == True:
        result = 1
    else:
        result =0

    print(f'#{tc} {result}')