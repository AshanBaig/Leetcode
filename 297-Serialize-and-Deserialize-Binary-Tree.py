# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        \\\Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        \\\
        l=[]
        q=[root]
        while len(q)!=0:
            arr=[]
            for i in range(len(q)):
                node=q.pop(0)
                if node==None:
                    arr.append(\null\)
                else:
                    arr.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            for i in arr:
                if i!=None:
                    l.append(arr)
                    break
        if len(l)==0:
            return \\
        s=\\
        for i in l:
            s+=str(i)+\!\
        return s
        

    def deserialize(self, data):
        \\\Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        \\\
        s=data.split(\!\)[0:-1]
        print(s)
        if len(s)==0:
            return None
        item=eval(s[0])[0]
        if item==\null\:
            return None
        root=TreeNode(int(item))
        s.pop(0)
        print(root)
        q=[root]
        while len(s)!=0:
            data=eval(s.pop(0))
            for i in range(0,len(data),2):
                node=q.pop(0)
                nl=TreeNode(data[i])
                nr=TreeNode(data[i+1])
                q.append(nl)
                q.append(nr)
                node.left=nl
                node.right=nr
        return root
                
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))