# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q=[[root,0]]
        ans=0
        while len(q)!=0:
            sub_l=[]
            mini=q[0][1]
            start,end=0,0
            size=len(q)
            for i in range(size):
                node,ind=q.pop(0)
                if i==0:
                    start=ind
                elif i==size-1:
                    end=ind
                sub_l.append([node.val,ind])
                if node.left!=None:
                    q.append([node.left,(2*(ind-mini))+1])
                if node.right!=None:
                    q.append([node.right,(2*(ind-mini))+2])
            ans=max(ans,end-start+1)
        return ans
        
