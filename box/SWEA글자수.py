T=int(input())
for tc in range(1,T+1):
    A=input()
    alpha=input()
    # 65~122
    bucket = [0]*130

    for i in range (len(alpha)):
        bucket[ord(alpha[i])]+=1

    change=[]
    for i in range(len(A)):
        change.append(ord(A[i]))

    result = []
    for i in change:
        result.append(bucket[i])

    MAX = -1
    for i in range(len(result)):
        if result[i]>MAX:
            MAX = result[i]
    print(f'#{tc} {MAX}')
