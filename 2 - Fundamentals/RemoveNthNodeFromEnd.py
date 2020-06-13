'''
Time Complexity:    O(n)
Space Complexity:   O(n)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        #   edge case check
        if (head == None or head.next == None):
            return None
        
        #   fast pointer
        fast = head
        
        #   move till you reach nth node from beginning
        while (n > 0 and fast != None):
            fast = fast.next
            n -= 1
        
        #   if asked to remove first node
        if (fast == None):
            return head.next
        
        #   slow pointer to head
        slow = head
        
        #   move both slow and fast until slow reaches n less node from end
        while (fast.next != None):
            slow = slow.next
            fast = fast.next
        
        #   remove nth node from end 
        slow.next = slow.next.next
        
        #   return the head
        return head