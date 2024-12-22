# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        prep=[]
        preq=[]
        def pre(node):
            if node==None:
                
                prep.append(None)
                return
            prep.append(node.val)
            pre(node.left)
            pre(node.right)
        pre(p)
        def pre(node):
            if node==None:
                preq.append(None)
                return
            preq.append(node.val)
            pre(node.left)
            pre(node.right)
        pre(q)
        # print(prep,preq)
        for i in range(len(prep)):
            if prep[i]!=preq[i]:
                return False
        return True