class phone:#base class
    def __init__(self,brand,modal,price):
        self.brand=brand
        self.modal=modal
        self.price=max(price,0)
    def full_name(self):
        return f"{self.brand} {self.modal}"
    def make_a_call(self,number):
        return f"calling{number}---"
    
class Smartphone(phone): #derived class
    def  __init__(self,brand,modal,price,ram,internal_memory,rear_camera):
        # super().__init__(brand,modal,price)
        phone.__init__(self,brand,modal,price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera
phone1=phone('nokia','1100',1000)
smartphone1=Smartphone('oneplus','6',30000,'6gb','64gb','20mp')
print(phone1.full_name())
print(smartphone1.full_name())
print(smartphone1)