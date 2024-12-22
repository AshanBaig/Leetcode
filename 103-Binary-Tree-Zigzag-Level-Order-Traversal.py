# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        l=[]
        q=[root]
        while len(q)!=0:
            sub_l=[]
            for i in range(len(q)):
                node=q.pop(0)
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
                sub_l.append(node.val)
            if len(l)%2!=0:
                l.append(sub_l[::-1])
            else:
                l.append(sub_l)
        return l