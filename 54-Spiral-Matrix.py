class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        l=[]
        self.r,self.c=0,0
        mat=[]
        count=0
        for _ in range(len(matrix)):
            chunk=[]
            for _ in range(len(matrix[0])):
                chunk.append(count)
                count+=1
            mat.append(chunk)
        print(mat)
        real_mat=[]
        for i in matrix:
            for j in i:
                real_mat.append(j)
        def Right():
            while self.c<len(matrix[self.r]):
                if mat[self.r][self.c] in l:
                    self.c-=1
                    break
                l.append(mat[self.r][self.c])
                self.c+=1
            else:
                self.c-=1
            self.r+=1
            Down()
        def Down():
            
            while self.r<len(matrix):
                # print(self.r,len(matrix),self.c)
                if mat[self.r][self.c] in l:
                    self.r-=1
                    break
                l.append(mat[self.r][self.c])
                self.r+=1
            else:
                self.r-=1
            self.c-=1
            Left()
        def Left():
            while self.c>-1:
                # print('in left',self.c,l)
                if mat[self.r][self.c] in l:
                    self.c+=1
                    break
                l.append(mat[self.r][self.c])
                self.c-=1
            else:
                self.c+=1
            self.r-=1
            Up()
        def Up():
            while self.r>-1:
                # print('in up')
                if mat[self.r][self.c] in l:
                    self.r+=1        
                    break
                l.append(mat[self.r][self.c])
                self.r-=1
            else:
                self.r+=1
            self.c+=1
        while len(l)!=len(matrix)*len(matrix[0]):
            Right()
        real_l=[real_mat[i] for i in l]
        return real_l