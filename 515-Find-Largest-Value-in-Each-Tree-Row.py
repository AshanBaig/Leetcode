# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        ans=[]
        q=[root]
        while len(q)!=0:
            maxi=(-2**31)-1
            for i in range(len(q)):
                node=q.pop(0)
                if node.val>maxi:
                    maxi=node.val
                if node.left!=None:
                    q.append(node.left)    
                if node.right!=None:
                    q.append(node.right)
            ans.append(maxi)
        return ans