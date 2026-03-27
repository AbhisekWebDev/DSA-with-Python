# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from linkedList import ListNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: If the list is empty or has only one node, it's already sorted.
        if not head or not head.next:
            return head
        
        # 1. Divide: Find the middle and split the list into two halves
        mid = self.get_mid(head)
        right_head = mid.next
        mid.next = None  # Sever the link between the left and right halves
        
        # 2. Conquer: Recursively sort both halves
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right_head)
        
        # 3. Combine: Merge the two sorted halves
        return self.merge(left_sorted, right_sorted)

    
    def get_mid(self, head: ListNode) -> ListNode:
        """Helper function to find the middle of the linked list."""
        # Starting fast at head.next ensures that in a 2-node list, 
        # slow stays on the 1st node. This prevents infinite recursion.
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow

    
    def merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        """Helper function to merge two sorted linked lists."""
        dummy = ListNode()
        tail = dummy
        
        # Traverse both lists, attaching the smaller value to our merged list
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        # Attach any remaining nodes from either list
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
            
        return dummy.next