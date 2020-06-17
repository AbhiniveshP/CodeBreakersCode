class Solution:

    #   Time Complexity:    O(NlogN + WlogW)
    #   Space Complexity:   O(N)

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        #   sort the difficulty and profit in parallel; then sort workers
        jobs = zip(difficulty, profit)
        
        jobs = sorted(jobs)
        worker.sort()
        
        cursor = 0
        totalMaxProfit = 0
        cursorMaxProfit = 0
        
        #   use a pointer for moving the cursor towards max profit and one more pointer for moving over jobs
        for skill in worker:
            
            while (cursor < len(jobs) and skill >= jobs[cursor][0]):
                cursorMaxProfit = max(cursorMaxProfit, jobs[cursor][1])
                cursor += 1
                
            totalMaxProfit += cursorMaxProfit
            
        return totalMaxProfit