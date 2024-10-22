# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        l=[0]
        def f(root,lvl):
            try:
                l[lvl]+=root.val
            except:
                l.extend([0])
                l[lvl]+=root.val
            if root.left!=None:
                f(root.left,lvl+1)
            if root.right!=None:
                f(root.right,lvl+1)
        f(root,1)
        l.sort()
        while 0 in l:
            l.remove(0)
        if k>len(l):
            return -1
        return l[-k]