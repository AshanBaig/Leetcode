class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        num='0'
        sign='+'
        num_present=0
        for i in s:
            # print(i,num)
            if i=='-':
                if num_present:
                    break
                num_present=1
                sign='-'
            elif i=='+':
                if num_present:
                    break
                num_present=1
                sign='+'
            elif i.isdigit():
                num_present=1
                num+=i
            else:
                break
        num=int(num)
        if sign=='-':
            num*=-1
        if num<(-1*2**31):
            return -1*2**31
        elif num>2**31-1:
            return 2**31-1
        return num