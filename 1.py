class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        l=[]
        len_b=len(bloomDay)
        l+='_'*len_b
        print(l)
        for day in sorted(set(bloomDay)):
            for j in range(len_b):
                if bloomDay[j]==day:
                    l[j]='x'
            count=0
            m_copy=m
            for i in l:
                if i=='x':
                    count+=1
                else:
                    m_copy-=int(count/k)
                    count=0
            if count>=k:
                        m_copy-=int(count/k)
            if m_copy<=0:
                return day
        return -1

        
                    

s=Solution()
print(s.minDays([7,7,7,7,12,7,7],2,3))
print(s.minDays([1000000000,1000000000],1,1))