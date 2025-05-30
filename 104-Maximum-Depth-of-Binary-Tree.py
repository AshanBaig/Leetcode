from queue import Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # def height(node,count):
        #     if node==None:
        #         return 0
        #     l=height(node.left,count+1)+1
        #     r=height(node.right,count+1)+1
        #     return max(l,r)
        # return height(root,0)
        if root==None:
            return 0
        q=Queue()
        level=0
        q.put(root)
        while not(q.empty()):
            for i in range(q.qsize()):
                node=q.get()
                if node.left!=None:
                    q.put(node.left)
                if node.right!=None:
                    q.put(node.right)
            level+=1
        return level