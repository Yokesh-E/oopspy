# #class & object

# # class cs():
# #     print("hii")

# # class cs():
# #     print("hii")
# # cs()
# # print(cs())

# class cs():
#     print("hii")
#     a=10
#     print(a)
#     def gf(self):
#         print("hello")
#     def bf(gf):
#         print("welcome")
#     def op(a,b):
#         print(a+b)
#     # n=gf()
#     # for i in range(5):
#     #     print(i)
# #print(a)  #error not find a because nt access a var
# bg=cs()
# bg1=cs()
# print(bg1.a)
# print(bg.a)
# # print(bg.n)
# # bg.gf()
# # bg.bf()
# #bg.op(3,4) #error

# class gh():
#     global d
#     d=20
#     def op(self,a,b):
#         print(a+b+d)
# vg=gh()
# vg.op(4,6)

# class gh():
    
#     d=20
#     def op(self,a,b):
#         print(a+b+self.d)
# vg=gh()
# vg.op(4,6)

#class gh():
    # print("hi")
    
    # d=20
    # def op(self,a,b):
    #     print(a+b+self.d)
    # def op1(s):
    #     print(s.d)
    # def p2(s,*h):
    #     l=sum(h)
    #     print(l)

# vg=gh()
# print(vg)
# vg.op(4,6)
# vg.op1()
# vg.p2(1,2,3,4,5)


# class person():
#     def details(self):
        
#         name="yoki"
#         age=24
#         gender="M"
        
#     def det(self):
#         print("name is",name)
#         print("age is",age)
#         print("gen is",gender)
# bg=person()
# bg.details() #error

# class person():
#     def details(self,name,age,gender):
        
#         self.name=name
#         print("name is",name)
#         print("age is",age)
#         print("gen is",gender)
#     def det(self):
#         print("na is ",self.name)
# bg=person()
# bg.details("yoki",23,"M")
#bg.det()

# class person():
#     def details(self,name,age,gender):
        
#         self.name="yokz"
#         self.gender="M"
#         self.age=23
        
#     def det(self):
#         print("na is ",self.name)
#         print("age is",self.age)
#         print("gen is",self.gender)
# bg=person()
# bg.details()
# bg.det()

# class person():
#     name=""
#     age=0
#     gender=""

#     def details(self,name,age,gender):
        
#         self.name="yokz"
#         self.gender="M"
#         self.age=23
        
#     def det(self):
#         print("na is ",bg.name)
#         print("age is",bg.age)
#         print("gen is",bg.gender)
# bg=person()
# bg.name="yoki"
# bg.age=23
# bg.name="yokz"#rewrite the values so ones assign the values
# bg.age=23
# # bg.details()
# bg.det()

# class person():
#     a=0
#     b=0

#     def gh(self):
        
#         print(self.a+self.b)
        
# vf=person()
# vf.a=10
# vf.b=10
# vf.gh()
# class n():
#     def a():
#         return "hi"
# e=n()
# e.a()  #return nt wrk

class person():

    def details(self):
        self.name="yokz"
        self.gender="M"
        self.age=23
    def t1(self):
        self.name="z"
        self.gender="M"
        self.age=2

        
    def det(self):
        print("na is ",self.name)
        print("age is",self.age)
        print("gen is",self.gender)

    def det2(self):
        print("na is ",self.name)
        print("age is",self.age)
        print("gen is",self.gender)    
m=person()
m.details()
m.det()
m.t1()
m.det2()

