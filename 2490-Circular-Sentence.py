class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        l=sentence.split()
        if l[0][0]!=l[-1][-1]:
            return False
        for i in range(len(l)-1,0,-1):
            if l[i][0]!=l[i-1][-1]:
                return False
        return True