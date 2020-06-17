class Solution:

    #   Time Complexity:    O(n)
    #   Space Complexity:   O(1)

    def lemonadeChange(self, bills: List[int]) -> bool:
        
        #   edge cases
        if (bills == None or len(bills) == 0):
            return True
        
        #   maintain number of fives and tens as number of twenties is not required.
        fives, tens = 0, 0
        
        #   for each evaluate the following cases
        for bill in bills:
            
            #   if bill is 5 => nothing to give back => add fives
            if bill == 5:
                
                fives += 1
            
            #   if bil is 10 => 5 has to bew given back => if there are fives, then decrement fives and increment tens
            #   else => return False
            elif bill == 10:
                
                if (fives >= 1):
                    fives -= 1
                    tens += 1
                
                else:
                    return False
            
            #   if bill is 20 => 15 has to be given back => 1 five and 1 ten (or) 3 fives must be present
            else:
                
                if (tens >= 1 and fives >= 1):
                    fives -= 1
                    tens -= 1
                
                elif (fives >= 3):
                    fives -= 3
                    
                else:
                    return False 
            
        return True