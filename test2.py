# 4 2 5 3 8
# a=8
# b=2
lst = map(int, input().split())
def BBQ():


    a=int(-21e8) # Max 구하기
    b=int(21e8) #Min구하기
    for i in lst:
        if i > a:
            a = i
        if i < b:
            b = i
    return print(f'a={a}\nb={b}')

BBQ()
