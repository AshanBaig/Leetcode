class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        l=[]
        while n:
            l.append(n%2)
            n=int(n/2)
        left=l[0]
        for i in range(0,len(l),2):
            if i+1<len(l) and l[i+1]==left:
                return False
            if left!=l[i]:
                return False

        return True
        