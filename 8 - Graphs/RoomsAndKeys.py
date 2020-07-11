class DFS:
    
    #   Time:   O(V + E)
    #   Space:  O(V)

    def __dfs(self, room: int, rooms: List[List[int]], visited: set) -> bool:
        
        #   if all rooms are visited => nothing extra to do
        if ( len(visited) == len(rooms) ):
            return True
        
        #   add current room to visited
        visited.add(room)
        
        #   for thr room's neighbor -> perform dfs and update visited set
        for neighbor in rooms[room]:
            
            if (neighbor not in visited):
                self.__dfs(neighbor, rooms, visited)
        
        #   if all rooms are visited => return True    
        return ( len(visited) == len(rooms) )
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        #   edge case check
        if (rooms == None or len(rooms) == 0):
            return True
        
        visited = set()
        
        #   perform dfs on first room
        return self.__dfs(0, rooms, visited)


from collections import deque

class BFS:

    #   Time:   O(V + E)
    #   Space:  O(V)
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        #   edge case check
        if (rooms == None or len(rooms) == 0):
            return True
        
        #   perform bfs on first room
        visited = set( [0] )
        queue = deque( [0] )
        
        while (queue):
            
            room = queue.popleft()
            
            #   for thr room's neighbor -> add it to the queue and update visited set
            for neighbor in rooms[room]:
                
                if (neighbor not in visited):
                    
                    queue.append(neighbor)
                    visited.add(neighbor)
                    
                    #   if all rooms are visited => nothing extra to do
                    if ( len(visited) == len(rooms) ):
                        return True
            
        #   if all rooms are visited => return True 
        return ( len(visited) == len(rooms) )