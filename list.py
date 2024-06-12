# mixed=[1,2,3,"harsh",'rahul',8.9,9.8]
# # # # # print(mixed)
# # # # # # print(mixed[3])
# # # # # # # for mix in mixed:
# # # # # #     # print(mix,end=" ")
# # # # # # mixed[3]=3
# # # # # # for mix in mixed:
# # # # # #     print(mix,end=" ")
# # # # # mixed[4:]=[7,8]
# # # # # print(mixed)
# # # fruits1=[]
# # # fruits1.append("mango")
# # # fruits1.append("guvava")
# # # fruits1.append("patato")
# # # fruits1.append("kiwi")
# # # # print(fruits1)
# # # # fruits1.insert(0,"lichi")
# # # # print(fruits1)
# # # fruits2=["tomato","capsicum"]
# # # fruits=fruits1+fruits2
# # # # print(fruits)
# # # # fruits1.extend(fruits2)
# # # # print(fruits1)
# # # # print(fruits2)
# # # # fruits1.extend(fruits2)
# # # # fruits1.append(fruits2)
# # # print(fruits)
# # # # fruits.pop(2)
# # # # print(fruits)
# # # # del fruits [1]
# # # # print(fruits)
# # # # fruits.remove("mango")
# # # # print(fruits)
# # # # if "mango" in fruits:
# # # #     print("apple is present")
# # # # else:
# # # #     print("not present ")
# # # print(fruits.count("mango")) 
# # # fruits.append("mango")
# # # print(fruits)
# # # fruits.sort()
# # # print(fruits)
# # num=[2,4,3,6,5,7,7]
# # print(sorted(num))
# # print(num)
# # # num.clear()
# # # print(num)
# # num_copy=num.copy()
# # print(num_copy)
# # user_info='harsh','gupta','deepak','gupta'.split()
# # print(user_info)
# # name=["harsh","ganesh","vinay","deepak"]
# # print(' '.join(name))
# # s="string"
# # t=s.title()
# # print(t)
# # print(type(s))
# i=0
# # while i<len(mixed):
# #     print(mixed[i],end=" ")
# #     i+=1
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# # for i in matrix:
# #     print(i ,end=" ")
# #     for var in i:
# #         print(var,end=" ")
# print(matrix[2][0])
# num=list(range(1,11))
# print(num)
num=[1,2,3,4,5,6,7,8]
def negative(l):
    negative=[]
    for i in l:
        negative.append(-i)
        return negative
print(negative(num))