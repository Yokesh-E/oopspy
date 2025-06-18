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

class gh():
    print("hi")
    
    d=20
    def op(self,a,b):
        print(a+b+self.d)
    def op1(s):
        print(s.d)
    def p2(s,*h):
        l=sum(h)
        print(l)


vg=gh()
print(vg)
# vg.op(4,6)
# vg.op1()
# vg.p2(1,2,3,4,5)