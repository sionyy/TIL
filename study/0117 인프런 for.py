#For 구문

# for v1 in range(10): # 0 ~ 9
#   print('v1 is :', v1)

# for v2 in range(1, 11): # 1 ~ 10

# for v3 in range(1, 11, 2) # 1 3 5 7 9


# 1부터 1000까지의 합
# 첫번째
# sum1 = 0
# for v in range(1,1001):
#   sum1 += v
# print(sum1)

# 두번째
# print(sum(range(1, 1001)))
# print(sum(range(4,1000,4))) # 4의 배수의 합

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전 = For문 사용 가능
# Iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip


# #예제1
# names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']
# for n in names:
#   print(n, end=' ')



# #예제2
# lotto_numbers = [11, 19, 21, 28, 36, 37]
# for n in lotto_numbers:
#   print(n, end=' ')



#예제3
# word = 'Beautiful'
# for s in word:
#   print(s, end=' ')



#예제4 [dict]
# my_info = {
#   "name" : 'Lee',
#   "Age" : 33,
#   "City" : "Seoul"
# }

# for k in my_info: #key 출력
#   print(k)
# print('>>>>>>>>>>>>>>')

# for k in my_info: #value 출력
#   print(my_info[k])


#예제5 #For 사용하여 대문자로 만들기
# name = 'FineAppLE'

# for n in name:
#   if n.isupper():
#     print(n)
#   else:
#     print(n.upper())


#Break 문 + for else ★★★ 예시좋음

# numbers = [14 ,3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
# for num in numbers:
#   if num == 34:
#       print('Found', num,'!')
#       break
# else:
#   print('Not Found', num)


#continue ★★★ 예시좋음
# n = ["1", 2, 5, True, 4.3, complex(4)]

# for v in n:
#   if type(v) is bool: #문자열 비교할 때는 is / is not
#     continue
#   print("current type:", v, type(v))


# 구구단 만들기 ★★
# for i in range(2,10):
#   for j in range(1,10):
#     print(i*j, end=' ')
#   print()

# for i in range(2,10):
#   for j in range(1,10):
#     print(f'{i} * {j} = {i*j}')
#   print()


#변환 예제
name2 = 'Aceman'

print('Reversed', reversed(name2)) #형변환을 해줘야 제대로 나옴!
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Tuple', tuple(name2))
print('Set', set(reversed(name2)))