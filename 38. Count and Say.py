class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        base='1'
        def func(base):
            s=''
            prev=-5
            j=1
            for i in base:
                count_el=1
                if prev==i:
                    continue
                prev=i
                while j<len(base) and  base[j]==i:
                    j+=1
                    count_el+=1
                j+=1
                s+=str(count_el)+i
            return s
        for i in range(n-1):
            base=func(base)
            
        return base    
s=Solution()
print(s.countAndSay(6))