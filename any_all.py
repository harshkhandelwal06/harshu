# # num1=[12,16,14]
# num2=[1,2,3,4,5,6]
#  print(any([num%2==0 for num in num2]))
# def my_sum(*args):
#     # if all ([type(args)==int or type(args) float for args in args ])
#     if all([type(args)==int or type(args) float for arg in args )]
#         total=0
#         for num in args:
#              total+=num
#         return total
#     else:
#         return "wrong print"
# print(my_sum(1,2,43,4,5,6))
# def func(item):
# #     return len(item)
# names=['harshit','mohit','ab','z']
# # print(max(names,key=func))
# print(max(names,key=lambda item:len(item)))
def outer_func(msg):
    def inner_fun():
        print(f" this is a {msg}")
    return inner_fun
var=outer_func("hello word ")
var()
def to_power(x):
    def calc_power(n):
        return n**x
    return calc_power
cube=to_power(3)
print(cube(5))