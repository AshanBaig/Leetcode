# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        q=deque()
        if root==None:
            return 0
        q.append(root)
        total=0
        while len(q)!=0:
            for i in range(len(q)):
                node=q.popleft()
                total+=1
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
        return total