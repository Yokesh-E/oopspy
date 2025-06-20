#constructor
# __init__

# class clas():
#     def vf(self):
#         print("hi")
# gh=clas()
# gh.vf() #its class

# class con():
#     def __init__(self):
#         print("hi")
#     def __init__(self):
#         print("hello")#over write
# obj=con() its constructr

#cnst with var values

# class con():
#     def __init__(self):
#         print("hi")
#         name="yokz"
#         age=23
#         print(name)
#         print(age)
    
# obj=con() #its constructr

# class con():
#     def __init__(self):
#         print("hi")
#         name="yokz"
#         age=23
#         print(name)
#         print(age)
    # def fe(self):
    #     print("name is",self.name)
    
# obj=con() 


# class con():
#     def __init__(self):
#         print("hi")
#         self.name="yokz"
#         self.age=23
#         print(self.name)
#         print(self.age)
#     def fe(self):
#         print("name is",self.name)
# obj=con() 
# obj.fe()

# class log():
#     def __init__(self):
#         self.uname="yokz"
#         self.upass="12345"
#     def chec(self):
#         name=input("enter")
#         pas=input("pass=")
#         if self.uname==name:
#             if self.upass==pas:
#                 print("login successed")
#             else:
#                 print("wrong passwrd")
#         else:
#             print("wrong username")

# obj=log()
# obj.chec()

# class log():
#     def __init__(self,name,age):
#         print(name,age)
# gh=log("yokz",23)

# class kl():
#     def __init__(self,a,b,*,c,d):
#         print(a)
#         print(b)
#         print(c)
#         print(d)
# obj=kl("pos1","pos2",c="key1",d="key2")

# class kl():
#     def __init__(self,a,b,/,c,d):
#         print(a)
#         print(b)
#         print(c)
#         print(d)
# obj=kl("pos1","pos2",c="key1",d="key2")

# class test():
#     def __init__(self,x,*y):
#         z=x
#         for i in y:
#             z=z+i
#             print(z)
# obj=test(10,10,20,30,10,20,9)

# class test():
#     def __init__(self,x,*y):
#         x1=y[0]
#         x2=y
#         print(x1)
#         print(x2)
# bj=test(10,10,10,10,9)


# class det():
#     def __init__(self,no,**val):
#         print(no)
#         print(val['n1'])
#         print(val['n2'])
#         print(val['n3'])
# pj=det("yokz",n1=10,n2=20,n3=30)#multiple keyword

# class det():
#     def __init__(self,no,*val):
#         print(no)
#         print(val[0])
#         print(val[1])
#         print(val[2])
# pj=det("yokz",10,20,30) # multiple positional 

# class det():
#     def __init__(self,no,*val):
#         print(no)
#         self.g=val[0]
#         print(val[0])
#         print(val[1])
#         print(val[2])
#     def hi(self):
#         print(self.g)
# pj=det("yokz",10,20,30) # multiple positional
# pj.hi() 


#  __str__

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)

# print(p1)

# class test():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# obj=test("yokz",23)
# print(obj.name)
# print(obj.age)

# obj.name="rck"
# obj.age=24
# print(obj.name)
# print(obj.age)


# class dr():
#     version=2005
#     def __init__(s,a,b,c):
#         s.a=a
#         s.b=b
#         s.c=c
#     def dis(s):
#         print(s.a,s.b,s.c,s.version)
# obj=dr("bmw","black",123)
# print(obj.a)
# print(obj.b)
# print(obj.c)
# obj.dis()


#inside function create var its instance variable
#inside class create var its called class variable

#two methods
#1.@class method
#2.@static method
#we use directly call function like print(gf.__init__(5,5)) 
#we dont create object like kj=gf

# class gf():
#     @staticmethod
#     def __init__(x,y):
#         return x+y
# print(gf.__init__(5,5))

# class bf():
#     num=10
#     @classmethod
#     def hk(r):
#         return r.num
# print(bf.hk())

# class bf():
#     num=10
    
#     def hk(r):
#         return r.num
# print(bf.hk())  #error

# class bf():
#     num=10
    
#     def hk(r):
#         return num
# kl=bf()
# print(kl.hk) #return address 

class bf():
    @classmethod  #error
    num=10 
    
    def hk(r):
        return r.num
print(bf.hk())

