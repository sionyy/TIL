# 0117 오전 라이브
# 조건문 / 제어문

# 조건문

# dust = 500 #int(input())
# print('미세먼지', end=(' '))
# if dust > 150:
#     print('매우나쁨')
#     if dust > 300:
#         print('실외 활동을 자제하세요')
# elif dust > 80:
#     print('나쁨')
# elif dust >30:
#     print('보통')
# elif dust >=0:
#     print('좋음')
# else:
#     print('값이 잘못되었습니다.')
# print('미세먼지 확인 완료!')

# print('>>>>>>>>>>>>>>>>>>>>>>')

# #조건 표현식
# # ture인경우값 / if / 조건 / else / false인경우값
# #예시
# num= -5
# value = num if num>=0 else -num #거짓인 경우에도 양수가 나옴
# print('홀수입니다') if num%2==1 else print('짝수입니다')

# 반복문
a = 0
while a < 5:
    print(a, end=' ')
    a += 1
print('끝')





count = 0
while count < 5:
    count = count + 1
    print(f'{count}번', end=' ')
    if count == 5:
        print('출석 완료')



for fruit in ['apple', 'mango', 'banana']:
    print(fruit)
print('끝')


chars='happy'
for idx in range(len(chars)):
    print(chars[idx])

chars1 = '양시온'
for i in range(len(chars1)):
    print(chars1[i])


members = ['김', '이', '박']
for n, m  in enumerate(members):
    print(n, m)



#List / Dictionary Comprehension
#code/for/변수/in/iterable

my_list = []
my_list2 = list()



ans = []
for i in range(1,4):
    ans.append(i**3)
    print(ans)

cubic_dict = {}
for number in  range(1,4):
    cubic_dict[number] = number**3



#반복문 제어
# break : 반복문 종료
# continue : continue 다음 반복 수행
# for / else : break로 중단되면 실행 x
# pass [vs continue 시험]
print('>>>>>>>>>>>>>>>')
