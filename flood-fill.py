class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if old_color == color:
            return image
        def inbound(x,y):
            return 0 <= x < len(image) and 0 <= y < len(image[0])
        
        def dfs(r,c):
            if image[r][c] == old_color:
                image[r][c] = color
                directions = [(0,1),(0,-1),(1,0),(-1,0)]
                for x,y in directions:
                    n_r,n_c = r+x,c+y
                    # print(n_r,n_c)
                    if inbound(n_r,n_c):
                        dfs(n_r,n_c)
        dfs(sr,sc)
        return image