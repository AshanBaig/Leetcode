class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lst=[]
        for _ in range(numRows):
            lst.append([])
        i=0
        while i<len(s):
            for l in range(len(lst)):
                if i>=len(s):
                    break
                lst[l].append(s[i])
                i+=1
            for j in range(numRows-2,0,-1):
                if i>=len(s):
                    break
                lst[j].append(s[i])
                i+=1
        s=''
        for i in lst:
            for j in i:
                s+=j
        return s