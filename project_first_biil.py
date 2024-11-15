print("welcome to our restaurant .Here's the menu: ")
menu={'pizza': 40,'pasta': 50,'burger':60,'salad': 70,'coffe': 80}
for item,price in menu.items():
    print(f"{item}  {price}")
total_order=0
order1=input("Enter your first item you want to order = ")
if order1 in menu:
    total_order += menu[order1]
    print(f"order of {order1} has been added")
else:
    print("you order is not available")
ask=input("Do want to order anything else ?(yes/no) ")
if ask=='yes':
    order2=input("Enter your second item you want to order = ")
    if order2 in menu:
        total_order += menu[order2]
        print(f"order of {order2} has been added")
    else:
        print("you order is not available")
print(f"your bill is {total_order}")
print("thanku for visiting")
    




    
