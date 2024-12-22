# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d={}
        def f(node,r,c):
            if node==None:
                return
            if c in d:
                for i in d[c]:
                
                    if r==i[0]:
                        i[1].append(node.val)
                        i[1].sort()
                        break
                else:
                    d[c].append([r,[node.val]])
            else:
                d[c]=[[r,[node.val]]]
            f(node.left,r+1,c-1)
            f(node.right,r+1,c+1)
        f(root,0,0)
        l=[]
        print(d)
        for i in sorted(list(d.keys())):
            s=[]
            d[i].sort(key=lambda x: x[0])
            for j in d[i]:
                s+=j[1]
            
            l.append(s)
            # print(l)
        return l