# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    #   Time:   O(N)
    #   Space:  O(H)
    
    def __height(self, node: TreeNode, maxDiameter: List[float]) -> int:
        
        #   base case
        if (node == None):
            return 0
        
        #   calculate left and right heights
        leftH = self.__height(node.left, maxDiameter)
        rightH = self.__height(node.right, maxDiameter)
        
        #   check if max diameter existing is less than diamter including current node
        maxDiameter[0] = max(maxDiameter[0], leftH + 1 + rightH)
        
        #   return the height of current node.
        return max(leftH, rightH) + 1
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        #   edge case check
        if (root == None):
            return 0
        
        #   to update max diameter at each node
        maxDiameter = [float('-inf')]
        
        #   update the max diameter using this function
        self.__height(root, maxDiameter)
        
        #   max diameter would be number of vertices in the path - 1
        return maxDiameter[0] - 1