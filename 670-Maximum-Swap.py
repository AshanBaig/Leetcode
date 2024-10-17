class Solution:
    def maximumSwap(self, num: int) -> int:
        l=[int(i) for i in str(num)]
        def last_occur(i,m):
            for j in range(len(l[i:])):
                if l[i:][j]==m:
                    ind=j
            return ind+i
        for i in range(len(l)):
            m=max(l[i:])
            if l[i]<m:
                ind=last_occur(i,m)
                l[i]+=l[ind]
                l[ind]=l[i]-l[ind]
                l[i]-=l[ind]
                s=\\
                for i in l:
                    s+=str(i)
                return int(s)
        return num