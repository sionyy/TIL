# 함수
lst=[6,6,9,8]
print(len(lst))
print(sum(lst)) #다더하기
print(max(lst))
print(sorted(lst)) #오름차순

a = 'A'
print(ord(a)) #아스키 코드값 변환
a=66
print(chr(a)) #코드값 문자로

a=-3
print(abs(a)) # 절댓값
print(id(a)) # 주소값
print(pow(3,2)) #3의 2제곱


import random
a = [1,2,3,4,5,6]
print(random.sample(a,2))


#map 함수
#리스트나 튜플같은 순회가능한 데이터 구조 값들의
#함수를 일괄 적용하고, 적용후 값을 map이라는 개체로 반환
#사용법 map(함수, iterebles)
num=['1','2','3']
lst2 = map(int,num)
print(lst2)
print(list(lst2))






def getsum(a,b):        # 매개변수 parameter
    return a+b
    return a*b

print(getsum(3,4))      # 인자값 argument


#언패킹시 남는 값을 *을 사용하여 리스트에 담을 수 있다.
num = [1,2,3,4,5]
num2 = (1,2,3,4,5)
a,b,*c=num
print(c)
a,b,*c=num2
print(c)

def print_into(**args):
    print(args)
    for i,j in args.items():
        print(i,j)