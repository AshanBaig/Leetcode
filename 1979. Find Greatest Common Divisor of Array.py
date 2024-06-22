class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def func_factors(n):
            factors=[]
            for i in range(1,n+1):
                if n%i==0:
                    factors.append(i)
            return set(factors)
        return max(func_factors(max(nums)).intersection(func_factors(min(nums))))

        