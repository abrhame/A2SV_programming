class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def inbound(i,j):
            return (0<= i < len(board)) and ( 0<= j < len(board[0]))

        def solve(i,j):
            if inbound(i,j) and board[i][j] == "O":
                board[i][j] = "V"
                solve(i,j+1)
                solve(i,j-1)
                solve(i-1,j)
                solve(i+1,j)
        
        for i in range(len(board)):
            solve(i,0)
            solve(i,len(board[0])-1)
        
        for j in range(len(board[0])):
            solve(0,j)
            solve(len(board)-1,j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'V':
                    board[i][j] = "O"
                elif board[i][j]=="O":
                    board[i][j] = "X"