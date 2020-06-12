# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class DetectCycle:

    #   Time Complexity:    O(n)
    #   Space Complexity:   O(1)

    def hasCycle(self, head: ListNode) -> bool:
        
        #   edge case check
        if (head == None or head.next == None):
            return False
        
        #   initializations
        slow = head
        fast = head.next
        
        #   iterate until either fast is None or fast's next is None
        while (fast != None and fast.next != None):
            
            #   Case where cycle exists
            if (slow == fast):
                return True
            
            #   update fast and slow pointers
            slow = slow.next
            fast = fast.next.next
        
        #   if reached here => no cycle   
        return False