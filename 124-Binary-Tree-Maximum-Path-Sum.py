# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if node==None:
                return 0
            l=height(node.left)
            r=height(node.right)
            if l<0:
                l=0
            if r<0:
                r=0
            self.maxi=max(self.maxi,node.val+l+r)
            return node.val+max(l,r)
        if root==None:
            return 0
        self.maxi=root.val
        height(root)
        return self.maxi    