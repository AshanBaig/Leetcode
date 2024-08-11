# class Solution:
#     def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
#         cc=[rStart,cStart]
#         l=[]
#         a=1
#         # l.append([cc[0],cc[1]])
#         while True:
#             print(l)
#             if len(l)>=(rows*cols):
#                 break
#             #goright
#             if a and cc[1]<cols:
#                 if [cc[0],cc[1]] not in l:
#                     l.append([cc[0],cc[1]])
#                 if cc[1]+1<cols:
#                     cc[1]+=1
#                     continue
#                 else:
#                     a=0     
#             else:
#                 a=1
#                 #check go down avalible 
#                 while cc[0]<rows:
#                     if [cc[0]+1,cc[1]] not in l:
#                         cc[0]+=1
#                         break
#                     cc[0]+=1
#                 # print(cc[0]>=row)
#                 if cc[0]>=rows:
#                     cc[0]=rows-1
#                 # godown()
#                 while True:
#                         # print(cc)
#                         if  cc[1]>-1:
#                             if [cc[0],cc[1]] not in l:
#                                 # if cc[0]>=rows:
#                                 #     cc[0]-=1
#                                 #     continue    
#                                 l.append([cc[0],cc[1]])
#                             else:
#                                 cc[1]-=1
#                                 continue
#                             if cc[0]-1>-1 and [cc[0]-1,cc[1]] not in l:
#                                 cc[0]-=1
#                                 break
#                             cc[1]-=1
#                 while cc[0]!=-1:
#                         l.append([cc[0],cc[1]])
#                         if cc[0]==0:
#                             break    
#                         cc[0]-=1
#                 # goup()
#                 #until it reaches row 0
#                 # after row zero continue
#         return l
class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        i,j = rStart, cStart

        diri, dirj = 0, 1 # directions to move
        twice = 2
        res = []
        moves = 1
        next_moves = 2

        while len(res) < (rows * cols):
            if (-1 < i < rows) and ( -1 < j < cols):
                res.append([i,j])
            
            i += diri
            j += dirj
            moves -= 1
            if moves == 0:
                diri, dirj = dirj, -diri # 90 deg Clockwise
                twice -= 1
                if twice == 0:
                    twice = 2
                    moves = next_moves
                    next_moves += 1
                else:
                    moves = next_moves - 1
        return res
s=Solution()
print(s.spiralMatrixIII(5,6,1,4))
print(s.spiralMatrixIII(3,3,0,0))