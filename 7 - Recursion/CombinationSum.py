class Solution:
    
    #   Time:   O(2^N)
    #   Space:  O(2^N)

    def __helper(self, candidates: List[int], currentIndex: int, currentSum: int, tempList: List[int],
                 target: int, finalLists: List[List[int]]) -> None:
        
        if (currentSum == target):
            finalLists.append(tempList[:])
            
        for index in range(currentIndex, len(candidates)):
            
            #   we need to do two things to proceed further, add the candidate to tempList and also to the sum
            tempList.append(candidates[index])
            currentSum += candidates[index]
            
            #   backtrack only if sum <= target
            if (currentSum <= target):
                self.__helper(candidates, index, currentSum, tempList, target, finalLists)
            
            #   undo the two things that were done prior    
            tempList.pop()
            currentSum -= candidates[index]

        return
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if (candidates == None or len(candidates) == 0):
            return []
        
        finalLists = []
        
        self.__helper(candidates, 0, 0, [], target, finalLists)
        
        return finalLists