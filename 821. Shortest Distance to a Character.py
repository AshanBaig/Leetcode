class Solution:
    def shortestToChar(self, s: str, c: str):
        l=[]
        r_l=[]
        for i,j in enumerate(s):
            if j==c:
                l.append(i)
        for i in range(len(s)):
            for j in range(len(l)):
                if j+1<len(l) and l[j]<i<l[j+1]:
                    r_l.append(min(abs(i-l[j]),abs(i-l[j+1])))
                    break
                elif i==l[j]:
                    r_l.append(0)
                    break
            else:
                if i<l[0]:
                    r_l.append(abs(i-l[0]))
                else:
                    r_l.append(abs(i-l[-1]))
        return r_l

        