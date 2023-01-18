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
        
        
print('>>>>>>>>>>>>')

#filter
#리스트나 튜플과 같은 순회 가능한 데이터구조값들을 함수에 적용하는데
#적용후 값중 True만 반환 !!!
#**데이터에 일괄적용 = map
#**데이터에 일괄 적용하는데 True 값만 따로 저장 = filter
#**lambda 익명함수 (사용자함수를 직접 적지 않고 간단하게 사용하고 싶을 때)

#리스트에서 짝수만
num = [1,2,3,4,5,6,7,8,9,10]

def get_even(t):
    return True if t%2==0 else False

result=filter(get_even, num)
print(list(result))
#filter(함수, iterebles)


#lambda
#익명함수. 함수를 간략하게 적기 위해서 사용

#숫자 2개 입력받고 getsum 함수로 전달
#get sum 함수에서 전달받은 두 수의 합을 리턴함
#리턴받은 값 출력하기

def summ(x,y):
    return x+y

ret=summ(3,5)
print(ret)

#lambda함수 활용
result = (lambda a,b:a+b)(3,5)
#또는
sum2 = (lambda a,b:a+b)
print(sum2(3,5))

#활용 =(lambda 파라미터:리턴)(인자값)

print('>>>>>>>>>>>>>>>')

#예제
# 두 리스트 값들의 합을 lst3에 람다함수를 사용하여 값을 채운 후 출력
# lst3 =[7,9,11,13,15]

lst1=[1,2,3,4,5]
lst2=[6,7,8,9,10]

result = (lambda x,y:x+y)
lst3 = map(result, lst1, lst2)
print(list(lst3))



#recursion 재귀 !! or  재귀호출
#함수가 하나 있는데 함수가 자기자신을 계속 호출

for i in range(1,11):
    print(i, end=' ')

print()

for i in range(10,0,-1):
    print(i, end=' ')
    
print()

def abc(level):
    if level == 4:
        return
    print(level,end=' ')
    abc(level+1)
    print(level,end=' ')
    
abc(1)