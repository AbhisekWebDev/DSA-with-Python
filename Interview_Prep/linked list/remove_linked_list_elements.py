# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # Fix head if it starts with target value
        while head and head.val == val :
            head = head.next

        # If list becomes empty
        if not head:
            return head

        # Use two pointers
        prev = head
        curr = head.next

        while curr :
            if curr.val == val :
                prev.next = curr.next      # delete node
            else :
                prev = curr                # move prev only when we keep the node
        
            curr = curr.next
    
        return head