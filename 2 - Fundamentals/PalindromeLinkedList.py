'''
Time Complexity:    O(n)
Space Complexity:   O(1)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    #   function to reverse a linked list
    def __reverse(self, head: ListNode) -> ListNode:
        
        if (head == None or head.next == None):
            return head
        
        prev, curr = None, head
        
        while (curr.next != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        curr.next = prev
        
        return curr
    
    def isPalindrome(self, head: ListNode) -> bool:
        
        #   edge case check
        if (head == None or head.next == None):
            return True
        
        #   initialize slow and fast pointers to find mid and reverse the second half
        slow = head
        fast = head.next
        
        #   find the mid node
        while(fast != None and fast.next != None):
            
            slow = slow.next
            fast = fast.next.next
        
        #   reverse the next half from mid node    
        secondHalf = self.__reverse(slow.next)
        
        #   start from head and mid's next node
        slow = head
        fast = secondHalf
        
        #   check for equality and return accordingly
        while (fast != None):
            
            if (slow.val != fast.val):
                return False
            
            slow = slow.next
            fast = fast.next
            
        return True