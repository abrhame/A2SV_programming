class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check(a,b,c,d,e,f,g,h,i):
            if (sorted([a,b,c,d,e,f,g,h,i]) == [1,2,3,4,5,6,7,8,9]) and (a+b+c == d+e+f == g+h+i == a+d+g == b+e+h == c+f+i == 15):
                return True
            return False
        count = 0
        for i in range(0,(len(grid) - 2)):
            for j in range(0, (len(grid) - 2)):
                if check(grid[i][j],grid[i][j+1],grid[i][j+2],grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]):
                    count += 1
        
        return count