'''
Time Complexity:    O(m + n)
Space Complexity:   O(1)
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    #   function to get length
    def __length(self, head: ListNode) -> int:
        
        if (head == None):
            return 0
        
        cursor = head
        count = 0
        
        while (cursor != None):
            cursor = cursor.next
            count += 1
            
        return count
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        #   edge case check
        if(headA == None or headB == None):
            return None
        
        #   lengths of A and B LinkedList
        lenA = self.__length(headA)
        lenB = self.__length(headB)
        
        #   assign small and large heads according to the lengths
        if (lenA < lenB):
            small = headA
            large = headB
        else:
            small = headB
            large = headA
        
        #   get the difference in lengths    
        diff = abs(lenA - lenB)
        
        #   initialize fast pointer and move it to the difference number of nodes
        fast = large
        
        while (diff > 0):
            fast = fast.next
            diff -= 1
        

        #   now move slow and fast pointers until they hit the same node.  
        slow = small
        
        while (fast != None):
            
            if (slow == fast):
                return slow
            
            slow = slow.next
            fast = fast.next
        
        #   if they don't match => return None   
        return None
        