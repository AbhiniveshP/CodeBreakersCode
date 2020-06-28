# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    #   Time:   O(N)
    #   Space:  O(logN)
    def __helper(self, node: TreeNode, maxPathSum: List[float]) -> int:
        
        #   base case
        if (node == None):
            return 0
        
        #   calculate left and right sums
        leftSum = max( self.__helper(node.left, maxPathSum), 0 )
        rightSum = max( self.__helper(node.right, maxPathSum), 0 )
        
        #   update the maximum sum path from whether it consists of current root or not
        maxPathSum[0] = max( maxPathSum[0], leftSum + node.val + rightSum )
        
        #   for this subproblem, return the max sum that includes root value and maximum subtree sum (either left or right)
        return ( max(leftSum, rightSum) + node.val )
    
    def maxPathSum(self, root: TreeNode) -> int:
        
        maxPathSum = [float('-inf')]
        
        self.__helper(root, maxPathSum)
        
        return maxPathSum[0]