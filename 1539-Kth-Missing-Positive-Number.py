class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]-(mid+1)<k:
                low=mid+1
            else:
                high=mid-1
        #missing
        # missing=arr[high]-(high+1)
        # arr[high]+more   #more is nothing but  k-missing
        #by adjusrting the formula we got  k+high+1
        print(high)
        return k+high+1
 