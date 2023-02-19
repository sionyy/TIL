T = int(input())
for tc in range(1,T+1):

#0초일때 0개 / 2초일때 2개 / 4초일때 4개 / 6초일 때 6개
#0초일때 0개 / 2초일때 1개 / 4초일때 2개 / 6초일 때 3개
# N명의 사람 / M시간 마다 / K개의 붕어빵

    N,M,K = list(map(int, input().split()))
    people = list(map(int, input().split()))
    ans = 'Possible'

    for i in range(len(people)-1,0,-1): # people.sort()
        for j in range(i):
            if people[j]>people[j+1]:
                people[j],people[j+1] = people[j+1],people[j]

    box_bread = [0]*(11111+1)
    box_people = [0]*(11111+1) #정렬된 손님의 bucket
    for i in range(len(people)):
        box_people[people[i]]+=1
    # print(box_people)

    for i in range(len(box_people)): # 시간에 맞춰 빵 굽기
        if i >=M and i%M==0:
            box_bread[i] = box_bread[i-1]+K
        if box_people[i]>0:
            box_bread[i]-=box_people[i]
        if i<=len(box_people)-2:
            box_bread[i+1] = box_bread[i]
        if box_bread[i] < 0:
            ans = 'Impossible'
            break

# print(box_bread)
# print(ans)
    print(f'#{tc} {ans}')