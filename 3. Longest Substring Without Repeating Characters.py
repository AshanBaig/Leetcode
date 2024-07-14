class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi=0
        for left in range(len(s)):
            sub_s=''
            for right in range(left,len(s)):
                    if s[right] not in sub_s:
                        sub_s=s[left:right+1]
                    else:
                        maxi=max(maxi,len(sub_s))
                        break
            maxi=max(maxi,len(sub_s))
        return maxi