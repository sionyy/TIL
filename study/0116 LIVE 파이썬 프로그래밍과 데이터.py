# 0116 월요일
# 프로그래밍 : 적절한 수행 절차를 정의하고 프로그래밍 언어로 표현하는 과정


# ssafy : 3.9.12버전
# Add python.exe to PATH 꼭 체크
#파이썬 VSCode 확장 프로그램 추천 검색 

#dust = 60
#60의 값을 dust에 할당한다


x=10
y=20

# 일때, 실습문제 x를 20, y를 20 출력

# 방법1) 임시 변수 활용!! 
tmp = x
x = y
y = tmp
print(x,y)

# 방법2)
# y, x = x, y

print('aaaaaa\rbbbb')



#변수
a=3
b=5

print(f'{a} + {b} = {a+b} 입니다.')
print(a, "+", b, "=",a+b , "입니다.")
# 3 + 5 = 8 입니다.


#swap
a=3
b=5

temp=a
a=b
b=temp
print(a,b)


# 자료형
a=3
print(type(a))

a=3.14
print(round(a,1)) #소수점 첫번째까지 출력[6부터 반올림]
print(f'{a:.1f}')

a=5
a=str(a)    #'5'
print(a, type(a))

#오늘은 "100%" 입니다.
print('오늘은 "100%" 입니다.')


#slicing 
#★ 꼭 시뮬레이션 해보기
s= "1234567"
print(s[:3])
print(s[3:])
print(s[2:5])
print(s[2:-2])
print(s[5:2:-1])
print(s[1:5:2])


#boolean
a,b = 0,-1
a,b = bool(a), bool(b)
print(a,b)


# 리스트
lst=[1,2,3,4,5]
print(lst)
print(len(lst[1:]))
print(lst[-1])


#튜플
tp=(1,2,3,4,5)
print(tp)
print(len(tp))
print(tp[-1])


#range
print(list(range(3)))
print(list(range(1,5)))


print('<<<<<<<<<<')

#set - 리스트에서 중복 제거
lst1 = [2, 1, 5, 6, 2, 2, 2, 2, 1, 3]
print(lst1)
lst_f = (set(lst1))
print(lst_f)

lst.sort()
print(lst)



#값 추가
s={1,2,3,4,5}
s.add(6) # 1개 추가
print(s)


s.update({11,12,8,6,7}) #여러개 추가
print(s)

print('>>>>>>>>>>>>>')
#값 삭제
s.remove(6) # 삭제하는 값이 없으면 버그남
print(s)

s.discard(12) # discard는 값이 없어도 버그 안남!!
print(s)

s.clear
print(s)

print('>>>>>>>>>>>>>>>>>')
#집합
s1 =[1,2,3,4,5]
s2 =[2,4,6,8]

#교집합
s1,s2=set(s1),set(s2)
print(s1&s2)

#합집합
print(s1|s2) #shift + \
print(s1.union(s2)) #union함수 이용

#차집합
print(s1-s20)