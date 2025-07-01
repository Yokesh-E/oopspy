#encapsulation

#public 
# class a():
#     def f(s):
#         s.name="yoks"
#         s.age=23
#         print("name iss ",bj.name)
    # def d(s):

    #     print("name iss ",bj.name)
    #     print("age is ",bj.age)
    #     print("name is ",s.name)
    #     print("age is ",s.age)     

# bj=a()
# bj.f()
# bj.d()
# bj.age=24
# print("name iis ",bj.name)
# print("age is ",bj.age) 


# private(using __double underscore)
# class a():
#     def f(s):
#         s.__name="yoks"
#         s.__age=23
#         print("name iss ",bj.__name)
#         print("name iss ",bj.__age)

# bj=a()
# bj.f()
# print("name iis ",bj.__name)
# print("age is ",bj.__age) 

# class a():
#     def __init__(s,name,age):
#         s.__name=name
#         s.__age=age
#     def d(s):
#         print("name is",bj.__name)
#         print("age is ",bj.__age)
# bj=a("yoks",23)
# bj.d()
# print("name is",bj.__name)
# print("age is ",bj.__age)


#mangling method  (obj._class__var)

# print(bj._a__name)

# class a():
#     def d(s):
#         s.un="Anna"
#         print(s.un)
#     def __c1(s):
#         s.c="engineering"
#         print(s.c)
#     def __c2(s):
#         print("engineering c")
# j=a()
# j.d()
# j._a__c1()
# j._a__c2()

# protected code (_ single underscore)

# class pro():
#     _name="karan"
#     _age=42
#     def dis(s):
#         print("name is",s._name)
#         print("age is",s._age)
# c=pro()
# c._name="raina"
# c.dis()
# print("name iss",c._name)
# print("age iss",c._age)

# class en():
#     def setname(s,n):
#         s.__n=n
#     def getname(s):
#         return s.__n
#     def dis(s):
#         print(s.getname())
# a=en()
# a.setname("kamal")
# a.dis()