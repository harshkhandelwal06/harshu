# guess number program with the help of random variabble
import random
random_no=random.randint(1,100)
i=0
while(i<7):
    print("enter the nnumber with the range in 1  to 100 :")
    num=int(input())
    if num==random_no:
        print("you won ! ")
        break
    elif num>random_no:
        print("you enter  number is to high ")
    else:
        print("you enter number is too low ")
    i=i+1

