class Solution:
    def distributeCandies(self, candyType) -> int:
            return min(int(len(candyType)/2),len(set(candyType)))
        