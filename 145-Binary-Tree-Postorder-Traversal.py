# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder=[]
        stack=[root]
        if root==None:
            return []
        while len(stack)!=0:
            root=stack.pop()
            postorder.append(root.val)
            if root.left!=None:
                stack.append(root.left)
            if root.right!=None:
                stack.append(root.right)    
        return postorder[::-1]