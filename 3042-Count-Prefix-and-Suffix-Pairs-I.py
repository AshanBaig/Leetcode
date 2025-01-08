class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count=0
        for i in range(len(words)):
            word=words[i]
            for j in range(i+1,len(words)):
                if word in words[j][0:len(word)] and word in words[j][-len(word):]:
                    
                    count+=1
        return count