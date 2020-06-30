class DFS:
    
    #   Time:   O(V + E)
    #   Space:  O(V)

    def __dfs(self, room: int, rooms: List[List[int]], visited: set) -> bool:
        
        if ( len(visited) == len(rooms) ):
            return True
        
        visited.add(room)
        
        for neighbor in rooms[room]:
            
            if (neighbor not in visited):
                self.__dfs(neighbor, rooms, visited)
                
        return ( len(visited) == len(rooms) )
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        if (rooms == None or len(rooms) == 0):
            return True
        
        visited = set()
        
        return self.__dfs(0, rooms, visited)


from collections import deque

class BFS:

    #   Time:   O(V + E)
    #   Space:  O(V)
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        if (rooms == None or len(rooms) == 0):
            return True
        
        visited = set( [0] )
        queue = deque( [0] )
        
        while (queue):
            
            room = queue.popleft()
            
            for neighbor in rooms[room]:
                
                if (neighbor not in visited):
                    
                    queue.append(neighbor)
                    visited.add(neighbor)
                    
                    if ( len(visited) == len(rooms) ):
                        return True
            
        
        return ( len(visited) == len(rooms) )