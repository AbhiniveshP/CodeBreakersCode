class DFS:
    
    #   Time:   O(V + E)
    #   Space:  O(V + E)

    def __dfs(self, vertex: int, visited: set, adjList: dict) -> None:
        
        visited.add(vertex)
        
        for neighbor in adjList[ vertex ]:
            if (neighbor not in visited):
                self.__dfs(neighbor, visited, adjList)
                
        return
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = { vertex: [] for vertex in range(n) }
        
        for edge in edges:
            adjList[ edge[0] ].append( edge[1] )
            adjList[ edge[1] ].append( edge[0] )
            
        count = 0
        visited = set()
        
        for vertex in range(n):
            
            if (vertex not in visited):
                self.__dfs(vertex, visited, adjList)
                count += 1
                
        return count


class BFS:

    #   Time:   O(V + E)
    #   Space:  O(V + E)
    
    def __bfs(self, vertex: int, visited: set, adjList: dict) -> None:
        
        visited.add(vertex)
        queue = deque( [vertex] )
        
        while (queue):
            
            removedVertex = queue.popleft()
            for neighbor in adjList[ removedVertex ]:
                if (neighbor not in visited):
                    visited.add(neighbor)
                    queue.append(neighbor)
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = { vertex: [] for vertex in range(n) }
        
        for edge in edges:
            adjList[ edge[0] ].append( edge[1] )
            adjList[ edge[1] ].append( edge[0] )
            
        count = 0
        visited = set()
        
        for vertex in range(n):
            
            if (vertex not in visited):
                self.__bfs(vertex, visited, adjList)
                count += 1
                
        return count