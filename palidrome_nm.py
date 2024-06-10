# name=input("enter the name : ")
# def check(name):
#     checking = ''.join(reversed(name))
#     if name.lower()==checking.lower():
#         print("this is palidrome")
#     else:
#         print("this word not a palidrome ")

# name=input("enter the name : ")
# check(name)
def check(name):
    return name==name[::-1]
print(check("naman"))