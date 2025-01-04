class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first={}
        last={}
        for i,char in enumerate(s):
            if char not in first:
                first[char]=i
            last[char]=i
        count=0
        print(first)
        print(last)
        sett=set()
        for i in first:
            if i in last:
                for j in range(first[i]+1,last[i]):
                    sub=i+s[j]+i
                    if sub not in sett:
                        sett.add(sub)
                        count+=1
            
        return count
        
        
        # sett=set()
        # self.count=0
        # def f(start,end):
        #     if  start>=end or end-start-1<=0:
        #         return
        #     if s[start]==s[end]:
        #         self.count+=end-start-1
        #         left=s[start]
        #         right=s[end]
        #         for j in range(start+1,end):
        #             temp=left+s[j]+right
        #             if temp in sett:
        #                 self.count-=1
        #             else:
        #                 sett.add(left+s[j]+right)
        #     f(start,end-1)
        # for i in range(len(s)-2):
        #     f(i,len(s)-1)
        # return self.count
            
        