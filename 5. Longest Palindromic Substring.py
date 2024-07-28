class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxi=''
        for left in range(len(s)):
            for right in range(left,len(s)):
                chunk=s[left:right+1]
                if len(chunk)>len(maxi) and chunk==chunk[::-1]:
                    maxi=chunk
        return maxi

        