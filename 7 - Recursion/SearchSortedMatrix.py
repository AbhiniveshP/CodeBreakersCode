class Solution:

    #   Time:   O(m + n)
    #   Space:  O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if (matrix == None or len(matrix) == 0):
            return False
        
        row, col = 0, len(matrix[0]) - 1
        
        while (row >= 0 and col >= 0 and row < len(matrix) and col < len(matrix[0])):
            
            if (matrix[row][col] == target):
                return True
            
            elif (target < matrix[row][col]):
                col -= 1
                
            else:
                row += 1
        
        return False