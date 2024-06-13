class Solution:
    def findAnagrams(self, s: str, p: str):
        from collections import Counter
        l=[]
        i=0
        p_counter=Counter(p)
        while True:
            if len(p)+i-1>=len(s):
                break
            chunk=s[i:len(p)+i]
            if Counter(chunk)==p_counter:
                l.append(i)
            i+=1
        return l

        