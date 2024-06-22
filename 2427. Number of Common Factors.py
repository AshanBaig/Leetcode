class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        def func_factors(n):
            factors=[]
            for i in range(1,n+1):
                    if n%i==0:
                        factors.append(i)
            return factors
        return len(set(func_factors(a)).intersection(set(func_factors(b))))
        