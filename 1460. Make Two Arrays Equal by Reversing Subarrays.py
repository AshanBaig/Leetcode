class Solution:
    def letterCombinations(self, digits: str) :
        d={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        l=[]
        r_lst=[]
        for i in str(digits):
            l.append(d[i])
        mul=1
        for i in range(1,len(l)):
            mul*=len(l[i])
        print(mul)
        for i in range(len(l[0])):
            r_lst+=l[0][i]*mul
        print(r_lst)

s=Solution()
print(s.letterCombinations('234'))