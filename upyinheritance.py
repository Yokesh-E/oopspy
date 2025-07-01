# inheritance

#types
#1.single level 
#2.multi level
#3.multiple 
#4.hybrid
#5.hierarical

#1.single level

# class pa():
#     def det(self):
#         print("hi")
# class ch(pa):
#     def det1(self):
#         print("hello")
# bj=ch()
# bj.det()
# bj.det1()

# class per():
#     def __init__(s,na,age,gen):
#         s.name=na
#         s.age=age
#         s.gen=gen
# class ch(per):
#     def det(s):
#         print(s.name,s.age,s.gen)
# fj=ch(1,2,3)
# fj.det()

# class per():
#     def h(s):
#         s.name="hi"
#         s.age=23
#         s.gen="m"
# class ch(per):
#     def det(s):
#         print(s.name,s.age,s.gen)
# fj=ch()
# fj.h()
# fj.det()

# class per():
#     def h1(s):
#         s.name="yokz"
#         s.age=23
#         s.gen="M"
# class per1(per):
#     def h2(s,city):
#         print(s.name,s.age,s.gen,city)
# gh=per1()
# gh.h1()
# gh.h2("chennai")

# class per():
#     city="chennai"
# class per1(per):
#     @classmethod
#     def h1(cls):
#         name="yokz"
#         age=23
#         gen="M"
#         data=name,age,gen,cls.city # cls is keyword
#         return data
# print(per1.h1())


# 2.Multilevel inheritance

# class gf():
#     def fun1(self):
#         print("hi grand son") 
# class fa(gf):
#     def fun2(self):
#         print("hi son")
# class son(fa):
#     def fun3(self):
#         print("hi")
# bj=son()
# bj.fun1()
# bj.fun2()
# bj.fun3()

# class per():
#     def det1(self):
#         self.name="yokz"
#         self.age=23
#         self.gender="male"
#         print("nmae is",self.name)
#         print("age is",self.age)
#         print("gender is",self.gender)
# class company(per):
#     def det2(self):
#         self.companyname="zoho"
#         self.locat="kkulathur"
#         print("company name is",self.companyname)
#         print("location is",self.locat)
# class other(company):
#     def det3(self):
#         self.salary=50000
#         self.design="software engineer"
#         print("my detail is",self.name,self.age,self.gender,self.companyname,self.locat,self.design,self.salary)
# bj=other()
# bj.det1()
# bj.det2()
# bj.det3()

# class per():
#     def det1(self,name,age,gen):
#         self.name=name
#         self.age=age
#         self.gender=gen
#         print("nmae is",self.name)
#         print("age is",self.age)
#         print("gender is",self.gender)
# class company(per):
#     def det2(self):
#         self.companyname="zoho"
#         self.locat="kkulathur"
#         print("company name is",self.companyname)
#         print("location is",self.locat)
# class other(company):
#     def det3(self):
#         self.salary=50000
#         self.design="software engineer"
#         print("my detail is",self.name,self.age,self.gender,self.companyname,self.locat,self.design,self.salary)
# bj=other()
# bj.det1("yokz",23,"Male")
# bj.det2()
# bj.det3()

# class per():
#     def det1(self):
#         self.name=input("enter name")
#         self.age=input("enter age")
#         self.gender=input("enter gen")
#         print("nmae is",self.name)
#         print("age is",self.age)
#         print("gender is",self.gender)
# class company(per):
#     def det2(self):
#         self.companyname="zoho"
#         self.locat="kkulathur"
#         print("company name is",self.companyname)
#         print("location is",self.locat)
# class other(company):
#     def det3(self):
#         self.salary=50000
#         self.design="software engineer"
#         print("my detail is",self.name,self.age,self.gender,self.companyname,self.locat,self.design,self.salary)
# bj=other()
# bj.det1()
# bj.det2()
# bj.det3()


# 3.Multiple inheritance
# multiple parent class single child class

# class fa():
#     def det1(self):
#         print("i am nt bad i am ur dad")
# class mom():
#     def det2(self):
#         print("hi my son")
# class son(fa,mom):
#     def det3(self):
#         print("hi mom and dad")
# bj=fa()
# bj.det1()
# bj.det2()
# bj.det3()

# class fa():
#     def det1():
#         print("i am nt bad i am ur dad")
# class mom():
#     def det2():
#         print("hi my son")
# class son(fa,mom):
#     def det3():
#         print("hi mom and dad")
# bj=son
# bj.det1()
# bj.det2()
# bj.det3()


# 4.hirarical inheritance
# one parant class or base class  multiple child class or derived class

# class para():
#     def prop(self):
#         self.car="rolls roise"
#         self.bike="bmw"
# class son1(para):
#     def det1(self):
#         print("my car is",self.car)
# class son2(para):
#     def det2(self):
#         print("my bike is",self.bike)
# bj=son2()
# bj.prop()
# bj.det2()

# class para():
#     def prop(self):
#         self.a=int(input("enter a="))
#         self.b=int(input("enter b="))
# class son1(para):
#     def det1(self):
#         print("my car is",self.a)
# class son2(para):
#     def det2(self):
#         a=self.a
#         b=self.b
#         for i in range(a):
#             c=i%b
#             print(c)
# bj=son2()
# bj.prop()
# bj.det2()


# class para():
#     def det1(self):
#         self.n="yokz"
#         self.a=23
#         self.g="m"
# class ch1(para):
#     def det2(self):
#         print(self.n,self.a,self.g)
# class para1():        
#     def det3(self):
#         self.l=1   
        
# class ch2(para1):
#     def det4(self):
#         self.k=2
#         print(self.l+self.k)
# class ch3(ch2):
#     def det5(self):
#         self.j=3
#         print(self.l*self.k*self.j)
# bj=ch3()
# bj.det3()
# bj.det4()
# bj.det5()

# bj1=ch1()
# bj1.det1()
# bj1.det2()


# 5.hybrid 

# class dog():
#     def fun1(s):
#         print("dog")
# class cat(dog): #its called single inheritance
#     def fun2(s):
#         print("cat")
# class elephant(dog): #its called hirarical inheritance
#     def fun3(s):
#         print("elephant")
# class horse(cat,elephant): #its called multiple inheritance
#     def fun4(s):
#         print("horse")
# bj=horse()
# bj.fun1()
# bj.fun2()
# bj.fun3()
# bj.fun4()


#   inheritance with same method name

# class a():
#     def f(s):
#         print("hi")
# class b():
#     def f(s):
#         print("hello")
# class c(a,b):  # MRO concept (method reslution order) class a is first execute after b class  execute
#     pass
# bj=c()
# bj.f()

# class a():
#     def f(s):
#         print("hi")
# class b():
#     def f(s):
#         print("hello")
# class c(a,b):  # MRO concept (method reslution order) class c is first execute class a is seecond execute after b class  execute
#     def f(s):
#         print("ji")
# bj=c()
# bj.f()


# class a():
#     def f(self):
#         print("a")
# class b(a):
#     pass
#     # def f(self):
#     #     print("b")
# class c(a):
#     pass
#     # def f(self):
#     #     print("c")
# class d(b):
#     pass
#     # def f(self):
#     #     print("d")
# class e(c):
#     pass
#     # def f(self):
#     #     print("e")
# class f(d,e):
#     pass  
#     # def f(self):
#     #     print("f")

# print(f.__mro__)

# bj=f()
# bj.f()


# super method
# directly call anotherr class functin
# class a():
#     def __init__(self):
#         print("hi")
# class b(a):
#     def __init__(self):
#         super().__init__()
#         print("hello")
# kl=b()

# class a():
#     def f1(s):
#         print("A")
# class b(a):
#     def f2(s):
#         print("B")
# class c(b):
#     def f3(s):
#         super().f1()
#         super().f2()
#         print("C")

# k=c()
# k.f3()

# class a():
#     def f1(s):
#         print("A")
# class b(a):
#     def f2(s):
#         print("B")
#         super.f1()
# class c(a):
#     def f3(s):
#         super().f2()
        
#         print("C")

# k=c()
# k.f3()
    
# class a():
#     def f1(s):
#         print("A")
# class b():
#     def f2(s):
#         print("B")
# class c(a,b):
#     def f3(s):
#         super().f1()
#         super().f2()
#         print("C")

# k=c()
# k.f3()


# class a():
#     def f1(s):
#         print("A")
# class b(a):
#     def f2(s):
#         print("B")
# class c(b):
#     def f3(s):
#         print("C")
# class d(b,c):
#     def f4(s):
#         super().f1()
#         super().f2()
#         super().f3()
#         print("D")

# k=c()
# k.f4()
    
# class dog():
#     def fun1(s):
#         print("dog")
# class cat(dog): #its called single inheritance
#     def fun2(s):
#         print("cat")
# class elephant(dog): #its called hirarical inheritance
#     def fun3(s):
#         print("elephant")
# class horse(cat,elephant): #its called multiple inheritance
#     def fun4(s):
#         super().fun2()
#         super().fun1()
#         super(). fun3()
#         print("horse")
# bj=horse()
# bj.fun4()

# class parent():
#     def __init__(self):
#         print("Father")
#         print("Mother0")
# class child1(parent):
#     def child1name(self):
#         super().__init__()
#         print("child1name is name")
# class child2(parent):
#     def child2name(self):
#         super().__init__()
#         print("child2name is child")
# obj=child1()
# obj1=child2()
# obj.child1name()
# obj1.child2name()

