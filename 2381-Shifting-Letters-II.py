class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        news=""
        d=[0]*(len(s)+1)
        for i in shifts:
            start,end,turn=i
            if turn==1:
                shift=1
            else:
                shift=-1
            d[start]+=shift
            if end+1<len(s):
                d[end+1]-=shift
        for i in range(1,len(s)):
            d[i]+=d[i-1]
        for i in range(len(s)):
            num=((ord(s[i])+d[i])-97)%26
            news+=chr(num+97)
        return news