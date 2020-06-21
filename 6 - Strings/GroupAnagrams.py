class Solution:

    #   Time Complexity:    O(N * K) ==> N is number of words and K is average length of the word
    #   Space Complexity:   O(1) (we try to append the same lists and so they pass by reference)
    
    def __getPrimeProduct(self, word: str, primes: List[int]) -> int:
        
        prod = 1
        
        for char in word:
            index = ord(char) - ord('a')
            prod *= primes[index]
            
        return prod
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        
        prodsAnagsMap = {}
        
        for word in strs:
            
            product = self.__getPrimeProduct(word, primes)
            
            if (product in prodsAnagsMap):
                prodsAnagsMap[product].append(word)
            else:
                prodsAnagsMap[product] = [word]
        
        finalResult = []
        for prod in prodsAnagsMap:
            finalResult.append(prodsAnagsMap[prod])
        return finalResult