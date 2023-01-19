'''
문자열
리스트 튜플 딕셔너리 셋 관련 메소드
copy (깊은복사 얕은복사)
'''

st = 'apple, banana, mango'

#문자 'a'가 존재하는지 확인하고자 합니다
#.find 메소드

# index=st.find('le') # [3번인덱스]
# print(index)

# index=st.find('a') # [0번인덱스]

# index=st.find('n') # [3번인덱스]
# print(index)

# index=st.find('a',1) # [1번 이후부터 찾기]
# #없으면 -1 반환



#대소문자 확인 !
lst = 'apple, banana, mango'
print(lst.isupper()) #대문자로만?
print(lst.islower()) #소문자로만?
print(lst.isalpha()) #알파벳으로만?
print(lst.count('a'))#몇개들었나?
print('>>>>>>>>>>>>')




#join (합치기)
st = ['a','p','p','l','e']
str2 = "".join(st)
print(str2)



#리스트인데 문자 사이사이 ,를 넣어라
str2=','.join(st)
print(str2)



print('>>>>>>>>>>>>')
#공백지우기
ap = '     apple'
print(ap)
ap2=ap.lstrip() # 오른쪽은 rstrip / 가운데는 strip
print(ap2)


#교체 replace
re = 'apple'
re2 = re.replace('ap', 'mp')
print(re2)





#리스트 값 추가
ft = ['apple', 'banana', 'mango']
ft.append('orange')
ft.insert(1, 'orange')
print(ft)



#리스트 뒤에 리스트 붙이기
st = [1,2,3]
str2 = [4,5]
#append로 하면 리스트로 추가됨


st.extend(str2)
st+=str2 #.extend와 같음
print(st)



#리스트 값 지우기
st = [1,2,3]
st.pop()
print(st)


st=[1,2,3,4,1,2,3,4]
st.remove(4) # 첫번째 4만 지워짐
print(st)



st=[1,2,3,4,1,2,3,4]
del st[3:]
print(st)



st=[1,2,3,4,5,1,2,3,4]
st.reverse()
print(st)
print(st[::-1])


#sort = 원본 데이터 변경
a1=[6,3,9]
print(a1)
a1.sort()
print(a1)
a1.sort(reverse=True) #오름차순 디폴트
print(a1)


print('>>>>>>>>>>>>>>>>')
#sorted = 원본 데이터값 유지
a1=[6,3,9]
ret = sorted(a1)
print(a1, ret)
ret = sorted(a1,reverse=True)



# a=5
# b=a
# print(b)

# lst=[1,2,3]
# lst2=lst
# lst[0]=100
# print(*lst2)

lst=[1,2,3]
#lst2=lst.copy()     # 얕은복사
lst2=lst[:]
lst[0]=100
print(lst2)

lst=[[1,2],[3,4]]
lst2=lst[:]   # copy() 얕은 복사 이후
lst[0][0]=100
print(lst2[0][0])


# 깊은 복사
import copy
lst=[[1,2],[3,4]]
lst2=copy.deepcopy(lst)
lst[0][0]=100
print(lst[0][0])

# 주소값을 찍어보자
a=5
b=5
print(id(a),id(b))
lst=[1,2,3]
lst2=lst
print(id(lst),id(lst2))


lst=[1,2,3]
lst2=lst[:]
print(id(lst),id(lst2))


lst=[[1,2],[3,4]]
lst2=lst[:]
print(id(lst),id(lst2))
print(id(lst[0]),id(lst2[0]))

import copy
lst=[[1,2],[3,4]]
lst2=copy.deepcopy(lst)
print(id(lst[0]),id(lst2[0]))