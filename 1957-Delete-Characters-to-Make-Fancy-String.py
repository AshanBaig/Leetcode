class Solution:
    def makeFancyString(self, s: str) -> str:
        l=list(s)
        for i in range(len(s)-1,1,-1):
            if l[i]==l[i-1]==l[i-2]:
                del l[i]
        
        return "".join(l)