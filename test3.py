from collections import Counter
lst = ['apple', 'mango', 'banana', 'mango', 'apple','apple']

# counter는 리스트 또는 문자열 안에 데이터가 각각 몇개씩 있는지 알려줌

print(Counter(lst))

ret = dict(Counter(lst))
print(ret)


st = 'an apple mango'
ret = dict(Counter(st))
print(ret)
ret = sorted(ret.items(), key = lambda x:x[1], reverse=True)
print(ret)


st = 'an applemango'
#st요소를 세어, 최빈값 n개를 반환한다.

ret = Counter(st).most_common(2)
print(ret)


#추가적으로 Counter를 가지고 덧셈 뺄셈도 지원합니다.
a = Counter('apple')
b = Counter('mango')
print(a+b)

# 문자열 대조할 때 사용 가능
a.subtract(b)
print(a)