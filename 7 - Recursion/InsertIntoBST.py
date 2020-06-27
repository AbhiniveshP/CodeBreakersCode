# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Recursion:

    #   Time:   O(logN)
    #   Space:  O(logN)
    
    def __helper(self, node: TreeNode, val: int) -> None:
        
        if (val < node.val):
            if (node.left == None):
                node.left = TreeNode(val)
                return
            else:
                self.__helper(node.left, val)
                
        else:
            if (node.right == None):
                node.right = TreeNode(val)
                return
            else:
                self.__helper(node.right, val)
    
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if (root == None):
            return TreeNode(val)
        
        self.__helper(root, val)
        
        return root

class Iteration:
    
    #   Time:   O(logN)
    #   Space:  O(1)

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if (root == None):
            return TreeNode(val)
        
        node = root
        
        while (node != None):
            
            if (val < node.val):
                if (node.left == None):
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
                
            else:
                if (node.right == None):
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right
        
        return root