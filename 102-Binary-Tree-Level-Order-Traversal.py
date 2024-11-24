# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        q=[root]
        ans=[]
        while len(q)!=0:
            sub_l=[]
            for _ in range(len(q)):
                node=q.pop(0)
                sub_l.append(node.val)
                if node.left!=None:
                    q.append(node.left) 
                if node.right!=None:
                    q.append(node.right)
            ans.append(sub_l)
        return ans
        
        
        
        
        
        # q=[]
        # lvlorder=[]
        # def levelorder(node,val):
        #     if node==None:
        #         return 
        #     try:
        #         lvlorder[val].append(node.val)
        #     except:
        #         lvlorder.append([node.val])
        #     levelorder(node.left,val+1)
        #     levelorder(node.right,val+1)
        # levelorder(root,0)
        # return lvlorder