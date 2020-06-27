# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class BFS:
    
    #   Time:   O(N)
    #   Space:  O(N)

    def isValidBST(self, root: TreeNode) -> bool:
        
        if (root == None):
            return True
        
        queue = deque([ (root, float('-inf'), float('inf')) ])
        
        while (len(queue) > 0):
            
            currentNodeInfo = queue.popleft()
            node = currentNodeInfo[0]
            minValue = currentNodeInfo[1]
            maxValue = currentNodeInfo[2]
            
            if (node.val <= minValue or node.val >= maxValue):
                return False
            
            if (node.left != None):
                queue.append( (node.left, minValue, node.val) )
                
            if (node.right != None):
                queue.append( (node.right, node.val, maxValue) )
                
        return True


class DFS:

    #   Time:   O(N)
    #   Space:  O(logN)
    
    def __helper(self, node: TreeNode, minValue: float, maxValue: float) -> bool:
        
        if (node.val <= minValue or node.val >= maxValue):
            return False
        
        leftCheck, rightCheck = True, True
        
        if (node.left != None):
            leftCheck = self.__helper(node.left, minValue, node.val)
            
        if (node.right != None):
            rightCheck = self.__helper(node.right, node.val, maxValue)
            
        return leftCheck and rightCheck
    
    def isValidBST(self, root: TreeNode) -> bool:
        
        if (root == None):
            return True
        
        return self.__helper(root, float('-inf'), float('inf'))