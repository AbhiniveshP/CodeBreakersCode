from collections import deque

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DFS:
    
    #   Time:   O(N)
    #   Space:  O(logN)

    def __helper(self, node: TreeNode, target: float, currentMinValues: List) -> None:
        
        currentDistance = abs(node.val - target)
        if (currentDistance < currentMinValues[0]):
            currentMinValues[0] = currentDistance
            currentMinValues[1] = node
            
        if (node.left != None):
            self.__helper(node.left, target, currentMinValues)
            
        if (node.right != None):
            self.__helper(node.right, target, currentMinValues)
    
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        if (root == None):
            return 0
        
        currentMinValues = [abs(root.val - target), root]
        
        self.__helper(root, target, currentMinValues)
        
        return currentMinValues[1].val


class BFS:
    
    #   Time:   O(N)
    #   Space:  O(N)

    def closestValue(self, root: TreeNode, target: float) -> int:
        
        if (root == None):
            return 0
        
        currentMinValues = [abs(root.val - target), root]
        
        queue = deque( [ root ] )
        
        while (len(queue) > 0):
            
            node = queue.popleft()
            
            currentDistance = abs(node.val - target)
            if (currentDistance < currentMinValues[0]):
                currentMinValues[0] = currentDistance
                currentMinValues[1] = node

            if (node.left != None):
                queue.append(node.left)

            if (node.right != None):
                queue.append(node.right)
            
        return currentMinValues[1].val