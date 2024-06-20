#\Time Taken by function
from collections import Counter
import time
def decorates(func):
    def wrapper(n):
        inital_time=time.time()
        # print(inital_time)
        print(func(n))
        final_time=time.time()
        print('time:',round(final_time-inital_time,3))
    return wrapper
    
@decorates
def countPrimes( n: int) -> int:
        l=[i for i in range(2,n+1)]
        loop=0
        print(l)
        p=l[loop]
        while int(0.5*p)<=n:
            for i in range(p,len(l)):
                print(p,'ppppp')
                if p !=0 and l[i]%p==0:
                    l[i]=0
            print(l)
                 
            p=l[loop]
            loop+=1
            while p==0:
                 p=l[loop]
                 loop+=1
                 
        while 0 in l:
                l.remove(0)
        return len(l)
            





print(countPrimes(10))  
# print(countPrimes(499979))