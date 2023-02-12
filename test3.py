A=[]
for i in range(1,80+1):
    A.append(i)

# 80에서 36을 찾기
# 40 다운
# 20 업
# 30 업
# 35 업
# 37 다운
# 36
cnt = 0
while True:
    cnt +=1
    if int(len(A))/2 > 37:
        A = A[:(len(A))/2]
    if int(len(A)) == 37:
        break
# while True:
