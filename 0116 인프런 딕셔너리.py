# 딕셔너리 
#순서x 키중복x 수정삭제o


#선언방법
a = {'name' : 'Kim', 'phone' : '010'}
b = {0: 'Hello Python'}
c = {'arr' : [1,2,3,4]}
d = {
   'Name':'Niceman',
   'City':'Seoul',
   'Age' : '33'
}
e = dict(
  name = 'Niceman',
  City = 'Seoul',
  Age = 33
)

#출력방법 주로 get 이용[없을 때 오류 대신 none 나와서]
print(a['name'])
print(a.get('name'))
print(a.get('name1'))