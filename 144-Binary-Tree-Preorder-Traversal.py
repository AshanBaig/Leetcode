# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        \\\
        :type root: Optional[TreeNode]
        :rtype: List[int]
        \\\
        if root==None:
            return []
        pre=[]
        stack=[root]
        while len(stack)!=0:
            root=stack.pop()
            print(root)
            pre.append((root.val))
            if root.right!=None:
                stack.append(root.right)
            if root.left!=None:
                stack.append(root.left)
        return pre
        # pre=[]
        # def preorder(root):
        #     if root==None:
        #         return
        #     pre.append(root.val)
        #     preorder(root.left)
        #     preorder(root.right)
        # preorder(root)
        # return pre
