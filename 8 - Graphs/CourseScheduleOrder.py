from collections import deque

class Solution:

    #   Time:   O(V + E)
    #   Space:  O(V + E)
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        if (numCourses == 0):
            return []
        
        adjacencyList = { prereq: [] for prereq in range(numCourses) }
        indegrees = [ 0 for prereq in range(numCourses) ]
        
        for pair in prerequisites:
            adjacencyList[ pair[1] ].append( pair[0] )
            indegrees[ pair[0] ] += 1
        
        queue = deque( [] )
        visited = set()
        courseOrder = []
        for course, indegree in enumerate(indegrees):
            if (indegree == 0):
                queue.append(course)
                visited.add(course)
                
                
        while (queue):
            
            currentCourse = queue.popleft()
            courseOrder.append(currentCourse)
            
            for dependent in adjacencyList[currentCourse]:
                indegrees[dependent] -= 1
                if (indegrees[dependent] == 0):
                    queue.append(dependent)
                    visited.add(dependent)
                    
        return ( courseOrder if len(visited) == numCourses else [])