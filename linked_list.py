# Reverse Linked List

# Define Node structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head
    
    while curr:
        nxt = curr.next     # store next
        curr.next = prev    # reverse link
        prev = curr         # move prev
        curr = nxt          # move forward
    
    return prev

# Helper function to print list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Create a linked list: 1 -> 2 -> 3 -> 4 -> None
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)

def create_linked_list(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head
    
    for value in arr[1:]:
        curr.next = ListNode(value)
        curr = curr.next
    
    return head

head = create_linked_list([1, 2, 3, 4])

print("Original List:")
printList(head)

# Call reverse
reversed_head = reverseList(head)

print("Reversed List:")
printList(reversed_head)