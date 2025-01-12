class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
            if len(s)%2:
                return False
            b=0
            for i in range(len(s)):
                if locked[i]=="0" or s[i]=="(":
                    b+=1
                else:
                    b-=1
                if b<0:
                    return False
            b=0
            for i in range(len(s)-1,-1,-1):
                if locked[i]=="0" or s[i]==")":
                    b+=1
                else:
                    b-=1
                if b<0:
                    return False        
            return True