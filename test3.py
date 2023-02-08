N= 10 # 배열크기
M= 3 # 연속개수

lst = [1,2,3,4,5,6,7,8,9,10]

#묶음 구하기
sum_lst = []
for i in range(0,N-M+1):
    gggg = sum(lst[i:i+M])

# N의 크기를 가진 list에서
# 연속된 M개 비교

Max = -int(21e8) #최대값 구하기
for i in range(0,N-M+1): # 묶기 위해 최대범위 -M+1
    if lst[i]+lst[i+1]+lst[i+2]>Max:
        Max = lst[i]+lst[i+1]+lst[i+2]
print(Max)