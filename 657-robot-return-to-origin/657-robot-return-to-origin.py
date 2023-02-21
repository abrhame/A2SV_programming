class Solution:
    def judgeCircle(self, moves: str) -> bool:
#         pos = [0,0]
        
#         for move in moves:
#             if move == "U":
#                 pos[1] += 1
#             elif move == "D":
#                 pos[1] -= 1
#             elif move == "L":
#                 pos[0] -= 1
#             elif move == "R":
#                 pos[0] += 1
#         if pos == [0,0]:
#             return True
#         return False
    
        return moves.count("U") == moves.count("D") and moves.count("R") == moves.count("L")