# # x='Global'
# # class A:
# #     x='Class A'
# #     def __init__(self) -> None:
# #         print('hello')
# #         x='Local A'
# #         c=self.B()
# #     class B:
# #         print(x)
        
# # a=A()
# # hello()
# # def hello():
# #     print('hello')
# class point:
#     def __init__(self,x=0,y=0):
#         self.xcord = x
#         self.ycord = y 
#     def _str_(self):
#         return f'{self.xcord},{self.ycord}'
# p1=point(4,5)   
# #print(p1)

# class DistanceFinder:
#     def distance(self,p1,p2):
#         return ((p2.xcord - p1.xcord)**2-(p2.ycord - p1.ycord)**2)**0.5
    
# class polygon(DistanceFinder):
#     def __init__(self):
#         self.point_lst = []

#     def add_point(self, point):
#         self.point_lst.append(point)

#     # @staticmethod 
#     # def distance(p1,p2):
#     #     return ((p2.xcord - p1.xcord)**2-(p2.ycord - p1.ycord)**2)**0.5
    
#     def perimeter(self):
#         if len(self.point_lst) < 2:
#             return 0 #perimeter can't be found 
        
#         perimeter = 0
#         point_length = len(self.point_lst)

#         for i in range(point_length - 1):
#             p1 = self.point_lst[i]
#             p2 = self.point_lst [i + 1]

#             distance = self.distance (p1,p2)

#             perimeter+=distance 

#         p1 = self.point_lst[-1]
#         p2 = self.point_lst[0]

#         distance_2 = self.distance(p1,p2)

#         perimeter+=distance_2

#         return perimeter

# square = [point(90,2),point(2,3),point(5,6),point(6,7)]  
# triangle = [point(1,7),point(8,10),point(5,10)]

# square_polygon = polygon()
# triangle_polygon = polygon()
# for i in square:
#     square_polygon.add_point(i)

# for i in triangle:
#     triangle_polygon.add_point(i)

# print(f'Perimeter of triangle is {triangle_polygon.perimeter()}')
# print(f'Perimeter of square is {square_polygon.perimeter()}')

# acc='b'
# a=['a','b','c']
# for i in range(len(a)):
#     if a[i].accountnumber==acc:
#         a[i].transiction.append()
        
# with open('a.txt') as f:
#     a=f.readline()
#     print(f.readline())
# class A:
#     def __init__(self) -> None:
#         self.COLOR='green'
#     @property
#     def COLOR(self):
#         return self.__color
#     @COLOR.setter
#     def COLOR(self,c):
#         self.__color=c

# a=A()
# print(a.COLOR,type(A.COLOR))
# Class3=1

# def test_load_accounts():
#     # Given a file 'BANK.txt' with known content
#     expected_total_accounts = 2  # Assume there are 2 accounts in the file
#     Class3.loadAccounts()  # Load accounts from the file
#     assert Class3.totalAccounts == expected_total_accounts, "Total accounts not loaded correctly"
#     assert len(Class3.accountsList) == expected_total_accounts, "Accounts list not loaded correctly"
    
class Circle:
    def __init__(self,radius) -> None:
        self.radius=0
        try:
            assert radius>0 ,'Hello'
            self.radius=radius
        except AssertionError as e:
            print(e)
    def area(self):
        return round(3.142*self.radius**2,2)

# import unittest
# class rCircle(unittest.TestCase):
#     def test_Area1(self):
#         c=Circle(2)
#         self.assertEqual(c.area(),12.57)
#     def test_glfksgskgrea2(self):
#         c=Circle(-2)
#         self.assertEqual(c.area(),False)
#     def test_Area3(self):
#         c=Circle(0)
#         self.assertEqual(c.area(),0.00)
            
            
# unittest.main()
import logging
from time import time,sleep
def mydecor(f):
    def wrapper():
        t1=time()
        f()
        t2=time()
        logging.critical(t2-t1)
    return wrapper

@mydecor
def inpt():
    input('Enter:')

inpt()
