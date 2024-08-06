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
