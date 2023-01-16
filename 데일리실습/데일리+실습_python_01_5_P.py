# 가로 n = 4
# 세로 m = 5

#1번
m = 5  # 세로
n = 4  # 가로

print((('*'*n)+'\n')*m)

#
for i in range(m):
    print('*' * n)