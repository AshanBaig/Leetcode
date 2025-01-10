from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        l=[]
        max_freq={}
        for i in words2:
            word_count=Counter(i)
            for char,val in word_count.items():
                max_freq[char]=max(val,max_freq.get(char,0))
        for i in words1:
            word_count=Counter(i)
            for char,val in max_freq.items():
                if val>word_count.get(char,0):
                    break
            else:
                l.append(i)
        return l
        