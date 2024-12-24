# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        l=[]
        def preorder(node,tupl,target):
            if node==None:
                return 
            if node==target:
                tupl+=(node,)
                l.append(tupl)
                return
            tupl+=(node,)
            preorder(node.left,tupl,target)
            preorder(node.right,tupl,target)
        ptupl=tuple()
        preorder(root,ptupl,p)
        qtupl=tuple()
        preorder(root,qtupl,q)
        ans=0
        for i in l[0]:
            for j in l[1]:
                
                if i==j and j!=None:
                    ans= i
        return ans




        
        