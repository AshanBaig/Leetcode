#\Time Taken by function
import time
def decorates(func):
    def wrapper(nums, goal):
        inital_time=time.time()
        # print(inital_time)
        print(func(nums, goal))
        final_time=time.time()
        print('time:',round(final_time-inital_time,3))
    return wrapper
    
@decorates