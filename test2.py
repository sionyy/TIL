# 0~9까지의 N장 카드
# 가장 많은 카드에 적힌 숫자, 카드가 몇장인지 출력하는 프로그램

# N = 카드 장 수
# 입력: 카드장수 n\ 카드번호
T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    lst = list(map(int, input()))

    bucket = [0] * 10

    for i in range(len(lst)):
        bucket[lst[i]] += 1

    Max = 0
    for i in range(len(bucket)):
        if bucket[i] > Max:
            Max = bucket[i]
        if Max == bucket[i]:
            ans = i  # 가장 많은 카드의 번호

    print(f'#{test_case} {ans} {Max}')