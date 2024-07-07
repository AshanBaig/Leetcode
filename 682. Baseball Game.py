class Solution:
    def calPoints(self, operations) -> int:
        l=[]
        for i in operations:
            if i=='+':
                l.append(int(l[-1]+l[-2]))
            elif i=='C':
                l.pop()
            elif i=='D':
                l.append(int(l[-1]*2))
            else:
                l.append(int(i))
        return sum(l)
                
        