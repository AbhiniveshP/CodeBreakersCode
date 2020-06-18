# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    #   Time:   O(N * N)
    #   Space:  O(N)
    def __insert(self, node: ListNode, dummyHead: ListNode) -> None:
        
        #   create a new node with same node value
        newNode = ListNode(node.val)
        
        #   iterate until you find current node's correct location
        cursor = dummyHead
        while (cursor.next != None and cursor.next.val <= node.val):
            cursor = cursor.next
        
        #   update the pointers to insert current node    
        nextNode = cursor.next
        cursor.next = newNode
        newNode.next = nextNode
        
        return
    
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        #   edge cases
        if (head == None or head.next == None):
            return head
        
        #   create a dummy node
        dummyHead = ListNode()
        dummyHead.next = ListNode(head.val)
        
        #   for each node => insert it in correct location
        cursor = head.next
        while (cursor != None):
            self.__insert(cursor, dummyHead)
            cursor = cursor.next
        
        #   return dummy node's next node   
        return dummyHead.next