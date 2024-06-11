from abc import ABC,abstractmethod
# class Vehicle(metaclass=ABCMeta):
#     @abstractmethod
#     def set_no_of_wheels(self):
#         pass
#     @abstractmethod
#     def calculate_speed_perhour(self):
#         pass

# class Car(Vehicle):
#     def set_no_of_wheels(self,n=4):
#         self.wheels=n
#         print(n,' Number of wheels  setted')
#     def calculate_speed_perhour(self,ts):
#         print("Total speed per hour is :",ts/3600)

# class Truck(Vehicle):
#     def set_no_of_wheels(self,n=6):
#         self.wheels=n
#         print(n,' Number of wheels  setted')
#     def calculate_speed_perhour(self,ts):
#         print("Total speed per hour is :",ts/3600)

# class Bike(Vehicle):
#     def set_no_of_wheels(self,n=2):
#         self.wheels=n
#         print(n,' Number of wheels  setted')
#     def calculate_speed_perhour(self,ts):
#         print("Total speed per hour is :",ts/3600)

# c1=Car()
# c1.calculate_speed_perhour(56000)
# c1.set_no_of_wheels(8)
        
# class Person(ABC):
#     def __init__(self,p) -> None:
#         self.prices=p
#     @abstractmethod
#     def ticket_price(self):
#         pass
# class Employed_person(Person):
#     def ticket_price(self):
#         concession=int(self.prices*5/100)
#         return self.prices-concession
    
# class Student(Person):
#     def ticket_price(self):
#         concession=int(self.prices*10/100)
#         return self.prices-concession
# s1=Student(200)
# print(s1.ticket_price())
# e1=Employed_person(200)
# print(e1.ticket_price())
        
        
class InputClass(ABC):
    def take_inpit(self):
        self.a=int(input('Enter First operand:'))
        self.b=int(input('Enter Second operand:'))
    @abstractmethod
    def Mathematical_Operation(self):
        pass
class Addition_operation(InputClass):
    def Mathematical_Operation(self):
        self.take_inpit()
        return self.a+self.b
class Subtraction_operation(InputClass):
    def Mathematical_Operation(self):
        self.take_inpit()
        return self.a-self.b
class Multiplication_operation(InputClass):
    def Mathematical_Operation(self):
        self.take_inpit()
        return self.a*self.b
class Division_operation(InputClass):
    def Mathematical_Operation(self):
        self.take_inpit()
        return self.a/self.b
    
m1=Multiplication_operation()
print(m1.Mathematical_Operation())
add=Addition_operation()
print(add.Mathematical_Operation())