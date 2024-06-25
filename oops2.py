class Laptop:
    discount_percent=10 #class variable
    def __init__(self,brand,modal,price):
        self.brand=brand
        self.modal=modal
        self.price=price
        self.laptop_name=brand +" "+ modal
    # def apply_discount(self):
    #     off_price=(Laptop.discount_percent/100)*self.price
    #     return self.price-off_price
    
l1=Laptop('hp','au1243',6000)
print("you paid total amount",l1.apply_discount())
print(l1. __dict__)
print(l1)