# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def search(node,target):
            if node==None:
                return [None,0]
            if node==target:
                return [node,0]
            if node.left!=None and node.left==target:
                return [node,1]
            if node.right!=None and node.right==target:
                return [node,2]
            x=search(node.left,target)
            if x[0]!=None:
                return x
            return search(node.right,target)
        
        visited=[target]
        q=[[target,0]]
        while len(q)!=0:
            ans=[]
            print(q)
            for i in range(len(q)):
                node,distance=q.pop(0)
                if distance==k:
                    ans.append(node.val)
                else:
                    x=search(root,node)
                    if x[0]!=None and x[1]!=0 and x[0] not in visited:
                        visited.append(x[0])
                        q.append([x[0],distance+1])
                    if node.left!=None and node.left not in visited:
                        q.append([node.left,distance+1])
                        visited.append(node.left)
                    if node.right!=None and node.right not in visited:
                        q.append([node.right,distance+1])
                        visited.append(node.right)
        return ans
                    


            
            
        
        
        
        
        
        
        ###############################
        # q=[]#node,remaining distance 
        # #ancestors of 5 
        # l=[]
        # def preorder(node,tupl):
        #     if node==None:
        #         return
        #     if node==target:
        #         tupl+=(node,)
        #         l.append(tupl)
        #         return 
        #     tupl+=(node,)
        #     preorder(node.left,tupl)
        #     preorder(node.right,tupl)
        # preorder(root,tuple())
        # print(l)
        # distance=k
        # for i in l[0][::-1]:
        #     q.append([i,distance])
        #     distance-=1
        # ans=[]
        # def travel(node,distance):
        #     if distance==0:
        #         ans.append(node.val)
        #     else:
        #         if node.left!=None and node.left!=target:
        #             q.append([node.left,distance-1])
        #         if node.right!=None and node.right!=target:
        #             q.append([node.right,distance-1])
        # while len(q)!=0:
        #     node,distance=q.pop(0)
        #     travel(node,distance)
        # return ans


        