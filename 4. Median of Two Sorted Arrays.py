class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums1+=nums2
        nums1.sort()
        l_num=len(nums1)
        if l_num%2:
            ind=nums1[int(l_num/2)]
            return ind/1
        ind=nums1[int((l_num/2)-1)]+nums1[int(l_num/2)]
        return ind/2
        

        