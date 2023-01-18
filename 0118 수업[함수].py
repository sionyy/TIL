#함수 hi LEGB

# print(add(x=2, y=5))
# print(add(2, y=5))
# print(add(x=2,5))
# 3번은 오류 -> keyword argument 다음에 Positional argument 활용할 수 없음

#[L] Local scope
#[E] Enclosed scope
#[G] Global scope
#[B] Built-in scope

# print(sum)
# print(sum(range(2)))
# sum = 5
# print(sum)
# print(sum(range(2)))
#내장함수보다 Global 할당 5 먼저 나옴 !


x = 0
def func1():
    x=1
    print(x)
    def func2():
        nonlocal x
        x = 2
    func2()
    print(x)    
        
func1()
print(x)



# lambda를 이용한 sort
lst=list(range(10))
print(lst)
ret=sorted(lst,key=lambda x:x) #  ret=sorted(lst)
ret=sorted(lst,key=lambda x:x,reverse=True)  #내림차순 !!  (문자건 숫자건 다 잘 작동)

ret=sorted(lst,key=lambda x:-x) # 내림차순!!  (문자는 정렬 안됨!!!)

lst=[(3,'banana'),(2,'apple'),(1,'carrot')]
ret=sorted(lst,key=lambda x:x[0])
print(ret)



## 딕셔너리
st={'kevin':1,'john':2,'bob':3}

# 딕셔너리 (key랑 value) 추가하기
st['kate']='hi'
print(st)

st['kevin']=11
print(st)

del st['kate']
print(st)

lst=st.keys()
print(list(lst))

lst=st.values()
print(list(lst))

lst=st.items()
print(list(lst))   # 튜플의 형태로 (key,value) 반환

# 딕셔너리 값 출력하기

st={'kevin':1,'john':2,'bob':[1,2,3]}
print(st.get('kecccin','값 없음 없다구요!!~'))

# 딕셔너리 값 정렬하기
st={'kevin':27,'john':22,'bob':35}
# 아이들의 나이가 적은 순으로 (오름차순으로) 딕셔너리를 정렬하기!!!
ret=dict(sorted(st.items(),key=lambda x:x[1]))
print(ret)


print('>>>>>>>>>>>>>>>>>>>>>')
print()

#COPY
# lst=[1,2,3]
# lst2=lst
# lst[0]=100
# print(lst2)

# 얕은복사
lst = [1,2,3]
lst2 = lst.copy()
#=lst2 = lst[:]
lst[0] = 100
print(lst2)



lst = [[1,2],[3,4]]
lst2 = lst[:] # = copy()
lst[0][0] = 100 #얕은복사 이후
print(lst2[0][0]) #lst2값을 안바꿨는데 100이 출력되는 문제!!



#깊은 복사
import copy
lst = [[1,2], [3,4]]
lst2 =copy.deepcopy(lst)
lst[0][0] = 100
print(lst[0][0])