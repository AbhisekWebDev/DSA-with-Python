from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Edge case: only one node
        if not head or not head.next:
            return None

        slow = head
        fast = head

        prev = None

        while fast != None and fast.next != None :
           
            prev = slow
            
            slow = slow.next
            fast = fast.next.next
        
        # Delete the middle node
        prev.next = slow.next
    
        return head

# -------- Helper Functions --------

def create_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head

    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    return head

def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# -------- Test Cases --------

# Example 1
head = create_linked_list([1, 2, 3, 4, 5])
print("Before deletion:")
print_linked_list(head)

sol = Solution()
head = sol.deleteMiddle(head)

print("After deletion:")
print_linked_list(head)

# Example 2
head = create_linked_list([1, 2, 3, 4])
print("\nBefore deletion:")
print_linked_list(head)

head = sol.deleteMiddle(head)

print("After deletion:")
print_linked_list(head)

# Example 3 (single node)
head = create_linked_list([1])
head = sol.deleteMiddle(head)
print("\nSingle node result:", head)