class DFS:
    
    #   Time:   O(V + E)
    #   Space:  O(V)

    def __isValidCell(self, image: List[List[int]], nr: int, nc: int, oldColor: int) -> bool:
        
        if ( nr >= 0 and nr < len(image) and nc >= 0 and nc < len(image[0]) and image[nr][nc] == oldColor):
            return True
        return False
    
    def __dfs(self, image: List[List[int]], sr: int, sc: int, newColor: int, oldColor: int) -> None:
        
        image[sr][sc] = newColor
        
        directions = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]
        
        for direction in directions:
            
            nr, nc = sr + direction[0], sc + direction[1]
            if (self.__isValidCell(image, nr, nc, oldColor)):
                self.__dfs(image, nr, nc, newColor, oldColor)
                
        return
                
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        oldColor = image[sr][sc]
        
        if (image == None or len(image) == 0 or oldColor == newColor):
            return image
        
        self.__dfs(image, sr, sc, newColor, oldColor)
        
        return image


from collections import deque

class BFS:

    #   Time:   O(V + E)
    #   Space:  O(V)
    
    def __isValidCell(self, image: List[List[int]], nr: int, nc: int, oldColor: int) -> bool:
        
        if ( nr >= 0 and nr < len(image) and nc >= 0 and nc < len(image[0]) and image[nr][nc] == oldColor):
            return True
        return False
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        oldColor = image[sr][sc]
        
        if (image == None or len(image) == 0 or oldColor == newColor):
            return image
        
        directions = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]
        queue = deque ( [ (sr, sc) ] )
        
        while (queue):
            
            sr, sc = queue.popleft()
            image[sr][sc] = newColor
            
            for direction in directions:
            
                nr, nc = sr + direction[0], sc + direction[1]
                if (self.__isValidCell(image, nr, nc, oldColor)):
                    queue.append( (nr, nc) )
        
        return image