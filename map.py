number=[1,2,3,4,5]
# def  square (a):
#     return a**2
# print(square(6))
# squares=tuple(list(map(lambda a : a**2,number)))
# print (squares)
square= [i**2 for i in number]
print (tuple(square))