class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        s=''
        sentence=sentence.split()
        count=1
        vowel='aeiouAEIOU'
        for i in sentence:
            if i[0] in vowel:
                s+=i+'ma'+(count*'a')+' '
            else:
                s+=i[1:]+i[0]+'ma'+(count*'a')+' '
            count+=1
        return s.strip()
        