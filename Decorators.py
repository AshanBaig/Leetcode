def mydecorator(func):
    def mywrapper(n):
        print('bfore')
        func(n)
        print('after')
    return mywrapper 


@mydecorator
def function_(n):
    print(n)

# print(function_('Ashan'))

from time import time
def find_time(f):
    def wrapper():
        t1=time()
        f()
        t2=time()
        return t2-t1
    return wrapper

@find_time
def func():
    for i in range(10000000):
        pass
# print(func())
def deco(f):
    def wrapper(a,b):
        avg=f(a,b)
        if avg>=6:
            print('pass')
        print(f'Your averege is :{avg}')
    return wrapper
        




@deco
def averege(a,b):
    return (a+b)/2
# averege(7,8.6)