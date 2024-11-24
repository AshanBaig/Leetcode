# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        \\\
        :type root: Optional[TreeNode]
        :rtype: List[int]
        \\\
        inorder=[]
        if root==None:
            return  []
        stack=[]
        node=root
        while True:
            if node!=None:
                stack.append(node)
                node=node.left
            else:
                if len(stack)==0:
                    break
                node=stack.pop()
                inorder.append(node.val)
                node=node.right
        return inorder


        # def inorder_(root):
        #     if root.left!=None:
        #         inorder_(root.left)
        #     inorder.append(root.val)
        #     if root.right!=None:
        #         inorder_(root.right)
        # inorder_(root)
        # return inorder
