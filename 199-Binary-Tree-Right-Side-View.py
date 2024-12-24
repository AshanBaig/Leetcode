# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=[root]
        if root==None:
            return []
        l=[]
        while len(q)!=0:
            sub_l=[]
            for i in range(len(q)):    
                node=q.pop(0)
                sub_l.append(node.val)
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
            l.append(sub_l[-1])
        return l

