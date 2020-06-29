# Definition for Employee.

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

from collections import deque

class BFS:

    #   Time:   O(V + E)
    #   Space:  O(V + E)

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        if (employees == None or len(employees) == 0):
            return 0
        
        empIdInfoMap = {}
        
        for employee in employees:
            empIdInfoMap[employee.id] = employee

        queue = deque( [ empIdInfoMap[id] ] )
        totalImportance = 0
        
        while (queue):
            
            currentEmployee = queue.popleft()
            totalImportance += currentEmployee.importance
            
            for subordinate in currentEmployee.subordinates:
                queue.append(empIdInfoMap[subordinate])
                
        return totalImportance

class DFS:

    #   Time:   O(V + E)
    #   Space:  O(V + E)
    
    def __dfs(self, id: int, empIdInfoMap: dict, totalImportance: List[int]) -> None:
        
        currentEmployee = empIdInfoMap[id]
        totalImportance[0] += currentEmployee.importance
        
        for subordinate in currentEmployee.subordinates:
            self.__dfs(subordinate, empIdInfoMap, totalImportance)
            
        return 
    
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        if (employees == None or len(employees) == 0):
            return 0
        
        empIdInfoMap = {}
        
        for employee in employees:
            empIdInfoMap[employee.id] = employee
        
        queue = deque( [ empIdInfoMap[id] ] )
        totalImportance = [0]
        
        self.__dfs(id, empIdInfoMap, totalImportance)
        
        return totalImportance[0]