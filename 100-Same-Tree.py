# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def pre(p,q):
            if p==None and q==None:
                return True
            try:
                if p.val!=q.val:
                    return False
            except:
                return False
            pl=pre(p.left,q.left)
            pr=pre(p.right,q.right)
            return pl and pr 
        return pre(p,q)