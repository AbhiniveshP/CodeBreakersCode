# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DFS:

	#	Time:	O(N)
    #	Space:	O(logN)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        if (root == None):
            return 0
        
        totalSum = 0
        
        if (root.left != None and root.left.left == None and root.left.right == None):
            totalSum += root.left.val
            
        totalSum += self.sumOfLeftLeaves(root.left)
        totalSum += self.sumOfLeftLeaves(root.right)
        
        return totalSum


from collections import deque

class BFS:


	#	Time:	O(N)
    #	Space:	O(N)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        if (root == None):
            return 0
        
        totalSum = 0
        
        queue = deque([root])
        
        while (len(queue) > 0):
            
            node = queue.popleft()
            
            if (node.left != None and node.left.left == None and node.left.right == None):
                totalSum += node.left.val
                
            if (node.left != None):
                queue.append(node.left)
                
            if (node.right != None):
                queue.append(node.right)            
            
        return totalSum