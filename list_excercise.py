# # number=list(range(1,15))
# # # number=int(input("enter the number "))
# # def square(s):
# #     for i in s:
# #        print(i*i,end=" ") 
    
# # # square(number)//excercise 2nd incomplete
# # num=["1,2,3,4"]
# # word=["word1, word2"]
# # def reverse(r):
# #     for i in r:
# #         print(''.join(reversed(i)))
# # reverse(num)
# # reverse(word)
#  num=[1,2,3,4]
# def reverse (r):
#     rev=[]
#     i=0
#     while r:
#         num1=r.pop(i)
#         rev.append(num1)
#     return rev
# print(reverse(num))
# num = [1, 2, 3, 4]

# def reverse(r):
#     rev = []
#     while r:  
#         num1 = r.pop() 
#         rev.append(num1)
#     return rev

# print( reverse(num))
# # print(reversed_list)
# num=list(range(1,11))
# print(num)
# def filter(a):
#     num1=[]
#     num2=[]
#     # num3=[]
#     for i in a:
#        if i%2==0:
#          num1.append(i)
#         # print(num1)
#        else:
#           num2.append(i) 
#         #  print(num2)
#     return num1,num2
# even,odd=filter(num)
# print("even is ",even)
# print("odd is", odd)
# even.append(odd)
# print(even)
num=[[1,2,3,4],[1,2,6,5]]
# as=[]
def same(a,b):
    num1=[]
    for i in a:
        if i in b:
            num1.append(i)
    return num1
print(same([1,2,3,4],[1,2,6,5]))
print(same(num))
