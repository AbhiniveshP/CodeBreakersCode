class DFS:
    
    def __dfs(self, matrix: List[List[int]], row: int, col: int, previousValue: float, ocean: List[List[int]]) -> None:
        
        #   base case
        if ( row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] < previousValue):
            return
        
        #   visited cell (kind of memoized)
        if (ocean[row][col] == 1):
            return
        
        #   update current cell
        ocean[row][col] = 1
        
        directions = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]
        
        #   dfs on all 4 directions
        for direction in directions:
            nr, nc = row + direction[0], col + direction[1]
            self.__dfs(matrix, nr, nc, matrix[row][col], ocean)
            
        return
            
    
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        
        #   edge case check
        if (matrix == None or len(matrix) == 0):
            return []
        
        #   initializations
        nRows, nCols = len(matrix), len(matrix[0])
        pacific = [ [ 0 for c in range(nCols) ] for r in range(nRows) ]
        atlantic = [ [ 0 for c in range(nCols) ] for r in range(nRows) ]
        outputCells = []
        
        #   now start dfs from all borders
        for c in range(nCols):
            self.__dfs(matrix, 0, c, float('-inf'), pacific)
            self.__dfs(matrix, len(matrix) - 1, c, float('-inf'), atlantic)
            
        for r in range(nRows):
            self.__dfs(matrix, r, 0, float('-inf'), pacific)
            self.__dfs(matrix, r, len(matrix[0]) - 1, float('-inf'), atlantic)
        
        #   if both pacific and atlantic are 1 => append the cell   
        for r in range(nRows):
            for c in range(nCols):
                if (pacific[r][c] == 1 and atlantic[r][c] == 1):
                    outputCells.append( [r, c] )
                    
        return outputCells



class BFS:
            
    def __bfs(self, matrix: List[List[int]], nRows: int, nCols: int, ocean: List[List[int]], queue: List) -> None:
        
        directions = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]
        
        while (queue):
            
            row, col, previousValue = queue.popleft()

            #   bfs on all 4 directions
            for direction in directions:
                nr, nc = row + direction[0], col + direction[1]
                
                #   base case
                if ( nr < 0 or nc < 0 or nr >= len(matrix) or nc >= len(matrix[0]) or matrix[nr][nc] < previousValue):
                    continue
                
                #   visited cell (kind of memoized)
                if (ocean[nr][nc] == 1):
                    continue

                queue.append( (nr, nc, matrix[nr][nc]) )
                ocean[nr][nc] = 1
                
        return
        
        
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        
        #   edge case check
        if (matrix == None or len(matrix) == 0):
            return []
        
        #   initializations
        nRows, nCols = len(matrix), len(matrix[0])
        pacific = [ [ 0 for c in range(nCols) ] for r in range(nRows) ]
        atlantic = [ [ 0 for c in range(nCols) ] for r in range(nRows) ]
        outputCells = []
        
        pacificQueue, atlanticQueue = deque([]), deque([])
        
        #   now start bfs from all borders
        for c in range(nCols):
            pacificQueue.append( (0, c, matrix[0][c]) )
            atlanticQueue.append( (nRows - 1, c, matrix[nRows - 1][c]) )
            pacific[0][c], atlantic[nRows - 1][c] = 1, 1
            
        for r in range(nRows):
            pacificQueue.append( (r, 0, matrix[r][0]) )
            atlanticQueue.append( (r, nCols - 1, matrix[r][nCols - 1]) )
            pacific[r][0], atlantic[r][nCols - 1] = 1, 1
        
        self.__bfs(matrix, nRows, nCols, pacific, pacificQueue)
        self.__bfs(matrix, nRows, nCols, atlantic, atlanticQueue)
        
        #   if both pacific and atlantic are 1 => append the cell 
        for r in range(nRows):
            for c in range(nCols):
                if (pacific[r][c] == 1 and atlantic[r][c] == 1):
                    outputCells.append( [r, c] )
                    
        return outputCells