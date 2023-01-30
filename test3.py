class car:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __add__(self, another):
        return self.price+another.price
    
    def __str__(self):
        return f'{self.name}의 가격은 {self.price}입니다.'
    
        
kia = car('k8', 300)
bmw = car('m5', 500)
hd = car('h2' , 100)
print(kia.price + bmw.price)

# 커스터마이즈 [.price안써도 되게하기]
print(kia+bmw+hd.price)


print(f'{kia.name}의 가격은 {kia.price}입니다.')

# __str__ 메서드 사용해서 print(kia)만 써도 되게 하기
print(kia)

# 인스턴스 삭제 : del
