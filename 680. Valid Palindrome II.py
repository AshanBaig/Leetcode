class Solution:
    def validPalindrome(self, s: str) -> bool:
        s_reverse=s[::-1]
        l=len(s)
        if s==s_reverse:
            return True
        for i in range(l):
            temp=s[:i]+s[i+1:]
            r_temp=s_reverse[:l-i-1]+s_reverse[l-i:]
            if temp==r_temp:
                return True
        return False
        