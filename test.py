arr = [list(map(int, input().split())) for _ in range(5)]
dummy = [list(map(int, input().split())) for _ in range(5)]

# ttry = []
# for i in range(5):
#     for j in range(5):
#         ttry.append(dummy[i][j])
#
# for k in range(25):
#     for i in range(5):
#         for j in range(5):
#             if arr[i][j] == ttry[k]:
#                 arr[i][j] = 0


def garo():
    for i in range(5):
        for j in range(5):
            if sum(arr[i][j:]) == 0:
                return 111


def sero():
    for i in range(5):
        summ = 0
        for j in range(5):
            summ += arr[j][i]
        if summ == 0:
            return 222

print(garo())
print(sero())