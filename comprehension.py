# square=[]
# for i in range(1,11):
#     square.append(i**2)
# print(square)
# square2=[i**2 for i in range(1,11)]
# print(square2)
# numbers=list(range(1,11))
# nums=[]
# # print(numbers)
# for i in numbers:
#     if i%2==0:
#         nums.append(i*2)
#     else:
#         nums.append(-i)
# print(nums)
# # num1=[i for i in range(1,11) if i%2==0]
# # print(num1)
# num1=[i*2 if (i%2==0) else (-i) for i in range(1,11)]
# print(num1)
# num=[[i for i in range(1,4)] for i in range (3)]
# print(num)
# num1=[]
# for i in range (3):
#     num1.append([1,2,3])
# print(num1) 
# square={num:num**2 for num in range(1,11)}
# print(square)
# square1={f"square of {num}":  {num**2} for num in range(1,10) }
# print(square1)
# string="harshit"
# for i in string:
#     print(i)
# word_count={char:string.count("char") for char in string}
# print(word_count)
# odd_even={i:('even'if i%2==0 else 'odd') for i in range(1,11) }
# print(odd_even)
# s={k for k in range(1,11)}
# print(s)
# name={"harshit","mohit","rahul"}
# name1={i[0] for i in name }
# print(name1):
# def multiply_total(nums,*args):
#     multiply=1
#     print(nums)
#     print(args)
#     for i in args:
#       multiply*=i
#     return multiply
# print(multiply_total(1,2,3,4))
# print(type(multiply_total))
# # print(args)
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
func(first='harsh',last='gupta')