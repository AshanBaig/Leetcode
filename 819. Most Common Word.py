class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        import re #r'[ ,;]+'
        l=re.split(r"[ !?',;.]+",paragraph)
        newl=[]
        for word in l:
            if word=='':
                continue
            if not word.isalpha():
                word=word[:-1]
            newl.append(word.lower())
        count=0
        for i in set(newl):
            if newl.count(i)>count and i not in banned:
                count=newl.count(i)
                r_value=i
        return r_value


        