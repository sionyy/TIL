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
print(id(x))