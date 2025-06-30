#polymorphism

#three types are using
# 1.operator overloading
# 2.method overloading
# 3.method overridding

# a=2
# b=3
# print(int.__add__(a,b))
# print(int.__sub__(a,b))
# print(int.__mul__(a,b))
# print(int.__truediv__(a,b))


# a="h"
# b="i"
# c="k"
# print(str.__add__(a,b))
# print(str.__add__(a,b,c))#error
# print(str.__sub__(a,b))
# print(str.__mul__(a,b))
# print(str.__truediv__(a,b))

# class math():
#     def add(self,a1,b1):
#         self.a=a1
#         self.b=b1
#     def __add__(self):
#         return self.a+self.b
# obj=math()
# obj.add(20,30)
# print(obj.__add__())
# obj.add(40,20)
# print(obj.__add__())


# class c():
#     def __init__(s,a,b):
#         s.a=a
#         s.b=b
# s1=c(2,3)
# s2=c(2,3)
# s3=s1+s2
# print(s3.a+s3.b)  #error


# class a():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self,other):
#         first_value=(self.a +self.b)
#         second_value=(other.a + other.b)
#         total=a(first_value,second_value)
#         return total
#     # def __sub__(self,other):
#     #     first_value=(self.a - self.b)
#     #     second_value=(other.a - other.b)
#     #     total=a(first_value,second_value)
#     #     return total
# s1=a(5,2)
# s2=a(7,3)
# total=s1+s2
# # sub=s1 - s2
# print(total.a)
# print(total.b)
# # print(sub.a)
# # print(sub.b)


# class a():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self,other):
#         first_value=(self.a +self.b)
#         second_value=(other.a + other.b)
#         total=a(first_value,second_value)
#         return total
#     def __sub__(self,other):
#         first_value=(self.a - self.b)
#         second_value=(other.a - other.b)
#         total=a(first_value,second_value)
#         return total
#     def __mul__(self,other):
#         first_value=(self.a * self.b)
#         second_value=(other.a * other.b)
#         total=a(first_value,second_value)
#         return total
#     def __truediv__(self,other):
#         first_value=(self.a / self.b)
#         second_value=(other.a / other.b)
#         total=a(first_value,second_value)
#         return total
# s1=a(8,6)
# s2=a(7,3)
# total=s1+s2
# sub=s1 - s2
# mu=s1 * s2
# di= s1 / s2
# print(total.a)
# print(total.b)
# print(sub.a)
# print(sub.b)
# print(mu.a)
# print(mu.b)
# print(di.a)
# print(di.b)


# comparison operator overloading






# method overlading

# class a():
#     def b(s,a,b,c):
#         print(a+b+c)
#     def b(s,a,b):
#         print(a+b)
#     def b(s,a):
#         print(a)

# m=a()
# m.b(2)
# m.b(2,3)
# m.b(2,3,4) #error


# class a():
#     def b(s,a=None,b=None,c=None):
#         if (a!=None and b!=None and c!=None):
#             print(a+b+c)
#         elif(a!=None and b!=None):
#             print(a+b)
#         else:
#             print(a)
# m=a()
# m.b(2,3,2)
# m.b(2,3)
# m.b(2)

####pip install multipledispatch

# from multipledispatch import dispatch
# class a():
#     @dispatch(int,int)
#     def f(a,b):
#       print(a+b)
#     @dispatch(int,int,int)
#     def f(a,b,c):
#         print(a+b+c)
# j=a()
# j.f(2,3,4)
# j.f(2,2)

# method overriding

# class a():
#     def f(s):
#         print("f1")
# class b(a):
#     def f(s):
#         super().f()
#         print("f2")
# class c(b):
#     # def f(s):
#         pass
# j=c()
# j.f()


# class a():
    
#     def b(s,*v):
#         s=0
#         for i in v:
#             s+=i
#             print(s)
# j=a()
# j.b(1,2,3)


class a():
    def b(s,n):
        