class Solution:
    def isValidSudoku(self, board) -> bool:
        import numpy as np
        arr=np.array(board)
        def check_1d(l):
            for i in range(len(l)):
                if l[i]!='.':
                    for f in range(len(l)):
                        if f!=i and l[i]==l[f]:
                            return False
            
            return True
        for row_check in arr:
            if not(check_1d(row_check)):
                return False
        for i in range(9):
            if not(check_1d(arr[:,i])):
                return False
        for i in range(3):
            for j in range(3):
                mat=arr[i*3:(i+1)*3,j*3:(j+1)*3]
                temp_mat=np.array([])
                for k in mat:
                    temp_mat=np.concatenate((k,temp_mat))
                if not(check_1d(temp_mat)):
                    return False
        return True
        
                    
s=Solution()
print(s.isValidSudoku([
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
print(s.isValidSudoku([
    [".",".","4",".",".",".","6","3","."],
    [".",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".","9","."],
    [".",".",".","5","6",".",".",".","."],
    ["4",".","3",".",".",".",".",".","1"],
    [".",".",".","7",".",".",".",".","."],
    [".",".",".","5",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]]))