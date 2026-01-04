# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head) :

        # approach - Two-Pointer + Skip all duplicates

        dummy = ListNode(0, head) # dummy node before head (helps delete first element if needed)

        prev = dummy # prev pointer → tracks last confirmed unique node

        curr = head # curr pointer to scan list

        while curr:
            
            # move curr while next has same value
            while curr.next and curr.val == curr.next.val:
                curr = curr.next

            # If prev.next == curr, no duplicates
            if prev.next == curr:
                prev = prev.next
            else:
                # Skip duplicates
                prev.next = curr.next
        
            curr = curr.next
        
        return dummy.next
    
# Helper function to print list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

def create_linked_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head
    
    for value in arr[1:]:
        curr.next = ListNode(value)
        curr = curr.next
    
    return head

head = create_linked_list([1, 2, 3, 4, 4])

print("Original List:")
printList(head)

print("Removed Duplicates:")
sol = Solution()
new_head = sol.deleteDuplicates(head)
printList(new_head)

# Remove ALL nodes that have duplicate numbers from a sorted linked list