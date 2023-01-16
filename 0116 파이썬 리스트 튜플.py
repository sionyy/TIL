# 리스트
# chapter 03-03

#리스트 자료형(순서o, 중복o, 수정o, 삭제o)

#리스트 한줄로 표기 방법
# for n in lis:
#     print(n, end=' ')
# print()

#선언
a = []
b = list()
c = [70, 75, 80, 85]
print(len(c))
d = [1000, 10000, 'Ace', 'Base', 'Captine']   #자료구조 달라도됨
e = [1000, 10000, ['Ace', 'Base', 'Captine']]   #리스트 안 리스트
f = [21.42, 'foobar', 3, 4, False, 3.14159]


#인덱싱
print('>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d -', d[-1])
print('e - ', e[-1][1]) # 뭐가 나올까요?
print('e- ' , list(e[-1][1])) #뭐가 나올까요?


#슬라이싱
print('>>>>>>>>')
print('d -', d[0:3])
print('e -', e[-1][1:3])


#리스트 연산
print('>>>>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0]))


#값 비교
print(c == c[:3] + c[3:])


# Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))



#리스트 수정, 삭제
print('>>>>>>>>')
c = [70, 75, 80, 85]
c[0] = 4
print('c - ', c)

c[1:2] = ['a', 'b', 'c']  ## 중요 !
print('c - ', c)

c[1] = ['a', 'b', 'c'] ## 중요 !
print('c - ', c)

c[1:3] = []
print('c - ', c) ## 뭘까요?

del c[2]
print('c - ', c)



#리스트 함수
print('>>>>>>>>')

a = [5, 2, 3, 1, 4]
print('a - ', a)

# a[5] = 10
# print('a - ', a)
# 불가 !!

a.append(10)
print('a - ', a)

a.sort()
print('a - ', a)

a.reverse()
print('a - ', a)

a = [5, 2, 3, 1, 4]
print('a - ', a)
print('a - ', a.index(3), a[3]) ## 주의 !!! 3의 위치의 값이 출력됨!
print('>>>>>>>>')

a.insert(2, 7)
print('a - ', a)

a.remove(1)
print('a - ', a)

print('a -', a.pop()) #기존 리스트 마지막원소 가져오고, 나머지로 다시 구성
print('a - ', a)
print('>>>>>>>>')

print('a -', a.count(2))

ex=[8,9]
a.extend(ex)
print('a - ', a)
# 삭제 : remove, pop, del


#반복문 활용
while a:
  data = a.pop()
  print(data)
  