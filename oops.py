class Person:
    count_instance=0
    def __init__(self,first_name,last_name,age):
        Person.count_instance +=1
        # instance variables
        print('init method called')
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    @classmethod #decorder
    def count_instances(cls):
        return f"you have created {cls.count_instance}" 
    @classmethod
    def from_string(cls,string):
        first,last,age=string.split(',')
        return cls(first,last,age)
    @staticmethod
    def hello():
        print('hello,static method called')
    
p3=Person.from_string('harshi,gupta,76')
print(p3.full_name)
p1=Person('harsh','gupta',24)
p2=Person('harshit','gupta',44)
print(p1)
print(p1.age)
print(p1.full_name())
print(Person.count_instances( ))
Person.hello()
