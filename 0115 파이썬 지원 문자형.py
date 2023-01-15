# Chapter 03-2
# 파이썬 문자형


#문자열 생성
str1 = "I am Python"
str2 = 'python'
str3 = """How are you"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1))



# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))


# 이스케이프 문자 사용
# I'm Boy

print("I'm Boy")
print('I\'m Boy')

print('a \"\" b')
print('a /t b')
print('a /n b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)


# 탭, 줄 바꿈
t_s1 = "Click \t Start"
t_s2 = "New Line \nCheck"
print(t_s1)
print(t_s2)


#Raw String 출력 [\ 표시]
raw_s = r'D\python\test'
print(raw_s)


#멀티라인 입력
multi_str =\
"""
문자열
멀티라인 입력
테스트
"""
#역슬래시 뺄거면 "을 = 옆으로
print(multi_str)


#문자열 연산
str_01 = "Python"
str_02 = "apple"
str_03 = "how are you doing"

print(str_01 * 3)
print(str_01 + str_02)
print('y' in str_01)
print('P' not in str_01)


# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))


#문자열 함수(upper, isalnum, startswith, count, endswith, isaLpha ...)

print("Capitalize: ", str_01.capitalize())
print("endswith?: ", str_02.endswith("e"))
print("replace :", str_01.replace("thon", 'Good'))
print("sorted :", sorted(str_01))
print("split :", str_03.split(' '))


# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) #__iter__

#출력
for i in im_str:
  print(i)


#슬라이싱
str_sl = "Nice Python"

#연습
print(str_sl[0:3])
print(str_sl[5:])
print(str_sl[:len(str_sl)])
print(str_sl[:len(str_sl)-1])
print(str_sl[1:9:2])
print(str_sl[-5:])
print(str_sl[1:-2])
print(str_sl[::-1])


#아스키 코드(또는 유니코드)
a= 'z'

print(ord(a)) # 문자 -> 아스키코드로
print(chr(122)) # 아스키코드 -> 문자로