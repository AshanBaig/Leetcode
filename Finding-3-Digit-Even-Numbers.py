class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        s=set()
        from itertools import permutations
        st="".join(map(str,digits))
        d= permutations(st,3)
        for i in d:
            if i[0]=="0":continue
            i="".join(i)
            i=int(i)
            if i%2==0 and i not in s:
                s.add(i)
        return sorted(list(s))