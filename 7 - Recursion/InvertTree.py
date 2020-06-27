# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DFS:

	#   Time:   O(N)
    #   Space:  O(logN)

    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if (root == None):
            return root
        
        rightTree = self.invertTree(root.right)
        leftTree = self.invertTree(root.left)
        
        root.right = leftTree
        root.left = rightTree
        
        return root


from collections import deque

class BFS:

	#   Time:   O(N)
    #   Space:  O(N)

    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if (root == None):
            return root
        
        queue = deque([root])
        
        while (len(queue) > 0):
            
            currentNode = queue.popleft()
            
            tempTree = currentNode.right
            currentNode.right = currentNode.left
            currentNode.left = tempTree
            
            if (currentNode.left != None):
                queue.append(currentNode.left)
                
            if (currentNode.right != None):
                queue.append(currentNode.right)
                
        return root