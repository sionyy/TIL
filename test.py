class Person():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_age(self, name, age):
        return name, age
    
        
person1 = Person('Mark', 20)
person2 = Person.get_age('Rohan', 1992)

print(person1.name, person1.age) 
print(person2.name, person2.age)
# print(person1.check_age())
# print(person2.check_age())
