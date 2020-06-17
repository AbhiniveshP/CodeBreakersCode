class Solution:

    #   Time Complexity:    O(NlogN)
    #   Space Complexity:   O(1)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #   edge cases
        if (intervals == None or len(intervals) == 0):
            return []
        
        #   we need to sort the array otherwise [ [1,4], [0,4] ] kind of cases won't work
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        
        mergedIntervals = []
        
        for interval in intervals:
            
            #   if new start is > old end => update start and end
            if (interval[0] > end):
                mergedIntervals.append([start, end])
                start = interval[0]
                end = interval[1]
            
            #   otherwise update end taking care of this condition max()   
            else:
                end = max(end, interval[1])
                
        mergedIntervals.append([start, end])
        
        return mergedIntervals