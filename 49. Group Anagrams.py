class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=[]
        for word1 in range(len(strs)):
            chunk=[strs[word1]]
            l_word1=[]
            l_word1+=strs[word1]
            l_word1.sort()
            for word2 in range(len(strs)):
                l_word2=[]
                if  len(strs[word1])==len(strs[word2]) and word1!=word2:
                    l_word2+=strs[word2]
                    l_word2.sort()
                    if l_word1==l_word2:
                        chunk.append(strs[word2])
            chunk.sort()
            if chunk not in l:
                l.append(chunk)
        return l