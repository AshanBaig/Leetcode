#Q1
x=1
def nester():
    print(x)
    class C:
        print(x)
        def method1(self):
            print(x)
        def method2(self):
            x=3
            print(x)
    l=C()
    l.method1()
    l.method2()
print(x)
nester()
#Q1b
class A:
    def inn(self):
        print('in a')
class Z(A):
    def inn(self):
        print('in Z')
        
z=Z()
z.inn() 

#Q1c
def star(func):
    def inner(a):
        print('X'*5)
        func(a)
        print('X'*5)
        
    return inner
def percent(func):
    def inner(a):
        print('T'*5)
        func(a)
        print('T'*5)
        
    return inner
@star
@percent
def printer(msg):   #printer=star(percent(printer))
    print(msg) 
printer('hello')

#Q1d
class A:
    def inn(self):
        print('in a')
class C:
    def inn(self):
        print('in c')
class X(A,C):
        pass
class Y(A):
    def inn(self):
        print('in Y')
class Z(X,Y):
        pass
obj=Z()
obj.inn()
# a=[1,1,1]
# for i in set(a):
#     print(i)
try:
    v=int(input('enter:'))
    if v<0:
        raise Exception ('Hello')
except Exception as e:
    print(e)