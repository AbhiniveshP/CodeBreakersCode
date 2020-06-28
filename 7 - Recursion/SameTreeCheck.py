# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DFS:
    
    #	Time:	O(N)
    #	Space:	O(logN)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if ( (p == None and q != None) or (p != None and q == None) ):
            return False
        
        if ( p == None and q == None):
            return True
        
        if (p.val != q.val):
            return False
        
        return ( self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) )

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class BFS:
    
    #	Time:	O(N)
    #	Space:	O(logN)
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        queue = deque( [ (p, q) ] )
        
        while (len(queue) > 0):
            
            nodesInfo = queue.popleft()
            p, q = nodesInfo[0], nodesInfo[1]
            
            if ( (p == None and q != None) or (p != None and q == None) ):
                return False

            elif (p != None and q != None and p.val != q.val):
                return False
            
            elif (p == None and q == None):
                continue
            
            else:
                queue.append( (p.left, q.left) )
                queue.append( (p.right, q.right) )
        
        return True