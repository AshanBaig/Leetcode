# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        d={}
        for i in range(len(inorder)):
            d[inorder[i]]=i
        
        def build(poststart,postend,instart,inend):
            if postend>poststart or instart>inend:
                return None
            #left,right,root post pr ulta jana prega prestart last ka hoga and preend means 0
            root=TreeNode(postorder[poststart])
            #left se acha right check kro Q k wo root ke thek brabar me hy post me

            inroot=d[root.val]
            inright=inend-inroot
            root.right=build(poststart-1,poststart-inright,inroot+1,inend)
            root.left=build(poststart-inright-1,postend,instart,inroot-1)
            return root
        return build(len(postorder)-1,0,0,len(inorder)-1)
