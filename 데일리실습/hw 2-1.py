#기존 주문
orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'



#1번 문제
coffee_num = (len(orders.split(',')))
print(f'총 {coffee_num}잔의 주문이 들어왔습니다.')




#2번 문제
a=orders.split(',')
b=sorted(set(a),reverse = True)
print(f'중복 없는 메뉴는 {b}입니다.')