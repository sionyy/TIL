N, M = map(int, input().split())  # 입력값 할당
flag = [input() for _ in range(N)]  # 국기 할당

needW, needB, needR = [], [], []  # 각각 행에서 W,B,R과 다른 알파벳 구하기
need = [[], [], []]
for i in range(len(flag)):
    needW.append(M - flag[i].count('W'))  # 각 행의 크기인 M에서 / 'W'가 없는만큼 append
    needB.append(M - flag[i].count('B'))
    needR.append(M - flag[i].count('R'))
print(needW)
print(needB)
# print(needR)
# result = []
# sumW = 0
# for i in range(0, N - 2):  # 시작점인서 B,R의 최소필요갯수 2를 제외한 최대 W의 행 개수
#     sumB = 0
#     sumW += needW[i]
#     for j in range(i + 1, N - 1):  # W의 최소필요행 1행과 R의 최소필요행 1행을 제외한 범위
#         sumR = 0
#         sumB += needB[j]
#         for k in range(j + 1, N):  # W,R을 제외한 끝까지의 행에 대한 범위
#             sumR += needR[k]
#         result.append(sumW + sumB + sumR)
# ans = min(result)  # 가장 적은 값이 ans!