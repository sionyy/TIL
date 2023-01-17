lst1=[1,2,3]
lst2=[4,5,6]
# lst3라는 리스트에 lst1과 lst2의 합을 저장하는 리스트로 만든 후 출력

def func(a,b):
    return a+b

lst3 = list(map(func, lst1, lst2))
print(lst3)