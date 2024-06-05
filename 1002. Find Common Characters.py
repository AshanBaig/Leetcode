class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s=''
        word=words[0]
        for char in word:
            if char not in s:
                count_char=word.count(char)
                for i in range(1,len(words)):
                    if char not in words[i] :
                        break
                    count_char=min(words[i].count(char),count_char)
                else:
                    s+=char*count_char
        return list(s)
        