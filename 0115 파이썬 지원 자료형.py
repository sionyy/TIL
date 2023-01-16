#Chapter 03 - 01
#숫자형

#파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열[시퀀스]
list : 리스트[시퀀스]
tuple : 튜플[시퀀스]
set : 집합
dict : 사전
"""

#데이터 타입
str1= "Python"
bool1 = True
str2 = 'Anaconda'
float = 10.0
int = 7
list = [str1, str2, ..., ...]
dict = {
      "neme": "Machine Learning",
      "version": 2.0
}
tuple1 = (7, 8, 9)
tuple2 = 7, 8, 9
set =  {3, 5, 7}

#데이터 타입 출력
print(type(str1))
print(type(bool1))
print(type(str2))
print(type(float))
print(type(int))
print(type(list))
print(type(dict))
print(type(tuple1))
print(type(set))


#숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x,y) : x**y -> 2**3 = 8
"""

# 정수 출력
i = 77
i2 = -14
big_int = 777777777777777777779999999999999999


#실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3/9


# 연산 실습
i1 = 39
i2 = 939
big_int1 = 79797878979842123156848978645645123
big_int2 = 12156185948942123132123123212121211
f1 = 1.234
f2 = 3.4894

# +
# 형 변환이 자동으로 이루어 진다


#형변환 규칙들
a = 3.
b = 6
c = .7
d = 12.7

#파이썬 소숫점 변환
# https://blockdmask.tistory.com/534

"""
print(float(b))
print(int(c))
print(int(d))
print(int(True)) # True : 1, False = 0
print(float(False))
print(complex(3)) 
"""


#수치 연산 함수
print(abs(-7))
x,y = divmod(100,8)
print(x,y)


print(pow(5,3), 5**3)


#외부 모듈
import math
print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수
print(math.pi)