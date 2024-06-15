# s={1,2,3}
# # print(s)
# l=[1,2,3,4,5,1,2,3,7,8,5]
# # print(set(l))
# s2=list(set(l))
# # print(s2)
# s.add(4)
# s.remove(3)
# s.discard(5)
# s1=s.copy()
# print(s1)
# print(s)
# s={'a','b','c'}
# for item in s:
#     print(item, end=" ")
s1={1,2,3}
s2={4,5,1,2}
print(s1 | s2)
print(s1 & s2)