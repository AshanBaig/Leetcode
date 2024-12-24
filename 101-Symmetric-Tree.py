# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root==None or (root.left==None and root.right==None):
            return True
        def inorder(node,l,lvl=0):
            if node==None:
                l.append(None)
                return
            inorder(node.left,l,lvl+1)
            l.append([node.val,lvl])
            inorder(node.right,l,lvl+1)
        l1=[]
        l2=[]
        inorder(root.left,l1)
        inorder(root.right,l2)
        print(l1,l2)
        if l1!=l2[::-1]:
            return False

        return True