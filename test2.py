students = [
    '박해피',
    '이영희',
    '조민지',
    '조민지',
    '김철수',
    '이영희',
    '이영희',
    '김해킹',
    '박해피',
    '김철수',
    '한케이',
    '강디티',
    '조민지',
    '박해피',
    '김철수',
    '이영희',
    '박해피',
    '김해킹',
    '박해피',
    '한케이',
    '강디티',
]

dic={}

for i in students:
    if i in dic:
        dic[i]+= 1
    else:
        dic[i] = 1
        
print(dic)
print(sorted(dic))