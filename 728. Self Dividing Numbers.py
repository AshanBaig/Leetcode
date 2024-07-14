class Solution:
    def selfDividingNumbers(self, left: int, right: int) :
        l=[]
        for i in range(left,right+1):
            s=str(i)
            for j in s:
                if '0' in s or i%int(j)!=0:
                    break
            else:
                l.append(i)
        return l
        