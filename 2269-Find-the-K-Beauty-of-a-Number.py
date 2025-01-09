class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        self.c=0
        num=str(num)
        def f(ind):
            if ind+k>len(num):
                return
            # num[ind:ind+k]
            a=int(num[ind:ind+k]) 
            if a!=0 and int(num)%a==0  :
                
                self.c+=1
            f(ind+1)
        f(0)
        return self.c