class Solution:
    def replaceWords(self, dictionary, sentence) -> str:
        sen=sentence.split()
        rstring=''
        for j in sen:
            for i in range(len(j)):
                if j[:i] in dictionary:
                    rstring+=j[:i]+' '
                    break
            else:
                    rstring+=j+' '
        return rstring.strip()
            
    
        