age=input("enter your age :")
age=int(age)
if 0>=age:
    print("you are not exit in the world ")
elif 1<=age<=3:
    print("your entry is free" )
elif 4<=age<=10:
    print("your ticket price is : 150")
elif 11<=age<18:
    print("your ticket price is :250")
else:
    print("your ticket price is :400")
