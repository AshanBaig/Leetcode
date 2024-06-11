class Solution:
    def relativeSortArray(self, arr1, arr2):
        l=[]
        for i in arr2:
            for j in arr1:
                if i==j:
                    l.append(j)
        arr1.sort()
        for j in arr1:
            if j not in l:
                # arr1.count(j)
                for i in range(arr1.count(j)):
                    l.append(j)
        return l