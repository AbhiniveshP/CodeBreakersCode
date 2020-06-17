class Solution:

    #   Time Complexity:    O(m + n)
    #   Space Complexity:   O(1)

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        #   start everything from the end, just in a reverse way of Merge Sort's Merge function
        mainCursor = m + n - 1
        first = m - 1
        second = n - 1
        
        #   update nums1 accordingly
        while (first >= 0 or second >= 0):
            
            if (first >= 0 and second >= 0):
                
                if nums1[first] > nums2[second]:
                    
                    nums1[mainCursor] = nums1[first]
                    first -= 1
                    mainCursor -= 1
                    
                else:
                    
                    nums1[mainCursor] = nums2[second]
                    second -= 1
                    mainCursor -= 1
                    
            elif (second >= 0):
                
                nums1[mainCursor] = nums2[second]
                second -= 1
                mainCursor -= 1
                
            else:
                first -= 1
                
        return