class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def f(s,pos,set_):
            if pos==len(s):
                self.maxi=max(self.maxi,len(set_))
            substr=""
            for i in range(pos,len(s)):
                substr+=s[i]
                if substr  not in set_:
                    set_.add(substr)
                    f(s,i+1,set_)
                    set_.remove(substr)

        self.maxi=0
        set_=set()
        f(s,0,set_)
        return self.maxi