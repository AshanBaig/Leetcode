class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        l=[]
        i=0

        while len(l)<len(A):
            total=0
            for j in range(i+1):
                for k in range(i+1):
                    if A[j]==B[k]:
                        total+=1
                        break    
            i+=1
            l.append(total)
        return l

                
        