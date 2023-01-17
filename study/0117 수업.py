'''
조건문
반복문
함수
map filter
lamda
'''


# a=int(input())
# if a>5:
#     print('오삼')
# elif a>3:
#     print('불고기')
# elif a>4 or a==-1:
#     print('재시도')
# else:
#     print('오삼불고기')



# a,b = map(int, input().split())
# if a>b:
#     print(a)
# else:
#     print(b)

# result = a if a>b else b # 조건 표현식 / 참일때 앞 반환
# print(result)


#FOR문

# for i in range(101):
#     print(i, end=' ')

# print()

# for a in range(100):
#     print('#', end='')


# i = 1
# while i < 101:
#     print(i, end=' ')
#     i=i+1



#lamda
'''
리스트 출력 for 이용하여 출력하기
'''

# lst = [[1,2,3],[4,5,6]]
# print(lst[0][1])

# print('>>>>>>>>>>>>>>>>')

# for i in range(0,2):
#     for j in range(0,3):
#         print(lst[i][j],end=' ')
#     print()



# 1차원 리스트
# lst = [[1,2,3], [4,5,6]]
# multi = []
# for i in range(2):
#     for j in range(3):
#         multi.append(lst[i][j]**2)

# print(multi)
# print(*multi) # 리스트 값 하나씩 나옴


# lst = [[1,2,3], [4,5,6]]
# multi = []
# for i in range(2):
#     temp=[]
#     for j in range(3):
#         temp.append(lst[i][j]**2)
#     multi.append(temp)

# print(multi)




# 딕셔너리

# di = {'kevin': 1, 'john': 2, 'bob' : 3}
# print(di)


# for i in di:
#     print(i, di[i])

# print('>>>>>>>>>>>>>>>')

# for i,j in di.items():  # key값 i, value값 j
#     print(i,j)

# print('>>>>>>>')
# for i in di:
#     print(i)




#Break 반복문을 중간에 멈추고 싶을 때

##return 함수의 값을 반환하거나 또는 그냥 함수 종료

# lst =[10,20,30,40,50,60,70]
# for i in lst:
#     if i ==50:
#         break
#     print(i, end=' ')


# flag = 0
# lst=[[1,2,3],[1,2,3],[1,2,3]]
# for i in range(3):
#     for j in range(4):
#         if lst[i][j]==3:
#             flag=1
#             break
#         print(lst[i][j], end=' ')
#     if flag:    # if flag==1:
#         break


#Continue #해당줄 실행 안되고 넘어감
lst = [1,2,3,4,5,6,7]

for i in lst:
    if i ==5:
        continue
    print(i,end=' ')

print('>>>>>>>>>>>>>>>')

lst2 = [[1,2,3], [1,2,3], [1,2,3]]
for i in range(3):
    for j in range(3):
        if lst2[i][j]==1:
            continue
        print(lst2[i][j], end=' ')