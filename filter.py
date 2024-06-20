number=[1,2,3]
def is_even(a):
    return a%2==0
even1=  list(filter(is_even,number))#way 1
print(even1)
even2=list(filter(lambda a:a%2==0,number))#way 2
print(even2)
even3=[i for i in number if i%2==0]
print(even3)