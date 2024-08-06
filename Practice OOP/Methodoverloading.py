'''#problem 1
class MyStr:
    def __init__(self,s) :
        self.s=s
    def __add__(self,n):
        return self.s+str(n)

s=MyStr('Computer ')
print(s+8) '''
        
#problem 2
class Point:
    def __init__(self,x=0,y=0) -> None:
        self.x=x
        self.y=y
    def __str__(self) -> str:
        return f'<{self.x},{self.y}>'
    # def __add__(self,p):
    #     return self.x+p.x,self.y+p.y
    def __add__(self,p):
        return Point(self.x+p.x,self.y+p.y)
    def __iadd__(self,p):
        # self.x+=p.x
        # self.y+=p.y
        return Point(self.x+p.x,self.y+p.y)  #Asssignment opearator overloading always close with return object name other wise none will be return and assign to self/p1
    def __neg__(self):
        return -self.x,-self.y 
p1=Point(2,3)
p2=Point(4,5)
print(p1+p2)
p1+=p2 #Point.__iadd__(p1,p2) or p1.__iadd__(p2)
print(-p1)   #Point.__neg__(p1) or p1.__neg__() 
a=p1+p2
print(type(a),a) #uncomment the code and check    
class Line:
    def __init__(self,p1=None,p2=None) -> None:
        print(type(p1),type(p2))
        if isinstance(p1,Point):
            self.p1=p1
        else:
            self.p1=Point(0,0)
        if isinstance(p2,Point):
            self.p2=p2
        else:
            self.p2=Point(0,0)
    def __invert__(self):
        return f'{self.p2.x**2}'
p1=Point(1,2)
p2=Point(5,6)
l=Line(p1,p2)
print(~l)

from abc import ABC,abstractmethod
from collections.abc import Container
class odd():
    @classmethod
    def c(cls):
        return 'iam classs method'
    def i(self):
        return 'iam instance'
    
o=odd()
print(odd.i(o))  #if i call instance function with class name so i have to provide object(self)
print(odd.c())  #if i call  clss method so no need of passing any argument bcz cls points to odd

print(o.c())  #o is passing as cls(class name)


def decor1(f):
    def inner():
        x=f()
        return x*x
    return inner
def decor(f):
    def inner():
        x=f()
        return 2*x
    return inner
@decor1
@decor 
def num():
    return 10
print(num())
@decor
@decor1
def num2():
    return 10
print(num2())