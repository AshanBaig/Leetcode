from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        c=Counter(s)
        odd=0
        if len(s)<k:
            return False
        for i in c:
            if c[i]%2:
                odd+=1 
        return odd<=k
                
        