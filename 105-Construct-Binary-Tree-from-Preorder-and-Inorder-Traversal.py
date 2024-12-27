# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #dict for givng index of inorder
        d={}
        for i in range(len(inorder)):
            d[inorder[i]]=i
        print(d)
        def build(prestart,preend,instart,inend):
            if (prestart>preend) or instart>inend:
                return None
            root=TreeNode(preorder[prestart])

            inroot=d[root.val]  #inorder me root kaha hy
            inleft=inroot-instart   #root ke left me kitne log hain
            root.left=build(prestart+1,prestart+inleft,instart,inroot-1)
            root.right=build(prestart+inleft+1,preend,inroot+1,inend)
            return root
        return build(0,len(preorder)-1,0,len(inorder)-1)
