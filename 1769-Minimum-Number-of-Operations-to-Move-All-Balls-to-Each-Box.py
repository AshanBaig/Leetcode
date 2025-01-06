class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        def f(ind,total):
            if ind>=len(boxes):
                return total
            for left in range(0,ind):
                if boxes[left]=="1":
                    total+=ind-left
            for right in range(ind+1,len(boxes)):
                if boxes[right]=="1":
                    total+=right-ind

            return total
        l=[]
        for i in range(len(boxes)):
            l.append(f(i,0))
        return l
