class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if (obstacleGrid == None or len(obstacleGrid) == 0):
            return 0
        
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        
        uniquePathsDP = [ [ 0 for c in range(cols)] for r in range(rows) ]
        if (obstacleGrid[0][0] == 0):   uniquePathsDP[0][0] = 1
            
        r, c = 1, 1
        
        while (r < rows):
            if (obstacleGrid[r][0] == 1):
                break
            uniquePathsDP[r][0] = uniquePathsDP[r - 1][0]
            r += 1
            
        while (c < cols):
            if (obstacleGrid[0][c] == 1):
                break
            uniquePathsDP[0][c] = uniquePathsDP[0][c - 1]
            c += 1
            
        for r in range(1, rows):
            for c in range(1, cols):
                
                left, top = 0, 0
                
                if (obstacleGrid[r][c - 1] != 1):   left += uniquePathsDP[r][c - 1]
                
                if (obstacleGrid[r - 1][c] != 1):   top += uniquePathsDP[r - 1][c]
                
                if (obstacleGrid[r][c] == 1):   uniquePathsDP[r][c] = 0
                else:   uniquePathsDP[r][c] = left + top
                    
        return uniquePathsDP[rows - 1][cols - 1]
                