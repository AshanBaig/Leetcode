# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi=0
        def height(node):
            if node==None:
                return 0
            l=height(node.left)
            r=height(node.right)
            self.maxi=max(self.maxi,l+r)
            return max(l,r)+1
        if root==None:
            return 0
        height(root)
        return self.maxi