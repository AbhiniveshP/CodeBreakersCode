class Solution:

    #   Time:   O(V + E)
    #   Space:  O(V + E)

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        #   edge case check
        if (maze == None or len(maze) == 0):
            return False
        
        #   initializations
        rows, cols = len(maze), len(maze[0])
        directions = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]
        
        #   initialize queue and visited
        queue = deque( [start] )
        visited = set( tuple(start) )
        
        while (queue):
            
            #   pop out current cell and check if destination
            cr, cc = queue.popleft()
            
            if ( destination == [cr, cc] ):
                    return True
            
            #   in all 4 directions,
            for x, y in directions:
                nr, nc = cr + x, cc + y
                
                #   move in the same direction until you hit wall
                while (nr >= 0 and nr < rows and nc >= 0 and nc < cols and maze[nr][nc] == 0):
                    nr, nc = nr + x, nc + y
                
                #   backtrack the last step    
                nr, nc = nr - x, nc - y
                
                #   add the new cell to the queue
                if ( tuple([nr, nc]) not in visited):
                    queue.append( [nr, nc] )
                    visited.add( tuple([nr, nc]) )
                
        return False.  