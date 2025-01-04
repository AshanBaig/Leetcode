class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        sub=""
        for i in words:
            sub+=i
            if sub==s:
                break
            if i not in s:
                return False
        if sub==s:return True
        return False