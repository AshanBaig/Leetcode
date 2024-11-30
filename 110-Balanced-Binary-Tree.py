# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans=True
        def height(node,count):
            if node==None:
                return 0
            l=height(node.left,count+1)+1
            r=height(node.right,count+1)+1
            print(l,r)
            if abs(l-r)>1:
                self.ans=False
            return max(l,r)
        height(root,0)   
        return self.ans