# 변수입력
# 1. test case
# 2. 가로길이 N
# 3. 상자높이 H

# 문제 설계: 상자 높이의 bucket을 만든다.
# 박스의 최상단 높이 기준 오른쪽 끝까지 0의 갯수를 센다.
# 가장 많은 0의 개수가 정답

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    bit = [0] * len(lst)

    def bitmaker(num):  # 수평기준 상자의 존재유무 (num = num층)
        for i in range(len(lst)):
            if lst[i] != 0:
                bit[i] = lst[i] - num + 1
                if bit[i] < 0:
                    bit[i] = 0
        return bit

    def zerocount(value): #기준 상자 오른쪽의 0의 개수 세기
        result = []
        for i in range(len(bitmaker(value))):
            if bitmaker(value)[i] != 0:
                result = bitmaker(value)[i:]
                break
        return result

    zerobox = []
    for i in range(N):
        zerobox.append(zerocount(i).count(0)) #zerobox에 각 층의 오른쪽0의 개수를 삽입
    print(f'#{test_case} {max(zerobox)}')