from collections import deque

class Solution:
    
    #   Time:   O(V + E)
    #   Space:  O(V)
    
    def __isValidCell(self, grid: List[List[int]], r: int, c: int) -> bool:
        
        if (r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] == 1):
            return True
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if (grid == None or len(grid) == 0):
            return 0
        
        directions = [ [0, 1], [0, -1], [1, 0], [-1, 0] ]
        queue = deque( [] )
        fresh = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                
                if (grid[r][c] == 1):   
                    fresh += 1
                if (grid[r][c] == 2):
                    queue.append( (r, c) )
        
        minutes = -1
        while (queue):
            
            levelSize = len(queue)
            for i in range(levelSize):
                
                currentCell = queue.popleft()
                for direction in directions:
                    nr, nc = currentCell[0] + direction[0], currentCell[1] + direction[1]
                    if (self.__isValidCell(grid, nr, nc)):
                        queue.append( (nr, nc) )
                        grid[nr][nc] = 2
                        fresh -= 1
                        
            minutes += 1
                    
        
        if (fresh != 0):
            return -1
        return minutes if minutes >= 0 else 0