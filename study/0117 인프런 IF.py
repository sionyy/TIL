# IF 파이썬 제어문

#기본 형식
print(type(True))
print(type(False))

# 산술 ,관계, 논리 우선순위

# 중첩조건문
grade = 'A'
total = 95

if grade =='A':
  if total >=90:
    print('장학금 100%')
  elif total >= 80:
    print('장학금 80%')
  else:
    print('장학금 50%')
else :
  print('장학금 없음')


# in , not in
q = [10, 20, 30] #리스트
w = {70, 80, 90, 100}
e = {"name" : "Lee", "city" : "Seoul"}