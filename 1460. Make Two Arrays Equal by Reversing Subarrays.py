class Solution:
    def canBeEqual(self, target, arr) -> bool:
        target.sort()
        arr.sort()
        return target==arr