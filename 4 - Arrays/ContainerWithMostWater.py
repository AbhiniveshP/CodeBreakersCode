class Solution:

    #   Time Complexity:    O(n)
    #   Space Complexity:   O(1)

    def maxArea(self, height: List[int]) -> int:
        
        #   edge cases
        if (height == None or len(height) < 2):
            return 0
        
        maxArea = 0
        
        #   As the length will anyway decrease => move min height forward and update the max area
        first = 0
        last = len(height) - 1
        
        while (first < last):
            
            minHeight = min(height[first], height[last])
            currentArea = minHeight * (last - first)
            maxArea = max(maxArea, currentArea)
            
            if (height[first] < height[last]):
                first += 1
            else:
                last -= 1
                
        return maxArea