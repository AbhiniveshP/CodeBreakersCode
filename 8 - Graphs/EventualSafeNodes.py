class Solution:

    #   Time:   O(V + E)
    #   Space:  O(V + E)

    #   exact reverse of Topological Sort Algorithm!!!
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        if (graph == None or len(graph) == 0):
            return []
        
        outdegrees = [ 0 for i in range(len(graph)) ]
        reverseAdjList = { i: [] for i in range(len(graph)) }
        queue = deque( [] )
        eventualSafeStates = []
        
        for vertex in range(len(graph)):
            
            toVertices = graph[vertex]
            outdegrees[vertex] = len(toVertices)
            
            for toVertex in toVertices:
                reverseAdjList[toVertex].append(vertex)
            
            if outdegrees[vertex] == 0:
                queue.append(vertex)
                eventualSafeStates.append(vertex)
                
        while (queue):
            
            vertex = queue.popleft()
            
            for fromVertex in reverseAdjList[vertex]:
                outdegrees[fromVertex] -= 1
                if (outdegrees[fromVertex] == 0):
                    queue.append(fromVertex)
                    eventualSafeStates.append(fromVertex)
                    
        return sorted(eventualSafeStates)
            
        