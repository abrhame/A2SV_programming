class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, len(board)):
            set1 = set()
            set2 = set()
            for j in range(0, len(board[0])):
                if board[i][j] in set1:
                    return False
                elif board[i][j] != ".":
                    set1.add(board[i][j])
                if board[j][i] in set2:
                    return False
                elif board[j][i] != ".":
                    set2.add(board[j][i])
                    
        for row in range(0,len(board), 3):
            for col in range(0, len(board[0]),3):
                set1 = set()
                
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if board[i][j] in set1:
                            return False
                        elif board[i][j] != ".":
                            set1.add(board[i][j])
        return True
           
                    
        