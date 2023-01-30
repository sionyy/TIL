# Calculator
# add, substract, multiply, divide

# 1 + 2
# 2 – 1
# 3 * 4
# 4 / 0

class Calculator():
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self) :
        result = self.first + self.second
        return result
    
    def substract(self) :
        result = self.first - self.second
        return result
    
    def multiply(self) :
        result = self.first * self.second
        return result
    
    def divive(self) :
        if self.second != 0:
            result = self.first / self.second
        elif self.second == 0 :
            result = f'{self.second}으로 나눌 수 없습니다.'
            
        return result



    
a = Calculator(10,2)
print(a.divive())

b = Calculator(4,0)
print(b.divive())