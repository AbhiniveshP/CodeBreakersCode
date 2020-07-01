#   Important thing here is to call DFS or BFS only on unvisited vertices !!!

class Solution:
    
    #   Time:   O(V + E)
    #   Space:  O(V)

    def __dfs(self, vertex: int, graph: List[List[int]], vertexColorMap: dict) -> bool:
        
        for neighbor in graph[ vertex ]:
            
            if (neighbor in vertexColorMap and vertexColorMap[neighbor] == vertexColorMap[vertex]):
                return False
            
            if (neighbor not in vertexColorMap):
                vertexColorMap[ neighbor ] = -vertexColorMap[ vertex ]
                if ( self.__dfs(neighbor, graph, vertexColorMap) == False ):
                    return False
            
        return True
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        if (graph == None or len(graph) <= 1):
            return True
        
        vertexColorMap = {}
        color = 1
        
        for vertex in range(len(graph)):
            
            if (vertex not in vertexColorMap):
                vertexColorMap[ vertex ] = 1
                if (self.__dfs(vertex, graph, vertexColorMap) == False):
                    return False
            
        return True


from collections import deque

class BFS:
    
    #   Time:   O(V + E)
    #   Space:  O(V)

    def __bfs(self, vertex: int, graph: List[List[int]], vertexColorMap: dict) -> bool:
        
        queue = deque( [vertex] )
        
        while (queue):
            
            vertex = queue.popleft()
            
            for neighbor in graph[ vertex ]:

                if (neighbor in vertexColorMap and vertexColorMap[neighbor] == vertexColorMap[vertex]):
                    return False

                if (neighbor not in vertexColorMap):
                    vertexColorMap[ neighbor ] = -vertexColorMap[ vertex ]
                    queue.append(neighbor)
                    
        return True
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        if (graph == None or len(graph) <= 1):
            return True
        
        vertexColorMap = {}
        color = 1
        
        for vertex in range(len(graph)):
            
            if (vertex not in vertexColorMap):
                vertexColorMap[ vertex ] = 1
                if (self.__bfs(vertex, graph, vertexColorMap) == False):
                    return False
            
        return True