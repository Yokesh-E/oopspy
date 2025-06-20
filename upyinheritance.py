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

class per():
    city="chennai"
class per1(per):
    @classmethod
    def h1(cls):
        name="yokz"
        age=23
        gen="M"
        data=name,age,gen,cls.city # cls is keyword
        return data
print(per1.h1())