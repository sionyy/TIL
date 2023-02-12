array = [7,5,9,0,3,1,6,2,4,8]

#선택정렬
# for i in range(len(array)):
#     MIN = i
#     for j in range(i+1,len(array)):
#         if array[MIN] > array[j]:
#             MIN = j
#     array[i],array[MIN] = array[MIN], array[i]
# print(array)

# 버블정렬
for i in range(len(array)-1,0,-1):
    for j in range(i):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
print(array)