# Q1
# from collections.abc import Container

# class OddCount:
#     def __contains__(self,x):
#         if not isinstance(x,int) or not x%2:
#             return False
#         return True
# print(issubclass(OddCount,Container))

#Q2
try:
    raise ValueError('This is always occur')
    print('this will never execute')
except Exception as ex:
    print(f'i  caught an exception :{ex!r}')
    
print('executed after the eceptopin ')

#Q3

animal='Cat'
family='Felidae'
class Pantherinae: 
    animal='Lion'
    family='Panthera'
    def __init__(self):
        self.family='Neofelis'
        animal="Leopard"
        def display_info():
            print (self.family)
            print(self.animal)
            print(family)
            print(animal)
        display_info()
f=Pantherinae()

#Q4
def decor1(func):
    def inner():

        x=func()
        return x*x
    return inner
def decor(func):

    def inner():
        x=func()
        return 2*x
    return inner
@decor1
@decor
def num1():
    return 10
print(num1())       
@decor
@decor1
def num2():
    return 10

print(num2())

#Q5
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def doActions(self):
        pass
# a=Animal()
#############################################    
#Q6(a)

class DistanceFinder:
    ##Q7a
    def finddistance(self,p):
        return pow((pow((p.x-self.x),2)+(pow((p.y-self.y),2))),(1/2))
    ##Q7b
    # def finddistance(p1,p2):
        # return pow((pow((p2.x-p1.x),2)+(pow((p2.y-p1.y),2))),(1/2))
class Point(DistanceFinder):
    def __init__(self,x=0,y=0) -> None:
        self.setter(x,y)
    def setter(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f'<{self.x},{self.y}>'
    
class LineSegment:
    def __init__(self,x1,y1,x2,y2):
        self.obj1=Point(x1,y1)
        self.obj2=Point(x2,y2)
    def setter_obj1(self,x1=0,y1=0):
        self.obj1=Point(x1,y1)
    def setter_obj2(self,x2=0,y2=0):
        self.obj2=Point(x2,y2)
    def findlength(self):
        return pow((pow((self.obj2.x-self.obj1.x),2)+(pow((self.obj2.y-self.obj1.y),2))),(1/2))
    def __gt__(line1,line2):
        print(line1.findlength(),line2.findlength())
        return line1.findlength()>line2.findlength()
    
line1=LineSegment(1,2,4,6)
line2=LineSegment(3,8,4,12)
print(line1>line2)
p1=Point(1,2)
p2=Point(4,6)
##Q7a
print(p1.finddistance(p2))
##Q7b
# print(p1.finddistance(p2))

#Q8a
class Exponential:
    def __init__(self,b=1,e=1):
        self.base=b
        self.exp=e
        if e==0 or b==0:
            raise ValueError ('invalid input')
    def __str__(self):
        return f'{self.base}^{self.exp}'
    def __mul__(self,obj1):
        if self.base==obj1.base:
            return Exponential(self.base,self.exp+obj1.exp)
        raise TypeError ('Can not multiply')
try:    

    v1=Exponential(2,3)
    v2=Exponential(2,4)
    print(v1*v2)
    v3=Exponential(4,3)
    print(v1*v3)
    # v4=Exponential(0,3)
    # print(v2*v4)
except Exception as ex:
    print(ex)
# v5=Exponential(2,3)