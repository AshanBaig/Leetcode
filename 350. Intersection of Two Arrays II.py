class Solution:
    def intersect(self, nums1, nums2):
        l=[]
        for i in nums1:
            if i not in l:
                r=min(nums1.count(i),nums2.count(i))
                for _ in range(r):
                    l.append(i)
        return l