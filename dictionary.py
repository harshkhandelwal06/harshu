user={'name':"harsh",'age':43}
# print(user['name'])
user_info={'name':"harsh",
           'age':43,
           'fav_movie':['animal','rowdy rahore'],
           'fav_web':["scam-1992",'asur'],
           }
# print(user_info["fav_web"])
user_info2={}
user_info2['name']='harsh'
user_info2['age']=76
# print(user_info2)
# if 'mame' in user_info:
#     print("present")

# else:
#     print("not present")
# for i in user_info.keys():
#     print(i)
# user_value=user_info.value()
# print(type(user_value))
# for i in user_info:
#     print(user_info[i])
# item method
# user_item=user_info.items()
# print(user_item)
# print(type(user_item))
# for i ,j in user_info.items():
#     print(f"keys is {i},value is {j}")
# user_info["fav_web"]=["indori ishq","civil war"]
# user_info["fav_web"]="rohini"
# for i ,j in user_info.items():
#    print(f"keys is {i},value is {j}")
# pop_item=user_info.pop("fav_web")
# print(pop_item)
# print(user_info)
# for i in user_info:
#     print(i)
# popitem method
# poped_item=user_info.popitem()
# print(poped_item)
# print(user_info)
# print(type(poped_item))
more_info={"state":"rajasthan","hobbies":['like cricket','watch movies']}
user_info.update(more_info)
# print(user_info)
d={'name':"harshit",'age':45}
# d.clear()
print(d)
# print(d.get['names'])
# if user_info.get('names'):
#     print("present")
# else:
#     print("not present")
d1=d.copy()
print(d1)
d2=d
print(d2)
print(d1 is d)
print(d.get('name','not  fount'))