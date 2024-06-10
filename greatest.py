def find(a,b,c):
    if a>b and a>c:
        print("a is greatest ")
    elif b>a and b>c:
        print("b is greatest ")
    else:
        print("c is greatest ")
a,b,c=input().split()
find(a,b,c)